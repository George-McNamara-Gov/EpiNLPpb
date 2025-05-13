'''
Main module of the package/evaluate package to be used in package/base.

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
from . import constants as c
from . import base as b
import matplotlib.pyplot as plt
import numpy as np
from .. import exceptions as e

class Evaluate:
    '''
    A class to be constructed in package/base to evaluate the NLP program.

    ...

    Attributes
    ----------
    actualFlags : list
        The flags from the test data.
    predictedFlags : list
        The NLP program's predicted flags for the test data.
    times : list
        The time taken by various processes in constructing the NLP program.
    spaces : list
        The peak memory used by various processes in constructing the NLP 
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
    radialPlot()
        Displays a radial plot of the key evaluation measures.
    timeSpace()
        Displays a breakdown of time and space usage.
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
            The time taken by various processes in constructing the NLP program.
        spaces : list
            The memory used by various processes in constructing the NLP program.
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
    
    def radialPlot(self):
        '''
        Displays a radial plot of the key evaluation measures.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        values = [self.prec, self.rec, 1 - self.totalTime / c.TIME_MAX,
                  1 - self.totalSpace / c.SPACE_MAX, self.prec]
        labels = ['Precision','Recall','Normalised Time','Normalise Memory']
        plt.figure(figsize=(10, 6))
        plt.subplot(polar=True)
        theta = np.linspace(0, 2 * np.pi, len(values))
        _, _ = plt.thetagrids(
            range(0, 360, int(360/len(labels))), (labels)
            )
        plt.plot(theta, values)
        plt.fill(theta, values, 'b', alpha=0.1)
        plt.show()
  
    def timeSpacePlot(self):
        '''
        Displays a breakdown of time and space usage.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        labels = ['Import', 
            'Filter', 
            'Training Data \n Extraction', 
            'Testing Data \n Extraction',
            'Data \n Vectorise',
            'ML Algorithm \n Training',
            'ML Algorithm \n Prediction',
            'Evaluation']
        
        self.spaces = [space/(1024*1024) for space in self.spaces]
        
        fig, ax1 = plt.subplots()

        X_axis = np.arange(len(labels))

        color = 'tab:red'
        ax1.set_xlabel('Process')
        ax1.set_ylabel('Time taken (s)', color=color)
        ax1.bar(X_axis - 0.2, self.times, width= 0.4, color=color)
        ax1.tick_params(axis='y', labelcolor=color)
        ax1.set(xticks=(list(range(0,8))))
        ax1.set(xticklabels=(labels))

        ax2 = ax1.twinx()

        color = 'tab:blue'
        ax2.set_ylabel('Peak memory used (MB)', color=color)
        ax2.bar(X_axis + 0.2, self.spaces, width = 0.4, color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()
        plt.show()