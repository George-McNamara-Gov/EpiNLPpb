'''
Creates a widget for selecting corpus level techniques in the vectorise tab.

Classes:

    Corpus

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QWidget,
                             QLabel,
                             QHBoxLayout,
                             QVBoxLayout,
                             QComboBox
                            )
from PyQt6.QtCore import QEvent
from . import base as vb
from .. import base as b
from ..info import Info

class Corpus(QWidget):
    '''
    A widget for selecting a corpus level technique in the vectorise tab.

    ...

    Attributes
    ----------
    info : Info
        A scroll area displayig the parameters of the program being built.
    mod : TechniqueCheck
        A TechniqueCheck for pre vectorisation modification.
    corpusLevelLA : str
        The name of the corpus level technique to use.
    Methods
    -------
    modInput(QEvenet)
        Alters the corpusLevelLA attribute and updates the info attribute.
    vectoriserInput(QEvenet)
        Sets the corpusLevelLA attribute and updates the info attribute.
    '''
    def __init__(self, info : Info):
        '''
        Constructs attributes and sets the layout for a Corpus object.

        Parameters
        ----------
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(Corpus, self).__init__()

        self.info = info

        displayLabel = QLabel()
        displayLabel.setText('Corpus Display')
        displayLayout = QVBoxLayout()
        displayLayout.addWidget(displayLabel)
        display = QWidget()
        display.setLayout(displayLayout)

        techLabel = QLabel()
        techLabel.setText('Corpus Level Techniques')

        self.mod = vb.TechniqueCheck('Pre Vectorisation Modification', 
                                     '')
        self.mod.check.stateChanged.connect(self.modInput)

        vectLabel = QLabel()
        vectLabel.setText('Vectorisers')

        vectoriser = QComboBox()
        vectoriser.addItems(['None',
                             'Count Vectoriser',
                             'Tfidf Vectoriser',
                             'Hashing Vectoriser'])
        vectoriser.currentIndexChanged.connect(self.vectoriserInput)
        
        frame = b.InputFrame([techLabel,
                              self.mod,
                              vectLabel,
                              vectoriser])

        layout = QHBoxLayout()
        layout.addWidget(display)
        layout.addWidget(frame)

        self.setLayout(layout)

        self.corpusLevelLA = ''

    def modInput(self, e : QEvent):
        '''
        Alters the corpusLevelLA attribute and updates the info attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the mod attribute.

        Returns
        -------
        None 
        '''
        if e == 0:
            if self.corpusLevelLA == 'MOD_BAG_OF_WORDS_C':
                self.corpusLevelLA = 'BAG_OF_WORDS_C'
            if self.corpusLevelLA == 'MOD_BAG_OF_WORDS_F':
                self.corpusLevelLA = 'BAG_OF_WORDS_F'
            if self.corpusLevelLA == 'MOD_BAG_OF_WORDS_H':
                self.corpusLevelLA = 'BAG_OF_WORDS_H'
        else:
            if self.corpusLevelLA == 'BAG_OF_WORDS_C':
                self.corpusLevelLA = 'MOD_BAG_OF_WORDS_C'
            if self.corpusLevelLA == 'BAG_OF_WORDS_F':
                self.corpusLevelLA = 'MOD_BAG_OF_WORDS_F'
            if self.corpusLevelLA == 'BAG_OF_WORDS_H':
                self.corpusLevelLA = 'MOD_BAG_OF_WORDS_H'
        self.info.corpusLevelLA = self.corpusLevelLA
        self.info.updateInfo()

    def vectoriserInput(self, e : QEvent):
        '''
        Sets the corpusLevelLA attribute and updates the info attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the vectoriser widget.

        Returns
        -------
        None
        '''
        match e:
            case 0:
                self.corpusLevelLA = ''
            case 1:
                if self.mod.check.isChecked():
                    self.corpusLevelLA = 'MOD_BAG_OF_WORDS_C'
                else:
                    self.corpusLevelLA = 'BAG_OF_WORDS_C'
            case 2:
                if self.mod.check.isChecked():
                    self.corpusLevelLA = 'MOD_BAG_OF_WORDS_F'
                else:
                    self.corpusLevelLA = 'BAG_OF_WORDS_F'
            case 3:
                if self.mod.check.isChecked():
                    self.corpusLevelLA = 'MOD_BAG_OF_WORDS_H'
                else:
                    self.corpusLevelLA = 'BAG_OF_WORDS_H'
        self.info.corpusLevelLA = self.corpusLevelLA
        self.info.updateInfo()