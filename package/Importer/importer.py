'''
Main module of the package/Importer package to be used in package/base.

Classes:

    Importer

Functions:

    splitPosAndNegFlags(list) -> tuple[list,list]

Misc variables:

    None

Exceptions:

    NegTrainSizeException
    NegTestSizeException
    TrainDistException
    TestDistException
    TrainPosPercentException
    TestPosPercentException
'''
from . import base as b
from .extractors import extractors as ex
from .. import base
from collections import deque
from .. import exceptions as e

class Importer:
    '''
    A class to be constructed in package/base to import the necessary data.

    ...

    Attributes
    ----------
    demographic : Demographic
        Demographic of the desired data.
    dataSet : DataSet
        The DataSet from which to draw the data.
    trainExtractor : Extractor
        An Extractor to obtain training data.
    testExtractor : Extractor
        An Extractor to obtain testing data.
    trainPosPercent : float
        The percentage of positively flagged training records to use.
    testPosPercent : float
        The percentage of positively flagged testing records to use.
    
    Methods
    -------
    importData() -> tuple[list, list]
        Creates a list of training records and a list of testing records.
    '''
    def __init__(self, 
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
                 trainPosPercent = -1,
                 testPosPercent = -1):
        '''
        Checks inputs are valid and constructs attributes for Importer object.

        Parameters
        ----------
        fileLocations : list
            List of strings of file names where the data is stored.
        dateColumnLabel : str
            The label of the column with the date data.
        hospitalColumnLabel : str
            The label of the column with the hospital data.
        sexColumnLabel : str
            The label of the column with the sex data.
        ageColumnLabel : str
            The label of the column with the age data.
        textFieldColumnLabels : list
            The labels of the columns with free text.
        flagColumnLabel : str
            The label of the column with the data flag.
        minAge : int
            Lowest age.
        maxAge : int
            Highest age.
        hospital : str
            Which hospital(s) to include.
        sex : str
            Which sex(es) to include.
        minYear : int
            Earliest year.
        maxYear : int
            Latest year.
        trainSize : int
            Number of records to use for training.
        trainDist : str
            How to sample the training data from the dataSet.
        testSize : int
            Number of records to use for testing.
        testDistribution : str
            How to sample the testing data from the dataSet.
        trainPosPercent : float
            The percentage of positively flagged records in the training data.
        testPosPercent : float
            The percentage of positively flagged records in the testing data.
        '''
        self.dataSet = b.DataSet(fileLocations, 
                                fileType, 
                                dateColumnLabel,
                                hospitalColumnLabel,
                                sexColumnLabel,
                                ageColumnLabel,
                                textFieldColumnLables,
                                flagColumnLabel
                                )
        self.demographic = b.Demographic(minAge, 
                                        maxAge,
                                        self.dataSet.ageIndex, 
                                        hospital,
                                        self.dataSet.hospIndex,
                                        sex,
                                        self.dataSet.sexIndex,
                                        minYear, 
                                        maxYear,
                                        self.dataSet.dateIndex)
        if trainSize < 0:
            raise e.NegTrainSizeException(
                'Train size must be a positive integer'
                )
        if testSize < 0:
            raise e.NegTestSizeException(
                'Test size must be a positive integer'
                )
        if trainDist not in ['NEWESTBLOCK', 'RANDOMBLOCK', 'UNIFORM']:
            raise e.TrainDistException(
                ('Training distribution must be "NEWESTBLOCK", "RANDOMBLOCK" '
                'or "UNIFORM"')
                )
        match trainDist:
            case 'NEWESTBLOCK':
                self.trainExtractor = ex.NewestBlock(trainSize)
            case 'RANDOMBLOCK':
                self.trainExtractor = ex.RandomBlock(trainSize)
            case 'UNIFORM':
                self.trainExtractor = ex.Uniform(trainSize)
        if testDist not in ['NEWESTBLOCK', 'RANDOMBLOCK', 'UNIFORM']:
            raise e.TestDistException(
                ('Testing distribution must be "NEWESTBLOCK", "RANDOMBLOCK" or '
                '"UNIFORM"')
                )
        match testDist:
            case 'NEWESTBLOCK':
                self.testExtractor = ex.NewestBlock(testSize)
            case 'RANDOMBLOCK':
                self.testExtractor = ex.RandomBlock(testSize)
            case 'UNIFORM':
                self.testExtractor = ex.Uniform(testSize)
        if trainPosPercent != -1:
            if trainPosPercent <= 0 or trainPosPercent >= 100:
                raise e.TrainPosPercentException(
                    'The percentage of positively flagged records '
                    'in the training data must be between 0 and 100'
                    )
        self.trainPosPercent = trainPosPercent
        if testPosPercent != -1:
            if testPosPercent <= 0 or testPosPercent >= 100:
                raise e.TestPosPercentException(
                    'The percentage of positively flagged records '
                    'in the testing data must be between 0 and 100'
                    )
        self.testPosPercent = testPosPercent

    def importData(self) -> tuple[list, list]:
        '''
        Creates a list of training records and a list of testing records.

        Parameters
        ----------
        None

        Returns
        -------
        trainData : list
            A list of training records.
        testData : list
            A list of testing records.
        '''
        print('Importing data...')
        time0 = base.startRec()
        data = self.dataSet.importToList()
        self.importTime, self.importSpace = base.stopRec(time0)

        print('Filtering data...')
        time0 = base.startRec()
        data = [
            rec for rec in data if self.demographic.demographicCheck(rec)]
        self.filterTime, self.filterSpace = base.stopRec(time0)

        print('Extracting training data...')
        time0 = base.startRec()
        if self.trainPosPercent == -1:
            extracted = self.trainExtractor.extract(data)
            trainData = extracted[0]
            remainingData = extracted[1]
        else:
            extracted = self.trainExtractor.extract(data)
            remainingData = extracted[1]

            posList, negList = splitPosAndNegFlags(data)
            amount = self.trainExtractor.amount
            newAmount = int(amount * (self.trainPosPercent/100))
            self.trainExtractor.changeAmount(newAmount)
            posRecs = self.trainExtractor.extract(posList)
            newAmount = amount - newAmount
            self.trainExtractor.changeAmount(newAmount)
            negRecs = self.trainExtractor.extract(negList)
            trainData = posRecs[0] + negRecs[0]

        self.trainExtractTime, self.trainExtractSpace = base.stopRec(time0)

        print('Extracting testing data...')
        time0 = base.startRec()
        if self.testPosPercent == -1:
            testData = self.testExtractor.extract(remainingData)[0]
        else:
            posList, negList = splitPosAndNegFlags(remainingData)
            amount = self.testExtractor.amount
            newAmount = int(amount * (self.testPosPercent/100))
            self.testExtractor.changeAmount(newAmount)
            posRecs = self.testExtractor.extract(posList)
            newAmount = amount - newAmount
            self.testExtractor.changeAmount(newAmount)
            negRecs = self.testExtractor.extract(negList)
            testData = posRecs[0] + negRecs[0]
        self.testExtractTime, self.testExtractSpace = base.stopRec(time0)

        return (trainData, testData)
    
def splitPosAndNegFlags(data : list) -> tuple[list,list]:
    '''
    Splits a list of records into a list of positively flagged records and a 
    list of negatively flagged records.

    Parameters
    ----------
    data : list
        The list of records to be split.

    Returns
    -------
    posList : list
        The list of positively flagged records.
    negList : list
        The list of negatively flagged records.
    '''
    positive = deque([])
    negative = deque([])
    index = 0
    while index < len(data):
        if data[index][len(data[index]) - 1] == 1:
            positive.append(data[index])
        else:
            negative.append(data[index])
        index += 1
    posList = list(positive)
    negList = list(negative)
    return (posList, negList)