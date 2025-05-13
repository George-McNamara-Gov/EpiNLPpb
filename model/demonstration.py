'''
This module can be run directly to demonstrate the flagging of records using a
saved NLP program through the command line.

Classes:

    None

Functions:

    main()

Misc variables:

    None

Exceptions:

    None
'''
import joblib
import sys
import os

def main():
    '''
    Demonstrate the flagging of records through the command line.

    Parameters
    ----------
    None

    Returns
    -------
    None
    '''
    sys.path.append(str(os.getcwd()) + '\\package')
    name = str(input(
        'Please enter the name of the model you wish to use for flagging: '
        ))
    path = (str(os.getcwd()) +
            '\\model\\' + name.upper() + '-NLP-Program')
    print('Loading NLP program...')

    try:
        nlp = joblib.load(path + '\\nlp.pkl')
    except FileNotFoundError:
        print(f'There is not model saved with the name {name.upper()}.')
        return
    
    while True:

        columnLabels = nlp.importer.dataSet.textFieldColumnLables
        textIndices = nlp.importer.dataSet.textIndices

        textInputs = []
        for label in columnLabels:
            textInputs.append(str(input(
                f'Please enter the {label} of the record you wish to flag: '
                )))
        
        record = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        index = 0
        for pos in textIndices:
            record[pos] = textInputs[index]
            index += 1

        flag = nlp.predictSingle(record)

        print('----------------------------------------------------------------'
              '---------------------------------------------------------')

        if flag == 0:
            print('This record was not flagged for suicide or self-harm.')
        if flag == 1:
            print('This record was flagged for suicide or self-harm.')

        print('----------------------------------------------------------------'
              '---------------------------------------------------------')

if __name__ == '__main__':
    main()