'''
Main module of the package/mlearn package to be used in package/base.py.

Classes:

    MLearn

Functions:

    startRec() -> float
    stopRec -> (float, float)

Misc variables:

    None

Exceptions:

    MLearnException
    MLAlgTypeException
    MacLearnInputException
    OverSampleOpsException
    UnderSampleOpsException
    ImpurityException
    RatioException
    NEstimatorsException
    LearningRateException
    MaxDepthException
    MinSamplesException
    KernelException
    CArgException
    GammaException
    PolynomialException
    SigmoidException
    EmptyFlagsVectorsException
    TrainVectorsFlagsNotEqualException
    VectorsNotEqualException
'''
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from imblearn.ensemble import BalancedRandomForestClassifier, RUSBoostClassifier
from imblearn.over_sampling import SMOTE, BorderlineSMOTE, ADASYN
from imblearn.under_sampling import TomekLinks, ClusterCentroids, NeighbourhoodCleaningRule, RandomUnderSampler
from scipy import sparse
from typing import Union
import copy
import time
import tracemalloc
from .. import exceptions as e

class MLearn:
    '''
    A class to be constructed in package/base.py to produce a trained ML algorithm
    and predict flags on test data.

    ...

    Attributes
    ----------
    Constructed by running the initialise() method:
    class_weight : dict
        The relative weights for the different classification classes.
    trainedModel : Union[DecisionTreeClassifier,
                        BalancedRandomForestClassifier,
                        RUSBoostClassifier,
                        SVC]
        The trained machine learning model used to predict flags.
    overSampleOps : dict
        A dictionary of input parameters relavent to over-sampling.
    underSampleOps : dict
        A dictionary of input parameters relavent to under-sampling.
    untrainedModel : Union[DecisionTreeClassifier,
                          BalancedRandomForestClassifier,
                          RUSBoostClassifier,
                          SVC]
        An untrained copy of the trainedModel attribute.
    
    Constructed by running the trainAndPredict() method:
    trainVectors : sparse.csr_matrix
        Vectorised training records.
    trainFlags : list
        Classification flags associated with training vectors.
    testVectors : sparse.csr_matrix
        Vectorised testing records.
    testFlags : list
        Classification flags associated with testing vectors.
    sampledTrainVectors : sparse.csr_matrix
        Over/under-sampled training vectors.
    sampledTrainFlags : list
        Over/under-sampled training flags.
    trainingTime : float
        Time taken to train the model.
    trainingSpace : float
        Peak memory used to train the model.
    predictionTime : float
        Time taken to predict testing flags using the model.
    predictionSpace : float
        Peak memory used to predict testing flags using the model.
    predictedFlags : list
        The predicted testing flags.
    
    Methods
    -------
    initialise(str, dict, dict, dict)
        Checks constructor inputs and creates attributes.
    overSample(sparse.csr_matrix, list) -> (sparse.csr_matrix, list)
        Applies over-sampling to training vectors.
    underSample(sparse.csr_matrix, list) -> (sparse.csr_matrix, list)
        Applies under-sampling to training vectors.
    trainAndPredict(sparse.csr_matrix, list, sparse.csr_matrix) -> 
        tuple[list, Union[DecisionTreeClassifier,
                          BalancedRandomForestClassifier,
                          RUSBoostClassifier,
                          SVC]]
        Creates trained ML algorithm and uses it to produce predicted flags.
    '''

    def __init__(self,
                 arg_dict : dict = None, 
                 mlAlgType : str = '', 
                 macLearnInput : dict = {},
                 overSampleOps : dict = {},
                 underSampleOps : dict = {}):
        '''
        Passes inputs from either arg_dict or keyword arguments.

        Parameters
        ----------
        arg_dict : dict
            A dictionary containing constructor arguments.
        mlAlgType : str
            The name of the type of ML algorithm to be used.
        macLearnInput : dict
            A dictionary of input parameters relavent to the type of ML algorithm.
        overSampleOps : dict
            A dictionary of input parameters relavent to over-sampling.
        underSampleOps : dict
            A dictionary of input parameters relavent to under-sampling.
        '''
        if arg_dict is not None:
            if not isinstance(arg_dict, dict):
                raise e.MLearnException(
                    'arg_dict must be a dictionary.'
                )
            
            if 'mlAlgType' not in arg_dict:
                raise e.MLAlgTypeException(
                    'When arg_dict is not None, it must have a mlAlgType key.'
                )
            else:
                mlAlgType = arg_dict['mlAlgType']
            if 'macLearnInput' not in arg_dict:
                raise e.MacLearnInputException(
                    'When arg_dict is not None, it must have a macLearnInput key.'
                )
            else:
                macLearnInput = arg_dict['macLearnInput']
            if 'overSampleOps' in arg_dict:
                overSampleOps = arg_dict['overSampleOps']
            if 'underSampleOps' in arg_dict:
                underSampleOps = arg_dict['underSampleOps']

        self.initialise(mlAlgType,
                        macLearnInput,
                        overSampleOps,
                        underSampleOps)         

    def initialise(self,
                   mlAlgType : str = '', 
                   macLearnInput : dict = {},
                   overSampleOps : dict = {},
                   underSampleOps : dict = {}):
        '''
        Checks constructor inputs and creates attributes.

        Parameters
        ----------
        mlAlgType : str
            The name of the type of ML algorithm to be used.
        macLearnInput : dict
            A dictionary of input parameters relavent to the type of ML algorithm.
        overSampleOps : dict
            A dictionary of input parameters relavent to over-sampling.
        underSampleOps : dict
            A dictionary of input parameters relavent to under-sampling.
        
        Returns
        -------
        None
        '''
        if not isinstance(mlAlgType, str):
            raise e.MLAlgTypeException(
                'mlAlgType must be a string.'
            )
        if not isinstance(macLearnInput, dict):
            raise e.MacLearnInputException(
                'macLearnInput must be a dictionary.'
            )
        if not isinstance(overSampleOps, dict):
            raise e.OverSampleOpsException(
                'overSampleOps must be a dictionary.'
            )
        if not isinstance(underSampleOps, dict):
            raise e.UnderSampleOpsException(
                'underSampleOps must be a dictionary.'
            )
        
        if 'impurity' in macLearnInput:
            if not isinstance(macLearnInput['impurity'], str):
                raise e.ImpurityException(
                    'impurity must be a string.'
                )
            if macLearnInput['impurity'] not in ['gini', 'entropy', 'log_loss']:
                raise e.ImpurityException(
                'impurity must be "gini", "entropy" or "log_loss"'
                )
        
        if 'ratio' in macLearnInput:
            if not isinstance(macLearnInput['ratio'], float):
                raise e.RatioException(
                    'ratio must be a float.'
                )
            if not (0 < macLearnInput['ratio'] < 1):
                raise e.RatioException(
                    'ratio must be strictly between 0 and 1.'
                )
            
        if 'n_estimators' in macLearnInput:
                if not isinstance(macLearnInput['n_estimators'], int):
                    raise e.NEstimatorsException(
                        'n_estimators must be an int.'
                    )
                if macLearnInput['n_estimators'] <= 0:
                    raise e.NEstimatorsException(
                        'n_estimators must be positive.'
                    )
                
        if 'learning_rate' in macLearnInput:
            if not isinstance(macLearnInput['learning_rate'], float | int):
                raise e.LearningRateException(
                    'learning_rate must be an int or a float.'
                )
            if macLearnInput['learning_rate'] <= 0:
                raise e.LearningRateException(
                    'learning_rate must be positive.'
                )
        
        if 'max_depth' in macLearnInput:
            if not isinstance(macLearnInput['max_depth'], int):
                raise e.MaxDepthException(
                    'max_depth must be an int.'
                )
            if macLearnInput['max_depth'] < 1:
                raise e.MaxDepthException(
                    'max_depth must be greater than or equal to 1.'
                )
            
        if 'min_samples_split' in macLearnInput:
            if not isinstance(macLearnInput['min_samples_split'], int):
                raise e.MinSamplesException(
                    'min_samples_split must be an int.'
                )
            if macLearnInput['min_samples_split'] < 0:
                raise e.MinSamplesException(
                    'min_samples_split must be greater than or equal to 0.'
                )
        
        if 'kernel' in macLearnInput:
            if not isinstance(macLearnInput['kernel'], str):
                raise e.KernelException(
                    'kernel must be a string.'
                )
            
        if 'C' in macLearnInput:
            if not isinstance(macLearnInput['C'], float | int):
                raise e.CArgException(
                    'C must be an int or a float'
                )
            if macLearnInput['C'] <= 0:
                raise e.CArgException(
                    'C must be greater than 0.'
                )
            
        if 'gamma' in macLearnInput:
            if macLearnInput['gamma'] not in ['auto', 'scale'] and not isinstance(macLearnInput['gamma'], float | int):
                raise e.GammaException(
                    'gamma must be auto, scale, an int, or a float.'
                )
            if isinstance(macLearnInput['gamma'], float | int) and macLearnInput['gamma'] <= 0:
                raise e.GammaException(
                    'gamma parameter must be greater than 0.'
                    )
            
        if 'degree' in macLearnInput:
            if not isinstance(macLearnInput['degree'], int):
                raise e.PolynomialException(
                    'degree must be an int.'
                )
            if macLearnInput['degree'] < 1:
                raise e.PolynomialException(
                    'degree must be greater than or equal to 1.'
                )
            
        if 'r' in macLearnInput:
            if not isinstance(macLearnInput['r'], float | int):
                raise e.SigmoidException(
                    'r must be an int or a float.'
                )

        if 'class_weight' in macLearnInput:
            if not isinstance(macLearnInput['class_weight'], dict):
                raise e.MacLearnInputException(
                    'class_weight must be a dictionary.'
                )
            if 0 not in macLearnInput['class_weight']:
                raise e.MacLearnInputException(
                    'class_weight must have a 0 key.'
                )
            if not isinstance(macLearnInput['class_weight'][0], int | float):
                raise e.MacLearnInputException(
                    'class_weight 0 must be an int or a float.'
                )
            if 1 not in macLearnInput['class_weight']:
                raise e.MacLearnInputException(
                    'class_weight must have a 1 key.'
                )
            if not isinstance(macLearnInput['class_weight'][1], int | float):
                raise e.MacLearnInputException(
                    'class_weight 1 must be an int or a float.'
                )
            self.class_weight = macLearnInput['class_weight']
        else:
            self.class_weight = None

        match mlAlgType:
            case 'DECISIONTREE':
                if 'impurity' not in macLearnInput:
                    raise e.MacLearnInputException(
                        'When mlAlgType is DECISIONTREE, macLearnInput must ',
                        'have an impurity key.'
                    )

                args = {'criterion' : macLearnInput['impurity']}
                if self.class_weight is not None:
                    args['class_weight'] = self.class_weight
                if 'max_depth' in macLearnInput:
                    args['max_depth'] = macLearnInput['max_depth']
                if 'min_samples_split' in macLearnInput:
                    args['min_samples_split'] = macLearnInput['min_samples_split']

                self.trainedModel = DecisionTreeClassifier(
                    random_state= 42,
                    **args
                )

            case 'RANDOMFOREST':
                if 'impurity' not in macLearnInput:
                    raise e.MacLearnInputException(
                        'When mlAlgType is RANDOMFOREST, macLearnInput must ',
                        'have an impurity key.'
                    )
                
                if 'ratio' not in macLearnInput:
                    raise e.MacLearnInputException(
                        'When mlAlgType is RANDOMFOREST, macLearnInput must',
                        'have a ratio key.'
                    )
   
                args = {'criterion' : macLearnInput['impurity'],
                        'sampling_strategy' : macLearnInput['ratio']}
                
                if self.class_weight is not None:
                    args['class_weight'] = self.class_weight
                if 'n_estimators' in macLearnInput:
                    args['n_estimators'] = macLearnInput['n_estimators']
                if 'max_depth' in macLearnInput:
                    args['max_depth'] = macLearnInput['max_depth']
                if 'min_samples_split' in macLearnInput:
                    args['min_samples_split'] = macLearnInput['min_samples_split']
                
                self.trainedModel = BalancedRandomForestClassifier(n_jobs= -1,
                                                                   random_state= 42,
                                                                   **args)

            case 'RUSBOOST':
                if 'impurity' not in macLearnInput:
                    raise e.MacLearnInputException(
                        'When mlAlgType is RUSBOOST, macLearnInput must ',
                        'have an impurity key.'
                    )
                
                if 'ratio' not in macLearnInput:
                    raise e.MacLearnInputException(
                        'When mlAlgType is RUSBOOST, macLearnInput must',
                        'have a ratio key.'
                    )
                    
                estimator_args = {'criterion' : macLearnInput['impurity']}

                if self.class_weight is not None:
                    estimator_args['class_weight'] = self.class_weight
                if 'max_depth' in macLearnInput:
                    estimator_args['max_depth'] = macLearnInput['max_depth']
                if 'min_samples_split' in macLearnInput:
                    estimator_args['min_samples_split'] = macLearnInput['min_samples_split']

                args = {'estimator' : DecisionTreeClassifier(**estimator_args),
                        'sampling_strategy' : macLearnInput['ratio']}
                
                if 'n_estimators' in macLearnInput:
                    args['n_estimators'] = macLearnInput['n_estimators']
                if 'learning_rate' in macLearnInput:
                    args['learning_rate'] = macLearnInput['learning_rate']

                self.trainedModel = RUSBoostClassifier(random_state= 42,
                                                       **args)

            case 'SVMACHINE':
                if 'kernel' not in macLearnInput:
                    raise e.MacLearnInputException(
                        'When mlAlgType is SVMACHINE, macLearnInput must have ',
                        'a kernel key.'
                    )              

                args = {'kernel' : macLearnInput['kernel']}
                if self.class_weight is not None:
                    args['class_weight'] = self.class_weight
                if 'C' in macLearnInput:
                    args['C'] = macLearnInput['C']
                
                match macLearnInput['kernel']:
                    case 'linear':
                        pass
                    
                    case 'rbf':
                        if 'gamma' not in macLearnInput:
                            raise e.GammaException(
                                'Need to specify a gamma parameter.'
                            )
                        args['gamma'] = macLearnInput['gamma']
                        
                    case 'poly':
                        if 'degree' not in macLearnInput or 'r' not in macLearnInput:
                            raise e.PolynomialException(
                                'Need to specify a degree and r parameter.'
                            )
                        args['degree'] = macLearnInput['degree']
                        args['coef0'] = macLearnInput['r']
                        
                    case 'sigmoid':
                        if 'gamma' not in macLearnInput or 'r' not in macLearnInput:
                            raise e.SigmoidException(
                                'Need to specify a gamma and r parameters.'
                            )
                        args['gamma'] = macLearnInput['gamma']
                        args['coef0'] = macLearnInput['r']
                        
                    case _ :
                        raise e.KernelException(
                        'Kernel must be in linear, rbf, poly, or sigmoid.'
                                    )
                    
                self.trainedModel = SVC(random_state= 42,
                                        **args)

            case _:
                raise e.MLAlgTypeException(
                    f'{mlAlgType} is not a valid mlAlgType.'
                )

        if overSampleOps != {}:
            if 'method' not in overSampleOps:
                raise e.OverSampleOpsException(
                    'If overSampleOps is not {}, it must contain a method key.'
                )
            if overSampleOps['method'] not in ['SMOTE', 'BorderSMOTE', 'ADASYN']:
                raise e.OverSampleOpsException(
                    'method must be SMOTE, BorderSMOTE, or ADASYN.'
                )
            if 'ratio' in overSampleOps:
                if not isinstance(overSampleOps['ratio'], float | int):
                    raise e.OverSampleOpsException(
                        'ratio must be an int or a float.'
                    )
                if overSampleOps['ratio'] >= 1 or overSampleOps['ratio'] <= 0:
                    raise e.OverSampleOpsException(
                        'ratio must be positive and less than or equal to 1.'
                    )
            if 'n_neighbors' in overSampleOps:
                if not isinstance(overSampleOps['n_neighbors'], int):
                    raise e.OverSampleOpsException(
                        'n_neighbors must be an int.'
                    )
            if 'kind' in overSampleOps:
                if not overSampleOps['kind'] in ['borderline-1', 'borderline-2']:
                    raise e.OverSampleOpsException(
                        'kind must be "borderline-1" or "borderline-2".'
                    )

        if underSampleOps != {}:
            if 'method' not in underSampleOps:
                raise e.UnderSampleOpsException(
                    'If underSampleOps is not {}, it must contain a method key.'
                )
            if underSampleOps['method'] not in ['RandomUnder', 'Tomek', 'ClusterCentroid', 'NCL']:
                raise e.UnderSampleOpsException(
                    'method must be RandomUnder, Tomek, ClusterCentroid, or NCL.' 
                )
            if 'ratio' in underSampleOps:
                if not isinstance(underSampleOps['ratio'], float | int):
                    raise e.UnderSampleOpsException(
                        'ratio must be an int or a float.'
                    )
                if underSampleOps['ratio'] > 1 or underSampleOps['ratio'] <= 0:
                    raise e.UnderSampleOpsException(
                        'ratio must be positive and less than or equal to 1.'
                    )
            if 'n_neighbors' in underSampleOps:
                if not isinstance(underSampleOps['n_neighbors'], int):
                    raise e.UnderSampleOpsException(
                        'n_neighbors must be an int.'
                    )
            if 'voting' in underSampleOps:
                if not underSampleOps['voting'] in ['hard', 'soft']:
                    raise e.UnderSampleOpsException(
                        'voting must be "hard" or "soft".'
                    )
     
        self.overSampleOps = overSampleOps
        self.underSampleOps = underSampleOps

        self.untrainedModel = copy.copy(self.trainedModel)
                    
    def overSample(self, trainVectors : sparse.csr_matrix, trainFlags : list) -> tuple[sparse.csr_matrix, list]:
        '''
        Applies over-sampling to training vectors.

        Parameters
        ----------
        trainVectors : sparse.csr_matrix
            Input training vectors.
        trainFlags : list
            Classification flags associated with training vectors.

        Returns
        -------
        trainVectors : sparse.csr_matrix
            Over-sampled training vectors.
        trainFlags : list
            Classification flags associated with over-sampled training vectors.
        '''
        match self.overSampleOps['method']:
            case 'SMOTE':
                if 'ratio' in self.overSampleOps:
                    if 'n_neighbors' in self.overSampleOps:
                        smote = SMOTE(sampling_strategy= self.overSampleOps['ratio'], 
                                      k_neighbors= self.overSampleOps['n_neighbors'], 
                                      random_state= 42)
                        trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                    else:
                        smote = SMOTE(sampling_strategy= self.overSampleOps['ratio'], 
                                      random_state= 42)
                        trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                else:
                    if 'n_neighbors' in self.overSampleOps:
                        smote = SMOTE(k_neighbors= self.overSampleOps['n_neighbors'],
                                      random_state= 42)
                        trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                    else:
                        smote = SMOTE(random_state= 42)
                        trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                        
            case 'BorderSMOTE':
                if 'ratio' in self.overSampleOps:
                    if 'n_neighbors' in self.overSampleOps:
                        if 'kind' in self.overSampleOps:
                            smote = BorderlineSMOTE(sampling_strategy= self.overSampleOps['ratio'],
                                                    k_neighbors = self.overSampleOps['n_neighbors'],
                                                    kind = self.overSampleOps['kind'], 
                                                    random_state= 42)
                            trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                        else:
                            smote = BorderlineSMOTE(sampling_strategy= self.overSampleOps['ratio'],
                                                    k_neighbors = self.overSampleOps['n_neighbors'], 
                                                    random_state= 42)
                            trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                    else:
                        if 'kind' in self.overSampleOps:
                            smote = BorderlineSMOTE(sampling_strategy= self.overSampleOps['ratio'],
                                                    kind = self.overSampleOps['kind'], 
                                                    random_state= 42)
                            trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                        else:
                            smote = BorderlineSMOTE(sampling_strategy= self.overSampleOps['ratio'], 
                                                    random_state= 42)
                            trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                else:
                    if 'n_neighbors' in self.overSampleOps:
                        if 'kind' in self.overSampleOps:
                            smote = BorderlineSMOTE(k_neighbors= self.overSampleOps['n_neighbors'],
                                                    kind= self.overSampleOps['kind'],
                                                    random_state= 42)
                            trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                        else:
                            smote = BorderlineSMOTE(k_neighbors= self.overSampleOps['n_neighbors'], 
                                                    random_state= 42)
                            trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                    else:
                        if 'kind' in self.overSampleOps:
                            smote = BorderlineSMOTE(kind= self.overSampleOps['kind'],
                                                    random_state= 42)
                            trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                        else:
                            smote = BorderlineSMOTE(random_state= 42)
                            trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)

            case 'ADASYN':
                if 'ratio' in self.overSampleOps:
                    if 'n_neighbors' in self.overSampleOps:
                        smote = ADASYN(sampling_strategy= self.overSampleOps['ratio'],
                                       n_neighbors = self.overSampleOps['n_neighbors'], 
                                       random_state= 42)
                        trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                    else:
                        smote = ADASYN(sampling_strategy= self.overSampleOps['ratio'], 
                                       random_state= 42)
                        trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                else:
                    if 'n_neighbors' in self.overSampleOps:
                        smote = ADASYN(n_neighbors = self.overSampleOps['n_neighbors'], 
                                       random_state= 42)
                        trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)
                    else:
                        smote = ADASYN(random_state= 42)
                        trainVectors, trainFlags = smote.fit_resample(trainVectors, trainFlags)

        return trainVectors, trainFlags

    def underSample(self, trainVectors : sparse.csr_matrix, trainFlags : list) -> tuple[sparse.csr_matrix, list]:
        '''
        Applies under-sampling to training vectors.

        Parameters
        ----------
        trainVectors : sparse.csr_matrix
            Input training vectors.
        trainFlags : list
            Classification flags associated with training vectors.

        Returns
        -------
        trainVectors : sparse.csr_matrix
            Under-sampled training vectors.
        trainFlags : list
            Classification flags associated with under-sampled training vectors.
        '''
        match self.underSampleOps['method']:
            case 'RandomUnder':
                if 'ratio' in self.underSampleOps:
                    randomUnder = RandomUnderSampler(sampling_strategy= self.underSampleOps['ratio'],
                                                     random_state= 42)
                    trainVectors, trainFlags = randomUnder.fit_resample(trainVectors, trainFlags)
                else:
                    randomUnder = RandomUnderSampler(random_state= 42)
                    trainVectors, trainFlags = randomUnder.fit_resample(trainVectors, trainFlags)

            case 'Tomek':
                tomek = TomekLinks(n_jobs= -1)
                trainVectors, trainFlags = tomek.fit_resample(trainVectors, trainFlags)

            case 'ClusterCentroid':
                if 'ratio' in self.underSampleOps:
                    if 'voting' in self.underSampleOps:
                        cluster = ClusterCentroids(sampling_strategy= self.overSampleOps['ratio'],
                                                   voting= self.underSampleOps['voting'], 
                                                   random_state= 42)
                        trainVectors, trainFlags = cluster.fit_resample(trainVectors, trainFlags)
                    else:
                        cluster = ClusterCentroids(sampling_strategy= self.overSampleOps['ratio'],
                                                   random_state= 42)
                        trainVectors, trainFlags = cluster.fit_resample(trainVectors, trainFlags)
                else:
                    if 'voting' in self.underSampleOps:
                        cluster = ClusterCentroids(voting= self.underSampleOps['voting'], 
                                                   random_state= 42)
                        trainVectors, trainFlags = cluster.fit_resample(trainVectors, trainFlags)
                    else:
                        cluster = ClusterCentroids(random_state= 42)
                        trainVectors, trainFlags = cluster.fit_resample(trainVectors, trainFlags)
            
            case 'NCL':
                if 'n_neighbors' in self.underSampleOps:
                    ncl = NeighbourhoodCleaningRule(n_neighbors= self.underSampleOps['n_neighbors'],
                                                    n_jobs= -1)
                    trainVectors, trainFlags = ncl.fit_resample(trainVectors, trainFlags)
                else:
                    ncl = NeighbourhoodCleaningRule(n_jobs= -1)
                    trainVectors, trainFlags = ncl.fit_resample(trainVectors, trainFlags)

        return trainVectors, trainFlags

    def trainAndPredict(self, 
                        trainVectors : sparse.csr_matrix, 
                        trainFlags : list, 
                        testVectors : sparse.csr_matrix) -> tuple[list, Union[DecisionTreeClassifier, 
                                                                              BalancedRandomForestClassifier, 
                                                                              RUSBoostClassifier, 
                                                                              SVC]]:
        '''
        Creates trained ML algorithm and uses it to produce predicted flags.

        Parameters
        ----------
        trainVectors : sparse.csr_matrix
            Vectorised training records.
        trainFlags : list
            The flags associated with the training data.
        testVectors : sparse.cst_matrix
            Vectorised testing records.

        Returns
        -------
        predictedFlags : list
            The predicted flags for the test data.
        trainedModel : Union[DecisionTreeClassifier,
                             BalancedRandomForestClassifier,
                             RUSBoostClassifier,
                             SVC]
            Trained ML model.
        '''
        if trainVectors.shape[0] == 0 or trainFlags == [] or testVectors.shape[0] == 0:
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
        
        self.trainVectors = trainVectors
        self.trainFlags = trainFlags
        self.testVectors = testVectors
        self.testFlags = None
        
        if self.overSampleOps != {}:
            print('Over-Sampling...')
            trainVectors, trainFlags = self.overSample(trainVectors, trainFlags)
            
        if self.underSampleOps != {}:
            print('Under-Sampling...')
            trainVectors, trainFlags = self.underSample(trainVectors, trainFlags)

        self.sampledTrainVectors = trainVectors
        self.sampledTrainFlags = trainFlags

        print('Training Machine Learning Algorithm...')
        time0 = startRec()
        self.trainedModel.fit(trainVectors, trainFlags)
        self.trainingTime, self.trainingSpace = stopRec(time0)

        print('Predicting with Machine Learning Algorithm...')
        time0 = startRec()
        predictedFlags = self.trainedModel.predict(testVectors)
        self.predictionTime, self.predictionSpace = stopRec(time0)

        self.predictedFlags = predictedFlags

        return (predictedFlags, self.trainedModel)
    
def startRec() -> float:
    '''
    Outputs the current time and begins tracking memory.

    Parameters
    ----------
    None

    Retruns
    -------
    time0 : float
        The current time.
    '''
    time0 = time.time()
    tracemalloc.start()
    return time0

def stopRec(time0 : float) -> tuple[float, float]:
    '''
    Outputs time passed and peak memory used since the last call of startRec().

    Parameters
    ----------
    time0 : float
        The output from the last call of startRec().

    Returns
    -------
    time1 : float
        The time passed since the last call of startRec().
    space : float
        The peak memory used since the last call of startRec().
    '''
    time1 = time.time() - time0
    _, space = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return (time1, space)