'''
Creates a widget for importing data for training and testing an NLP program.

Classes:

    Importer

Functions:

    getYear(str) -> int
    getYearExcel(str) -> int

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QWidget,
                            QVBoxLayout,
                            QLabel,
                            QHBoxLayout,
                            QLineEdit,
                            QPushButton,
                            QComboBox,
                            QFileDialog
                            )
from PyQt6.QtCore import QEvent
from .info import Info
from .filter import Filter
from . import base as b
import os
import pandas as pd

class Importer(QWidget):
    '''
    A widget for importing data for trianing and testing an NLP program.

    ...

    Attributes
    ----------
    filter : Filter
        The filter tab widget.
    info : Info
        A scroll area displayig the parameters of the program being built.
    dataDisplay : QLineEdit
        A widget to input and display the path to the training and testing data 
        for an NLP program.
    textColumns : QComboBox
        A widget for selecting which data column(s) contain free text data.
    flagColumn : QComboBox
        A widget for selecting which data column contains the annotations.
    textFieldDisplay : QLabel
        A widget to dispaly which data columns free text is being extracted from.
    demoDate : DemographicCheck
        A widget for selecting whether to filter the data by date.
    demoHosp : DemographicCheck
        A widget for selecting whether to filter the data by hospital.
    demoSex : DemographicCheck
        A widget for selecting whether to filter the data by sex.
    demoAge : DemographicCheck
        A widget for selecting whether to filter the data by age.
    fileLocations : list
        A list of file locations where data is stored.
    fileType : str
        The type of file in which the data is stored.
    dateColumnLabel : str
        The title of the column containing the date data.
    hospitalColumnLabel : str
        The title of the column containing the hospital data.
    sexColumnLabel : str
        The title of the column containing the sex data.
    ageColumnLabel : str
        The title of the column containing the age data.
    textFieldColumnLabels : list
        The titles of the columns containing the free text data.
    flagColumnLabel : str
        The title of the column containing the data annotations.
    
    Methods
    -------
    selectFiles()
        Opens a file dialog to select data location(s) and updates column
        selection attributes.
    addTextField()
        Adds the column name in the textColumns attribute to the 
        textFieldColumnLabels attribute.
    removeTextField()
        Removes the column name in the textColumns attribute from the 
        textFieldColumnLabels attribute.
    setDateColumn(QEvent)
        Updates the dateColumnLabel attribute and activates date selection.
    setHospColumn(QEvent)
        Updates the hospColumnLabel attribute and activates hospital selection.
    setSexColumn(QEvent)
        Updates the sexColumnLabel attribute and activates sex selection.
    setAgeColumn(QEvent)
        Updates the ageColumnLabel attribute and activates age selection.
    setFlagColumn()
        Updates the flagColumnLabel attribute.
    '''
    def __init__(self, filter : Filter, info : Info):
        '''
        Constructs attributes and sets the layout of an Importer object.

        Parameters
        ----------
        filter : Filter
            The filter tab widget.
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(Importer, self).__init__()

        self.filter = filter
        self.info = info

        selectLabel = QLabel()
        selectLabel.setText('Select Data File(s)')

        dataLabel = QLabel()
        dataLabel.setText('Data File:')
        self.dataDisplay = QLineEdit()
        dataBrowse = QPushButton('Browse')
        dataBrowse.clicked.connect(self.selectFiles)

        dataLayout = QHBoxLayout()
        dataLayout.addWidget(dataLabel)
        dataLayout.addWidget(self.dataDisplay)
        dataLayout.addWidget(dataBrowse)
        dataWidget = QWidget()
        dataWidget.setLayout(dataLayout)

        dFrame = b.InputFrame([selectLabel, dataWidget])

        annotatedLabel = QLabel()
        annotatedLabel.setText('Annotated Data')

        textColumnLabel = QLabel()
        textColumnLabel.setText('Select columns to draw free text from')

        self.textColumns = QComboBox()
        self.textColumns.addItem('None')

        self.flagColumn = QComboBox()
        self.flagColumn.addItem('None')
        self.flagColumn.currentIndexChanged.connect(self.setFlagColumn)

        add = QPushButton('Add')
        add.pressed.connect(self.addTextField)
        remove = QPushButton('Remove')
        remove.pressed.connect(self.removeTextField)

        fieldAddLayout = QHBoxLayout()
        fieldAddLayout.addWidget(textColumnLabel)
        fieldAddLayout.addWidget(self.textColumns)
        fieldAddLayout.addWidget(add)
        fieldAddLayout.addWidget(remove)

        fieldAddWidget = QWidget()
        fieldAddWidget.setLayout(fieldAddLayout)

        self.textFieldDisplay = QLabel()
        self.textFieldDisplay.setText('Free Text Fields:\n')

        textErrorLabel = QLabel()

        textDisplayLayout = QHBoxLayout()
        textDisplayLayout.addWidget(self.textFieldDisplay)
        textDisplayLayout.addWidget(textErrorLabel)

        textDisplayWidget = QWidget()
        textDisplayWidget.setLayout(textDisplayLayout)

        textColumnLayout = QVBoxLayout()
        textColumnLayout.addWidget(fieldAddWidget)
        textColumnLayout.addWidget(textDisplayWidget)

        textColumnWidget = QWidget()
        textColumnWidget.setLayout(textColumnLayout)

        flagColumnLabel = QLabel()
        flagColumnLabel.setText('Select Column containing flags')

        flagErrorLabel = QLabel()

        flagColumnLayout = QHBoxLayout()
        flagColumnLayout.addWidget(flagColumnLabel)
        flagColumnLayout.addWidget(self.flagColumn)
        flagColumnLayout.addWidget(flagErrorLabel)

        flagColumnWidget = QWidget()
        flagColumnWidget.setLayout(flagColumnLayout)

        aFrame = b.InputFrame([annotatedLabel, 
                               textColumnWidget, 
                               flagColumnWidget])

        demoLabel = QLabel()
        demoLabel.setText('Demographic Data')

        self.demoDate = b.DemographicCheck('Date Column', 
                                         self.filter.dFrame, 
                                         filter,
                                         '')
        self.demoDate.columns.currentIndexChanged.connect(self.setDateColumn)
        self.demoHosp = b.DemographicCheck('Hospital Column', 
                                         self.filter.hFrame, 
                                         filter,
                                         '')
        self.demoHosp.columns.currentIndexChanged.connect(self.setHospColumn)
        self.demoSex = b.DemographicCheck('Sex Column', 
                                        self.filter.sFrame, 
                                        filter,
                                        '')
        self.demoSex.columns.currentIndexChanged.connect(self.setSexColumn)
        self.demoAge = b.DemographicCheck('Age Column', 
                                         self.filter.aFrame, 
                                         filter,
                                         '')
        self.demoAge.columns.currentIndexChanged.connect(self.setAgeColumn)

        demoFrame = b.InputFrame([demoLabel, 
                                self.demoDate,
                                self.demoHosp,
                                self.demoSex,
                                self.demoAge])

        layout = QVBoxLayout()
        layout.addWidget(dFrame)
        layout.addWidget(aFrame)
        layout.addWidget(demoFrame)

        self.setLayout(layout)

        self.columnNames = []

        self.fileLocations = []
        self.fileType = ''
        self.dateColumnLabel = ''
        self.hospitalColumnLabel = ''
        self.sexColumnLabel = ''
        self.ageColumnLabel = ''
        self.textFieldColumnLabels = []
        self.flagColumnLabel = ''
   
    def selectFiles(self):
        '''
        Opens a file dialog to select data location(s) and updates column
        selection attributes.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.textColumns.clear()
        self.flagColumn.clear()
        self.demoDate.emptyColumns()
        self.demoHosp.emptyColumns()
        self.demoSex.emptyColumns()
        self.demoAge.emptyColumns()
        file_filter = 'CSV File (*.csv);; Excel File (*.xlsx)'
        response = QFileDialog.getOpenFileNames(
            parent = self,
            caption = 'Select Data Files',
            directory = os.getcwd(),
            filter = file_filter,
            initialFilter = 'CSV File (*.csv)'
        )
        self.dataDisplay.setText(str(response[0][0]))
        self.fileLocations = response[0]
        self.info.fileLocations = self.fileLocations
        self.info.updateInfo()
        if response[1] == 'CSV File (*.csv)':
            self.fileType = 'CSV'
        elif response[1] == 'Excel File (*.xlsx)':
            self.fileType = 'XLSX'
        self.info.fileType = self.fileType
        self.info.updateInfo()
        if self.fileType == 'CSV':
            self.columnNames = list(pd.read_csv(self.fileLocations[0], 
                                                nrows = 1).columns)
            self.columnNames = list(pd.read_csv(self.fileLocations[0], 
                                                nrows = 1).columns)
        elif self.fileType == 'XLSX':
            self.columnNames = list(pd.read_excel(self.fileLocations[0], 
                                                  nrows = 1).columns)
            self.columnNames = list(pd.read_excel(self.fileLocations[0], 
                                                  nrows = 1).columns)
        self.textColumns.addItems(self.columnNames)
        self.flagColumn.addItems(self.columnNames)
        self.demoDate.addColumns(self.columnNames)
        self.demoHosp.addColumns(self.columnNames)
        self.demoSex.addColumns(self.columnNames)
        self.demoAge.addColumns(self.columnNames)

    def addTextField(self):
        '''
        Adds the column name in the textColumns attribute to the 
        textFieldColumnLabels attribute.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.textColumns.currentText() != 'None' and self.textColumns.currentText() not in self.textFieldColumnLabels:
            self.textFieldColumnLabels.append(self.textColumns.currentText())
            self.info.textFieldColumnLabels = self.textFieldColumnLabels
            self.info.updateInfo()
            self.textFieldDisplay.setText(f'Free Text Fields:\n'
                                          f'{self.textFieldColumnLabels}')
        
    def removeTextField(self):
        '''
        Removes the column name in the textColumns attribute from the 
        textFieldColumnLabels attribute.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.textColumns.currentText() != 'None' and self.textColumns.currentText() in self.textFieldColumnLabels:
            self.textFieldColumnLabels.remove(self.textColumns.currentText())
            self.info.textFieldColumnLabels = self.textFieldColumnLabels
            self.info.updateInfo()
            self.textFieldDisplay.setText(f'Free Text Fields:\n'
                                          f'{self.textFieldColumnLabels}')

    def setDateColumn(self, e : QEvent):
        '''
        Updates the dateColumnLabel attribute and activates date selection.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the index of the demoDate attribute.

        Returns
        -------
        None
        '''
        self.dateColumnLabel = self.demoDate.value()
        self.info.dateColumnLabel = self.dateColumnLabel
        self.info.updateInfo()
        if e != 0:
            years = []
            try:
                if self.fileType == 'CSV':
                    for file in self.fileLocations:
                        yearList = pd.read_csv(file, 
                                        usecols = [self.demoDate.value()],
                                        encoding_errors= 'ignore', 
                                        low_memory= False).values.tolist()
                        years = years + yearList
                    years = [getYear(year) for year in years]
                elif self.fileType == 'XLSX':
                    for file in self.fileLocations:
                        yearList = pd.read_excel(file, 
                                                 usecols = [
                                                     self.demoDate.value()
                                                     ], dtype= str
                                                     ).values.tolist()
                        yearList = pd.read_excel(file, 
                                                 usecols = [
                                                     self.demoDate.value()
                                                     ], dtype= str
                                                     ).values.tolist()
                        years = years + yearList
                    years = [getYearExcel(year) for year in years]
                minYear = min(years)
                maxYear = max(years)
                if minYear < 1900 or maxYear > 2100:
                    print(
                        'raise an error here. The column was able to be parsed '
                        'but wasnt dates or wasnt dates in the correct format')
                    print(
                        'raise an error here. The column was able to be parsed '
                        'but wasnt dates or wasnt dates in the correct format')
                self.filter.minYearIn.setMinimum(minYear)
                self.filter.minYearIn.setMaximum(maxYear)
                self.filter.maxYearIn.setMinimum(minYear)
                self.filter.maxYearIn.setMaximum(maxYear)
                self.filter.minYearDefault = minYear
                self.filter.maxYearDefault = maxYear
                self.filter.maxYearLabel.setText('Select a latest year')
            except ValueError:
                pass
            except IndexError:
                print(
                    'Say something about the date column not being formatted '
                    'correctly')
                print(
                    'Say something about the date column not being formatted '
                    'correctly')
            '''
            except:
                minYear = 1950
                maxYear = 2024
                self.filter.minYearIn.setMinimum(minYear)
                self.filter.minYearIn.setMaximum(maxYear)
                self.filter.maxYearIn.setMinimum(minYear)
                self.filter.maxYearIn.setMaximum(maxYear)
                self.filter.minYearDefault = minYear
                self.filter.maxYearDefault = maxYear
                self.filter.maxYearLabel.setText('Select a latest year')
                print(
                    f'Tell the user that we couldnt infer the year ranges from '
                    f'this data and hence set the min to {minYear} and max to '
                    f'{maYear}')
                print(
                    f'Tell the user that we couldnt infer the year ranges from '
                    f'this data and hence set the min to {minYear} and max to '
                    f'{maYear}')
            '''
        self.demoDate.activateDemo(e)
        
    def setHospColumn(self, e : QEvent):
        '''
        Updates the hospColumnLabel attribute and activates hospital selection.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the index of the demoHosp attribute.

        Returns
        -------
        None
        '''
        self.hospitalColumnLabel = self.demoHosp.value()
        self.info.hospitalColumnLabel = self.hospitalColumnLabel
        self.info.updateInfo()
        self.demoHosp.activateDemo(e)

    def setSexColumn(self, e):
        '''
        Updates the sexColumnLabel attribute and activates sex selection.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the index of the demoSex attribute.

        Returns
        -------
        None
        '''
        self.sexColumnLabel = self.demoSex.value()
        self.info.sexColumnLabel = self.sexColumnLabel
        self.info.updateInfo()
        self.demoSex.activateDemo(e)

    def setAgeColumn(self, e):
        '''
        Updates the ageColumnLabel attribute and activates age selection.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the index of the demoAge attribute.

        Returns
        -------
        None
        '''
        self.ageColumnLabel = self.demoAge.value()
        self.info.ageColumnLabel = self.ageColumnLabel
        self.info.updateInfo()
        self.demoAge.activateDemo(e)

    def setFlagColumn(self):
        '''
        Updates the flagColumnLabel attribute.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.flagColumn.currentText() != 'None':
            self.flagColumnLabel = self.flagColumn.currentText()
            self.info.flagColumnLabel = self.flagColumnLabel
            self.info.updateInfo()
        else:
            self.flagColumnLabel = ''

def getYear(string: str) -> int:
    '''
    Determines the year a record belongs to.

    Parameters
    ----------
    string : str
        Text in the date field of the CSV file.

    Returns
    -------
    year : int
        The year the patient presented to the ED.
    '''
    string = string[0]
    string = str(string)
    split = string.split("/")
    yearData = split[2]
    parts = yearData.split(" ")
    year = int(parts[0])
    return year

def getYearExcel(string : str) -> int:
    '''
    Determines the year a record belongs to.

    Parameters
    ----------
    string : str
        Text in the date field of the XLSX file.

    Returns
    -------
    year : int
        The year the patient presented to the ED.
    '''
    string = string[0]
    string = str(string)
    split = string.split("-")
    year = int(split[0])
    return year