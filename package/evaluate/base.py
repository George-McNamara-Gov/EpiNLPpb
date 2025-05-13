'''
Helper functions and classes to support package/evaluate/evaluate.py.

Classes:

    ComplexityApproximator

Functions:

    precisionAndRecall(list, list) -> tuple[float, float]
    f1(list, list) -> float
    sample(int, deque) -> list
    complexity(list, list) -> float
    measureSpace(int, function, deque) -> float
    measureTime(int, function, deque) -> float

Misc variables:

    None

Exceptions :

    InsufficientMeasureListException
'''

from . import constants as c
from collections import deque
import time
import numpy as np
import warnings
import tracemalloc
from .. import exceptions as e

warnings.filterwarnings("error")

class ComplexityApproximator:
    '''
    A class to measure the complexity of a function on a given set of inputs.

    ...

    Attributes
    ----------
    measureSizes : list
        Set of sizes to measure complexity.
    measureQue : deque
        Records to be drawn from to measure complexity.
    inputFunction : function
        The function which is having its complexity measured.

    Methods
    -------
    approxSpaceComplexity() -> float
        Approximates the space complexity of inputFunction.
    approxTimeComplexity() -> float
        Approximates the time complexity of inputFunction.
    '''

    def __init__(self, 
                 measureList : list, 
                 inputFunction):
        '''
        Checks inputs are valid, chooses measure sizes and constructs attributes
        for the ComplexityApproximator object.

        Parameters
        ----------
        measureList : list
            A list of records to be drawn from to measure complexity.
        inputFunction : function
            The function which is having its complexity measured.
        '''
        if len(measureList) < max(c.MEASURE_SIZES1):
            val = max(c.MEASURE_SIZES1)
            raise e.InsufficientMeasureListException(
                f'Measure List must provide at least {val}' 
                ' to approximate complexity'
                )
        
        self.measureSizes = c.MEASURE_SIZES4

        if len(measureList) <= 1000:
            self.measureSizes = c.MEASURE_SIZES1
        if 1000 < len(measureList) <= 5000:
            self.measureSizes = c.MEASURE_SIZES2
        if 5000 < len(measureList) <= 10000:
            self.measureSizes = c.MEASURE_SIZES3
        
        self.measureQue = deque(measureList)
        self.inputFunction = inputFunction

    def approxSpaceComplexity(self) -> float:
        '''
        Approximates the space complexity of inputFunction.

        Parameters
        ----------
        None

        Returns
        -------
        complex : float
            The approximate space complexity of inputFunction.
        '''
        spaces = [
            measureSpace(size,self.inputFunction,self.measureQue) 
            for size in self.measureSizes
            ]
        complex = complexity(self.measureSizes, spaces)
        
        return complex

    def approxTimeComplexity(self) -> float:
        '''
        Approximates the time complexity of inputFunction.

        Parameters
        ----------
        None

        Returns
        -------
        complex : float
            The approximate time complexity of inputFunction.
        '''
        times = [
            measureTime(size,self.inputFunction,self.measureQue)
            for size in self.measureSizes
            ]
        complex = complexity(self.measureSizes, times)
        
        return complex

def precisionAndRecall(actualFlags : list, 
                       predictedFlags : list) -> tuple[float, float]:
    '''
    Calculates the precision and recall of predicted compared to actual flags.

    Parameters
    ----------
    actualFlags : list
        List of flags extracted from the data to compare to.
    preditedFlags : list
        List of flags produced by the NLP program to measure.
    
    Returns
    -------
    precision : float
        The calculated precision.
    recall : float
        The calculated recall.
    '''
    truePositives = 0
    falsePositives = 0
    falseNegatives = 0
    actualQue = deque(actualFlags)
    predictedQue = deque(predictedFlags)
    while len(actualQue) > 0:
        actual = actualQue.pop()
        predicted = predictedQue.pop()
        match (actual,predicted):
            case (0,1):
                falsePositives += 1
            case (1,0):
                falseNegatives += 1
            case (1,1):
                truePositives += 1
            case _:
                pass
    if truePositives == 0:
        return (0,0)
    precision = truePositives / (truePositives + falsePositives)
    recall = truePositives / (truePositives + falseNegatives)
    return (precision, recall)

def f1(actualFlags : list, 
       predictedFlags : list) -> float:
    '''
    Calculates the f1 score based on actual and predicted flags.

    Parameters
    ----------
    actualFlags : list
        List of flags extracted from the data to compare to.
    preditedFlags : list
        List of flags produced by the NLP program to measure.
    
    Returns
    -------
    f1 : float
        The calculated f1 score.
    '''
    precision, recall = precisionAndRecall(actualFlags, predictedFlags)
    try:
        f1 = (2*precision*recall)/(precision + recall)
    except ZeroDivisionError:
        f1 = 0
    return f1

def sample(size : int, 
           source : deque) -> list:
    '''
    Produces a sample of a specific size from source.

    Parameters
    ----------
    size : int
        The number of records to include in the sample.
    source : deque
        A deque containing the records from which to sample.

    Returns
    -------
    sample : list
        A list of the specified size containing the sample records.
    '''
    sample = []
    while len(sample) < size:
        sample.append(source.pop())
    return sample

def complexity(sizes : list, 
               results : list) -> float:
    '''
    Approximates the O(n^k) complexity of the given results on the sample sizes.

    Parameters
    ----------
    sizes : list
        The sizes on which to measure time or space.
    results : list
        The corresponding time or space measurements for each size.

    Returns
    -------
    k : float
        The approximated k for O(n^k) complexity.
    '''
    logSizes = [np.log(size) for size in sizes]
    logResults = []
    for result in results:
        try:
            logRes = np.log(result)          
        except RuntimeWarning:
            print(
                'Fastest execution time is too low. ' 
                'Increase the lowest size in sizes.'
                )
            return 0
        logResults.append(logRes)
    slope, _ = np.polyfit(logSizes, logResults, 1)
    k = abs(slope)
    return k

def measureSpace(size : int, 
                 func, 
                 que : deque) -> float:
    '''
    Measures the maximum memory used to run a function on a sample of a 
    specified size.

    Parameters
    ----------
    size : int
        The specified size of the sample.
    func : function
        The function to measure.
    que : deque
        Where to extract the sample from.
    
    Returns
    -------
    space : float
        The maximum memory used to run func on the sample.
    '''
    resetMeasure = que.copy()       
    samp = sample(size, resetMeasure)
           
    tracemalloc.start()
    func(samp)
    _, space = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return space

def measureTime(size : int, 
                func, 
                que : deque) -> float:
    '''
    Measures the time taken to run a function on a sample of a 
    specified size.

    Parameters
    ----------
    size : int
        The specified size of the sample.
    func : function
        The function to measure.
    que : deque
        Where to extract the sample from.
    
    Returns
    -------
    time1 : float
        The time taken to run func on the sample.
    '''
    resetMeasure = que.copy()      
    samp = sample(size, resetMeasure)
         
    time0 = time.time()
    func(samp)
    time1 = time.time() - time0
    return time1