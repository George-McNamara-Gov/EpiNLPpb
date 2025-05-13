'''
Creates custom exceptions to be used throughout package.

Classes:

    InsufficientMeasureListException
    EmptyActualFlagsException
    EmptyPredictedFlagsException
    FlagsNotEqualException
    BadActualFlagException
    BadPredictedFlagException
    TimesSpacesNotEqualException
    MoreDataThanRecordsException
    UnsupportedFileTypeException
    MinAgeException
    MaxAgeException
    HospitalException
    SexException
    MinYearException
    MaxYearException
    MinMaxYearException
    TrainDistException
    TestDistException
    TrainPosPercentException
    TestPosPercentException
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
    NoLATechniquesException
    NoTokeniserException
    TokeniserException
    PreLAException
    TokenLevelException
    TextLevelException
    CorpusLevelException
    NegTrainSizeException
    NegTestSizeException
    NoTextFieldsException
    NoFlagFieldException
    ColumnLabelException
    NameExistsException
    NotEnoughClassesException
    TreeGraphException

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''

class InsufficientMeasureListException(Exception):
    '''
    Raised when measureList does not provide enough records to approximate 
    complexity.
    '''
    pass

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

class MinAgeException(Exception):
    '''
    Raised when minAge is less than 0.
    '''
    pass

class MaxAgeException(Exception):
    '''
    Raised when maxAge is less than minAge.
    '''
    pass

class HospitalException(Exception):
    '''
    Raised when the hospital input is invalid.
    '''
    pass

class SexException(Exception):
    '''
    Raised when the sex input is invalid.
    '''
    pass

class MinYearException(Exception):
    '''
    Raised when minYear is out of range.
    '''
    pass

class MaxYearException(Exception):
    '''
    Raised when maxYear is out of range.
    '''
    pass

class MinMaxYearException(Exception):
    '''
    Raised when maxYear is less than minYear.
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

class TrainPosPercentException(Exception):
    '''
    Raised when the percentage of positively flagged training records is less
    than or equal to 0 or greater than or equal to 100.
    '''
    pass

class TestPosPercentException(Exception):
    '''
    Raised when the percentage of positively flagged testing records is less
    than or equal to 0 or greater than or equal to 100.
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

class NoRBFGammaException(Exception):
    '''
    Raised when no gamma parameter is provided in macLearnInput for an RBF
    kernel.
    '''
    pass

class NegRBFGammaException(Exception):
    '''
    Raised when the gamma parameter provided in macLearnInput for an RBF
    kernel is non-positive.
    '''
    pass

class NoPolynomialParameterException(Exception):
    '''
    Raised when no degree or r parameter is provided in macLearnInput for a
    polynomial kernel.
    '''
    pass

class NegPolynomialDegreeException(Exception):
    '''
    Raised when the degree parameter provided in macLearnInput for a polynomial
    kernel is non-positive.
    '''
    pass

class NoSigmoidParameterException(Exception):
    '''
    Raised when no gamma or r parameter is provided in macLearnInput for a
    sigmoid kernel.
    '''
    pass

class NegSigmoidGammaException(Exception):
    '''
    Raised when the gamma parameter provided in macLearnInput for a sigmoid
    kernel is non-positive.
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

class NoLATechniquesException(Exception):
    '''
    Raised when no token, text or corpus level LA techniques are provided.
    '''
    pass

class NoTokeniserException(Exception):
    '''
    Raised when token level techniques are provided with no tokeniser.
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

class NoTextFieldsException(Exception):
    '''
    Raised when no text field column labels are provided.
    '''
    pass

class NoFlagFieldException(Exception):
    '''
    Raised when no flag column label is provided.
    '''
    pass

class ColumnLabelException(Exception):
    '''
    Raised when one of the column labels cannot be found in the data file.
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

class TreeGraphException(Exception):
    '''
    Raised when trying to plot a tree graph for a SVM algorithm.
    '''
    pass