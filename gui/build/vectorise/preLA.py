'''
Creates a widget for selecting preLA techniques in the vectorise tab.

Classes:

    PreLA

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
                             QVBoxLayout
                            )
from PyQt6.QtCore import QEvent
from . import base as vb
from .. import base as b
from ..info import Info

class PreLA(QWidget):
    '''
    A widget for selecting preLA techniques in the vectorise tab.

    ...

    Attributes
    ----------
    info : Info
        A scroll area displayig the parameters of the program being constructed.
    preLAChanges : list
        A list of names of pre LA techniques to use.

    Methods
    -------
    removeStopInput(QEvent)
        Alters the preLAChanges attribute and updates the info attribute.
    stemmingInput(QEvent)
        Alters the preLAChanges attribute and updates the info attribute.
    '''
    def __init__(self, info : Info):
        '''
        Constructs attributes and sets the layout for a preLA object.

        Parameters
        ----------
        info : Info
            A scroll area displayig the parameters of the program being built.
        '''
        super(PreLA, self).__init__()

        self.info = info

        displayLabel = QLabel()
        displayLabel.setText('PreLA Display')
        displayLayout = QVBoxLayout()
        displayLayout.addWidget(displayLabel)
        display = QWidget()
        display.setLayout(displayLayout)

        techLabel = QLabel()
        techLabel.setText('Pre Linguistic Analysis Techniques')

        removeStopwords = vb.TechniqueCheck('Remove Stopwords',
                                            '')
        removeStopwords.check.stateChanged.connect(self.removeStopInput)
        stemming = vb.TechniqueCheck('Stemming',
                                     '')
        stemming.check.stateChanged.connect(self.stemmingInput)

        frame = b.InputFrame([techLabel,
                              removeStopwords,
                              stemming])

        layout = QHBoxLayout()
        layout.addWidget(display)
        layout.addWidget(frame)

        self.setLayout(layout)

        self.preLAChanges = []

    def removeStopInput(self, e : QEvent):
        '''
        Alters the preLAChanges attribute and updates the info attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the removeStopwords widget.

        Returns
        -------
        None
        '''
        if e == 0 and 'REMOVE_STOPWORDS' in self.preLAChanges:
            self.preLAChanges.remove('REMOVE_STOPWORDS')
        elif 'REMOVE_STOPWORDS' not in self.preLAChanges:
            self.preLAChanges.append('REMOVE_STOPWORDS')
        self.info.preLAChanges = self.preLAChanges
        self.info.updateInfo()


    def stemmingInput(self, e : QEvent):
        '''
        Alters the preLAChanges attribute and updates the info attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the stemming widget.

        Returns
        -------
        None
        '''
        if e == 0 and 'STEMMING' in self.preLAChanges:
            self.preLAChanges.remove('STEMMING')
        elif 'STEMMING' not in self.preLAChanges:
            self.preLAChanges.append('STEMMING')
        self.info.preLAChanges = self.preLAChanges
        self.info.updateInfo()