'''
Main module of the package/evaluate package to be used in package/base.py.

Classes:

    Evaluate

Functions:

    None

Misc Variables:

    None

Exceptions:

    EmptyActualFlagsException
    EmptyPredictedFlagsException
    FlagsNotEqualException
    BadActualFlagException
    BadPredictedFlagException
    TimesSpacesNotEqualException
'''
from . import base as b
from .. import exceptions as e

class Evaluate:
    '''
    A class to be constructed in package/base.py to evaluate an NLP program.

    ...

    Attributes
    ----------
    actualFlags : list
        The flags from the test data.
    predictedFlags : list
        The NLP program's predicted flags for the test data.
    times : list
        The times taken by various processes in constructing an NLP program.
    spaces : list
        The peak memories used by various processes in constructing an NLP 
        program.

    Constructed by running the evaluate() method:
    prec : float
        The calculated precision.
    rec : float
        The calculated recall.
    totalTime : float
        Total time taken to construct the NLP program.
    totalSpace : float
        Peak memory used to construct the NLP program. 

    Methods
    -------
    evaluate() -> dict
        Sets prec, rec, totalTime and totalSpace attributes and produces a
        dictionary with the evaluation.
    '''
    def __init__(self, 
                 actualFlags : list, 
                 predictedFlags : list, 
                 times : list,
                 spaces : list):
        '''
        Checks inputs are valid and constucts acutalFlags, predictedFlags, times
        and spaces attributes for an Evaluate object.

        Parameters
        ----------
        actualFlags : list
            The flags from the test data.
        predictedFlags : list
            The NLP program's predicted flags for the test data.
        times : list
            The times taken by various processes in constructing the NLP program.
        spaces : list
            The memories used by various processes in constructing the NLP program.
        '''
        if actualFlags == []:
            raise e.EmptyActualFlagsException(
                '"actualFlags" is empty. Please provide some flags'
                )
        
        if list(predictedFlags) == []:
            raise e.EmptyPredictedFlagsException(
                '"predictedFlags" is empty. Please provide some flags'
                )

        if len(actualFlags) != len(predictedFlags):
            raise e.FlagsNotEqualException(
                '"actualFlags" and "predictedFlags" inputs'
                ' are of different lengths.'
                )
        
        actualFlags = [int(flag) for flag in actualFlags]
        predictedFlags = [int(flag) for flag in predictedFlags]

        for flag in actualFlags:
            if flag not in [0,1]:
                raise e.BadActualFlagException(
                    '"actualFlags" contains a flag not in (0,1)'
                    )
        for flag in predictedFlags:
            if flag not in [0,1]:
                raise e.BadPredictedFlagException(
                    '"predictedFlags" contains a flag not in (0,1)'
                    )
        if len(times) != len(spaces):
            raise e.TimesSpacesNotEqualException(
                'Unequal amounts of times and spaces entered.'
                )
        self.actualFlags = actualFlags
        self.predictedFlags = predictedFlags
        self.times = times
        self.spaces = spaces
    
    def evaluate(self) -> dict:
        '''
        Sets prec, rec, totalTime and totalSpace attributes and produces a
        dictionary with the evaluation.

        Parameters
        ----------
        None

        Returns
        -------
        outputDic : dict
            A dictionary containing all the information about the evaluation.
        '''
        self.prec, self.rec = b.precisionAndRecall(self.actualFlags, 
                                                   self.predictedFlags)
        self.totalTime = sum(self.times)
        self.totalSpace = max(self.spaces)

        outputDic = dict(Precision = self.prec,
                        Recall = self.rec,
                        TotalTime = self.totalTime,
                        TotalSpace = self.totalSpace,
                        ImportTime = self.times[0],
                        ImportSpace = self.spaces[0],
                        FilterTime = self.times[1],
                        FilterSpace = self.spaces[1],
                        TrainExtractTime = self.times[2],
                        TrainExtractSpace = self.spaces[2],
                        TestExtractTime = self.times[3],
                        TestExtractSpace = self.spaces[3],
                        VectoriseTime = self.times[4],
                        VectoriseSpace = self.spaces[4],
                        MLTrainingTime = self.times[5],
                        MLTrainingSpace = self.spaces[5],
                        MLPredictionTime = self.times[6],
                        MLPredictionSpace = self.spaces[6],
                        )
        return outputDic