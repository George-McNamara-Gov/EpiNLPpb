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
from collections import deque
from ..package import exceptions as ex

class TestEvaluate(unittest.TestCase):
    '''
    A class of tests to check the operation of the package/importer package.

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
    test_sample()
        Tests that the sample function outputs samples of the correct size.
    test_complexity()
        Tests that the complexity method calculates the correct value.
    test_CompAppError()
        Tests that having insufficiently long measureList input into Complexity
        Approximator raises an excpetion.
    test_CompAppSizes()
        Tests that the correct set of measureSizes is used.
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

    def test_sample(self):
        self.assertEqual(b.sample(0,deque(range(0,100))),[])
        self.assertEqual(len(b.sample(10,deque(range(0,100)))),10)
        self.assertEqual(len(b.sample(50,deque(range(0,100)))),50) 
        self.assertEqual(len(b.sample(100,deque(range(0,100)))),100)     
    
    def test_complexity(self):
        sizes = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000]
        func1 = lambda x : 10*x
        times = [func1(x) for x in sizes]
        self.assertTrue(0.99 < b.complexity(sizes,times) < 1.01)
        func1 = lambda x : 8*x*x
        times = [func1(x) for x in sizes]
        self.assertTrue(1.99 < b.complexity(sizes,times) < 2.01)
        func1 = lambda x : 25*x**1.5
        times = [func1(x) for x in sizes]
        self.assertTrue(1.49 < b.complexity(sizes,times) < 1.51)
        func1 = lambda x : 50*x**0.6
        times = [func1(x) for x in sizes]
        self.assertTrue(0.59 < b.complexity(sizes,times) < 0.61)
    
    def test_CompAppError(self):
        inputFunc = lambda x : x
        with self.assertRaises(ex.InsufficientMeasureListException):
            _ = b.ComplexityApproximator([], inputFunc)
        with self.assertRaises(ex.InsufficientMeasureListException):
            _ = b.ComplexityApproximator(list(range(0,199)), inputFunc)
        _ = b.ComplexityApproximator(list(range(0,200)), inputFunc)

    def test_CompAppSizes(self):
        func = lambda x : 1
        with self.assertRaises(ex.InsufficientMeasureListException):
            cp = b.ComplexityApproximator(list(range(0,100)),func)
        cp = b.ComplexityApproximator(list(range(0,900)),func)
        self.assertEqual(cp.measureSizes, [10,20,50,100,200])
        cp = b.ComplexityApproximator(list(range(0,4900)),func)
        self.assertEqual(cp.measureSizes, [20,50,100,200,500])
        cp = b.ComplexityApproximator(list(range(0,9000)),func)
        self.assertEqual(cp.measureSizes, [100,200,500,1000,2000])
        cp = b.ComplexityApproximator(list(range(0,40000)),func)
        self.assertEqual(cp.measureSizes, [200,500,1000,2000,5000])

if __name__ == '__main__':
    unittest.main()