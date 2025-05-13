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
        Tests that the Mlearn class can be constructed and the trainAndPredict
        method can be run on valid inputs without error.
    test_mlAlgTypeError()
        Tests that invlaid mlAlgType inputs cause exceptions.
    test_macLearnInputError()
        Tests that invalid macLearnInput inputs cause exceptions.
    test_macLearnLackArg()
        Tests that too few elements in macLearnInput causes an exception.
    test_negativeGammaError()
        Tests that providing a negative Gamma parameter causes an exception.
    test_negativeDegreeError()
        Tests that providing a negative degree parameter causes an exception.
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
        ml = m.MLearn('DECISIONTREE',['GINI'])
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])
        ml = m.MLearn('DECISIONTREE',['GINI',7,'test',False])
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])
        ml = m.MLearn('SVMACHINE',['LINEAR'])
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])
        ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])
        ml = m.MLearn('SVMACHINE',['SIGMOID',2,3,7,'test',False])
        _, model = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        _ = model.predict([[1,0]])

    def test_mlAlgTypeError(self):
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn('invalid',['GINI'])
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn('decisiontree',['GINI'])
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn('invalid',['LINEAR'])
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn('svmachine',['LINEAR'])
        with self.assertRaises(e.MLAlgTypeException):
            _ = m.MLearn('',['LINEAR'])

    def test_macLearnInputError(self):
        with self.assertRaises(IndexError):
            _ = m.MLearn('DECISIONTREE',[])
        with self.assertRaises(e.ImpurityException):
            _ = m.MLearn('DECISIONTREE',['invalid'])
        with self.assertRaises(IndexError):
            _ = m.MLearn('SVMACHINE',[])
        with self.assertRaises(e.KernelException):
            _ = m.MLearn('SVMACHINE',['invalid'])
    
    def test_macLearnLackArg(self):
        with self.assertRaises(e.NoPolynomialParameterException):
            _ = m.MLearn('SVMACHINE',['POLYNOMIAL', 3])
        with self.assertRaises(e.NoRBFGammaException):
            _ = m.MLearn('SVMACHINE',['RBF'])
        with self.assertRaises(e.NoSigmoidParameterException):
            _ = m.MLearn('SVMACHINE',['SIGMOID', 3])

    def test_negativeGammaError(self):
        with self.assertRaises(e.NegSigmoidGammaException):
            _ = m.MLearn('SVMACHINE',['SIGMOID', -1 ,2])
        with self.assertRaises(e.NegRBFGammaException):
            _ = m.MLearn('SVMACHINE',['RBF', -1])

    def test_negativeDegreeError(self):
        with self.assertRaises(e.NegPolynomialDegreeException):
            _ = m.MLearn('SVMACHINE',['POLYNOMIAL', -1, 1])

    def test_trainEmptyError(self):
        with self.assertRaises(e.TrainVectorsFlagsNotEqualException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([]), [0,1], sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.EmptyFlagsVectorsException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [0,1], sparse.csr_matrix([])
                )

    def test_trainInputError(self):
        with self.assertRaises(e.TrainVectorsFlagsNotEqualException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1],[0,0]]), [0,1], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.TrainVectorsFlagsNotEqualException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [0,1,0], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.EmptyFlagsVectorsException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.TrainVectorsFlagsNotEqualException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([]), [0,1], sparse.csr_matrix([[1,0],[0,0]])
                )

    def test_trainVectorsError(self):
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0],[1]]), [0,1], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                sparse.csr_matrix([[1],[0]])
                )
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[],[]]), [0,1], 
                sparse.csr_matrix([[1,0],[0,0]])
                )
        with self.assertRaises(e.VectorsNotEqualException):
            ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
            _, _ = ml.trainAndPredict(
                sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                sparse.csr_matrix([[],[]])
                )

    def test_trainOutputLength(self):
        ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
        flags, _ = ml.trainAndPredict(sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
                                      sparse.csr_matrix([[1,0],[0,0]]))
        self.assertEqual(len(flags),2)
        ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
        flags, _ = ml.trainAndPredict(
            sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
            sparse.csr_matrix([[1,0],[0,0],[1,1]])
            )
        self.assertEqual(len(flags),3)

    def test_modelInputSize(self):
        ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
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
        ml = m.MLearn('SVMACHINE',['SIGMOID',2,3])
        _, model = ml.trainAndPredict(
            sparse.csr_matrix([[0,1],[1,1]]), [0,1], 
            sparse.csr_matrix([[1,0],[0,0]])
            )
        predictedFlags = model.predict([[1,0],[1,1],[2,1],[3,20],[0,0]])
        for flag in predictedFlags:
            self.assertTrue(flag in [0,1])

if __name__ == '__main__':
    unittest.main() 