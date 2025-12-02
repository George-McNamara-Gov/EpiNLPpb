# ACT Health Epidemiology NLP Program Builder (EpiNLP Builder)

This package builds customised Natural Language Processing (NLP) programs for classifying free text snippets based on the presence of a specified characteristic. These NLP programs provide binary classifications of free text based on Linguistic Analysis and Machine Learning techniques. The output of these programs is an additional variable, in an existing data set containing free text, indicating a classification of the free text. This project was initially created to identify Emergency Department presentations related to suicide or self-harm from triage notes. In the case of suicide or self-harm related Emergency Department presentations, this classification process is more efficient than manual annotation, more precise than keyword searching, and more comprehensive than classifying based on ICD-10 clinical codes. The NLP programs are customised by the choice of annotated data, demographic, data size and distribution, linguistic analysis techniques and machine learning algorithm. This enables users to create and use NLP programs optimised to their needs. 

Disclaimer: This software package was developed during a proof-of-concept project. The NLP techniques included do not claim to be cutting edge or comprehensive. This software package is useful for experimentation with and exploration of NLP programs but may not be suited to large-scale implementations.

## Repository Structure

The directories (D) and packages (P) within this repository are structured as follows:

```text 
├── data                (D) # A convenient location to store test data. 
├── model               (P) # Save location for NLP programs.                  
├── package             (P) # The backend of the program builder.
│   ├── Importer        (P) # The component of package which imports data.
|   |   └──extractors   (P) # The component of package which extracts specified data. 
│   ├── evaluate        (P) # The component of package which evaluates NLP programs.
│   ├── mlearn          (P) # The component of package which utilises a machine learning algorithm.
│   └── vectorise       (P) # The component of package which vectorizes free text.
└── tests               (P) # Tests for 'package' and its sub-packages.
```

## Dependencies

All code is written in Python 3.13.3. Dependencies can be found in requirements.txt.

Ensure that 'python' is set as a path variable or that the terminal being used is Anaconda PowerShell.

## Set up

### Requirements

To run this project, you will need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer.

### Installation

Complete the following steps once, when first installing the repository. If you are using multiple python projects on your machine, consider creating a virtual environment for this project.

To install this project, open a terminal in the location you wish to store this repository. Run the following command:
```text
git clone https://github.com/George-McNamara-Gov/EpiNLPpb.git
```
Then navigate into this repository by running:
```text
cd EpiNLPpb
```
Next use Python's default dependency manager 'pip' to install this project's dependencies by running:
```text
pip install -r requirements.txt
```
If the above command returns an error and you are trying to install through a proxy server, instead run:
```text
pip install --proxy http://<USERNAME>:<PASSWORD>@<PROXY>:<PORT> --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```
Finally, you will need to download dictionaries from NLTK by running:
```text
python -m nltk_install
```
If the above command returns an error and you are trying to install through a proxy server, instead run:
```text
python -m nltk_install_proxy <USERNAME> <PASSWORD> <PROXY> <PORT> 
```

## Usage

