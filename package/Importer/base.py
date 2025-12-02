'''
Helper functions and classes to support package/Importer/importer.py.

Classes:

    DataSet
    Demographic

Functions:

    inRange(int, tuple) -> bool
    getFileType(str) -> str
    getYear(str) -> int
    handleNaN(float) -> int | float

Misc variables:

    None

Exceptions:

    FileException
    ColumnLabelException
    UnsupportedFileTypeException
    BoundsException
'''
from . import constants as c
import pandas as pd
import math
from .. import exceptions as e

class DataSet:
    '''
    A class to represent a Data Set.

    ...

    Attributes
    ----------
    columnLabels : list
        The labels of the columns with relavant data.
    textFieldColumnLabels : list
        The labels of the columns with free text.
    trainFile : str
        The path to a file containing training data.
    testFile : str
        The path to a file containing testing data.
    fileLocations : list
        List of paths of files where data is stored.

    Methods
    -------
    importToFrame() -> pd.DataFrame | tuple:
        Creates a data frame or pair of data frames containing data from the provided files.
    fileToFrame(str) -> pd.DataFrame:
        Extracts a data frame of records from a given file.
    '''

    def __init__(self,
                 trainFile : str,
                 testFile : str, 
                 fileLocations: list,
                 dateColumnLabel : str,
                 hospitalColumnLabel : str,
                 sexColumnLabel : str,
                 ageColumnLabel : str,
                 customColumnLabels : list,
                 textFieldColumnLabels : list,
                 flagColumnLabel : str):
        '''
        Constructs attributes for DataSet object.

        Parameters
        ----------
        trainFile : str
            The path to a file containing training data.
        testFile : str
            The path to a file containing testing data.
        fileLocations : list
            List of paths of files where data is stored.
        dateColumnLabel : str
            The label of the column with the date data.
        hospitalColumnLabel : str
            The label of the column with the hospital data.
        sexColumnLabel : str
            The label of the column with the sex data.
        ageColumnLabel : str
            The label of the column with the age data.
        customColumnLabels : list
            The labels of columns with custom data to filter.
        textFieldColumnLabels : list
            The labels of the columns with free text.
        flagColumnLabel : str
            The label of the column with the classification flag.
        '''
        if not isinstance(trainFile, str):
            raise e.FileException(
                'trainFile must be a string.'
            )
        if not isinstance(testFile, str):
            raise e.FileException(
                'testFile must be a string.'
            )
        if not isinstance(fileLocations, list):
            raise e.FileException(
                'fileLocations must be a list.'
            )
        for file in fileLocations:
            if not isinstance(file, str):
                raise e.FileException(
                    'Files in fileLocations must be strings.'
                )
        if not isinstance(dateColumnLabel, str):
            raise e.ColumnLabelException(
                'dateColumnLabel must be a string.'
            )
        if not isinstance(hospitalColumnLabel, str):
            raise e.ColumnLabelException(
                'hospitalColumnLabel must be a string.'
            )
        if not isinstance(sexColumnLabel, str):
            raise e.ColumnLabelException(
                'sexColumnLabel must be a string.'
            )
        if not isinstance(ageColumnLabel, str):
            raise e.ColumnLabelException(
                'ageColumnLabel must be a string.'
            )
        if not isinstance(customColumnLabels, list):
            raise e.ColumnLabelException(
                'customColumnLabels must be a list.'
            )
        for label in customColumnLabels:
            if not isinstance(label, str):
                raise e.ColumnLabelException(
                    'Labels in customColumnLabels must be strings.'
                )
        if not isinstance(textFieldColumnLabels, list):
            raise e.ColumnLabelException(
                'textFieldColumnLabels must be a list.'
            )
        for label in textFieldColumnLabels:
            if not isinstance(label, str):
                raise e.ColumnLabelException(
                    'Labels in textFieldColumnLabels must be strings.'
                )
        if not isinstance(flagColumnLabel, str):
            raise e.ColumnLabelException(
                'flagColumnLabel must be a string.'
            )
        
        if trainFile != '' and testFile == '':
            raise e.FileException(
                'If providing a trainfile, also need to provide a testFile.'
            )
        if trainFile == '' and testFile != '':
            raise e.FileException(
                'If providing a testfile, also need to provide a trainFile.'
                )
        if trainFile == '' and testFile == '' and fileLocations == []:
            raise e.FileException(
                'Need to provide at least one data file.'
            )
        
        if textFieldColumnLabels == []:
            raise e.ColumnLabelException(
                'Must provide at least one text field column label.'
            )
        
        if flagColumnLabel == '':
            raise e.ColumnLabelException(
                'Must provide a flag column label.'
            )
        
        self.columnLabels = []

        if dateColumnLabel != '':
            self.columnLabels.append(dateColumnLabel)
        
        if hospitalColumnLabel != '':
            self.columnLabels.append(hospitalColumnLabel)
        
        if sexColumnLabel != '':
            self.columnLabels.append(sexColumnLabel)

        if ageColumnLabel != '':
            self.columnLabels.append(ageColumnLabel)

        for label in customColumnLabels:
            self.columnLabels.append(label)
        
        for label in textFieldColumnLabels:
            self.columnLabels.append(label)

        self.columnLabels.append(flagColumnLabel)
 
        self.textFieldColumnLabels = textFieldColumnLabels

        self.trainFile = trainFile
        self.testFile = testFile
        self.fileLocations = fileLocations

    def importToFrame(self) -> pd.DataFrame | tuple:
        '''
        Creates a data frame or pair of data frames containing data from the provided files.

        Parameters
        ----------
        None

        Returns
        -------
        dataFrame : pd.DataFrame
            A data frame of records with relavent columns from the data files.
        
        OR

        trainFrame : pd.DataFrame
            A data frame of training records with relavent columns from the data files.
        testFrame : pd.DataFrame
            A data frame of testing records with relavent columns from the data files.
        '''
        if self.trainFile != '' and self.testFile != '':
            trainFrame = self.fileToFrame(self.trainFile)
            testFrame = self.fileToFrame(self.testFile)
            return (trainFrame, testFrame)
        else:
            dataFrame = self.fileToFrame(self.fileLocations[0])
            for file in self.fileLocations[1:len(self.fileLocations)]:
                dataFrame = pd.concat([dataFrame, self.fileToFrame(file)], axis= 0)
            return dataFrame
    
    def fileToFrame(self, 
                   file : str) -> pd.DataFrame:
        '''
        Extracts a data frame of records from a given file.

        Parameters
        ----------
        file : str
            The path of the file to extract the records from.

        Retruns
        -------
        outFrame : pd.DataFrame
            The data frame of records extracted from the file.
        '''
        fileType = getFileType(file)
        if fileType not in c.SUPPORTED_FILE_TYPES:
            raise e.UnsupportedFileTypeException(
                'Must provide files of type csv or xlsx.'
            )
        if fileType == 'csv':
            try:
                outFrame = pd.read_csv(
                    file, 
                    usecols = self.columnLabels, 
                    encoding_errors= 'ignore', 
                    low_memory= False
                    )
            except ValueError:
                raise e.ColumnLabelException(
                    'One of the column labels was not found in the data file.'
                )
        elif fileType == 'xlsx':
            try:
                outFrame = pd.read_excel(
                    file, 
                    usecols = self.columnLabels
                    )
            except ValueError:
                raise e.ColumnLabelException(
                    'One of the column labels was not found in the data file.'
                )
        return outFrame

