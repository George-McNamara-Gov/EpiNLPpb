'''
Helper functions and classes to support package/evaluate/evaluate.py.

Classes:

    None

Functions:

    precisionAndRecall(list, list) -> tuple[float, float]
    f1(list, list) -> float

Misc variables:

    None

Exceptions :

    None
'''

from collections import deque
import warnings

warnings.filterwarnings("error")

def precisionAndRecall(actualFlags : list, 
                       predictedFlags : list) -> tuple[float, float]:
    '''
    Calculates the precision and recall of predicted compared to actual flags.

    Parameters
    ----------
    actualFlags : list
        List of flags extracted from the data to compare to.
    preditedFlags : list
        List of flags produced by the NLP program to evaluate.
    
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
    trueNegatives = 0
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
                trueNegatives += 1
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
        List of flags produced by the NLP program to evaluate.
    
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