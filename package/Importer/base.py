'''
Helper functions and classes to support package/Importer/importer.py.

Classes:

    DataSet
    Demographic

Functions:

    getYear(str) -> int
    getYearExcel(pd.Timestamp) -> int

Misc variables:

    None

Exceptions :

    UnsupportedFileTypeException
    NoTextFieldsException
    NoFlagFieldException
    ColumnLabelException
    MinAgeException
    MaxAgeExcpetion
    HospitalException
    SexException
    MinYearException
    MaxYearException
    MinMaxYearException
'''
from . import constants as c
import pandas as pd
from .. import exceptions as e

class DataSet:
    '''
    A class to represent a Data Set.

    ...

    Attributes
    ----------
    columnLabels : list
        The labels of the columns with relavant data.
    dateIndex : int
        The index in a record containing the date data.
    hospIndex : int
        The index in a record containing the hospital data.
    sexIndex : int
        The index in a record containing the sex data.
    ageIndex : int
        The index in a record containing the age data.
    textIndicies : list
        The indices in a record containing the free text.
    flagIndex : int
        The index in a record containing the flag.
    textFieldColumnLabels : list
        The labels of the columns with free text. Used only in 
        model/demonstration.py.
    fileLocations : list
        List of strings of file locations where the data is stored.
    fileType : str
        A string encoding the type of the files.

    Methods
    -------
    importToList() -> list:
        Creates a list containing the data from the files.
    fileToList(str) -> list:
        Extracts a list of records from a given file.
    '''

    def __init__(self, 
                 fileLocations: list, 
                 fileType : str, 
                 dateColumnLabel : str,
                 hospitalColumnLabel : str,
                 sexColumnLabel : str,
                 ageColumnLabel : str,
                 textFieldColumnLables : list,
                 flagColumnLabel : str):
        '''
        Constructs attributes for DataSet object.

        Parameters
        ----------
        fileLocations : list
            List of strings of file names where the data is stored.
        fileType : str
            A string encoding the type of the files.
        dateColumnLabel : str
            The label of the column with the date data.
        hospitalColumnLabel : str
            The label of the column with the hospital data.
        sexColumnLabel : str
            The label of the column with the sex data.
        ageColumnLabel : str
            The label of the column with the age data.
        textFieldColumnLabels : list
            The labels of the columns with free text.
        flagColumnLabel : str
            The label of the column with the flag.
        '''
        if fileType not in c.SUPPORTED_FILE_TYPES:
            raise e.UnsupportedFileTypeException(
                f'File type must be one of {c.SUPPORTED_FILE_TYPES}.'
                )

        if textFieldColumnLables == []:
            raise e.NoTextFieldsException(
                'Must provide at least one text field column label.'
            )
        
        if flagColumnLabel == '':
            raise e.NoFlagFieldException(
                'Must provide a flag column label.'
            )
        
        self.columnLabels = []
        index = 0

        if dateColumnLabel == '':
            self.dateIndex = -1
        else:
            self.dateIndex = index
            index += 1
            self.columnLabels.append(dateColumnLabel)
        
        if hospitalColumnLabel == '':
            self.hospIndex = -1
        else:
            self.hospIndex = index
            index += 1
            self.columnLabels.append(hospitalColumnLabel)
        
        if sexColumnLabel == '':
            self.sexIndex = -1
        else:
            self.sexIndex = index
            index += 1
            self.columnLabels.append(sexColumnLabel)

        if ageColumnLabel == '':
            self.ageIndex = -1
        else:
            self.ageIndex = index
            index += 1
            self.columnLabels.append(ageColumnLabel)
        
        for label in textFieldColumnLables:
            self.columnLabels.append(label)
        self.textIndices = list(
            range(index, index + len(textFieldColumnLables))
            )

        self.columnLabels.append(flagColumnLabel)
        self.flagIndex = index + len(textFieldColumnLables)
        
        self.textFieldColumnLables = textFieldColumnLables

        self.fileLocations = fileLocations
        self.fileType = fileType

    def importToList(self) -> list:
        '''
        Creates a list containing the data from the files.

        Parameters
        ----------
        None

        Returns
        -------
        dataList : list
            A list of records with relavent columns from the data files.
        '''
        data_frames = [self.fileToList(file) for file in self.fileLocations]
        data_list = [record for df in data_frames for record in df]
        return data_list
    
    def fileToList(self, 
                   file : str) -> list:
        '''
        Extracts a list of records from a given file.

        Parameters
        ----------
        file : str
            The file to extract the records from.

        Retruns
        -------
        outList : list
            The list of records extracted from the file.
        '''
        if self.fileType == 'CSV':
            try:
                outList = pd.read_csv(
                    file, 
                    usecols = self.columnLabels, 
                    encoding_errors= 'ignore', 
                    low_memory= False
                    ).values.tolist()
            except ValueError:
                raise e.ColumnLabelException(
                    'One of the column labels was not found in the data file.'
                )
        elif self.fileType == 'XLSX':
            try:
                outList = pd.read_excel(
                    file, 
                    usecols = self.columnLabels
                    ).values.tolist()
            except ValueError:
                raise e.ColumnLabelException(
                    'One of the column labels was not found in the data file.'
                )

        return outList

