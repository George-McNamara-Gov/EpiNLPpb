'''
Main module of the gui/build/vectorise package to create a tab in 
gui/build/build.py.

Classes:

    Vectorise

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QTabWidget,
                            QWidget,
                            QVBoxLayout
                            )
from . import preLA as p
from . import token as t
from . import text as te
from . import corpus as c
from ..info import Info

class Vectorise(QWidget):
    '''
    A widget to select the vectorisation techniques for an NLP program.

    ...

    Attributes
    ----------
    info : Info
        A scroll area displayig the parameters of the program being built.
    preLA : preLA
        A widget for selecting preLA techniques.
    tokenLevel : Token
        A widget for selecting token level techniques.
    textLevel : Text
        A widget for selecting text level techniques.
    corpusLevel : Corpus
        A widget for selecting a corpus level technique.

    Methods
    -------
    None
    '''
    def __init__(self, info : Info):
        '''
        Constructs attributes and sets the layout for a Vectorise object.

        Parameters
        ----------
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(Vectorise, self).__init__()

        self.info = info

        self.preLA = p.PreLA(info)
        self.tokenLevel = t.Token(info)
        self.textLevel = te.Text(info)
        self.corpusLevel = c.Corpus(info)

        vectoriseTab = QTabWidget()
        vectoriseTab.addTab(self.preLA, 'Pre-LA')
        vectoriseTab.addTab(self.tokenLevel, 'Token Level')
        vectoriseTab.addTab(self.textLevel, 'Text Level')
        vectoriseTab.addTab(self.corpusLevel, 'Corpus Level')

        vectoriseLayout = QVBoxLayout()
        vectoriseLayout.addWidget(vectoriseTab)

        self.setLayout(vectoriseLayout)