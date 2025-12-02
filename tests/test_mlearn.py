'''
Test module for the package/mlearn package.

Classes:

    TestMlearn

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
import unittest
from scipy import sparse

from ..package.mlearn import mlearn as m
from ..package import exceptions as e

class TestMlearn(unittest.TestCase):
    '''
    A class of tests to check the operation of the package/mlearn package.

    Attributes
    ----------
    None

    Methods
    -------
    test_noError()
        Tests that the MLearn class can be constructed and the trainAndPredict
        method can be run on valid inputs without error.
    test_argTypeError()
        Tests the MLearn constructor arguments of the wrong type cause exceptions.
    test_mlAlgTypeError()
        Tests that invlaid mlAlgType inputs cause exceptions.
    test_macLearnLackArg()
        Tests that too few elements in macLearnInput causes an exception.
    test_negativeGammaError()
        Tests that providing a negative Gamma parameter causes an exception.
    test_negativeDegreeError()
        Tests that providing a negative degree parameter causes an exception.
    test_samplingInputs()
        Test that providing invalid over/under-sampling inputs causes an exception.
    test_trainEmptyError()
        Tests that providing no train vectors, train flags or test vectors
        causes an exception.
    test_trainInputError()
        Tests that providing different amounts of train vectors to train flags
        causes an exception.
    test_trainVectorsError()
        Tests that providing train and test vectors of different lengths causes
        an exception.
    test_trainOutputLength()
        Tests that the predicted flags output is of the correct size.
    test_modelInputSize()
        Tests the using the model to predict vectors of the wrong size causes
        an exception.
    test_modelOutputResults()
        Tests the using the model to predict vectors outputs values in range.
    '''
    def test_noError(self):
        ml = m.MLearn(mlAlgType= 'DECISIONTREE',
                      macLearnInput= {'impurity' : 'gini'})
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])

        ml = m.MLearn(mlAlgType= 'DECISIONTREE', macLearnInput= {'impurity' : 'gini', 
                                                                 'other' : 7,
                                                                 'another' : 'test',
                                                                 'another other' : False})
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])

        ml = m.MLearn(mlAlgType= 'RANDOMFOREST',
                      macLearnInput= {'impurity' : 'gini',
                                      'ratio' : 0.5})

        ml = m.MLearn(mlAlgType= 'RANDOMFOREST', macLearnInput= {'impurity' : 'gini',
                                                                 'ratio' : 0.5, 
                                                                 'other' : 7,
                                                                 'another' : 'test',
                                                                 'another other' : False})

        ml = m.MLearn(mlAlgType= 'RUSBOOST',
                      macLearnInput= {'impurity' : 'gini',
                                      'ratio' : 0.5})

        ml = m.MLearn(mlAlgType= 'RUSBOOST', macLearnInput= {'impurity' : 'gini',
                                                            'ratio' : 0.5, 
                                                            'other' : 7,
                                                            'another' : 'test',
                                                            'another other' : False})

        ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'linear'})
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])

        ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])

        ml = m.MLearn(mlAlgType= 'SVMACHINE',
                      macLearnInput= {'kernel' : 'sigmoid',
                                      'gamma' : 2,
                                      'r' : 3,
                                      'other' : 7,
                                      'another' : 'test',
                                      'another other' : False})
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])

    def test_argTypeError(self):
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn(mlAlgType= 0,
                         macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.MacLearnInputException):
            _ = m.MLearn(mlAlgType= 'DECISIONTREE',
                         macLearnInput= 'not a dictionary')
        with self.assertRaises(e.OverSampleOpsException):
            _ = m.MLearn(mlAlgType= 'DECISIONTREE',
                         macLearnInput= {'impurity' : 'gini'},
                         overSampleOps= [1, 2])
        with self.assertRaises(e.UnderSampleOpsException):
            _ = m.MLearn(mlAlgType= 'DECISIONTREE',
                         macLearnInput= {'impurity' : 'gini'},
                         underSampleOps= (0, 1))
            
    def test_mlAlgTypeError(self):
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn(mlAlgType= 'invalid',
                         macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn(mlAlgType= 'decisiontree', macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn(mlAlgType= 'invalid', macLearnInput= {'kernel' : 'linear'})
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn(mlAlgType= 'svmachine', macLearnInput= {'kernel' : 'linear'})
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn(mlAlgType= '', macLearnInput= {'kernel' : 'linear'})
    
    def test_macLearnLackArg(self):
        with self.assertRaises(e.MacLearnInputException):
            _ = m.MLearn(mlAlgType= 'DECISIONTREE', macLearnInput= {})
        with self.assertRaises(e.ImpurityException):
            _ = m.MLearn(mlAlgType= 'DECISIONTREE', macLearnInput= {'impurity' : 'invalid'})

        with self.assertRaises(e.MacLearnInputException):
            _ = m.MLearn(mlAlgType= 'RANDOMFOREST',
                         macLearnInput= {})
        with self.assertRaises(e.MacLearnInputException):
            _ = m.MLearn(mlAlgType= 'RANDOMFOREST',
                         macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.MacLearnInputException):
            _ = m.MLearn(mlAlgType= 'RANDOMFOREST',
                         macLearnInput= {'ratio' : 0.5})
            
        with self.assertRaises(e.MacLearnInputException):
            _ = m.MLearn(mlAlgType= 'RUSBOOST',
                         macLearnInput= {})
        with self.assertRaises(e.MacLearnInputException):
            _ = m.MLearn(mlAlgType= 'RUSBOOST',
                         macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.MacLearnInputException):
            _ = m.MLearn(mlAlgType= 'RUSBOOST',
                         macLearnInput= {'ratio' : 0.5})

        with self.assertRaises(e.MacLearnInputException):
            _ = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {})
        with self.assertRaises(e.KernelException):
            _ = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'invalid'})    
        with self.assertRaises(e.PolynomialException):
            _ = m.MLearn(mlAlgType= 'SVMACHINE', 
                         macLearnInput= {'kernel' : 'poly', 
                                         'degree' : 3})
        with self.assertRaises(e.GammaException):
            _ = m.MLearn(mlAlgType= 'SVMACHINE', 
                         macLearnInput= {'kernel' : 'rbf'})
        with self.assertRaises(e.SigmoidException):
            _ = m.MLearn(mlAlgType= 'SVMACHINE', 
                         macLearnInput= {'kernel' : 'sigmoid', 
                                         'gamma' : 3})

    def test_negativeGammaError(self):
        with self.assertRaises(e.GammaException):
            _ = m.MLearn(mlAlgType= 'SVMACHINE',
                         macLearnInput= {'kernel' : 'sigmoid', 
                                         'gamma' : -1 ,
                                         'r' : 2})
        with self.assertRaises(e.GammaException):
            _ = m.MLearn(mlAlgType= 'SVMACHINE', 
                         macLearnInput= {'kernel' : 'rbf', 
                                        'gamma' : -1})

    def test_negativeDegreeError(self):
        with self.assertRaises(e.PolynomialException):
            _ = m.MLearn(mlAlgType= 'SVMACHINE',
                         macLearnInput= {'kernel' : 'poly', 
                                         'degree' : -1, 
                                         'r' : 1})
    
    def test_samplingInputs(self):
        with self.assertRaises(e.OverSampleOpsException):
            _ = m.MLearn(mlAlgType= 'DECISIONTREE',
                         macLearnInput= {'impurity' : 'gini'},
                         overSampleOps= {'ratio' : 0.5})
        with self.assertRaises(e.UnderSampleOpsException):
            _ = m.MLearn(mlAlgType= 'DECISIONTREE',
                         macLearnInput= {'impurity' : 'gini'},
                         underSampleOps= {'ratio' : 0.5})
        with self.assertRaises(e.OverSampleOpsException):
            _ = m.MLearn(mlAlgType= 'DECISIONTREE',
                         macLearnInput= {'impurity' : 'gini'},
                         overSampleOps= {'method' : 'invalid'})
        with self.assertRaises(e.UnderSampleOpsException):
            _ = m.MLearn(mlAlgType= 'DECISIONTREE',
                         macLearnInput= {'impurity' : 'gini'},
                         underSampleOps= {'method' : 'invalid'})
    
    def test_trainEmptyError(self):
        with self.assertRaises(e.TrainVectorsFlagsNotEqualException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([]), [0,1], sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.EmptyFlagsVectorsException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [0,1], sparse.csr_matrix([])
                )

    def test_trainInputError(self):
        with self.assertRaises(e.TrainVectorsFlagsNotEqualException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1],[0,0]]), [0,1], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.TrainVectorsFlagsNotEqualException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [0,1,0], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.EmptyFlagsVectorsException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.TrainVectorsFlagsNotEqualException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([]), [0,1], sparse.csr_matrix([[1,0],[0,0]])
                )

    def test_trainVectorsError(self):
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0],[1]]), [0,1], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                sparse.csr_matrix([[1],[0]])
                )
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[],[]]), [0,1], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                sparse.csr_matrix([[],[]])
                )

    def test_trainOutputLength(self):
        ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
        flags, _ = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        self.assertEqual(len(flags),2)
        ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
        flags, _ = ml.trainAndPredict(
            sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
            sparse.csr_matrix([[1,0],[0,0],[1,1]])
            )
        self.assertEqual(len(flags),3)

    def test_modelInputSize(self):
        ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
        _, model = ml.trainAndPredict(
            sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
            sparse.csr_matrix([[1,0],[0,0]])
            )
        _ = model.predict([[1,0]])
        with self.assertRaises(ValueError):
            _ = model.predict([[1,0,1]])
        with self.assertRaises(ValueError):
            _ = model.predict([[]])

    def test_modelOutputResults(self):
        ml = m.MLearn(mlAlgType= 'SVMACHINE', macLearnInput= {'kernel' : 'sigmoid',
                                                             'gamma' : 2,
                                                             'r' : 3})
        _, model = ml.trainAndPredict(
            sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
            sparse.csr_matrix([[1,0],[0,0]])
            )
        predictedFlags = model.predict([[1,0],[1,1],[2,1],[3,20],[0,0]])
        for flag in predictedFlags:
            self.assertTrue(flag in [0,1])

if __name__ == '__main__':
    unittest.main() 