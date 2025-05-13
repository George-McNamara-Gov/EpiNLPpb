'''
Creates a widget for building, evaluating and exporting NLP programs.

Classes:

    Create

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QWidget,
                             QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QFileDialog
                            )
from PyQt6.QtCore import QSize
import sys
import os

sys.path.append(str(os.getcwd()) + '\\package')

from ...package import base
from . import base as b
from . import importer as i
from . import filter as f
from . import extract as ex
from .vectorise import vectorise as v
from . import mlearn as m
from .info import Info

class Create(QWidget):
    '''
    A widget to build, evaluate and export NLP programs once their parameters
    are set.

    ...

    Attributes
    ----------
    importer : Importer
        The importer tab widget.
    filter : Filter
        The filter tab widget.
    extract : Extract
        The extract tab widget.
    vectorise : Vectorise
        The vectorise tab widget.
    mlearn : MLearn
        The machine learning tab widget.
    info : Info
        A scroll area displaying the parameters of the program being built.
    name : QLineEdit
        A widget to input the name of the NLP program.
    createButton : QPushButton
        A widget to initiate the creation of an NLP program.
    evaluateButton : QPushButton
        A widget to initiate the evaluation of an NLP program.
    apprComp : QPushButton
        A widget to initiate approximating the complexity of an NLP program.
    exportDisplay : QLineEdit
        A widget to input and display the path to export an NLP program to.
    exportBrowse : QPushButton
        A widget to initiate browsing file locations for export.
    exportButton : QPushButton
        A widget to initiate the export of an NLP program.

    Methods
    -------
    nameEntered()
        Activates the createButton attribute once a name has been input.
    createModel()
        Extracts parameters from the tabs in the build object, creates an NLP
        object, and creates an NLP program.
    evaluateModel()
        Evaluates an NLP program.
    approximateComplexities()
        Approximates the complexities of an NLP program.
    helpPopUp()
        Displays a pop-up window with a help message.
    selectLocation()
        Provides the export location to the exportDisplay and exportButton 
        attributes.
    exportModel()
        Exports an NLP program.
    '''
    def __init__(self, 
                 importer : i.Importer,
                 filter : f.Filter,
                 extract : ex.Extract,
                 vectorise : v.Vectorise,
                 mlearn : m.MLearn,
                 info : Info):
        '''
        Constructs attributes and sets the layout of a Create object.

        Parameters
        ----------
        importer : Importer
            The importer tab widget.
        filter : Filter
            The filter tab widget.
        extract : Extract
            The extract tab widget.
        vectorise : Vectorise
            The vectorise tab widget.
        mlearn : MLearn
            The machine learning tab widget.
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(Create, self).__init__()

        self.importer = importer
        self.filter = filter
        self.extract = extract
        self.vectorise = vectorise
        self.mlearn = mlearn
        self.info = info

        createLabel = QLabel('Create NLP program')

        nameLabel = QLabel('Enter a model name:')

        self.name = QLineEdit()
        self.name.setPlaceholderText('Enter name here')
        self.name.textChanged.connect(self.nameEntered)

        nameLayout = QHBoxLayout()
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(self.name)

        nameWidget = QWidget()
        nameWidget.setLayout(nameLayout)

        self.createButton = QPushButton('Create Model')
        self.createButton.pressed.connect(self.createModel)
        self.createButton.setEnabled(False)

        importLabel = QLabel('Importing ')

        importLayout = QHBoxLayout()
        importLayout.addWidget(importLabel)

        importWidget = QWidget()
        importWidget.setLayout(importLayout)

        filterLabel = QLabel('Filtering ')

        filterLayout = QHBoxLayout()
        filterLayout.addWidget(filterLabel)

        filterWidget = QWidget()
        filterWidget.setLayout(filterLayout)

        extractLabel = QLabel('Extracting ')

        extractLayout = QHBoxLayout()
        extractLayout.addWidget(extractLabel)

        extractWidget = QWidget()
        extractWidget.setLayout(extractLayout)

        vectoriseLabel = QLabel('Vectorising ')

        vectoriseLayout = QHBoxLayout()
        vectoriseLayout.addWidget(vectoriseLabel)

        vectoriseWidget = QWidget()
        vectoriseWidget.setLayout(vectoriseLayout)

        mlLabel = QLabel('Training Algorithm')

        mlLayout = QHBoxLayout()
        mlLayout.addWidget(mlLabel)

        mlWidget = QWidget()
        mlWidget.setLayout(mlLayout)

        cFrame = b.InputFrame([createLabel,
                               nameWidget,
                               self.createButton,
                               importWidget,
                               filterWidget,
                               extractWidget,
                               vectoriseWidget,
                               mlWidget])
        
        evaluateLabel = QLabel('Evaluate NLP program')

        self.evaluateButton = QPushButton('Evaluate Model')
        self.evaluateButton.setEnabled(False)
        self.evaluateButton.pressed.connect(self.evaluateModel)

        self.apprComp = QPushButton('Approximate Complexities')
        self.apprComp.setEnabled(False)
        self.apprComp.pressed.connect(self.approximateComplexities)

        help = QPushButton('?')
        help.setFixedSize(QSize(20,20))
        help.pressed.connect(self.helpPopUp)

        apprCompLayout = QHBoxLayout()
        apprCompLayout.addWidget(self.apprComp)
        apprCompLayout.addWidget(help)

        apprCompWidget = QWidget()
        apprCompWidget.setLayout(apprCompLayout)

        approxLabel = QLabel('Approximating Complexities')

        approxLayout = QHBoxLayout()
        approxLayout.addWidget(approxLabel)

        approxWidget = QWidget()
        approxWidget.setLayout(approxLayout)

        eFrame = b.InputFrame([evaluateLabel,
                               self.evaluateButton,
                               apprCompWidget,
                               approxWidget])
        
        exportTitle = QLabel('Export NLP program')

        exportLabel = QLabel()
        exportLabel.setText('Export Location:')
        self.exportDisplay = QLineEdit()
        self.exportBrowse = QPushButton('Browse')
        self.exportBrowse.setEnabled(False)
        self.exportBrowse.clicked.connect(self.selectLocation)

        exportLayout = QHBoxLayout()
        exportLayout.addWidget(exportLabel)
        exportLayout.addWidget(self.exportDisplay)
        exportLayout.addWidget(self.exportBrowse)
        exportWidget = QWidget()
        exportWidget.setLayout(exportLayout)

        self.exportButton = QPushButton('Export Model')
        self.exportButton.setEnabled(False)
        self.exportButton.pressed.connect(self.exportModel)

        exFrame = b.InputFrame([exportTitle,
                                exportWidget,
                                self.exportButton])

        layout = QVBoxLayout()
        layout.addWidget(cFrame)
        layout.addWidget(eFrame)
        layout.addWidget(exFrame)

        self.setLayout(layout)

    def nameEntered(self):
        '''
        Activates the createButton attribute once a name has been input.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        '''
        self.createButton.setEnabled(True)
    
    def createModel(self):
        '''
        Extracts parameters from the tabs in the build object, creates an NLP
        object, and creates an NLP program.

        Parameters
        ----------
            None
        
        Returns
        -------
            None
        '''

        name = self.name.text()
        fileLocations = self.importer.fileLocations
        fileType = self.importer.fileType
        dateColumnLabel = self.importer.dateColumnLabel
        hospitalColumnLabel = self.importer.hospitalColumnLabel
        sexColumnLabel = self.importer.sexColumnLabel
        ageColumnLabel = self.importer.ageColumnLabel
        textFieldColumnLabels = self.importer.textFieldColumnLabels
        flagColumnLabel = self.importer.flagColumnLabel
        minAge = self.filter.minAge
        maxAge = self.filter.maxAge
        hospital = self.filter.hospital
        sex = self.filter.sex
        minYear = self.filter.minYear
        maxYear = self.filter.maxYear
        trainSize = self.extract.trainSize
        trainDist = self.extract.trainDist
        testSize = self.extract.testSize
        testDist = self.extract.testDist
        tokeniser = self.vectorise.tokenLevel.tokeniser
        preLAChanges = self.vectorise.preLA.preLAChanges
        tokenLevelLA = self.vectorise.tokenLevel.tokenLevelLA
        textLevelLA = self.vectorise.textLevel.textLevelLA
        corpusLevelLA = self.vectorise.corpusLevel.corpusLevelLA
        mlAlgType = self.mlearn.mlAlgType
        macLearnInput = self.mlearn.macLearnInput 
        trainPosPercent = self.extract.trainPosPercent
        testPosPercent = self.extract.testPosPercent

        print(name)
        print(fileLocations)
        print(fileType)
        print(dateColumnLabel)
        print(hospitalColumnLabel)
        print(sexColumnLabel)
        print(ageColumnLabel)
        print(textFieldColumnLabels)
        print(flagColumnLabel)
        print(minAge)
        print(maxAge)
        print(hospital)
        print(sex)
        print(minYear)
        print(maxYear)
        print(trainSize)
        print(trainDist)
        print(testSize)
        print(testDist)
        print(tokeniser)
        print(preLAChanges)
        print(tokenLevelLA)
        print(textLevelLA)
        print(corpusLevelLA)
        print(mlAlgType)
        print(macLearnInput)
        print(trainPosPercent)
        print(testPosPercent)

        self.nlp = base.NLP(name,
                       fileLocations,
                       fileType,
                       dateColumnLabel,
                       hospitalColumnLabel,
                       sexColumnLabel,
                       ageColumnLabel,
                       textFieldColumnLabels,
                       flagColumnLabel,
                       minAge,
                       maxAge,
                       hospital,
                       sex,
                       minYear,
                       maxYear,
                       trainSize,
                       trainDist,
                       testSize,
                       testDist,
                       tokeniser,
                       preLAChanges,
                       tokenLevelLA,
                       textLevelLA,
                       corpusLevelLA,
                       mlAlgType,
                       macLearnInput,
                       trainPosPercent,
                       testPosPercent)
        
        self.nlp.create()

        self.name.setEnabled(False)
        self.createButton.setEnabled(False)
        self.evaluateButton.setEnabled(True)

    def evaluateModel(self):
        '''
        Evaluates an NLP program.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.nlp.evaluateNLP()
        self.info.precision = round(self.nlp.outputDic['Precision']*100)
        self.info.recall = round(self.nlp.outputDic['Recall']*100)
        self.info.totalTime = round(self.nlp.outputDic['TotalTime'],3)
        self.info.totalSpace = round(
            self.nlp.outputDic['TotalSpace'] / (1024*1024),3)
        self.info.updateInfo()
        self.evaluateButton.setEnabled(False)
        self.apprComp.setEnabled(True)
        self.exportBrowse.setEnabled(True)

    def approximateComplexities(self):
        '''
        Approximates the complexities of an NLP program.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.nlp.approximateComplexities()
        self.apprComp.setEnabled(False)

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

    def selectLocation(self):
        '''
        Provides the export location to the exportDisplay and exportButton 
        attributes.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        dir = QFileDialog.getExistingDirectory()
        self.exportDisplay.setText(dir)
        self.exportButton.setEnabled(True)

    def exportModel(self):
        '''
        Exports an NLP program.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.nlp.exportNLP()
        self.exportButton.setEnabled(False)
        self.exportBrowse.setEnabled(False)
        self.apprComp.setEnabled(False)