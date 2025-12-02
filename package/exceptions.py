'''
Creates custom exceptions to be used throughout package.

Classes:

    EmptyActualFlagsException
    EmptyPredictedFlagsException
    FlagsNotEqualException
    BadActualFlagException
    BadPredictedFlagException
    TimesSpacesNotEqualException
    MoreDataThanRecordsException
    UnsupportedFileTypeException
    TrainDistException
    TestDistException
    MLAlgTypeException
    ImpurityException
    KernelException
    EmptyFlagsVectorsException
    TrainVectorsFlagsNotEqualException
    VectorsNotEqualException
    TokeniserException
    PreLAException
    TokenLevelException
    TextLevelException
    CorpusLevelException
    NGramException
    NegTrainSizeException
    NegTestSizeException
    NameExistsException
    NotEnoughClassesException
    MacLearnInputException
    OverSampleOpsException
    UnderSampleOpsException
    GammaException
    PolynomialException
    SigmoidException
    ImporterException
    VectoriseException
    MLearnException
    FileException
    ColumnLabelException
    BoundsException
    RatioException
    NEstimatorsException
    LearningRateException
    MaxDepthException
    MinSamplesException
    CArgException
    CrossValidateException

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''

class EmptyActualFlagsException(Exception):
    '''
    Raised when actualFlags is empty.
    '''
    pass

class EmptyPredictedFlagsException(Exception):
    '''
    Raised when predictFlags is empty.
    '''
    pass

class FlagsNotEqualException(Exception):
    '''
    Raised when the lengths of actualFlags and predictedFlags are not equal.
    '''
    pass

class BadActualFlagException(Exception):
    '''
    Raised when an actualFlag is not 0 or 1.
    '''
    pass

class BadPredictedFlagException(Exception):
    '''
    Raised when a predictedFlag is not 0 or 1.
    '''
    pass

class TimesSpacesNotEqualException(Exception):
    '''
    Raised when the lengths of times and spaces are not equal.
    '''
    pass

class MoreDataThanRecordsException(Exception):
    '''
    Raised when trying to extract more data than there are records available.
    '''
    pass

class UnsupportedFileTypeException(Exception):
    '''
    Raised when fileType is not in SUPPORTED_FILE_TYPES.
    '''
    pass

class TrainDistException(Exception):
    '''
    Raised when the input training distribution is invalid.
    '''
    pass

class TestDistException(Exception):
    '''
    Raised when the input testing distribution is invalid.
    '''
    pass

class MLAlgTypeException(Exception):
    '''
    Raised when the input mlAlgType is invalid.
    '''
    pass

class ImpurityException(Exception):
    '''
    Raised when the impurity measure in macLearnInput is invalid.
    '''
    pass

class KernelException(Exception):
    '''
    Raised when the kernel in macLearnInput is invalid.
    '''
    pass

class EmptyFlagsVectorsException(Exception):
    '''
    Raised when trainVectors, trainFlags or testVectors are empty.
    '''
    pass

class TrainVectorsFlagsNotEqualException(Exception):
    '''
    Raised when the number of training vectors and flags are not equal.
    '''
    pass

class VectorsNotEqualException(Exception):
    '''
    Raised when the lengths of testing and training vectors are not equal.
    '''
    pass

class TokeniserException(Exception):
    '''
    Raised when the input tokeniser is invalid.
    '''
    pass

class PreLAException(Exception):
    '''
    Raised when the input pre-LA changes are invalid.
    '''
    pass

class TokenLevelException(Exception):
    '''
    Raised when the input token level techniques are invalid.
    '''
    pass

class TextLevelException(Exception):
    '''
    Raised when the input text level techniques are invalid.
    '''
    pass

class CorpusLevelException(Exception):
    '''
    Raised when the input corpus level technique is invalid.
    '''
    pass

class NGramException(Exception):
    '''
    Raised when the input ngramRange is invalid.
    '''

class NegTrainSizeException(Exception):
    '''
    Raised when train size is less than 0.
    '''
    pass

class NegTestSizeException(Exception):
    '''
    Raised when test size is less than 0.
    '''
    pass

class NameExistsException(Exception):
    '''
    Raised when trying to export an NLP program and there is already a program
    stored with that name.
    '''
    pass

class NotEnoughClassesException(Exception):
    '''
    Raised when trainedModel.fit() raises "ValueError: The number of classes has
    to be greater than one; got 1 class".
    '''
    pass

class MacLearnInputException(Exception):
    '''
    Raised when the input macLearnInput is invalid.
    '''
    pass

class OverSampleOpsException(Exception):
    '''
    Raised when the input overSampleOps is invalid.
    '''
    pass

class UnderSampleOpsException(Exception):
    '''
    Raised when the input underSampleOps is invalid.
    '''
    pass

class GammaException(Exception):
    '''
    Raised when the macLearnInput gamma is invalid.
    '''
    pass

class PolynomialException(Exception):
    '''
    Raised when the polynomial parameters are invalid.
    '''
    pass

class SigmoidException(Exception):
    '''
    Raised when the sigmoid parameters are invalid.
    '''
    pass

class ImporterException(Exception):
    '''
    Raised when Importer input is invalid.
    '''
    pass

class VectoriseException(Exception):
    '''
    Raised when Vectorise input is invalid.
    '''
    pass

class MLearnException(Exception):
    '''
    Raised when MLearn input is invalid.
    '''
    pass

class FileException(Exception):
    '''
    Raised when a file input is invalid.
    '''
    pass

class ColumnLabelException(Exception):
    '''
    Raised when a columnLabel input is invalid.
    '''
    pass

class BoundsException(Exception):
    '''
    Raised when demographic bounds inputs are invalid.
    '''
    pass

class RatioException(Exception):
    '''
    Raised when macLearnInput ratio input is invalid.
    '''
    pass

class NEstimatorsException(Exception):
    '''
    Raised when macLearnInput n_estimators input is invalid.
    '''
    pass

class LearningRateException(Exception):
    '''
    Raised when macLearnInput learning_rate input is invalid.
    '''
    pass

class MaxDepthException(Exception):
    '''
    Raised when macLearnInput max_depth input is invalid.
    '''
    pass

class MinSamplesException(Exception):
    '''
    Raised when macLearnInput min_samples_split input is invalid.
    '''
    pass

class CArgException(Exception):
    '''
    Raised when macLearnInput C input is invalid.
    '''
    pass

class CrossValidateException(Exception):
    '''
    Raised when nFolds input to crossValidate function is invalid.
    '''
    pass