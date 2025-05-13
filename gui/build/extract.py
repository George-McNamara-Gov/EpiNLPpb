'''
Creates a widget for extracting data for training and testing an NLP program.

Classes:

    Extract

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QWidget,
                             QLabel,
                             QComboBox,
                             QLineEdit,
                             QHBoxLayout,
                             QVBoxLayout,
                             QDoubleSpinBox,
                             QPushButton,
                             QCheckBox
                            )
from PyQt6.QtCore import QEvent
from . import base as b
from .info import Info
import pandas as pd
import math

class Extract(QWidget):
    '''
    A widget for extracting data for training and testing an NLP program.

    ...

    Attributes
    ----------
    info : Info
        A scroll area displaying the parameters of the program being built.
    fileLocations : list
        A list of file locations where data is stored.
    fileType : str
        The type of file in which the data is stored.
    flagColumnLabel : str
        The title of the column containing the data annotations.
    ratio : QComboBox
        A widget for selecting the ratio of train and test data.
    availableAmount : QLabel
        A widget for displaying the amount of records available.
    amount : QLineEdit
        A widget to input the amount of records to extract.
    trainPosPercentMax : QLabel
        A widget for displaying the maximum percentage of positively flagged
        records available.
    trainPosPercentIn : QDoubleSpinBox
        A widget for inputting the percentage of positively flagged training
        records to use.
    testPosPercentIn : QDoubleSpinBox
        A widget for inputting the percentage of positively flagged testing
        records to use.
    trainSize : int
        The amount of training records to use.
    trainDist : str
        The distribution to use when extracting training records.
    testSize : int
        The amount of testing records to use.
    testDist : str
        The distribution to use when extracting testing records.
    trainPosPercent : float
        The percentage of positively flagged training records to extract.
    testPosPercent : float
        The percentage of positively flagged testing records to extract.

    Methods
    -------
    updateAvailableRecords()
        Updates the availableAmount and trainPosPercentMax attributes.
    ratioInput(QEvent)
        Updates the trainTestRatio attribute in the info attribute.
    amountInput(QEvent)
        Updates trainSize and testSize attributes and the positive percentages.
    trainDistInput(QEvent)
        Updates the trainDist attribute.
    trainPosPercentInput(QEvent)
        Updates the trainPosPercent input.
    testDistInput(QEvent)
        Updates the testDist attribute.
    testPosPercentInput(QEvent)
        Updates the testPosPercent input.
    activatePosPercent(QEvent)
        Activates or deactivates the trainPosPercent and testPosPercent 
        attributes based on the state of the posPercentCheck widget.
    '''
    def __init__(self, info : Info):
        '''
        Constructs attributes and sets the layout of an Extract object.

        Parameters
        ----------
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(Extract, self).__init__()

        self.info = info

        self.fileLocations = []
        self.fileType = ''
        self.flagColumnLabel = ''

        ratioLabel = QLabel()
        ratioLabel.setText('Ration of Training to Testing records (Train:Test)')

        self.ratio = QComboBox()
        self.ratio.addItems(['60:40',
                        '70:30',
                        '80:20',
                        '90:10'])
        self.ratio.currentIndexChanged.connect(self.ratioInput)
        
        ratioLayout = QHBoxLayout()
        ratioLayout.addWidget(ratioLabel)
        ratioLayout.addWidget(self.ratio)
        
        ratioWidget = QWidget()
        ratioWidget.setLayout(ratioLayout)
        
        self.availableAmount = QLabel()
        self.availableAmount.setText(
            'Number of Records Available: Waiting to Import Data')

        update = QPushButton('Update')
        update.pressed.connect(self.updateAvailableRecords)

        availableAmountLayout = QHBoxLayout()
        availableAmountLayout.addWidget(self.availableAmount)
        availableAmountLayout.addWidget(update)

        availableAmountWidget = QWidget()
        availableAmountWidget.setLayout(availableAmountLayout)

        amountLabel = QLabel('Select the number of records to use')
        self.amount = QLineEdit()
        self.amount.setPlaceholderText('Enter number of records here')
        self.amount.textChanged.connect(self.amountInput)

        amountErrorLabel = QLabel()

        amountLayout = QHBoxLayout()
        amountLayout.addWidget(amountLabel)
        amountLayout.addWidget(self.amount)
        amountLayout.addWidget(amountErrorLabel)

        amountWidget = QWidget()
        amountWidget.setLayout(amountLayout)

        rFrame = b.InputFrame([ratioLabel,
                               ratioWidget,
                               availableAmountWidget,
                               amountWidget])

        distLabel = QLabel()
        distLabel.setText('Select data extraction Distributions')

        trainDistLabel = QLabel()
        trainDistLabel.setText('Training Data Distribution')

        trainDist = QComboBox()
        trainDist.addItems(['Uniform',
                            'Newest Block',
                            'Random Block'])
        trainDist.currentIndexChanged.connect(self.trainDistInput)
        
        trainDistLayout = QHBoxLayout()
        trainDistLayout.addWidget(trainDistLabel)
        trainDistLayout.addWidget(trainDist)

        trainDistWidget = QWidget()
        trainDistWidget.setLayout(trainDistLayout)

        testDistLabel = QLabel()
        testDistLabel.setText('Testing Data Distribution')

        testDist = QComboBox()
        testDist.addItems(['Uniform',
                            'Newest Block',
                            'Random Block'])
        testDist.currentIndexChanged.connect(self.testDistInput)
        
        testDistLayout = QHBoxLayout()
        testDistLayout.addWidget(testDistLabel)
        testDistLayout.addWidget(testDist)

        testDistWidget = QWidget()
        testDistWidget.setLayout(testDistLayout)

        dFrame = b.InputFrame([distLabel,
                              trainDistWidget,
                              testDistWidget])

        posPercentCheck = QCheckBox()
        posPercentCheck.stateChanged.connect(self.activatePosPercent)

        posPercentLabel = QLabel()
        posPercentLabel.setText(
            'Specify percentage of positively flagged records')

        posPercentLayout = QHBoxLayout()
        posPercentLayout.addWidget(posPercentCheck)
        posPercentLayout.addWidget(posPercentLabel)

        posPercentWidget = QWidget()
        posPercentWidget.setLayout(posPercentLayout)

        self.trainPosPercentMax = QLabel()
        self.trainPosPercentMax.setText(
            'Maximum Percentage of Positively Flagged Training Records: '
            'Waiting to Import Data')
        trainPosPercentLabel = QLabel()
        trainPosPercentLabel.setText(
            'Percentage of positively flagged training records')

        self.trainPosPercentIn = QDoubleSpinBox()
        self.trainPosPercentIn.setMinimum(0)
        self.trainPosPercentIn.setSingleStep(0.25)
        self.trainPosPercentIn.valueChanged.connect(self.trainPosPercentInput)
        self.trainPosPercentIn.setEnabled(False)

        trainPosErrorLabel = QLabel()

        trainPosLayout = QHBoxLayout()
        trainPosLayout.addWidget(trainPosPercentLabel)
        trainPosLayout.addWidget(self.trainPosPercentIn)
        trainPosLayout.addWidget(trainPosErrorLabel)

        trainPosWidget = QWidget()
        trainPosWidget.setLayout(trainPosLayout)

        testPosPercentLabel = QLabel()
        testPosPercentLabel.setText('Percentage of positively flagged testing '
                                    'records')

        self.testPosPercentIn = QDoubleSpinBox()
        self.testPosPercentIn.setMinimum(0)
        self.testPosPercentIn.setSingleStep(0.25)
        self.testPosPercentIn.valueChanged.connect(self.testPosPercentInput)
        self.testPosPercentIn.setEnabled(False)

        testPosErrorLabel = QLabel()

        testPosLayout = QHBoxLayout()
        testPosLayout.addWidget(testPosPercentLabel)
        testPosLayout.addWidget(self.testPosPercentIn)
        testPosLayout.addWidget(testPosErrorLabel)

        testPosWidget = QWidget()
        testPosWidget.setLayout(testPosLayout)

        pFrame = b.InputFrame([posPercentWidget,
                               self.trainPosPercentMax,
                               trainPosWidget,
                               testPosWidget])

        layout = QVBoxLayout()
        layout.addWidget(rFrame)
        layout.addWidget(dFrame)
        layout.addWidget(pFrame)

        self.setLayout(layout)

        self.trainSize = 0
        self.trainDist = 'UNIFORM'
        self.testSize = 0
        self.testDist = 'UNIFORM'
        self.trainPosPercent = -1
        self.testPosPercent = -1

    def updateAvailableRecords(self):
        '''
        Updates the availableAmount and trainPosPercentMax attributes.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.amount.text() == '':
            if self.fileLocations != [] and self.flagColumnLabel != '':
                if self.fileType == 'CSV':
                    values = []
                    for location in self.fileLocations:
                        values = values + pd.read_csv(location, 
                                                usecols= [self.flagColumnLabel], 
                                                encoding_errors= 'ignore'
                                                ).values.tolist()
                    self.numberOfRecords = len(values)
                    try:
                        sum = 0
                        for val in values:
                            sum += val[0]
                        self.maxPosPercent = round(100*sum/len(values),2)
                    except TypeError:
                        print('The flag column doesnt have the correct format')
                        self.maxPosPercent = 0
                    if self.trainPosPercentIn.value() > self.maxPosPercent:
                        self.trainPosPercentIn.setValue(0)
                    self.trainPosPercentIn.setMaximum(self.maxPosPercent)
                    if self.testPosPercentIn.value() > self.maxPosPercent:
                        self.testPosPercentIn.setValue(0)
                    self.testPosPercentIn.setMaximum(self.maxPosPercent)
                    self.sum = sum
                elif self.fileType == 'XLSX':
                    values = []
                    for location in self.fileLocations:
                        values = values + pd.read_excel(location, 
                                                usecols= [self.flagColumnLabel]
                                                ).values.tolist()
                        values = values + pd.read_excel(location, 
                                                usecols= [self.flagColumnLabel]
                                                ).values.tolist()
                    self.numberOfRecords = len(values)
                    sum = 0
                    for val in values:
                        sum += val[0]
                    self.maxPosPercent = round(100*sum/len(values),2)
                    if self.trainPosPercentIn.value() > self.maxPosPercent:
                        self.trainPosPercentIn.setValue(0)
                    self.trainPosPercentIn.setMaximum(self.maxPosPercent)
                    if self.testPosPercentIn.value() > self.maxPosPercent:
                        self.testPosPercentIn.setValue(0)
                    self.testPosPercentIn.setMaximum(self.maxPosPercent)
                self.availableAmount.setText(
                    f'Number of Records Available: {self.numberOfRecords}')
                self.trainPosPercentMax.setText(
                    f'Maximum Percentage of Positively Flagged Records: '
                    f'{self.maxPosPercent} %')
                self.sum = sum
            else:
                print('idk what to do here yet')
        else:
            try:
                amount = int(self.amount.text)
            except:
                print('Amount couldnt be converted to an int')
                amount = 100000
            if self.fileLocations != [] and self.flagColumnLabel != '':
                if self.fileType == 'CSV':
                    values = []
                    for location in self.fileLocations:
                        values = values + pd.read_csv(location, 
                                                usecols= [self.flagColumnLabel], 
                                                encoding_errors= 'ignore'
                                                ).values.tolist()
                    self.numberOfRecords = len(values)
                    try:
                        sum = 0
                        for val in values:
                            sum += val[0]
                        self.maxPosPercent = round(100*sum/amount,2)
                    except TypeError:
                        print('The flag column doesnt have the correct format')
                        self.maxPosPercent = 0
                    if self.trainPosPercentIn.value() > self.maxPosPercent:
                        self.trainPosPercentIn.setValue(0)
                    self.trainPosPercentIn.setMaximum(self.maxPosPercent)
                    if self.testPosPercentIn.value() > self.maxPosPercent:
                        self.testPosPercentIn.setValue(0)
                    self.testPosPercentIn.setMaximum(self.maxPosPercent)
                    self.sum = sum
                elif self.fileType == 'XLSX':
                    values = []
                    for location in self.fileLocations:
                        values = values + pd.read_excel(location, 
                                                usecols= [self.flagColumnLabel]
                                                ).values.tolist()
                        values = values + pd.read_excel(location, 
                                                usecols= [self.flagColumnLabel]
                                                ).values.tolist()
                    self.numberOfRecords = len(values)
                    sum = 0
                    for val in values:
                        sum += val[0]
                    self.maxPosPercent = round(100*sum/len(values),2)
                    if self.trainPosPercentIn.value() > self.maxPosPercent:
                        self.trainPosPercentIn.setValue(0)
                    self.trainPosPercentIn.setMaximum(self.maxPosPercent)
                    if self.testPosPercentIn.value() > self.maxPosPercent:
                        self.testPosPercentIn.setValue(0)
                    self.testPosPercentIn.setMaximum(self.maxPosPercent)
                self.availableAmount.setText(
                    f'Number of Records Available: {self.numberOfRecords}')
                self.trainPosPercentMax.setText(
                    f'Maximum Percentage of Positively Flagged Records: '
                    f'{self.maxPosPercent} %')
                self.sum = sum
            else:
                print('idk what to do here yet')

    def ratioInput(self, e : QEvent):
        '''
        Updates the trainTestRation attribute in the info attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the index of the ratio attribute.

        Returns
        -------
        None
        '''
        match e:
            case 0:
                self.info.trainTestRation = '60:40'
                self.info.updateInfo()
            case 1:
                self.info.trainTestRation = '70:30'
                self.info.updateInfo()
            case 2:
                self.info.trainTestRation = '80:20'
                self.info.updateInfo()
            case 3:
                self.info.trainTestRation = '90:10'
                self.info.updateInfo()

    def amountInput(self, e : QEvent):
        '''
        Updates trainSize and testSize attributes and the positive percentages.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the text of the amount attribute.

        Returns
        -------
        None
        '''
        try:
            amount = int(e)
            self.info.numberOfRecords = amount
            self.info.updateInfo()
            try:
                self.maxPosPercent = round(100*self.sum/amount,2)
            except AttributeError:
                print('Update hasnt been pressed yet so there is no self.sum')
                self.maxPosPercent = 100
            self.trainPosPercentIn.setMaximum(self.maxPosPercent)
            self.testPosPercentIn.setMaximum(self.maxPosPercent)
            if self.maxPosPercent > 100:
                self.maxPosPercent = 100
            if self.trainPosPercentIn.value() > self.maxPosPercent:
                self.trainPosPercentIn.setValue(0)
                self.trainPosPercentIn.setMaximum(self.maxPosPercent)
            if self.testPosPercentIn.value() > self.maxPosPercent:
                self.testPosPercentIn.setValue(0)
                self.testPosPercentIn.setMaximum(self.maxPosPercent)
            self.trainPosPercentMax.setText(
                    f'Maximum Percentage of Positively Flagged Records: '
                    f'{self.maxPosPercent} %')    
            match self.ratio.currentText():
                case '60:40':
                    self.trainSize = math.floor(0.6*amount)
                    self.testSize = amount - self.trainSize
                case '70:30':
                    self.trainSize = math.floor(0.7*amount)
                    self.testSize = amount - self.trainSize
                case '80:20':
                    self.trainSize = math.floor(0.8*amount)
                    self.testSize = amount - self.trainSize
                case '90:10':
                    self.trainSize = math.floor(0.9*amount)
                    self.testSize = amount - self.trainSize
        except (UnboundLocalError, ValueError):
            print(
                'Amount couldnt be converted to an int or theres nothing there')
            self.maxPosPercent = 100

    def trainDistInput(self, e : QEvent):
        '''
        Updates the trainDist attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the index of the trainDist widget.

        Returns
        -------
        None
        '''
        match e:
            case 0:
                self.trainDist = 'UNIFORM'
            case 1:
                self.trainDist = 'NEWESTBLOCK'
            case 2:
                self.trainDist = 'RANDOMBLOCK'
        self.info.trainDist = self.trainDist
        self.info.updateInfo()

    def trainPosPercentInput(self, e : QEvent):
        '''
        Updates the trainPosPercent attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the value of the trainPosPercentIn
            attribute.

        Returns
        -------
        None 
        '''
        if e == 0:
            self.trainPosPercent = -1
        else:
            self.trainPosPercent = e
        self.info.trainPosPercent = self.trainPosPercent
        self.info.updateInfo()

    def testDistInput(self, e : QEvent):
        '''
        Updates the testDist attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the index of the testDist widget.

        Returns
        -------
        None
        '''
        match e:
            case 0:
                self.testDist = 'UNIFORM'
            case 1:
                self.testDist = 'NEWESTBLOCK'
            case 2:
                self.testDist = 'RANDOMBLOCK'
        self.info.testDist = self.testDist
        self.info.updateInfo()

    def testPosPercentInput(self, e : QEvent):
        '''
        Updates the testPosPercent attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the value of the testPosPercentIn
            attribute.

        Returns
        -------
        None 
        '''
        if e == 0:
            self.testPosPercent = -1
        else:
            self.testPosPercent = e
        self.info.testPosPercent = self.testPosPercent
        self.info.updateInfo()

    def activatePosPercent(self, e : QEvent):
        '''
        Activates or deactivates the trainPosPercent and testPosPercent 
        attributes based on the state of the posPercentCheck widget.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the posPercentCheck widget.

        Returns
        -------
        None
        '''
        if e == 0:
            self.trainPosPercentIn.setEnabled(False)
            self.trainPosPercentIn.setValue(0)
            self.testPosPercentIn.setEnabled(False)
            self.testPosPercentIn.setValue(0)
            self.trainPosPercent = -1
            self.testPosPercent = -1
            self.info.trainPosPercent = self.trainPosPercent
            self.info.testPosPercent = self.testPosPercent
            self.info.updateInfo()
        else:
            self.trainPosPercentIn.setEnabled(True)
            self.testPosPercentIn.setEnabled(True)