class Demographic:
    '''
    A class to represent a demographic.

    ...

    Attributes
    ----------
    dateColumnLabel : str
        The label of the column with the date data.
    hospitalColumnLabel : str
        The label of the column with the hospital data.
    sexColumnLabel : str
        The label of the column with the sex data.
    ageColumnLabel : str
        The label of the column with the age data.
    customColumnLabels : list
        A list of labels of columns with custom data to filter.
    ageBounds : tuple
        The minimum and maximum age values for included records.
    hospital : str
        The hospital ID for included records.
    sex : int
        An integer representing the sex(es) for included records. 
        0 for all. 1 for male. 2 for female.
    yearBounds : tuple
        The minimum and maximum year values for included records.
    customBounds : list
        A list of bounds for columns with custom data.
    
    Methods
    -------
    filer(pd.DataFrame) -> pd.DataFrame
        Filters a data frame of records and returns those satisfying designated demographic.
    '''
    
    def __init__(self,
                dateColumnLabel : str,
                hospitalColumnLabel : str,
                sexColumnLabel : str,
                ageColumnLabel : str,
                customColumnLabels : list, 
                ageBounds : tuple,
                hospital: str,
                sex: int,
                yearBounds : tuple,
                customBounds : list):
        '''
        Checks inputs are valid and constructs attributes.

        Parameters
        ----------
        dateColumnLabel : str
            The label of the column with the date data.
        hospitalColumnLabel : str
            The label of the column with the hospital data.
        sexColumnLabel : str
            The label of the column with the sex data.
        ageColumnLabel : str
            The label of the column with the age data.
        customColumnLabels : list
            A list of labels of columns with custom data to filter.
        ageBounds : tuple
            The minimum and maximum age values for included records.
        hospital : str
            The hospital ID for included records.
        sex : int
            An integer representing the sex(es) for included records. 
            0 for all. 1 for male. 2 for female.
        yearBounds : tuple
            The minimum and maximum year values for included records
        customBounds : list
            A list of bounds for columns with custom data.
        '''
        try:
            _ = ageBounds[0]
        except (TypeError, IndexError):
            raise e.BoundsException(
                'Cannot index into ageBounds.'
                )
        
        if isinstance(ageBounds[0], tuple):
            for bound in ageBounds:
                if not isinstance(bound[0], int):
                    raise e.BoundsException(
                        'lower ageBound must be an int.'
                    )
                if not isinstance(bound[1], int):
                    raise e.BoundsException(
                        'upper ageBound must be an int.'
                    )
                if bound[0] < 0:
                    raise e.BoundsException(
                        'Minimum age cannot be less than 0.'
                    )
                if bound[1] < bound[0]:
                    raise e.BoundsException(
                        'Maximum age cannot be less than minimum age.'
                    ) 
        else:
            if not isinstance(ageBounds[0], int):
                raise e.BoundsException(
                    'lower ageBound must be an int.'
                )
            if not isinstance(ageBounds[1], int):
                raise e.BoundsException(
                    'upper ageBound must be an int.'
                )
            if ageBounds[0] < 0:
                raise e.BoundsException(
                    'Minimum age cannot be less than 0.'
                    )
            if ageBounds[1] < ageBounds[0]:
                raise e.BoundsException(
                    'Maximum age cannot be less than minimum age.'
                ) 
            
        if hospital not in ['ALL', 'CHHS', 'CHPB']:
            raise e.BoundsException(
                'Hospital must be "ALL","CHHS" or "CHPB"'
                )
        
        if sex not in [0, 1, 2]:
            raise e.BoundsException('Sex must be 0 (all), 1 (male), or 2 (female).')
        
        try:
            _ = yearBounds[0]
        except (TypeError, IndexError):
            raise e.BoundsException(
                'Cannot index into yearBounds.'
                )
        
        if isinstance(yearBounds[0], tuple):
            for bound in yearBounds:
                if not isinstance(bound[0], int):
                    raise e.BoundsException(
                        'Lower yearBound must be an int.'
                    )
                if not isinstance(bound[1], int):
                    raise e.BoundsException(
                        'Upper yearBound must be an int.'
                    )
                if not (1900 <= bound[0] <= 2100):
                    raise e.BoundsException(
                        'Minimum year must be in the range 1900 to 2100.'
                        )
                if not (1900 <= bound[1] <= 2100):
                    raise e.BoundsException(
                        'Maximum year must be in the range 1900 to 2100.'
                        )
                if bound[1] < bound[0]:
                    raise e.BoundsException(
                        'Maximum year cannot be less than minimum year'
                        )
        else:
            if not isinstance(yearBounds[0], int):
                raise e.BoundsException(
                    'Lower yearBound must be an int.'
                )
            if not isinstance(yearBounds[1], int):
                raise e.BoundsException(
                    'Upper yearBound must be an int.'
                )
            if not (1900 <= yearBounds[0] <= 2100):
                raise e.BoundsException(
                    'Minimum year must be in the range 1900 to 2100'
                    )
            if not (1900 <= yearBounds[1] <= 2100):
                raise e.BoundsException(
                    'Maximum year must be in the range 1900 to 2100'
                    )
            if yearBounds[1] < yearBounds[0]:
                raise e.BoundsException(
                    'Maximum year cannot be less than minimum year'
                    )
        
        for customBound in customBounds:
            if isinstance(customBound, str) or isinstance(customBound, int):
                pass
            else:
                try:
                    _ = customBound[0]
                except (TypeError, IndexError):
                    raise e.BoundsException(
                        'Cannot index into customBounds.'
                    )
            
                if isinstance(customBound[0], float | int):
                    if not isinstance(customBound[1], float | int):
                        raise e.BoundsException(
                            'Upper customBound must be a float or int.'
                        )
                    if customBound[1] < customBound[0]:
                        raise e.BoundsException(
                            'Upper customBound cannot be less than lower customBound.'
                        )
                    
                elif isinstance(customBound[0], tuple):
                    for bound in customBound:
                        if not isinstance(bound[0], float | int):
                            raise e.BoundsException(
                                'A sequence of bounds must be a sequence of tuples of ints or floats.'
                            )
                        if not isinstance(bound[0], float | int):
                            raise e.BoundsException(
                                'A sequence of bounds must be a sequence of tuples of ints or floats.'
                            )
                        if bound[1] < bound[0]:
                            raise e.BoundsException(
                                'Upper customBound cannot be less than lower customBound.'
                            )
                else:
                    raise e.BoundsException(
                        'customBound must be a string, int/float, tuple of int/float, or tuple of tuples of int/float.'
                    )
            
        self.dateColumnLabel = dateColumnLabel
        self.hospitalColumnLabel = hospitalColumnLabel
        self.sexColumnLabel = sexColumnLabel
        self.ageColumnLabel = ageColumnLabel
        self.customColumnLabels = customColumnLabels
        self.ageBounds = ageBounds
        self.hospital = hospital
        self.sex = sex
        self.yearBounds = yearBounds
        self.customBounds = customBounds
       
    def filter(self, data : pd.DataFrame) -> pd.DataFrame:
        '''
        Filters a data frame of records and returns those satisfying designated demographic.

        Parameters
        ----------
        data : pd.DataFrame
            The records to be filtered.

        Returns
        -------
        data : pd.DataFrame
            The filtered records.
        '''
        if self.hospitalColumnLabel != '' and self.hospital != 'ALL':
            data = data[data[self.hospitalColumnLabel] == self.hospital]

        if self.sexColumnLabel != '' and self.sex != 0:
            passes = [int(val) == self.sex for val in data[self.sexColumnLabel]]
            data = data[passes]

        if self.ageColumnLabel != '':
            if isinstance(self.ageBounds[0], tuple):
                passes = [inRange(handleNaN(val), self.ageBounds) for val in data[self.ageColumnLabel].values.tolist()]
                data = data[passes]
            else:
                passes = [self.ageBounds[0] <= handleNaN(val) <= self.ageBounds[1] for val in data[self.ageColumnLabel].values.tolist()]
                data = data[passes]

        if self.dateColumnLabel != '':
            if isinstance(self.yearBounds[0], tuple):
                passes = [inRange(getYear(str(val)), self.yearBounds) for val in data[self.dateColumnLabel]]
                data = data[passes]
            else:
                passes = [(self.yearBounds[0] <= getYear(str(val)) <= self.yearBounds[1]) for val in data[self.dateColumnLabel]]
                data = data[passes]

        for i in range(0, len(self.customBounds)):
            print(len(data))
            customBound = self.customBounds[i]
            if len(self.customColumnLabels) > i:
                customLabel = self.customColumnLabels[i]
                if isinstance(customBound, int):
                    passes = [handleNaN(val) == customBound for val in data[customLabel]]
                    data = data[passes]
                elif isinstance(customBound, str):
                    passes = [str(val) == customBound for val in data[customLabel]]
                    data = data[passes]
                elif isinstance(customBound[0], int):
                    passes = [customBound[0] <= handleNaN(val) <= customBound[1] for val in data[customLabel]]
                    data = data[passes]
                elif isinstance(customBound[0], tuple):
                    passes = [inRange(val, customBound) for val in data[customLabel] if not math.isnan(val)]
                    data = data[passes]

        return data
    
