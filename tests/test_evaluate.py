'''
Test module for the package/evaluate package.

Classes:

    TestEvaluate

Functions:

    None

Misc Variables:

    None

Exceptions:

    None   
'''
import unittest

from ..package.evaluate import evaluate as e
from ..package.evaluate import base as b
from ..package import exceptions as ex

class TestEvaluate(unittest.TestCase):
    '''
    A class of tests to check the operation of the package/evaluate package.

    Attributes
    ----------
    None

    Methods
    -------
    test_noError()
        Tests that the Evaluate class can be constructed and the evaluate method
        can run without errors on valid inputs.
    test_emptyFlagsError()
        Test that having an empty actualFlags or predictedFalgs input raises an 
        exception.
    test_flagError()
        Tests that having different sized actualFalgs and predictedFlags inputs 
        raises an exception. Also tests the having an entry which is not 0 or 1 
        in either actualFlags or predictedFalgs raises an exception. 
    test_timeSpaceError()
        Tests that having different sized times and spaces inputs raises an 
        exception.
    test_evalDict()
        Tests that the dictionary output from the evaluate method has the 
        correct number of entries with the correct keys.
    test_precAndRec()
        Tests that precisionAndRecall function calculates the correct values.
    '''

    def test_noError(self):
        eval = e.Evaluate([0,1],
                          [1,0],
                          [2.3,2.5,1.1,3.4,3,3,3,3],
                          [1000,2000,3000,500,500,500,500,500])
        eval.evaluate()

    def test_emptyFlagsError(self):
        with self.assertRaises(ex.EmptyActualFlagsException):
            _ = e.Evaluate([],[],[],[])
        with self.assertRaises(ex.EmptyActualFlagsException):
            _ = e.Evaluate([],[],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.EmptyActualFlagsException):
            _ = e.Evaluate([],[1],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.EmptyPredictedFlagsException):
            _ = e.Evaluate([0],[],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.EmptyActualFlagsException):
            _ = e.Evaluate([],[1],[],[])
        with self.assertRaises(ex.EmptyPredictedFlagsException):
            _ = e.Evaluate([0],[],[],[])
        
    def test_flagError(self):
        with self.assertRaises(ex.EmptyActualFlagsException):
            _ = e.Evaluate([],[1],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.EmptyPredictedFlagsException):
            _ = e.Evaluate([1],[],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.FlagsNotEqualException):
            _ = e.Evaluate([1],[1,0],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.FlagsNotEqualException):
            _ = e.Evaluate([1,0],[1],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500])
        with self.assertRaises(ex.BadActualFlagException):
            _ = e.Evaluate([2],[1],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.BadPredictedFlagException):
            _ = e.Evaluate([1],[2],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.BadActualFlagException):
            _ = e.Evaluate([2],[2],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])

    def test_timeSpaceError(self):
        with self.assertRaises(ex.TimesSpacesNotEqualException):
            _ = e.Evaluate([0,1],[1,0],[],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.TimesSpacesNotEqualException):
            _ = e.Evaluate([0,1],[1,0],[2.3,2.5,1.1,3.4,3.0,3,3,3,3],[])
        with self.assertRaises(ex.TimesSpacesNotEqualException):
            _ = e.Evaluate([0,1],[1,0],[2.3,2.5,1.1,3.4,3.0,3,3,3,3],
                              [1000,2000,3000,500,500,500,500,500])
        with self.assertRaises(ex.TimesSpacesNotEqualException):
            _ = e.Evaluate([0,1],[1,0],[2.3,2.5,1.1,3.4,3,3,3,3],
                              [1000,2000,3000,500,4000,500,500,500,500])
        _ = e.Evaluate([0,1],[1,0],[],[])

    def test_evalDict(self):
        eval = e.Evaluate([0,1],[1,0],[2.3,2.5,1.1,3.4,3,3,3,3],
                          [1000,2000,3000,500,500,500,500,500])
        dict = eval.evaluate()
        self.assertEqual(len(dict),18)
        self.assertNotEqual(dict.get('Precision','no key'), 'no key')
        self.assertNotEqual(dict.get('Recall','no key'), 'no key')
        self.assertNotEqual(dict.get('TotalTime','no key'), 'no key')
        self.assertNotEqual(dict.get('TotalSpace','no key'), 'no key')
        self.assertNotEqual(dict.get('ImportTime','no key'), 'no key')
        self.assertNotEqual(dict.get('ImportSpace','no key'), 'no key')
        self.assertNotEqual(dict.get('FilterTime','no key'), 'no key') 
        self.assertNotEqual(dict.get('FilterSpace','no key'), 'no key') 
        self.assertNotEqual(dict.get('TrainExtractTime','no key'), 'no key') 
        self.assertNotEqual(dict.get('TrainExtractSpace','no key'), 'no key') 
        self.assertNotEqual(dict.get('TestExtractTime','no key'), 'no key') 
        self.assertNotEqual(dict.get('TestExtractSpace','no key'), 'no key') 
        self.assertNotEqual(dict.get('VectoriseTime','no key'), 'no key') 
        self.assertNotEqual(dict.get('VectoriseSpace','no key'), 'no key')  
        self.assertNotEqual(dict.get('MLTrainingTime','no key'), 'no key') 
        self.assertNotEqual(dict.get('MLTrainingSpace','no key'), 'no key') 
        self.assertNotEqual(dict.get('MLPredictionTime','no key'), 'no key') 
        self.assertNotEqual(dict.get('MLPredictionSpace','no key'), 'no key')

    def test_precAndRec(self):
        actual =    [0,0,0,0,1,1,1,1,1]
        predicted = [0,0,0,1,1,1,0,0,1]
        precision, recall = b.precisionAndRecall(actual, predicted)
        self.assertEqual(precision, 3 / (3 + 1))
        self.assertEqual(recall, 3 / (3 + 2))

if __name__ == '__main__':
    unittest.main()