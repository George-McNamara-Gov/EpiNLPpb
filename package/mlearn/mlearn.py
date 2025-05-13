'''
Main module of the package/mlearn package to be used in package/base.

Classes:

    MLearn

Functions:

    None

Misc variables:

    None

Exceptions:

    MLAlgTypeException
    ImpurityException
    KernelException
    NoRBFGammaException
    NegRBFGammaException
    NoPolynomialParameterException
    NegPolynomialDegreeException
    NoSigmoidParameterException
    NegSigmoidGammaException
    EmptyFlagsVectorsException
    TrainVectorsFlagsNotEqualException
    VectorsNotEqualException
    NotEnoughClassesException
'''
from sklearn import tree
from sklearn import svm
from scipy import sparse
from .. import base
from .. import exceptions as e
from typing import Union

class MLearn:
    '''
    A class to be constructed in package/base to produce a trained ML algorithm
    and predict flags on text data.

    ...

    Attributes
    ----------
    trainedModel : Union[tree.DecisionTreeClassifier, svm.SVC]
        The trained machine learning model used to predict flags.
    
    Constructed by running trainAndPredict() method:
    trainingTime : float
        Time taken to train the model.
    trainingSpace : float
        Peak memory used to train the model.
    predictionTime : float
        Time taken to predict testing flags using the model.
    predictionSpace : float
        Peak memory used to predict testing flags using the model.

    Methods
    -------
    trainAndPredict(sparse.csr_matrix,list,sparse.csr_matrix) -> 
        tuple[list, Union[tree.DecisionTreeClassifier, svm.SVC]]
        Creates trained ML algorithm and uses it to produce predicted flags.
    '''

    def __init__(self, 
                 mlAlgType : str, 
                 macLearnInput : list):
        '''
        Checks inputs are valid and constructs attributes for MLearn object.

        Parameters
        ----------
        mlAlgType : str
            The name of the type of ML algorithm to be used.
        macLearnInput : list
            A list of input parameters relevant to the type of ML algorithm.
        '''
        if mlAlgType not in ['DECISIONTREE', 'SVMACHINE']:
            raise e.MLAlgTypeException(
                'The Machine Learning Algorithm type must be "DECISIONTREE" '
                'or "SVMACHINE"'
                )
        if mlAlgType == 'DECISIONTREE':
            if macLearnInput[0] not in ['GINI', 'ENTROPY', 'LOGLOSS']:
                raise e.ImpurityException(
                    'Criterion must be "GINI", "ENTROPY" or "LOGLOSS"'
                    )
            match macLearnInput[0]:
                case 'GINI':
                    self.trainedModel = tree.DecisionTreeClassifier(
                        criterion='gini'
                        )
                case 'ENTROPY':
                    self.trainedModel = tree.DecisionTreeClassifier(
                        criterion='entropy'
                        )
                case 'LOGLOSS':
                    self.trainedModel = tree.DecisionTreeClassifier(
                        criterion='log_loss'
                        )

        if mlAlgType == 'SVMACHINE':
            if macLearnInput[0] not in ['LINEAR', 
                                        'RBF', 
                                        'POLYNOMIAL', 
                                        'SIGMOID']:
                raise e.KernelException(
                    'Kernel must be "LINEAR", "RBF", "POLYNOMIAL" or "SIGMOID"'
                                )
            match macLearnInput[0]:
                case 'LINEAR':
                    self.trainedModel = svm.SVC(kernel='linear')
                case 'RBF':
                    if len(macLearnInput) < 2:
                        raise e.NoRBFGammaException(
                            'Need to specify a Gamma parameter.'
                        )
                    if macLearnInput[1] not in ['auto', 'scale']:
                        if macLearnInput[1] <= 0:
                            raise e.NegRBFGammaException(
                                'Gamma parameter must be greater than 0.'
                                )
                    self.trainedModel = svm.SVC(kernel='rbf', 
                                                gamma= macLearnInput[1])
                case 'POLYNOMIAL':
                    if len(macLearnInput) < 3:
                        raise e.NoPolynomialParameterException(
                            'Need to specify a degree and r parameter'
                        )
                    if macLearnInput[1] < 1:
                        raise e.NegPolynomialDegreeException(
                            'Degree must be greater than or equal to 0.'
                            )
                    self.trainedModel = svm.SVC(kernel='poly', 
                                                degree= macLearnInput[1], 
                                                coef0= macLearnInput[2])
                case 'SIGMOID':
                    if len(macLearnInput) < 3:
                        raise e.NoSigmoidParameterException(
                            'Need to specify a Gamma and r parameter'
                        )
                    if macLearnInput[1] not in ['auto', 'scale']:
                        if macLearnInput[1] <= 0:
                            raise e.NegSigmoidGammaException(
                                'Gamma parameter must be greater than 0.'
                                )
                    self.trainedModel = svm.SVC(kernel='sigmoid', 
                                                gamma= macLearnInput[1], 
                                                coef0= macLearnInput[2])

    def trainAndPredict(self, 
                        trainVectors : sparse.csr_matrix, 
                        trainFlags : list, 
                        testVectors : sparse.csr_matrix) -> tuple[list, Union[tree.DecisionTreeClassifier, svm.SVC]]:
        '''
        Creates trained ML algorithm and uses it to produce predicted flags.

        Parameters
        ----------
        trainVectors : sparse.csr_matrix
            A list of vectorised training data.
        trainFlags : list
            The flags associated with the test data.
        testVectors : sparse.cst_matrix
            A list of vectorised test data.

        Returns
        -------
        predictedFlags : list
            The predicted flags for the test data.
        trainedModel : Union[tree.DecisionTreeClassifier, svm.SVC]
            Trained ML model.
        '''
        if trainVectors == [] or trainFlags == [] or testVectors == []:
            raise e.EmptyFlagsVectorsException(
                'Cannot have any empty inputs.'
            )
        
        if trainVectors.shape[0] != len(trainFlags):
            raise e.TrainVectorsFlagsNotEqualException(
                '"trainVectors" and "trainFlags" must be the same length.'
                )
        
        if trainVectors.shape[1] != testVectors[0].shape[1]:
            raise e.VectorsNotEqualException(
                '"trainVectors" entries and "testVectors" entries must be the '
                'same length.'
            )
        
        print('Training Machine Learning Algorithm...')
        time0 = base.startRec()
        try:
            self.trainedModel.fit(trainVectors, trainFlags)
        except ValueError:
            raise e.NotEnoughClassesException(
                'Records are all of the same class. Provide more records.'
            )
        self.trainingTime, self.trainingSpace = base.stopRec(time0)

        print('Predicting with Machine Learning Algorithm...')
        time0 = base.startRec()
        predictedFlags = self.trainedModel.predict(testVectors)
        self.predictionTime, self.predictionSpace = base.stopRec(time0)

        return (predictedFlags, self.trainedModel)