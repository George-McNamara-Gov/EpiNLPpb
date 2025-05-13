'''
Creates a widget for filtering data for training and testing an NLP program.

Classes:

    Filter

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QLabel,
                            QVBoxLayout,
                            QWidget,
                            QSlider,
                            QCheckBox,
                            QHBoxLayout
                            )
from PyQt6.QtCore import (Qt,
                          QEvent)
from . import base as b
from .info import Info

class Filter(QWidget):
    '''
    A widget for filtering data for training and testing an NLP program.

    ...

    Attributes
    ----------
    info : Info
        A scroll area displaying the parameters of the program being built.
    minAgeLabel : QLabel
        A widget to display the minimum age.
    minAgeIn : QSlider
        A widget to select the minimum age.
    maxAgeLabel : QLabel
        A widget to display the maximum age.
    maxAgeIn : QSlider
        A widget to select the maximum age.
    aFrame : InputFrame
        A frame to hold the age related widgets.
    CHHS : QCheckBox
        A widget to select whether to include the CHHS hospital.
    CHPB : QCheckBox
        A widget to select whether to include the CHPB hospital.
    hFrame : InputFrame
        A frame to hold the hospital related widgets.
    male : QCheckBox
        A widget to select whether to include male patients.
    female : QCheckBox
        A widget to select whether to include female patients.
    sFrame : InputFrame
        A frame to hold the sex related widgets.
    minYearDefault : int
        A default minimum year value.
    maxYearDefault : int
        A default maximum year value.
    minYearLabel : QLabel
        A widget to display the minimum year.
    minYearIn : QSlider
        A widget to select the minimum year.
    maxYearLabel : QLabel
        A widget to display the maximum year.
    maxYearIn : QSlider
        A widget to select the maximum year.
    dFrame : InputFrame
        A frame to hold the year related widgets.
    minAge : int
        The minimum age of patients to include.
    maxAge : int
        The maximum age of patients to include.
    hospital : str
        The hospitals to include data from.
    sex : str
        The sex(es) of patients to include.
    minYear : int
        The minimum year to include data from.
    maxYear : int
        The maximum year to include data before.

    Methods
    -------
    useAllDataFunc(QEvent)
        Sets all inputs to the broadest values.
    displayMinAge(QEvent)
        Updates the minAgeLabel and minAge attributes.
    displayMaxAge(QEvent)
        Updates the maxAgeLabel and maxAge attributes.
    displayMinYear(QEvent)
        Updates the minYearLabel and minYear attributes.
    displayMaxYear(QEvent)
        Updates the maxYearLabel and maxYear attributes.
    setHosp()
        Updates the hospital attribute.
    setSex()
        Updates the sex attribute.
    aFrameDefault()
        Updates minAgeIn, maxAgeIn, minAgeLabel, and maxAgeLabel attributes to
        their default values.
    hFrameDefault()
        Updates the CHHS and CHPB attributes to their default values.
    sFrameDefault()
        Updates the male and female attributes to their default values.
    dFrameDefault()
        Updates minYearIn, maxYearIn, minYearLabel, and maxYearLabel attributes
        to their default values.
    '''
    def __init__(self, info : Info):
        '''
        Constructs attributes and sets the layout of a Filter object.

        Parameters
        ----------
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(Filter, self).__init__()

        self.info = info

        useAllData = QCheckBox('Use all available data')
        useAllData.stateChanged.connect(self.useAllDataFunc)

        ageDemoLabel = QLabel()
        ageDemoLabel.setText('Age Demographic')

        self.minAgeLabel = QLabel("Select a minimum age: 0")

        self.minAgeIn = QSlider(Qt.Orientation.Horizontal)
        self.minAgeIn.setMinimum(0)
        self.minAgeIn.setMaximum(150)
        self.minAgeIn.setSingleStep(1)
        self.minAgeIn.valueChanged.connect(self.displayMinAge)

        self.maxAgeLabel = QLabel('Select a maximum age: 150')

        self.maxAgeIn = QSlider(Qt.Orientation.Horizontal)
        self.maxAgeIn.setMinimum(0)
        self.maxAgeIn.setMaximum(150)
        self.maxAgeIn.setSingleStep(1)
        self.maxAgeIn.setValue(150)
        self.maxAgeIn.valueChanged.connect(self.displayMaxAge)

        self.aFrame = b.InputFrame([ageDemoLabel, 
                               self.minAgeLabel,
                               self.minAgeIn,
                               self.maxAgeLabel,
                               self.maxAgeIn])
        self.aFrame.setEnabled(False)

        hospDemoLabel = QLabel()
        hospDemoLabel.setText('Hospital Demographic')

        hospitalLabel = QLabel('Select a hospital(s)')

        self.CHHS = QCheckBox('CHHS')
        self.CHHS.setChecked(True)
        self.CHHS.stateChanged.connect(self.setHosp)
        self.CHPB = QCheckBox('CHPB')
        self.CHPB.setChecked(True)
        self.CHPB.stateChanged.connect(self.setHosp)

        hospOpsLayout = QVBoxLayout()
        hospOpsLayout.addWidget(self.CHHS)
        hospOpsLayout.addWidget(self.CHPB)

        hospOpsWidget = QWidget()
        hospOpsWidget.setLayout(hospOpsLayout)

        hospErrorLabel = QLabel()

        hospLayout = QHBoxLayout()
        hospLayout.addWidget(hospOpsWidget)
        hospLayout.addWidget(hospErrorLabel)

        hospWidget = QWidget()
        hospWidget.setLayout(hospLayout)

        self.hFrame = b.InputFrame([hospDemoLabel,
                                    hospitalLabel,
                                    hospWidget])
        self.hFrame.setEnabled(False)

        sexDemoLabel = QLabel()
        sexDemoLabel.setText('Sex Demographic')

        sexLabel = QLabel('Select a sex(es)')

        self.male = QCheckBox('MALE')
        self.male.setChecked(True)
        self.male.stateChanged.connect(self.setSex)
        self.female = QCheckBox('FEMALE')
        self.female.setChecked(True)
        self.female.stateChanged.connect(self.setSex)

        sexOpsLayout = QVBoxLayout()
        sexOpsLayout.addWidget(self.male)
        sexOpsLayout.addWidget(self.female)

        sexOpsWidget = QWidget()
        sexOpsWidget.setLayout(sexOpsLayout)

        sexErrorLabel = QLabel()

        sexLayout = QHBoxLayout()
        sexLayout.addWidget(sexOpsWidget)
        sexLayout.addWidget(sexErrorLabel)

        sexWidget = QWidget()
        sexWidget.setLayout(sexLayout)

        self.sFrame = b.InputFrame([sexDemoLabel,
                                    sexLabel,
                                    sexWidget])
        self.sFrame.setEnabled(False)

        dateDemoLabel = QLabel()
        dateDemoLabel.setText('Date Demographic')

        self.minYearDefault = 2015
        self.maxYearDefault = 2022

        self.minYearLabel = QLabel('Select an earliest year')

        self.minYearIn = QSlider(Qt.Orientation.Horizontal)
        self.minYearIn.setMinimum(2015)
        self.minYearIn.setMaximum(2022)
        self.minYearIn.setSingleStep(1)
        self.minYearIn.valueChanged.connect(self.displayMinYear)

        self.maxYearLabel = QLabel('Select a latest year')

        self.maxYearIn = QSlider(Qt.Orientation.Horizontal)
        self.maxYearIn.setMinimum(2015)
        self.maxYearIn.setMaximum(2022)
        self.maxYearIn.setSingleStep(1)
        self.maxYearIn.setValue(2022)
        self.maxYearIn.valueChanged.connect(self.displayMaxYear)

        self.dFrame = b.InputFrame([dateDemoLabel,
                               self.minYearLabel,
                               self.minYearIn,
                               self.maxYearLabel,
                               self.maxYearIn])
        self.dFrame.setEnabled(False)
        
        layout = QVBoxLayout()
        layout.addWidget(useAllData)
        layout.addWidget(self.aFrame)
        layout.addWidget(self.hFrame)
        layout.addWidget(self.sFrame)
        layout.addWidget(self.dFrame)
        
        self.setLayout(layout)

        self.minAge = 0
        self.maxAge = 150
        self.hospital = 'ALL'
        self.sex = 'ALL'
        self.minYear = 2015
        self.maxYear = 2022

    def useAllDataFunc(self, e : QEvent):
        '''
        Sets all inputs to the broadest values.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the useAllData widget.

        Returns
        -------
        None
        '''
        if e == 2:
            self.minAgeIn.setValue(0)
            self.minAgeIn.setEnabled(False)
            self.minAgeLabel.setText('Select a minimum age')
            self.maxAgeIn.setValue(150)
            self.maxAgeIn.setEnabled(False)
            self.maxAgeLabel.setText('Select a maximum age')
            self.CHHS.setCheckState(Qt.CheckState.Checked)
            self.CHHS.setEnabled(False)
            self.CHPB.setCheckState(Qt.CheckState.Checked)
            self.CHPB.setEnabled(False)
            self.male.setCheckState(Qt.CheckState.Checked)
            self.male.setEnabled(False)
            self.female.setCheckState(Qt.CheckState.Checked)
            self.female.setEnabled(False)
            self.minYearIn.setValue(self.minYearDefault)
            self.minYearLabel.setText('Select an earliest year')
            self.minYearIn.setEnabled(False)
            self.maxYearIn.setValue(self.maxYearDefault)
            self.maxYearIn.setEnabled(False)
            self.maxYearLabel.setText('Select a latest year')
            self.minAge = 0
            self.info.minAge = self.minAge
            self.maxAge = 150
            self.info.maxAge = self.maxAge
            self.hospital = 'ALL'
            self.info.hospital = self.hospital
            self.sex = 'ALL'
            self.info.sex = self.sex
            self.minYear = self.minYearDefault
            self.info.minyear = self.minYear
            self.maxYear = self.maxYearDefault
            self.info.maxYear = self.maxYear
            self.info.updateInfo()
        else:
            self.minAgeIn.setEnabled(True)
            self.maxAgeIn.setEnabled(True)
            self.CHHS.setEnabled(True)
            self.CHPB.setEnabled(True)
            self.male.setEnabled(True)
            self.female.setEnabled(True)
            self.minYearIn.setEnabled(True)
            self.maxYearIn.setEnabled(True)

    def displayMinAge(self, e : QEvent):
        '''
        Updates the minAgeLabel and minAge attributes.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the value of the minAgeIn attribute.

        Returns
        -------
        None
        '''
        self.minAgeLabel.setText(f"Select a minimum age: {e}")
        self.minAge = e
        self.info.minAge = self.minAge
        self.info.updateInfo()
        if self.maxAgeIn.value() <= e:
            self.maxAgeIn.setValue(e)
            self.maxAgeLabel.setText(f"Select a maximum age: {e}")
            self.maxAge = e
            self.info.maxAge = self.maxAge
            self.info.updateInfo()
        self.maxAgeIn.setMinimum(e)
        
    def displayMaxAge(self, e : QEvent):
        '''
        Updates the maxAgeLabel and maxAge attributes.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the value of the maxAgeIn attribute.

        Returns
        -------
        None
        '''
        self.maxAgeLabel.setText(f"Select a maximum age: {e}")
        self.maxAge = e
        self.info.maxAge = self.maxAge
        self.info.updateInfo()

    def displayMinYear(self, e : QEvent):
        '''
        Updates the minYearLabel and minYear attributes.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the value of the minYearIn attribute.

        Returns
        -------
        None
        '''
        self.minYearLabel.setText(f"Select an earliest year: {e}")
        self.minYear = e
        self.info.minYear = self.minYear
        self.info.updateInfo()
        if self.maxYearIn.value() <= e:
            self.maxYearIn.setValue(e)
            self.maxYearLabel.setText(f"Select a latest year: {e}")
            self.maxYear = e
            self.info.maxyear = self.maxYear
            self.info.updateInfo()
        self.maxYearIn.setMinimum(e)

    def displayMaxYear(self, e : QEvent):
        '''
        Updates the maxYearLabel and maxYear attributes.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the value of the maxYearIn attribute.

        Returns
        -------
        None
        '''
        self.maxYearLabel.setText(f"Select a latest year: {e}")
        self.maxYear = e
        self.info.maxYear = self.maxYear
        self.info.updateInfo()

    def setHosp(self):
        '''
        Updates the hospital attribute.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.CHHS.isChecked() and self.CHPB.isChecked():
            self.hospital = 'ALL'
            self.info.hospital = self.hospital
            self.info.updateInfo()
        elif self.CHHS.isChecked() and not self.CHPB.isChecked():
            self.hospital = 'CHHS'
            self.info.hospital = self.hospital
            self.info.updateInfo()
        elif not self.CHHS.isChecked() and self.CHPB.isChecked():
            self.hospital = 'CHPB'
            self.info.hospital = self.hospital
            self.info.updateInfo()
        else:
            print('Need an error here')

    def setSex(self):
        '''
        Updates the sex attribute.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.male.isChecked() and self.female.isChecked():
            self.sex = 'ALL'
            self.info.sex = self.sex
            self.info.updateInfo()
        elif self.male.isChecked() and not self.female.isChecked():
            self.sex = 'MALE'
            self.info.sex = self.sex
            self.info.updateInfo()
        elif not self.male.isChecked() and self.female.isChecked():
            self.sex = 'FEMALE'
            self.info.sex = self.sex
            self.info.updateInfo()
        else:
            print('Need an error here')

    def aFrameDefault(self):
        '''
        Updates minAgeIn, maxAgeIn, minAgeLabel, and maxAgeLabel attributes to
        their default values.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.minAgeIn.setValue(0)
        self.maxAgeIn.setValue(150)
        self.minAgeLabel.setText("Select a minimum age")
        self.maxAgeLabel.setText('Select a maximum age')

    def hFrameDefault(self):
        '''
        Updates the CHHS and CHPB attributes to their default values.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.CHHS.setChecked(True)
        self.CHPB.setChecked(True)

    def sFrameDefault(self):
        '''
        Updates the male and female attributes to their default values.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.male.setChecked(True)
        self.female.setChecked(True)

    def dFrameDefault(self):
        '''
        Updates minYearIn, maxYearIn, minYearLabel, and maxYearLabel attributes
        to their default values.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.minYearIn.setValue(self.minYearDefault)
        self.maxYearIn.setValue(self.maxYearDefault)
        self.minYearLabel.setText('Select an earliest year')
        self.maxYearLabel.setText('Select a latest year')