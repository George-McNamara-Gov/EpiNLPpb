'''
Main module of the gui/build package to create a tab in gui/gui.py.

Classes:

    Build

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import QTabWidget
from . import importer as i
from . import filter as f
from . import extract as ex
from .vectorise import vectorise as v
from . import mlearn as m
from . import create as ev
from .info import Info

class Build(QTabWidget):
    '''
    A widget to select the parameters for building an NLP program.

    ...

    Attributes
    ----------
    info : Info
        A scroll area displaying the parameters of the program being built.
    filter : Filter
        The filter tab widget.
    importer : Importer
        The importer tab widget.
    extract : Extract
        The extract tab widget.
    vectorise : Vectorise
        The vectorise tab widget.
    mlearn : MLearn
        The machine learning tab widget.
    createTab : Create
        The create tab widget.

    Methods
    -------
    importInfoExtractor()
        Passes data from the importer attribute to the extract attribute.
    '''
    def __init__(self, info : Info):
        '''
        Constructs attributes and adds tabs to a Build object.

        Parameters
        ----------
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(Build, self).__init__()

        self.info = info

        self.filter = f.Filter(info)
        self.importer = i.Importer(self.filter, info)
        self.extract = ex.Extract(info)
        self.vectorise = v.Vectorise(info)
        self.mlearn = m.MLearn(info)
        self.createTab = ev.Create(self.importer,
                                self.filter,
                                self.extract,
                                self.vectorise,
                                self.mlearn,
                                self.info)

        self.importer.dataDisplay.textChanged.connect(self.importInfoExtractor)
        self.importer.flagColumn.currentIndexChanged.connect(
                                                    self.importInfoExtractor)

        self.addTab(self.importer, 'Import')
        self.addTab(self.filter, 'Filter')
        self.addTab(self.extract, 'Extract')
        self.addTab(self.vectorise, 'Vectorise')
        self.addTab(self.mlearn, 'Machine Learning')
        self.addTab(self.createTab, 'Create')

    def importInfoExtractor(self):
        '''
        Passes data from the importer attribute to the extract attribute.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        '''
        self.extract.fileLocations = self.importer.fileLocations
        self.extract.fileType = self.importer.fileType
        self.extract.flagColumnLabel = self.importer.flagColumnLabel