def inRange(value : int, bounds : tuple) -> bool:
    '''
    Determines if an integer value is within one of several bounds.

    Parameters
    ----------
    value : int
        The value to check.
    bounds : tuple
        A tuple containing several bounds.

    Returns
    ------
    check : bool
        Whether the value is contained in any of the bounds.
    '''
    check = False
    for bound in bounds:
        if bound[0] <= value <= bound[1]:
            check = True
    return check
    
def getFileType(path : str) -> str:
    '''
    Returns the file extension of a given path.

    Parameters
    ----------
    path : str
        The path to get the file extension of.

    Returns
    -------
    extension : str
        The file extension, excluding the '.'.
    '''
    parts = path.split('.')
    extension = parts[-1]
    return extension
 
def getYear(string: str) -> int:
    '''
    Determines the year a record belongs to.

    Parameters
    ----------
    string : str
        Text in the date field of the csv file.

    Returns
    -------
    year : int
        The year the patient presented to the ED.
    '''
    string = str(string)
    split = string.split("/")
    yearData = split[-1]
    parts = yearData.split(" ")
    try:
        year = int(parts[0])
    except ValueError:
        split = parts[0].split("-")
        year = int(split[0])
    return year

def handleNaN(val : float) -> int | float:
    '''
    A helper function for handling possible NaN values from files.

    Parameters
    ----------
    val : float
        The float value read from the file.

    Returns
    -------
    out : int | val
        The non-NaN value to replace the NaN value.
    '''
    try:
        val = int(val)
    except:
        out = -math.inf
        return out
    if math.isnan(val):
        out = -math.inf
        return out
    out = int(val)
    return out