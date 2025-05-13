'''
Main module of package. This module constructs, evaluates, exports, and utilises
NLP programs.

Classes:

    NLP

Functions:

    extarctFlags(list) -> list
    startRec() -> float
    stopRec(float) -> tuple[float, float]

Misc variables:

    cwd : str
        A string containing the path to the current working directory when the
        module is first run.

Exceptions:

    NameExistsException
    TreeGraphException
'''
import os
from .Importer import importer as i
from .vectorise import vectorise as v
from .mlearn import mlearn as m
from .evaluate import evaluate as e
from .evaluate import base as b
from . import exceptions as ex
import joblib
import time
import tracemalloc
from sklearn import tree
from matplotlib import pyplot as plt
import openpyxl
import pandas as pd
import csv

cwd = os.getcwd()

class NLP:
    '''
    A class to represent an NLP program.

    ...

    Attributes
    ----------
    parameters : dict
        A dictionary containing the parameters used to build the NLP program.
    name : str
        The name of the NLP program.
    importer : Importer
        The importer used to extract the data.
    vectorise : Vectorise
        The vectoriser used to vectorise the data.
    mlearn : MLearn
        The machine learning model used to predict flags.

    Constructed by running the create() method:
    trainData : list
        A list of records used to train the model and evaluate the complexity.
    vectTime : float
        The time taken to vectorise the training data.
    vectSpace : float
        The peak memory used when vectorising the training data.
    trainedModel : Union[tree.DecisionTreeClassifier, svm.SVC]]
        The useable NLP programs which can calssify input vectors.
    actualFlags : list
        The flags from the training data.
    predictedFlags : list
        The predicted flags for the training data produced by the NLP 
        program.
    times : list
        The measured times taken by different processes.
    spaces : list
        The measured memory usages of different processes.
    
    Constructed by running the evaluateNLP() method.
    eval : Evaluate
        The evaluater used to evaluate the program.
    outputDict : dict
        A dictionary containing the evaluation measures of the NLP program.
    
    Constructed by running the exportNLP() method.
    cwd : str
        The directory from which base is run.
    directoryName : str
        The name of the directory where files are exported to.

    Methods
    -------
    create()
        Imports, vectorises and uses data to train ML component. Then makes 
        predictions and constructs attributes.
    evaluateNLP()
        Evaluates the NLP program and constructs final attributes.
    approximateComplexities()
        Approximates the time and space complexities of the program.
    predictSingle(list) -> int
        Uses the trained model to predict the flag of a single record.
    exportNLP()
        Pickles and exports the NLP object to the model directory.
    annotateDataCSV(str, list, str)
        Write classifications into a CSV file of records.
    annotateDataXLSX(str, str, list, str)
        Write classifications into a XLSX file of records.
    viewEvaluation()
        Prints the evaluation to the command line.
    viewParameters()
        Prints the parameters to the command line.
    viewTreeGraph()
        Shows a labelled Decision Tree plot implemented by Sci-Kit Learn.
    writeToExcel()
        Writes program parameters and evaluation into model/model_results.xlsx.
    errorWritetoExcel()
        Writes program parameters and evaluation into model/model_results.xlsx
        when there is an error buidling the program.
    '''
    def __init__(self, 
                 name : str,
                 fileLocations: list, 
                 fileType : str, 
                 dateColumnLabel : str,
                 hospitalColumnLabel : str,
                 sexColumnLabel : str,
                 ageColumnLabel : str,
                 textFieldColumnLables : list,
                 flagColumnLabel : str, 
                 minAge: int, 
                 maxAge: int, 
                 hospital: str, 
                 sex: str, 
                 minYear: int, 
                 maxYear: int, 
                 trainSize: int, 
                 trainDist: str, 
                 testSize: int, 
                 testDist: str,
                 tokeniser : str,
                 preLAChanges : list,
                 tokenLevelLA : list,
                 textLevelLA : list,
                 corpusLevelLA : str,
                 mlAlgType : str,
                 macLearnInput : list,
                 trainPosPercent = -1,
                 testPosPercent = -1):
        '''
        Checks name input valid and contructs initial attributes for NLP object.

        Parameters
        ----------
        name : str
            A name for the NLP program.
        dateColumnLabel : str
            The label of the column with the date data.
        hospitalColumnLabel : str
            The label of the column with the hospital data.
        sexColumnLabel : str
            The label of the column with the sex data.
        ageColumnLabel : str
            The label of the column with the age data.
        textFieldColumnLabel : list
            The labels of the columns with free text.
        flagColumnLabel : str
            The label of the column with the data flag.
        minAge: int
            Minimum age for the demographic. 
        maxAge: int
            Maximum age for the demographic. 
        hospital: str
            The hospital(s) from which to draw the data. 
        sex: str
            The sex(es) for the demographic.
        minYear: int
            The minimum year from which to draw the data.
        maxYear: int
            The maximum year from which to draw the data.
        trainSize: int
            The amount of training records. 
        trainDist: str
            The distribution to use for selecting the training records. 
        testSize: int
            The amount of testing records.
        testDist: str
            The dsitribution to use for selecting testing records.
        tokeniser : str
            A choice of tokeniser to use for vectorising.
        preLAChanges : list
            A choice of pre LA changes for vectorising.
        tokenLevelLA : list
            A choice of token level techniques for vectorising.
        textLevelLA : list
            A choice of text level techniques for vectorising.
        corpusLevelLA : str
            A choice of corpus level technique for vectorising.
        mlAlgType : str
            A choice of machine learning algorithm type.
        macLearnInput : list
            Additional machine learning algorithm specifications.
        trainPosPercent : float
            The percentage of positively flagged records in the training data.
        testPosPercent : float
            The percentage of positively flagged records in the testing data.
        '''
        self.parameters = dict(
            Name = name,
            FileLocations = fileLocations,
            FileType = fileType,
            DateColumnLabel = dateColumnLabel,
            HospitalColumnLabel = hospitalColumnLabel,
            SexColumnLabel = sexColumnLabel,
            AgeColumnLabel = ageColumnLabel,
            TextFieldColumnLables = textFieldColumnLables,
            FlagColumnLabel = flagColumnLabel,
            MinimumAge = minAge,
            MaximumAge = maxAge,
            Hospital = hospital,
            Sex = sex,
            MinimumYear = minYear,
            MaximumYear = maxYear,
            TrainingDataSize = trainSize,
            TrainingDistribution = trainDist,
            TestingDataSize = testSize,
            TestingDistribution = testDist,
            TrainingDataPositivePercentage = trainPosPercent,
            TestingDataPositivePercentage = testPosPercent,
            Tokeniser = tokeniser,
            PreLAChanges = preLAChanges,
            TokenLevelLinguisticAnalysisTechniques = tokenLevelLA,
            TextLevelLinguisticAnalysisTechniques = textLevelLA,
            CorpusLevelLinguisticAnalysisTechnique = corpusLevelLA,
            MachineLearningAlgorithmType = mlAlgType,
            macLearnInput = macLearnInput
        )
        self.name = name
        self.importer = i.Importer(fileLocations, 
                                fileType, 
                                dateColumnLabel,
                                hospitalColumnLabel,
                                sexColumnLabel,
                                ageColumnLabel,
                                textFieldColumnLables,
                                flagColumnLabel,
                                minAge,
                                maxAge,
                                hospital,
                                sex,
                                minYear,
                                maxYear,
                                trainSize,
                                trainDist,
                                testSize,
                                testDist,
                                trainPosPercent,
                                testPosPercent
                                )
        self.vectorise = v.Vectorise(tokeniser,
                                     preLAChanges, 
                                     tokenLevelLA, 
                                     textLevelLA,
                                     corpusLevelLA,
                                     self.importer.dataSet.textIndices)
        self.mlearn = m.MLearn(mlAlgType, macLearnInput)

    def create(self):
        '''
        Imports, vectorises and uses data to train ML component. Then makes 
        predictions and constructs attributes.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.trainData, testData = self.importer.importData()

        trainFlags = extractFlags(self.trainData)
        actualFlags = extractFlags(testData)

        print('Vectorising Data...')
        time0 = startRec()
        trainVectors, testVectors = self.vectorise.vectorise(self.trainData, 
                                                             testData)
        self.vectTime, self.vectSpace = stopRec(time0)

        predictedFlags, trainedModel = self.mlearn.trainAndPredict(trainVectors, 
                                                                trainFlags, 
                                                                testVectors)

        times = [self.importer.importTime, 
                 self.importer.filterTime,
                 self.importer.trainExtractTime,
                 self.importer.testExtractTime,
                 self.vectTime,
                 self.mlearn.trainingTime,
                 self.mlearn.predictionTime]
        
        spaces = [self.importer.importSpace,
                  self.importer.filterSpace,
                  self.importer.trainExtractSpace,
                  self.importer.testExtractSpace,
                  self.vectSpace,
                  self.mlearn.trainingSpace,
                  self.mlearn.predictionSpace]

        self.trainedModel = trainedModel
        self.actualFlags = actualFlags
        self.predictedFlags = predictedFlags
        self.times = times
        self.spaces = spaces
        print('NLP program Created')
                
    def evaluateNLP(self):
        '''
        Evaluates the NLP program and constructs additional attributes.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        print('Evaluating Model...')
        time0 = startRec()
        self.eval = e.Evaluate(self.actualFlags, 
                                self.predictedFlags,
                                self.times,
                                self.spaces)
        self.outputDic = self.eval.evaluate()
        evalTime, evalSpace = stopRec(time0)
        self.eval.times.append(evalTime)
        self.eval.spaces.append(evalSpace)
        self.outputDic['EvaluateTime'] = evalTime
        self.outputDic['EvaluateSpace'] = evalSpace

    def approximateComplexities(self):
        '''
        Approximates the time and space complexities of the program.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        print('Approximating Complexities...')
        time0 = startRec()
        predict = lambda x : [self.predictSingle(record) for record in x]
        comp = b.ComplexityApproximator(self.trainData, predict)
        timeComp = comp.approxTimeComplexity()
        spaceComp = comp.approxSpaceComplexity()
        compTime, compSpace = stopRec(time0)
        self.eval.times.append(compTime)
        self.eval.spaces.append(compSpace)
        self.outputDic['ComplexityApproxTime'] = compTime
        self.outputDic['ComplexityApproxSpace'] = compSpace
        self.outputDic['PredictionTimeComplexity'] = timeComp
        self.outputDic['PredictionSpaceComplexity'] = spaceComp

    def predictSingle(self, 
                      record : list) -> int:
        '''
        Uses the trained model to predict the flag of a single record.

        Parameters
        ----------
        record : str
            The record for which the flag is to be predicted.

        Returns
        -------
        flag : int
            A 0 or 1 flag.
        '''  
        vectList = self.vectorise.vectoriseSingle(record)
        flags = self.trainedModel.predict(vectList)
        flag = flags[0]
        return flag

    def exportNLP(self):
        '''
        Pickles and exports the NLP object to the model directory.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.cwd = cwd
        self.directoryName = self.name + '-NLP-Program'
        path = str(os.getcwd()) + '\\EpiNLPpb\\model'
        os.chdir(path)

        if os.path.exists(str(os.getcwd()) + '\\' + self.directoryName):
            raise ex.NameExistsException(
                'There is already an NLP program stored with this name.'
                )

        os.makedirs(self.directoryName)
        path = (
            str(os.getcwd()) + '\\' + self.directoryName
                )
        os.chdir(path)
        print('Exporting NLP program...')
        joblib.dump(self, "nlp.pkl")
        os.chdir(cwd)
        print('Done')

    def annotateDataCSV(self, 
                        path : str, 
                        textFieldColumnLabels : list,
                        columnLabel : str):
        '''
        Write classifications into a CSV file of records.

        Parameters
        ----------
        path : str
            The location of the CSV file to be annotated.
        textFieldColumnLabels : list
            The lables of the columns containg the text to be used.
        columnLabel : str
            A label for the column of annotations.

        Returns
        -------
        None
        '''
        currentTextIndices = self.vectorise.textIndices
        newTextIndices = list(range(0,len(textFieldColumnLabels)))
        self.vectorise.setTextIndices(newTextIndices)
        print('Importing text...')
        outList = pd.read_csv(
                    path, 
                    usecols = textFieldColumnLabels, 
                    encoding_errors= 'ignore', 
                    low_memory= False
                    ).values.tolist()
        print('Vectorising...')
        vectors = self.vectorise.vectoriseList(outList)
        print('Predicting...')
        flags = self.trainedModel.predict(vectors)
        print('Annotating file...')
        csv_file_path = path
        try:
            with open(file= csv_file_path, mode= 'r', errors= 'replace') as file:
                reader = csv.reader(file)
                data = list(reader)
            data[0].append(columnLabel)
            rowIndex = 1
            for flag in flags:
                data[rowIndex].append(flag)
                rowIndex += 1
            print('Saving file...')
            with open(csv_file_path, 'w', newline='', errors= 'replace') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print('Data annotated.')

            self.vectorise.setTextIndices(currentTextIndices)
        except Exception as ex:
            print(ex)
            print(flags.sum())


    def annotateDataXLSX(self, 
                        path : str, 
                        sheet : str, 
                        textFieldColumnLabels : list,
                        columnLabel : str):
        '''
        Write classifications into a XLSX file of records.

        Parameters
        ----------
        path : str
            The location of the XLSX file to be annotated.
        sheet : str
            The name of the sheet to be annotated.
        textFieldColumnLabels : list
            The lables of the columns containg the text to be used.
        columnLabel : str
            A label for the column of annotations.

        Returns
        -------
        None
        '''
        print('Opening file...')
        file = openpyxl.load_workbook(path)
        sheet = file[sheet]
        currentTextIndices = self.vectorise.textIndices
        newTextIndices = list(range(0,len(textFieldColumnLabels)))
        self.vectorise.setTextIndices(newTextIndices)
        print('Importing text...')
        outList = pd.read_excel(
                    path, 
                    usecols = textFieldColumnLabels
                    ).values.tolist()
        print('Vectorising...')
        vectors = self.vectorise.vectoriseList(outList)
        print('Predicting...')
        flags = self.trainedModel.predict(vectors)
        print('Annotating file...')
        colIndex = 1
        while sheet.cell(row = 1, column = colIndex).value != None:
            colIndex += 1
        sheet.cell(row = 1, column = colIndex).value = columnLabel
        rowIndex = 2
        for flag in flags:
            sheet.cell(row = rowIndex, column = colIndex).value = flag
            rowIndex += 1
        print('Saving file...')
        file.save(path)
        self.vectorise.setTextIndicies(currentTextIndices)
    
    def viewEvaluation(self):
        '''
        Prints the evaluation to the command line.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        print('Precision: ', round(self.outputDic['Precision']*100), ' %')
        print('Recall: ', round(self.outputDic['Recall']*100), ' %')
        print('Total', '\n', 'Time: ', 
            round(self.outputDic['TotalTime'],3), '(s) Space: ', 
            round(self.outputDic['TotalSpace'] / (1024*1024),3), 
            '(MB)')
        if 'PredictionTimeComplexity' in self.outputDic:
            print('Prediction Complexity O(n^k)', '\n', 'Time: ', 
                round(self.outputDic['PredictionTimeComplexity'], 3), ' Space: ', 
                round(self.outputDic['PredictionSpaceComplexity'], 3))
        print('Importing', '\n', 'Time: ', 
            round(self.outputDic['ImportTime'],3), '(s) Space: ', 
            round(self.outputDic['ImportSpace'] / (1024*1024),3), 
            '(MB)')
        print('Filtering', '\n', 'Time: ', 
            round(self.outputDic['FilterTime'],3), '(s) Space: ', 
            round(self.outputDic['FilterSpace'] / (1024*1024),3), 
            '(MB)')
        print('Extracting Training Data ', '\n', 'Time: ', 
            round(self.outputDic['TrainExtractTime'],3), '(s) Space: ', 
            round(self.outputDic['TrainExtractSpace'] / (1024*1024),3), 
            '(MB)')
        print('Extracting Testing Data ', '\n', 'Time: ', 
            round(self.outputDic['TestExtractTime'],3), '(s) Space: ', 
            round(self.outputDic['TestExtractSpace'] / (1024*1024),3), 
            '(MB)')
        print('Data Vectorising ', '\n', 
            round(self.outputDic['VectoriseTime'],3), '(s) Space: ', 
            round(self.outputDic['VectoriseSpace'] / (1024*1024),3), 
            '(MB)')
        print('ML Algorithm Training', '\n', 'Time: ', 
            round(self.outputDic['MLTrainingTime'],3), '(s) Space: ', 
            round(self.outputDic['MLTrainingSpace'] / (1024*1024),3), 
            '(MB)')
        print('ML Algorithm Predicting', '\n', 'Time: ', 
            round(self.outputDic['MLPredictionTime'],3), '(s) Space: ', 
            round(self.outputDic['MLPredictionSpace'] / (1024*1024),3), 
            '(MB)')
        print('Evaluating', '\n', 'Time: ', 
            round(self.outputDic['EvaluateTime'],3), '(s) Space: ', 
            round(self.outputDic['EvaluateSpace'] / (1024*1024),3), 
            '(MB)')
        if 'ComplexityApproxTime' in self.outputDic:
            print('Complexity Approximating', '\n', 'Time: ', 
                round(self.outputDic['ComplexityApproxTime'],3), '(s) Space: ', 
                round(self.outputDic['ComplexityApproxSpace'] / (1024*1024),3), 
                '(MB)')
        print('----------------------------------------------------------------'
              '---------------------------------------------------------')
    
    def viewParameters(self):
        '''
        Prints the parameters to the command line.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        print('Name: ', 
            self.parameters['Name'])
        print('File Locations: ',
            self.parameters['FileLocations'])
        print('FIle Type: ',
            self.parameters['FileType'])
        print('Date Column Label: ',
            self.parameters['DateColumnLabel'])
        print('Hospital Column Label: ',
            self.parameters['HospitalColumnLabel'])
        print('Sex Column Label: ',
            self.parameters['SexColumnLabel'])
        print('Age Column Label: ',
            self.parameters['AgeColumnLabel'])
        print('Text Field Column Labels: ',
            self.parameters['TextFieldColumnLables'])
        print('Flag Column Label: ',
            self.parameters['FlagColumnLabel'])
        print('Minimum Age: ', 
            self.parameters['MinimumAge'])
        print('Maximum Age: ', 
            self.parameters['MaximumAge'])
        print('Hospital: ', 
            self.parameters['Hospital'])
        print('Sex: ', 
            self.parameters['Sex'])
        print('Minimum Year: ', 
            self.parameters['MinimumYear'])
        print('Maximum Year: ', 
            self.parameters['MaximumYear'])
        print('Training Data Size: ', 
            self.parameters['TrainingDataSize'])
        print('Training Data Distribution: ', 
            self.parameters['TrainingDistribution'])
        if self.parameters['TrainingDataPositivePercentage'] != -1:
            print('Training Positively Flagged Percentage: ',
                self.parameters['TrainingDataPositivePercentage'])
        print('Testing Data Size: ', 
            self.parameters['TestingDataSize'])
        print('Testing Data Distribution: ', 
            self.parameters['TestingDistribution'])
        if self.parameters['TestingDataPositivePercentage'] != -1:
            print('Testing Positively Flagged Percentage: ',
                self.parameters['TestingDataPositivePercentage'])
        print('Tokeniser: ',
            self.parameters['Tokeniser'])
        print('Pre-LA Changes: ',
            self.parameters['PreLAChanges'])
        print('Token Level LA Tehcniques: ', 
            self.parameters['TokenLevelLinguisticAnalysisTechniques'])
        print('Text Level LA Techniques: ', 
            self.parameters['TextLevelLinguisticAnalysisTechniques'])
        print('Corpus Level LA Technique: ',
            self.parameters['CorpusLevelLinguisticAnalysisTechnique'])
        print('ML Algorithm Type: ', 
            self.parameters['MachineLearningAlgorithmType'])
        if self.parameters['MachineLearningAlgorithmType'] == 'DECISIONTREE':
            print('Criterion: ',
                self.parameters['macLearnInput'][0])
        if self.parameters['MachineLearningAlgorithmType'] == 'SVMACHINE':
            print('Kernel: ',
                self.parameters['macLearnInput'][0])
            if self.parameters['macLearnInput'][0] == 'RBF':
                print('Gamma Paramter: ',
                    self.parameters['macLearnInput'][1])
            if self.parameters['macLearnInput'][0] == 'POLYNOMIAL':
                print('Degree: ',
                    self.parameters['macLearnInput'][1])
                print('"r" parameter: ',
                    self.parameters['macLearnInput'][2])
            if self.parameters['macLearnInput'][0] == 'SIGMOID':
                print('Gamma Paramter: ',
                    self.parameters['macLearnInput'][1])
                print('"r" parameter: ',
                    self.parameters['macLearnInput'][2])
        print('----------------------------------------------------------------'
              '---------------------------------------------------------')
    
    def viewTreeGraph(self):
        '''
        Shows a labelled Decision Tree plot implemented by Sci-Kit Learn.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        featureNames = list(self.vectorise.vectoriser.get_feature_names_out())
        featureSupport = [x.upper() for x in featureNames]
        try:
            _ = tree.plot_tree(self.mlearn.trainedModel,
                           feature_names=  featureNames + featureSupport,
                           class_names= ['Not SSH', 'SSH'],
                           filled=True,
                           fontsize= 6)
            plt.show()
        except:
            raise ex.TreeGraphException(
                'Cannot create a Tree Graph for a Support Vector Machine '
                'Algorithm.'
            )
        
    def writeToExcel(self):
        '''
        Writes program parameters and evaluation into model/model_results.xlsx.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        file = openpyxl.load_workbook('EpiNLPpb/model/model_results.xlsx')
        sheet = file['model_results']
        index = 2
        while sheet['A' + f'{index}'].value != None:
            index += 1
        sheet['A' + f'{index}'] = str(self.parameters['Name'])
        sheet['B' + f'{index}'] = str(self.parameters['FileLocations'])
        sheet['C' + f'{index}'] = str(self.parameters['FileType'])
        sheet['D' + f'{index}'] = str(self.parameters['DateColumnLabel'])
        sheet['E' + f'{index}'] = str(self.parameters['HospitalColumnLabel'])
        sheet['F' + f'{index}'] = str(self.parameters['SexColumnLabel'])
        sheet['G' + f'{index}'] = str(self.parameters['AgeColumnLabel'])
        sheet['H' + f'{index}'] = str(self.parameters['TextFieldColumnLables'])
        sheet['I' + f'{index}'] = str(self.parameters['FlagColumnLabel'])
        sheet['J' + f'{index}'] = self.parameters['MinimumAge']
        sheet['K' + f'{index}'] = self.parameters['MaximumAge']
        sheet['L' + f'{index}'] = str(self.parameters['Hospital'])
        sheet['M' + f'{index}'] = str(self.parameters['Sex'])
        sheet['N' + f'{index}'] = self.parameters['MinimumYear']
        sheet['O' + f'{index}'] = self.parameters['MaximumYear']
        sheet['P' + f'{index}'] = self.parameters['TrainingDataSize']
        sheet['Q' + f'{index}'] = str(self.parameters['TrainingDistribution'])
        sheet['R' + f'{index}'] = self.parameters[
            'TrainingDataPositivePercentage']
        sheet['S' + f'{index}'] = self.parameters['TestingDataSize']
        sheet['T' + f'{index}'] = str(self.parameters['TestingDistribution'])
        sheet['U' + f'{index}'] = self.parameters['TestingDataPositivePercentage']
        sheet['V' + f'{index}'] = str(self.parameters['Tokeniser'])
        sheet['W' + f'{index}'] = str(self.parameters['PreLAChanges'])
        sheet['X' + f'{index}'] = str(
            self.parameters['TokenLevelLinguisticAnalysisTechniques'])
        sheet['Y' + f'{index}'] = str(
            self.parameters['TextLevelLinguisticAnalysisTechniques'])
        sheet['Z' + f'{index}'] = str(
            self.parameters['CorpusLevelLinguisticAnalysisTechnique'])
        sheet['AA' + f'{index}'] = str(
            self.parameters['MachineLearningAlgorithmType'])
        if self.parameters['MachineLearningAlgorithmType'] == 'DECISIONTREE':
            sheet['AB' + f'{index}'] = str(self.parameters['macLearnInput'][0])
        if self.parameters['MachineLearningAlgorithmType'] == 'SVMACHINE':
            sheet['AC' + f'{index}'] = str(self.parameters['macLearnInput'][0])
            if self.parameters['macLearnInput'][0] == 'RBF':
                sheet['AD' + f'{index}'] = self.parameters['macLearnInput'][1]
            if self.parameters['macLearnInput'][0] == 'POLYNOMIAL':
                sheet['AF' + f'{index}'] = self.parameters['macLearnInput'][1]
                sheet['AE' + f'{index}'] = self.parameters['macLearnInput'][2]
            if self.parameters['macLearnInput'][0] == 'SIGMOID':
                sheet['AD' + f'{index}'] = self.parameters['macLearnInput'][1]
                sheet['AE' + f'{index}'] = self.parameters['macLearnInput'][2]
        sheet['AG' + f'{index}'] = round(self.outputDic['Precision']*100)
        sheet['AH' + f'{index}'] = round(self.outputDic['Recall']*100)
        sheet['AI' + f'{index}'] = round(self.outputDic['TotalTime'],3)
        sheet['AJ' + f'{index}'] = round(
            self.outputDic['TotalSpace'] / (1024*1024),3)
        sheet['AK' + f'{index}'] = round(self.outputDic['ImportTime'])
        sheet['AL' + f'{index}'] = round(
            self.outputDic['ImportSpace'] / (1024*1024),3)
        sheet['AM' + f'{index}'] = round(self.outputDic['FilterTime'],3)
        sheet['AN' + f'{index}'] = round(
            self.outputDic['FilterSpace'] / (1024*1024),3)
        sheet['AO' + f'{index}'] = round(self.outputDic['TrainExtractTime'],3)
        sheet['AP' + f'{index}'] = round(
            self.outputDic['TrainExtractSpace'] / (1024*1024),3)
        sheet['AQ' + f'{index}'] = round(self.outputDic['TestExtractTime'],3)
        sheet['AR' + f'{index}'] = round(
            self.outputDic['TestExtractSpace'] / (1024*1024),3)
        sheet['AS' + f'{index}'] = round(self.outputDic['VectoriseTime'],3)
        sheet['AT' + f'{index}'] = round(
            self.outputDic['VectoriseSpace'] / (1024*1024),3)
        sheet['AU' + f'{index}'] = round(self.outputDic['MLTrainingTime'],3)
        sheet['AV' + f'{index}'] = round(
            self.outputDic['MLTrainingSpace'] / (1024*1024),3)
        sheet['AW' + f'{index}'] = round(self.outputDic['MLPredictionTime'],3)
        sheet['AX' + f'{index}'] = round(
            self.outputDic['MLPredictionSpace'] / (1024*1024),3)

        file.save('EpiNLPpb/model/model_results.xlsx')

    def errorWriteToExcel(self):
        '''
        Writes program parameters and evaluation into model/model_results.xlsx
        when there is an error buidling the program.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        file = openpyxl.load_workbook('model/model_results.xlsx')
        sheet = file['model_results']
        index = 2
        while sheet['A' + f'{index}'].value != None:
            index += 1
        sheet['A' + f'{index}'] = str(self.parameters['Name'])
        sheet['B' + f'{index}'] = str(self.parameters['FileLocations'])
        sheet['C' + f'{index}'] = str(self.parameters['FileType'])
        sheet['D' + f'{index}'] = str(self.parameters['DateColumnLabel'])
        sheet['E' + f'{index}'] = str(self.parameters['HospitalColumnLabel'])
        sheet['F' + f'{index}'] = str(self.parameters['SexColumnLabel'])
        sheet['G' + f'{index}'] = str(self.parameters['AgeColumnLabel'])
        sheet['H' + f'{index}'] = str(self.parameters['TextFieldColumnLables'])
        sheet['I' + f'{index}'] = str(self.parameters['FlagColumnLabel'])
        sheet['J' + f'{index}'] = self.parameters['MinimumAge']
        sheet['K' + f'{index}'] = self.parameters['MaximumAge']
        sheet['L' + f'{index}'] = str(self.parameters['Hospital'])
        sheet['M' + f'{index}'] = str(self.parameters['Sex'])
        sheet['N' + f'{index}'] = self.parameters['MinimumYear']
        sheet['O' + f'{index}'] = self.parameters['MaximumYear']
        sheet['P' + f'{index}'] = self.parameters['TrainingDataSize']
        sheet['Q' + f'{index}'] = str(self.parameters['TrainingDistribution'])
        sheet['R' + f'{index}'] = self.parameters[
            'TrainingDataPositivePercentage']
        sheet['S' + f'{index}'] = self.parameters['TestingDataSize']
        sheet['T' + f'{index}'] = str(self.parameters['TestingDistribution'])
        sheet['U' + f'{index}'] = self.parameters['TestingDataPositivePercentage']
        sheet['V' + f'{index}'] = str(self.parameters['Tokeniser'])
        sheet['W' + f'{index}'] = str(self.parameters['PreLAChanges'])
        sheet['X' + f'{index}'] = str(
            self.parameters['TokenLevelLinguisticAnalysisTechniques'])
        sheet['Y' + f'{index}'] = str(
            self.parameters['TextLevelLinguisticAnalysisTechniques'])
        sheet['Z' + f'{index}'] = str(
            self.parameters['CorpusLevelLinguisticAnalysisTechnique'])
        sheet['AA' + f'{index}'] = str(
            self.parameters['MachineLearningAlgorithmType'])
        if self.parameters['MachineLearningAlgorithmType'] == 'DECISIONTREE':
            sheet['AB' + f'{index}'] = str(self.parameters['macLearnInput'][0])
        if self.parameters['MachineLearningAlgorithmType'] == 'SVMACHINE':
            sheet['AC' + f'{index}'] = str(self.parameters['macLearnInput'][0])
            if self.parameters['macLearnInput'][0] == 'RBF':
                sheet['AD' + f'{index}'] = self.parameters['macLearnInput'][1]
            if self.parameters['macLearnInput'][0] == 'POLYNOMIAL':
                sheet['AF' + f'{index}'] = self.parameters['macLearnInput'][1]
                sheet['AE' + f'{index}'] = self.parameters['macLearnInput'][2]
            if self.parameters['macLearnInput'][0] == 'SIGMOID':
                sheet['AD' + f'{index}'] = self.parameters['macLearnInput'][1]
                sheet['AE' + f'{index}'] = self.parameters['macLearnInput'][2]
        sheet['AG' + f'{index}'] = 'ERROR'

        file.save('model/model_results.xlsx')

def extractFlags(records : list) -> list:
    '''
    Extracts the flags from a list of records.

    Parameters
    ----------
    records : list
        A list of records.
    
    Returns
    -------
    flags : list
        The flags corresponding to each record.
    '''
    flags = [int(record[len(record) - 1]) for record in records]
    return flags
 
def startRec() -> float:
    '''
    Outputs the current time and begins tracking memory.

    Parameters
    ----------
    None

    Retruns
    -------
    time0 : float
        The current time.
    '''
    time0 = time.time()
    tracemalloc.start()
    return time0

def stopRec(time0 : float) -> tuple[float, float]:
    '''
    Outputs time passed and peak memory used since the last call of startRec().

    Parameters
    ----------
    time0 : float
        The output from the last call of startRec().

    Returns
    -------
    time1 : float
        The time passed since the last call of startRec().
    space : float
        The peak memory used since the last call of startRec().
    '''
    time1 = time.time() - time0
    _, space = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return (time1, space)