To use the program builder, import the NLP class from package/base.py.
```text
from EpiNLPpb.package.base import NLP
```
The NLP class contains all the functionality required to create, evaluate, export, and use an NLP program. To do this, first create an NLP object with the desired customisations.
```text
nlp = NLP(
    name= 'program name',
    fileLocations= ['/path/to/data/file1', '/path/to/data/file2'],
    dateColumnLabel= 'date column label',
    hospitalColumnLabel= 'hospital column label',
    sexColumnLabel= 'sex column label',
    ageColumnLabel= 'age column label',
    textFieldColumnLabels= ['text field 1 column label', 'text field 2 column label'],
    flagColumnLabel= 'flag column label',
    ageBounds= (15, 60),     # (minimum age, maximum age)
    hospital= 'CHHS', #hospital
    sex= 1, # 0 for persons, 1 for male, 2 for female
    yearBounds= (2017, 2021),   # (earliest year, latest year)
    trainSize= 15000,  #amount of training data
    trainDist= 'TRAIN_DIST',
    testSize= 2000,   #amount of testing data
    testDist= 'TEST_DIST',
    tokeniser= 'tokeniser',
    preLAChanges= ['pre LA change 1', 'pre LA change 2'],
    tokenLevelLA= ['token level 1'],
    textLevelLA= ['text level 1', 'text level 2', 'text level 3'],
    corpusLevelLA= 'corpus level technique',
    mlAlgType= 'ml algorithm type',
    macLearnInput= {
        'ml alg param 1' : 0.01,
        'ml alg param 2' : 15
    }
)
```
An NLP object can also be created using dictionaries containing constructor arguments for the Importer, Vectorise, and MLearn objects. If an argument dictionary is provided for Importer, Vectorise, or MLearn, the related keyword arguments provided to the NLP constructor will be ignored.
```
nlp = NLP(
    name= 'program name',
    imp_arg_dict= {
        'fileLocations' : ['/path/to/data/file1', '/path/to/data/file2'],
        'dateColumnLabel' : 'date column label',
        'hospitalColumnLabel' : 'hospital column label',
        'sexColumnLabel' : 'sex column label',
        'ageColumnLabel' : 'age column label',
        'textFieldColumnLabels' : ['text field 1 column label', 'text field 2 column label'],
        'flagColumnLabel' : 'flag column label',
        'ageBounds' : (15, 60),
        'hospital' : 'CHHS',
        'sex' : 1,
        'yearBounds' : (2017, 2021),
        'trainSize' : 15000,
        'trainDist' : 'TRAIN_DIST',
        'testSize' : 2000,
        'testDist' : 'TEST_DIST'
    },
    vect_arg_dict= {
        'tokeniser' : 'tokeniser',
        'preLAChanges' : ['pre LA change 1', 'pre LA change 2'],
        'tokenLevelLA' : ['token level 1'],
        'textLevelLA' : ['text level 1', 'text level 2', 'text level 3'],
        'corpusLevelLA' : 'corpus level technique',
    },
    ml_arg_dict= {
        'mlAlgType' : 'ml algorithm type',
        'macLearnInput' : {
            'ml alg param 1' : 0.01,
            'ml alg param 2' : 15
        }
    }
)
```
Information about the format of and options for each parameter in the NLP constructor can be found in the EpiNLP Builder Technical Notes and the Release Notes for Update 1.1.0.

Use the create method to build an NLP program with these desired customisations.
```text
nlp.create()
```
Use the evaluateNLP method to evaluate this NLP program.
```text
nlp.evaluateNLP()
nlp.viewEvaluation()
```
Use the exportNLP method to save this NLP program in the model directory.
```text
nlp.exportNLP()
```
Use the annotateDataCSV or annotateDataXLSX methods to use this NLP program to annotate an existing data set.
```text
nlp.annotateDataCSV(
    '/path/to/existing/data/set.csv',
    ['text field 1 column label', 'text field 2 column label'],
    'label for annotation column'
)
```
Or
```text
nlp.annotateDataXLSX(
    '/path/to/existing/data/set.xlsx',
    'sheet name',
    ['text field 1 column label', 'text field 2 column label'],
    'label for annotation column'
)
```

NLP programs can also be trained and evaluated in a cross-validate fashion using crossValidate.
```
scores = nlp.crossValidate(
    5 # number of folds to use during cross-validation
)
print(scores)
```

For more information about using the software package please consult the package documentation.

## Tests

A suite of tests is provided for the backend of this project implemented in the 'package' directory. These tests are organised by module with tests for 'package/base', 'Importer', 'vectorise', 'vectorise/nltk', 'mlearn', and 'evaluate'. To run the tests, open a terminal in the directory containing this repository and run:
```text
python -m EpiNLPpb.tests.test
```

## Development

This project began development through the Vacation Study Program 2023-24 run by the ACT Health Research Strategy Team. The development continues in the ACT Health Directorate, Epidemiology Section, Knowledge Translation and Health Outcomes Team. All development is internal to ACT Health. For enquiries, please email the following address:

epicentre@act.gov.au

## Credits

This software uses the following open source packages:
- NLTK
- Sci-Kit Learn

This project was written by George McNamara.

This project was supervised by Glenn Draper, Dr Louise Freebairn, Dr Erin Walsh and Dr Gao Zhu.

The initial data for classifying ED records related to SSH was provided by Paul Mayers.

Technical support and problem solving was facilitated by Aidan Whitfield.

The documentation for this project was generated using [Doxygen](https://www.doxygen.nl/index.html).

## License

EpiNLP Builder is free and open-source software released under the [GPL](https://github.com/George-McNamara-Gov/ACTHealthNLPProgramBuilder/blob/main/LICENSE) (General Public License).