class Demographic:
    '''
    A class to represent a demographic.

    ...

    Attributes
    ----------
    minAge : int
        Lowest age.
    maxAge : int
        Highest age.
    ageIndex : int
        The index in a record containing the age data.
    hospital : str
        Which hospital(s) to include.
    hospitalIndex : int
        The index in a record containing the hospital data.
    sex : str
        Which sex(es) to include.
    sexIndex : int
        The index in a record containing the sex data.
    minYear : int
        Earliest year.
    maxYear : int
        Latest year.
    dateIndex : int
        The index in a record containing the date data.

    Methods
    -------
    demographicCheck(list) -> bool
        Checks if a record relates to a patient in the demographic.
    '''
    
    def __init__(self, 
                minAge: int, 
                maxAge: int,
                ageIndex : int, 
                hospital: str,
                hospIndex : int, 
                sex: str,
                sexIndex : str, 
                minYear: int, 
                maxYear: int,
                dateIndex : int):
        '''
        Checks inputs are valid and constructs attributes for Demographic.

        Parameters
        ----------
        minAge : int
            Lowest age.
        maxAge : int
            Highest age.
        ageIndex : int
            The index in a record containing the age data.
        hospital : str
            Which hospital(s) to include.
        hospitalIndex : int
            The index in a record containing the hospital data.
        sex : str
            Which sex(es) to include.
        sexIndex : int
            The index in a record containing the sex data.
        minYear : int
            Earliest year.
        maxYear : int
            Latest year.
        dateIndex : int
            The index in a record containing the date data.
        '''
        if minAge < 0:
            raise e.MinAgeException(
                'Minimum age cannot be less than 0'
                )
        if maxAge < minAge:
            raise e.MaxAgeException(
                'Maximum age cannot be less than minimum age'
                )
        if hospital not in ['ALL', 'CHHS', 'CHPB']:
            raise e.HospitalException(
                'Hospital must be "ALL","CHHS" or "CHPB"'
                )
        if sex not in ['ALL', 'MALE', 'FEMALE']:
            raise e.SexException('Sex must be "ALL", "MALE" or "FEMALE"')
        if not (2015 <= minYear <= 2022):
            raise e.MinYearException(
                'Minimum year must be in the range 2015 to 2022'
                )
        if not (2015 <= maxYear <= 2022):
            raise e.MaxYearException(
                'Maximum year must be in the range 2015 to 2022'
                )
        if maxYear < minYear:
            raise e.MinMaxYearException(
                'Maximum year cannot be less than minimum year'
                )
        self.minAge = minAge
        self.maxAge = maxAge
        self.ageIndex = ageIndex
        self.hospital = hospital
        self.hospIndex = hospIndex
        self.sex = sex
        self.sexIndex = sexIndex
        self.minYear = minYear
        self.maxYear = maxYear
        self.dateIndex = dateIndex
    
    def demographicCheck(self, 
                         record : list) -> bool:
        '''
        Checks if a record relates to a patient in the demographic.

        Parameters
        ----------
        record : list
            The record related to the patient to check.

        Returns
        -------
        check : bool
            Whether or not the related patient is in the demographic.
        '''
        check = True
        if self.dateIndex != -1:
            if isinstance(record[self.dateIndex], pd.Timestamp):
                check = check and (
                    self.minYear <= getYearExcel(record[self.dateIndex]) <= self.maxYear)
            else:
                check = check and (
                    self.minYear <= getYear(record[self.dateIndex]) <= self.maxYear)
        if self.hospIndex != -1 and self.hospital != 'ALL':
            if self.hospital == 'CHHS':
                check = check and record[self.hospIndex] == 'CHHS'
            if self.hospital == 'CHPB':
                check = check and record[self.hospIndex] == 'CHPB'
            check = check and record[self.hospIndex] == self.hospital
        if self.sexIndex != -1 and self.sex != 'ALL':
            if self.sex == 'MALE':
                check = check and int(record[self.sexIndex]) == 1
            if self.sex == 'FEMALE':
                check = check and int(record[self.sexIndex]) == 2
        if self.ageIndex != -1:
            check = check and (
                self.minAge <= float(record[self.ageIndex]) <= self.maxAge)
        return check
 
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
    yearData = split[2]
    parts = yearData.split(" ")
    year = int(parts[0])
    return year

def getYearExcel(date : pd.Timestamp) -> int:
    '''
    Determines the year a record belongs to.

    Parameters
    ----------
    date : pd.Timestamp
        Data in the date field of the xlsx file.

    Returns
    -------
    year : int
        The year the patient presented to the ED.
    '''
    year = date.year
    return year