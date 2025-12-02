'''
Main module of the package/Importer package to be used in package/base.py.

Classes:

    Importer

Functions:

    startRec() -> float
    stopRec(float) -> (float, float)

Misc variables:

    None

Exceptions:

    ImporterException
    NegTrainSizeException
    NegTestSizeException
    TrainDistException
    TestDistException
'''
from . import base as b
from .extractors import extractors as ex
from .. import exceptions as e
import time
import tracemalloc
import pandas as pd

class Importer:
    '''
    A class to be constructed in package/base.py to import the necessary data.

    ...

    Attributes
    ----------
    Constructed by running the initialise() method:
    dataSet : DataSet
        The DataSet from which to draw the data.
    demographic : Demographic
        Demographic of the desired data.
    trainExtractor : Extractor
        An Extractor to obtain training data.
    testExtractor : Extractor
        An Extractor to obtain testing data.
    textFieldColumnLabels : list
        The labels of the columns with free text.
    flagColumnLabel : str
        The label of the column with the classification flag.

    Constructed by running the importData() method:
    importTime : float
        Time taken to import data.
    importSpace : float
        Peak space used to import data.
    filterTime : float
        Time taken to filter data.
    filterSpace : float
        Peak space used to filter data.
    trainExtractTime : float
        Time taken to extract training data.
    trainExtractSpace : float
        Peak space used to extract training data.
    testExtractTime : float
        Time taken to extract testing data.
    testExtractSpace : float
        Peak space used to extract testing data.
    
    Methods
    -------
    initialise()
        Checks constructor inputs and creates attributes.
    importData() -> tuple[pd.DataFrame, pd.DataFrame]
        Creates a data frame of training records and a data frame of testing records.
    '''
    def __init__(self,
                 arg_dict : dict = None,
                 trainFile : str = '',
                 testFile : str = '', 
                 fileLocations: list = [], 
                 dateColumnLabel : str = '',
                 hospitalColumnLabel : str = '',
                 sexColumnLabel : str = '',
                 ageColumnLabel : str = '',
                 customColumnLabels : list = [],
                 textFieldColumnLabels : list = [],
                 flagColumnLabel : str = '', 
                 ageBounds : tuple = (0, 150), 
                 hospital: str = 'ALL', 
                 sex: int = 0, 
                 yearBounds : tuple = (1900, 2100),
                 customBounds : list = [], 
                 trainSize: int = 0, 
                 trainDist: str = 'NEWESTBLOCK', 
                 testSize: int = 0, 
                 testDist: str = 'NEWESTBLOCK'):
        '''
        Passes inputs from either arg_dict or keyword arguments.

        Parameters
        ----------
        arg_dict : dict
            A dictionary containing constructor arguments.
        trainFile : str
            The path to a file containing training data.
        testFile : str
            The path to a file containing testing data.
        fileLocations : list
            List of paths of files where data is stored.
        dateColumnLabel : str
            The label of the column with the date data.
        hospitalColumnLabel : str
            The label of the column with the hospital data.
        sexColumnLabel : str
            The label of the column with the sex data.
        ageColumnLabel : str
            The label of the column with the age data.
        customColumnLabels : list
            The labels of columns with custom data to filter.
        textFieldColumnLabels : list
            The labels of the columns with free text.
        flagColumnLabel : str
            The label of the column with the classification flag.
        ageBounds : tuple
            The minimum and maximum age values for included records.
        hospital : str
            Which hospital(s) to include.
        sex : int
            Which sex(es) to include.
        yearBounds : tuple
            The minimum and maximum year values for included records.
        customBounds : list
            A list of bounds for columns with custom data.
        trainSize : int
            Number of records to use for training.
        trainDist : str
            How to sample the training data from the dataSet.
        testSize : int
            Number of records to use for testing.
        testDistribution : str
            How to sample the testing data from the dataSet.
        '''
        if arg_dict is not None:
            if not isinstance(arg_dict, dict):
                raise e.ImporterException(
                    'arg_dict must be a dictionary.'
                )
            
            if 'tranFile' in arg_dict:
                trainFile = arg_dict['trainFile']
            if 'testFile' in arg_dict:
                testFile = arg_dict['testFile']
            if 'fileLocations' in arg_dict:
                fileLocations = arg_dict['fileLocations']
            if 'dateColumnLabel' in arg_dict:
                dateColumnLabel = arg_dict['dateColumnLabel']
            if 'hospitalColumnLabel' in arg_dict:
                hospitalColumnLabel = arg_dict['hospitalColumnLabel']
            if 'sexColumnLabel' in arg_dict:
                sexColumnLabel = arg_dict['sexColumnLabel']
            if 'ageColumnLabel' in arg_dict:
                ageColumnLabel = arg_dict['ageColumnLabel']
            if 'customColumnLables' in arg_dict:
                customColumnLabels = arg_dict['customColumnLabels']
            if 'textFieldColumnLabels' in arg_dict:
                textFieldColumnLabels = arg_dict['textFieldColumnLabels']
            if 'flagColumnLabel' in arg_dict:
                flagColumnLabel = arg_dict['flagColumnLabel']
            if 'ageBounds' in arg_dict:
                ageBounds = arg_dict['ageBounds']
            if 'hospital' in arg_dict:
                hospital = arg_dict['hospital']
            if 'sex' in arg_dict:
                sex = arg_dict['sex']
            if 'yearBounds' in arg_dict:
                yearBounds = arg_dict['yearBounds']
            if 'customBounds' in arg_dict:
                customBounds = arg_dict['customBounds']
            if 'trainSize' in arg_dict:
                trainSize = arg_dict['trainSize']
            if 'trainDist' in arg_dict:
                trainDist = arg_dict['trainDist']
            if 'testSize' in arg_dict:
                testSize = arg_dict['testSize']
            if 'testDist' in arg_dict:
                testDist = arg_dict['testDist']

        self.initialise(trainFile,
                        testFile, 
                        fileLocations, 
                        dateColumnLabel,
                        hospitalColumnLabel,
                        sexColumnLabel,
                        ageColumnLabel,
                        customColumnLabels,
                        textFieldColumnLabels,
                        flagColumnLabel, 
                        ageBounds, 
                        hospital, 
                        sex, 
                        yearBounds,
                        customBounds, 
                        trainSize, 
                        trainDist, 
                        testSize, 
                        testDist)

    def initialise(self,
                trainFile : str = '',
                testFile : str = '', 
                fileLocations: list = [], 
                dateColumnLabel : str = '',
                hospitalColumnLabel : str = '',
                sexColumnLabel : str = '',
                ageColumnLabel : str = '',
                customColumnLabels : list = [],
                textFieldColumnLabels : list = [],
                flagColumnLabel : str = '', 
                ageBounds : tuple = (0, 150), 
                hospital: str = 'ALL', 
                sex: int = 0, 
                yearBounds : tuple = (1900, 2100),
                customBounds : list = [], 
                trainSize: int = 0, 
                trainDist: str = 'NEWESTBLOCK', 
                testSize: int = 0, 
                testDist: str = 'NEWESTBLOCK'):
        '''
        Checks constructor inputs and creates attributes.

        Parameters
        ----------
        trainFile : str
            The path to a file containing training data.
        testFile : str
            The path to a file containing testing data.
        fileLocations : list
            List of paths of files where the data is stored.
        dateColumnLabel : str
            The label of the column with the date data.
        hospitalColumnLabel : str
            The label of the column with the hospital data.
        sexColumnLabel : str
            The label of the column with the sex data.
        ageColumnLabel : str
            The label of the column with the age data.
        customColumnLabels : list
            The labels of columns with custom data to filter.
        textFieldColumnLabels : list
            The labels of the columns with free text.
        flagColumnLabel : str
            The label of the column with the classification flag.
        ageBounds : tuple
            The minimum and maximum age values for included records.
        hospital : str
            Which hospital(s) to include.
        sex : int
            Which sex(es) to include.
        yearBounds : tuple
            The minimum and maximum year values for included records.
        customBounds : list
            A list of bounds for columns with custom data.
        trainSize : int
            Number of records to use for training.
        trainDist : str
            How to sample the training data from the dataSet.
        testSize : int
            Number of records to use for testing.
        testDistribution : str
            How to sample the testing data from the dataSet.

        Returns
        -------
        None
        '''
        self.dataSet = b.DataSet(trainFile,
                                testFile,
                                fileLocations,
                                dateColumnLabel,
                                hospitalColumnLabel,
                                sexColumnLabel,
                                ageColumnLabel,
                                customColumnLabels,
                                textFieldColumnLabels,
                                flagColumnLabel
                                )
        
        self.demographic = b.Demographic(dateColumnLabel,
                                        hospitalColumnLabel,
                                        sexColumnLabel,
                                        ageColumnLabel,
                                        customColumnLabels,
                                        ageBounds,
                                        hospital,
                                        sex,
                                        yearBounds,
                                        customBounds)
        
        if trainSize <= 0 or not isinstance(trainSize, int):
            raise e.NegTrainSizeException(
                'Train size must be a positive integer'
                )
        if testSize <= 0 or not isinstance(testSize, int):
            raise e.NegTestSizeException(
                'Test size must be a positive integer'
                )
       
        match trainDist:
            case 'NEWESTBLOCK':
                self.trainExtractor = ex.NewestBlock(trainSize)
            case 'RANDOMBLOCK':
                self.trainExtractor = ex.RandomBlock(trainSize)
            case 'UNIFORM':
                self.trainExtractor = ex.Uniform(trainSize)
            case _ :
                raise e.TrainDistException(
                    ('Training distribution must be "NEWESTBLOCK", "RANDOMBLOCK" '
                    'or "UNIFORM"')
                    )

        match testDist:
            case 'NEWESTBLOCK':
                self.testExtractor = ex.NewestBlock(testSize)
            case 'RANDOMBLOCK':
                self.testExtractor = ex.RandomBlock(testSize)
            case 'UNIFORM':
                self.testExtractor = ex.Uniform(testSize)
            case _:
                raise e.TestDistException(
                    ('Testing distribution must be "NEWESTBLOCK", "RANDOMBLOCK" or '
                    '"UNIFORM"')
                    )
            
        self.textFieldColumnLabels = textFieldColumnLabels    
        self.flagColumnLabel = flagColumnLabel

    def importData(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        '''
        Creates a data frame of training records and a data frame of testing records.

        Parameters
        ----------
        None

        Returns
        -------
        trainData : pd.DataFrame
            A data frame of training records.
        testData : pd.DataFrame
            A data frame of testing records.
        '''
        print('Importing data...')
        time0 = startRec()
        data = self.dataSet.importToFrame()
        self.importTime, self.importSpace = stopRec(time0)

        print('Filtering data...')
        time0 = startRec()
        if isinstance(data, tuple):
            data = (self.demographic.filter(data[0]), self.demographic.filter(data[1]))
        else:
            data = self.demographic.filter(data)
        self.filterTime, self.filterSpace = stopRec(time0)
        
        if isinstance(data, tuple):
            print('Extracting training data...')
            time0 = startRec()
            trainData = self.trainExtractor.extract(data[0])[0]
            self.trainExtractTime, self.trainExtractSpace = stopRec(time0)

            print('Extracting testing data...')
            time0 = startRec()
            testData = self.testExtractor.extract(data[1])[0]
            self.testExtractTime, self.testExtractSpace = stopRec(time0)
        else:
            print('Extracting training data...')
            time0 = startRec()
            extracted = self.trainExtractor.extract(data)
            trainData = extracted[0]
            remainingData = extracted[1]
            self.trainExtractTime, self.trainExtractSpace = stopRec(time0)

            print('Extracting testing data...')
            time0 = startRec()
            testData = self.testExtractor.extract(remainingData)[0]
            self.testExtractTime, self.testExtractSpace = stopRec(time0)
    
        return (trainData, testData)
    
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