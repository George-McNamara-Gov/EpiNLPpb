'''
Creates a widget for initialising machine learning parameters.

Classes:

    MLearn

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QWidget,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QLabel,
                             QComboBox,
                             QSpinBox)
from PyQt6.QtCore import (QSize,
                          QEvent)
from .info import Info
from . import base as b

class MLearn(QWidget):
    '''
    A widget for initialising machine learning parameters.

    ...

    Attributes
    ----------
    info : Info
        A scroll area displaying the parameters of the program being built.
    decisionTree : QPushButton
        A widget to select a decision tree machine learning algorithm.
    svm : QPushButton
        A widget to select an SVM machine learning algorithm.
    impurity : QComboBox
        A widget to select the impurity measure for a decision tree.
    kernelLabel : QLabel
        A label for the kernel attribute.
    kernel : QComboBox
        A widget to select the kernel for an SVM algorithm.
    gammaLabel : QLabel
        A label for the gamma attribute.
    gamma : QSpinBox
        A widget to select the gamma parameter for an SVM kernel.
    gammaAuto : QPushButton
        A widget to select the auto preset gamma parameter for an SVM kernel.
    gammaScale : QPushButton
        A widget to select the scale preset gamma parameter for an SVM kernel.
    rLabel : QLabel
        A label for the r attribute.
    r : QSpinBox
        A widget to select the r parameter for an SVM kernel.
    degreeLabel : QLabel
        A label for the degree attribute.
    degree : QSpinBox
        A widget to select the degree parameter for an SVM kernel.
    mlAlgType : str
        The type of machine learning algorithm to use.
    macLearnInput : list
        The parameters for the machine learning algorithm.

    Methods
    -------
    treeModel()
        Activates the widgets required for a decision tree algorithm.
    vectorModel()
        Activates the widgets required for an SVM algorithm.
    kernelInput(QEvent)
        Activates the parameter widgets required for a particular SVM kernel.
    gammaManual()
        Updates the gamma parameter using a manual input.
    gammaPresetAuto()
        Deactivates other gamma input widgets.
    gammaAutoInput()
        Updates the gamma parameter using an auto preset input.
    gammaPresetScale()
        Deactivates other gamma input widgets.
    gammaScaleInput()
        Updates the gamma parameter using a scale preset input.
    impurityInput(QEvent)
        Updates the impurity parameter.
    rInput()
        Updates the r parameter.
    degreeInput()
        Updates the degree parameter.
    helpPopUp()
        Displays a pop-up window with a help message.
    '''
    def __init__(self, info : Info):
        '''
        Constructs attributes and sets the layout of a MLearn object.

        Parameters
        ----------
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(MLearn, self).__init__()

        self.info = info

        algorithmLabel = QLabel()
        algorithmLabel.setText('Select a Machine Learning Algorithm')

        self.decisionTree = QPushButton('Decision Tree')
        self.decisionTree.setCheckable(True)
        self.decisionTree.pressed.connect(self.treeModel)

        self.svm = QPushButton('Support Vector Machine')
        self.svm.setCheckable(True)
        self.svm.pressed.connect(self.vectorModel)

        algorithmLayout = QHBoxLayout()
        algorithmLayout.addWidget(self.decisionTree)
        algorithmLayout.addWidget(self.svm)

        algorithmWidget = QWidget()
        algorithmWidget.setLayout(algorithmLayout)

        aFrame = b.InputFrame([algorithmLabel,
                               algorithmWidget])

        impurityLabel = QLabel()
        impurityLabel.setText('Select Impurity Criterion')

        self.impurity = QComboBox()
        self.impurity.addItems(['GINI',
                           'Entropy',
                           'Log Loss'])
        self.impurity.setEnabled(False)
        self.impurity.currentIndexChanged.connect(self.impurityInput)
        
        tFrame = b.InputFrame([impurityLabel,
                               self.impurity])

        self.kernelLabel = QLabel('Select a kernel')
        self.kernelLabel.setEnabled(False)

        self.kernel = QComboBox()
        self.kernel.addItems(
            ['Linear', 'Radial Basis Function', 'Polynomial', 'Sigmoid']
            )
        self.kernel.currentIndexChanged.connect(self.kernelInput)
        self.kernel.setEnabled(False)

        self.gammaLabel = QLabel('Select a Gamma parameter')
        self.gammaLabel.setEnabled(False)

        self.gamma = QSpinBox()
        self.gamma.setEnabled(False)
        self.gamma.valueChanged.connect(self.gammaManual)

        self.gammaAuto = QPushButton('Auto')
        self.gammaAuto.setCheckable(True)
        self.gammaAuto.setEnabled(False)
        self.gammaAuto.pressed.connect(self.gammaPresetAuto)
        self.gammaAuto.clicked.connect(self.gammaAutoInput)
        self.gammaScale = QPushButton('Scale')
        self.gammaScale.setCheckable(True)
        self.gammaScale.setEnabled(False)
        self.gammaScale.pressed.connect(self.gammaPresetScale)
        self.gammaScale.clicked.connect(self.gammaScaleInput)

        help = QPushButton('?')
        help.setFixedSize(QSize(20,20))
        help.pressed.connect(self.helpPopUp)

        gammaPresetLayout = QHBoxLayout()
        gammaPresetLayout.addWidget(self.gammaAuto)
        gammaPresetLayout.addWidget(self.gammaScale)
        gammaPresetLayout.addWidget(help)

        gammaPreset = QWidget()
        gammaPreset.setLayout(gammaPresetLayout)

        self.rLabel = QLabel('Select an "r" parameter')
        self.rLabel.setEnabled(False)

        self.r = QSpinBox()
        self.r.setEnabled(False)
        self.r.valueChanged.connect(self.rInput)

        self.degreeLabel = QLabel('Select a degree')
        self.degreeLabel.setEnabled(False)

        self.degree = QSpinBox()
        self.degree.setEnabled(False)
        self.degree.valueChanged.connect(self.degreeInput)

        sFrame = b.InputFrame([self.kernelLabel,
                               self.kernel,
                               self.gammaLabel,
                               self.gamma,
                               gammaPreset,
                               self.rLabel,
                               self.r,
                               self.degreeLabel,
                               self.degree])

        paramsLayout = QHBoxLayout()
        paramsLayout.addWidget(tFrame)
        paramsLayout.addWidget(sFrame)

        paramsWidget = QWidget()
        paramsWidget.setLayout(paramsLayout)

        layout = QVBoxLayout()
        layout.addWidget(aFrame)
        layout.addWidget(paramsWidget)

        self.setLayout(layout)

        self.mlAlgType = 'DECISIONTREE'
        self.macLearnInput = ['GINI']

    def treeModel(self):
        '''
        Activates the widgets required for a decision tree algorithm.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.decisionTree.isChecked():
            self.impurity.setEnabled(False)
        else:
            self.svm.setChecked(False)
            self.kernel.setEnabled(False)
            self.kernel.setCurrentIndex(0)
            self.gamma.setEnabled(False)
            self.r.setEnabled(False)
            self.degree.setEnabled(False)
            self.impurity.setEnabled(True)
        self.mlAlgType = 'DECISIONTREE'
        self.macLearnInput = ['GINI']
        self.info.mlAlgType = self.mlAlgType
        self.info.impurity = self.macLearnInput[0]
        self.info.kernel = None
        self.info.updateInfo()

    def vectorModel(self):
        '''
        Activates the widgets required for an SVM algorithm.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        if self.svm.isChecked():
            self.svm.setChecked(False)
            self.kernel.setEnabled(False)
            self.gamma.setEnabled(False)
            self.r.setEnabled(False)
            self.degree.setEnabled(False)
        else:
            self.decisionTree.setChecked(False)
            self.impurity.setEnabled(False)
            self.impurity.setCurrentIndex(0)
            self.kernel.setEnabled(True)
        self.mlAlgType = 'SVMACHINE'
        self.macLearnInput = ['LINEAR',0,0]
        self.info.mlAlgType = self.mlAlgType
        self.info.impurity = None
        self.info.kernel = 'LINEAR'
        self.info.updateInfo()

    def kernelInput(self, e : QEvent):
        '''
        Activates the parameter widgets required for a particular SVM kernel.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the index of the kernel attribute.

        Returns
        -------
            None
        '''
        match e:
            case 0:
                self.gammaLabel.setEnabled(False)
                self.gamma.setEnabled(False)
                self.gammaAuto.setEnabled(False)
                self.gammaScale.setEnabled(False)
                self.gammaScale.setChecked(False)
                self.gamma.setValue(0)
                self.rLabel.setEnabled(False)
                self.r.setEnabled(False)
                self.r.setValue(0)
                self.degreeLabel.setEnabled(False)
                self.degree.setEnabled(False)
                self.degree.setValue(0)
                self.macLearnInput[0] = 'LINEAR'
                self.info.kernel = 'LINEAR'
                self.info.gamma = 0
                self.info.r = 0
                self.info.degree = 0
            case 1:
                self.gammaLabel.setEnabled(True)
                self.gamma.setEnabled(True)
                self.gammaAuto.setEnabled(True)
                self.gammaAuto.setChecked(False)
                self.gammaScale.setEnabled(True)
                self.gammaScale.setChecked(False)
                self.rLabel.setEnabled(False)
                self.r.setEnabled(False)
                self.r.setValue(0)
                self.degreeLabel.setEnabled(False)
                self.degree.setEnabled(False)
                self.degree.setValue(0)
                self.macLearnInput[0] = 'RBF'
                self.info.kernel = 'RBF'
                self.info.r = 0
                self.info.degree = 0
            case 2:
                self.gammaLabel.setEnabled(False)
                self.gamma.setEnabled(False)
                self.gammaAuto.setEnabled(False)
                self.gammaAuto.setChecked(False)
                self.gammaScale.setEnabled(False)
                self.gammaScale.setChecked(False)
                self.gamma.setValue(0)
                self.rLabel.setEnabled(True)
                self.r.setEnabled(True)
                self.degreeLabel.setEnabled(True)
                self.degree.setEnabled(True)
                self.macLearnInput[0] = 'POLYNOMIAL'
                self.info.kernel = 'POLYNOMIAL'
                self.info.gamma = 0
            case 3:
                self.gammaLabel.setEnabled(True)
                self.gamma.setEnabled(True)
                self.gammaAuto.setEnabled(True)
                self.gammaAuto.setChecked(False)
                self.gammaScale.setEnabled(True)
                self.gammaScale.setChecked(False)
                self.rLabel.setEnabled(True)
                self.r.setEnabled(True)
                self.degreeLabel.setEnabled(False)
                self.degree.setEnabled(False)
                self.degree.setValue(0)
                self.macLearnInput[0] = 'SIGMOID'
                self.info.kernel = 'SIGMOID'
                self.info.r = 0
        self.info.updateInfo()

    def gammaManual(self):
        '''
        Updates the gamma parameter using a manual input.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.gammaAuto.setChecked(False)
        self.gammaScale.setChecked(False)
        self.macLearnInput[1] = self.gamma.value()
        self.info.gamma = self.macLearnInput[1]
        self.info.updateInfo()
    
    def gammaPresetAuto(self):
        '''
        Deactivates other gamma input widgets.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.macLearnInput[1] = 'auto'
        self.info.gamma = self.macLearnInput[1]
        self.info.updateInfo()
        if self.gammaAuto.isChecked():
            self.gammaAuto.setChecked(False)
        else:
            self.gamma.setValue(0)
            self.gammaScale.setChecked(False)
    
    def gammaAutoInput(self):
        '''
        Updates the gamma parameter using an auto preset input.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.macLearnInput[1] = 'auto'
        self.info.gamma = self.macLearnInput[1]
        self.info.updateInfo()

    def gammaPresetScale(self):
        '''
        Deactivates other gamma input widgets.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.macLearnInput[1] = 'scale'
        self.info.gamma = self.macLearnInput[1]
        self.info.updateInfo()
        if self.gammaScale.isChecked():
            self.gammaScale.setChecked(False)
        else:
            self.gamma.setValue(0)
            self.gammaAuto.setChecked(False)

    def gammaScaleInput(self):
        '''
        Updates the gamma parameter using a scale preset input.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.macLearnInput[1] = 'scale'
        self.info.gamma = self.macLearnInput[1]
        self.info.updateInfo()

    def impurityInput(self, e : QEvent):
        '''
        Updates the impurity parameter.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the index of the impurity attribute.

        Returns
        -------
        None
        '''
        match e:
            case 0:
                self.macLearnInput[0] = 'GINI'
            case 1: 
                self.macLearnInput[0] = 'ENTROPY'
            case 2:
                self.macLearnInput[0] = 'LOGLOSS'
        self.info.impurity = self.macLearnInput[0]
        self.info.updateInfo()

    def rInput(self):
        '''
        Updates the r parameter.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.macLearnInput[2] = self.r.value()
        self.info.r = self.macLearnInput[2]
        self.info.updateInfo()

    def degreeInput(self):
        '''
        Updates the degree parameter.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.macLearnInput[1] = self.degree.value()
        self.info.degree = self.macLearnInput[1]
        self.info.updateInfo()

    def helpPopUp(self):
        '''
        Displays a pop-up window with a help message.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        helpMessage = ''
        dlg = b.CustomDialog(helpMessage)
        dlg.exec()