'''
Creates a widget for selecting token level techniques in the vectorise tab.

Classes:

    Token

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
from PyQt6.QtCore import (QEvent,
                          Qt)
from . import base as vb
from .. import base as b
from ..info import Info

class Token(QWidget):
    '''
    A widget for selecting token level techniques in the vectorise tab.

    ...

    Attributes
    ----------
    info : Info
        A scroll area displayig the parameters of the program being constructed.
    posTag : TechniqueCheck
        A TechniqueCheck for part of speech tagging.
    tokeniser : str
        The name of the tokeniser to use.
    tokenLevelLA : list
        A list of names of token level techniques to use.

    Methods
    -------
    tokeniserInput(QEvent)
        Sets the tokeniser attribute and updates the info attribute.
    posTagInput(QEvent)
        Alters the tokenLevelLA attribute and updates the info attribute.
    '''
    def __init__(self, info : Info):
        '''
        Constructs attributes and sets the layout for a Token object.

        Parameters
        ----------
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(Token, self).__init__()

        self.info = info

        displayLabel = QLabel()
        displayLabel.setText('Token Display')
        displayLayout = QVBoxLayout()
        displayLayout.addWidget(displayLabel)
        display = QWidget()
        display.setLayout(displayLayout)

        tokeniserLabel = QLabel()
        tokeniserLabel.setText('Tokenisers')

        tokeniser = QComboBox()
        tokeniser.addItems(['None',
                            'Word Tokeniser',
                            'Punctuation Tokeniser',
                            'Tweet Tokeniser'])
        tokeniser.currentIndexChanged.connect(self.tokeniserInput)
        
        techLabel = QLabel()
        techLabel.setText('Token Level Techniques')
        
        self.posTag = vb.TechniqueCheck('Part of Speech Tagging',
                                        '')
        self.posTag.check.setEnabled(False)
        self.posTag.check.stateChanged.connect(self.posTagInput)

        frame = b.InputFrame([tokeniserLabel,
                              tokeniser,
                              techLabel,
                              self.posTag])

        layout = QHBoxLayout()
        layout.addWidget(display)
        layout.addWidget(frame)

        self.setLayout(layout)

        self.tokeniser = ''
        self.tokenLevelLA = []

    def tokeniserInput(self, e : QEvent):
        '''
        Sets the tokeniser attribute and updates the info attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the tokeniser widget.

        Returns
        -------
        None
        '''
        match e:
            case 0:
                self.posTag.check.setEnabled(False)
                self.posTag.check.setCheckState(Qt.CheckState.Unchecked)
                self.tokeniser = ''
                self.tokenLevelLA = []
                self.info.tokeniser = ''
                self.info.tokenLevelLA = []
            case 1:
                self.posTag.check.setEnabled(True)
                self.tokeniser = 'WORD_TOKENISER'
                self.info.tokeniser = self.tokeniser
            case 2:
                self.posTag.check.setEnabled(True)
                self.tokeniser = 'PUNC_TOKENISER'
                self.info.tokeniser = self.tokeniser
            case 3:
                self.posTag.check.setEnabled(True)
                self.tokeniser = 'TWEET_TOKENISER'
                self.info.tokeniser = self.tokeniser
        self.info.updateInfo()
        print(self.tokeniser)

    def posTagInput(self, e : QEvent):
        '''
        Alters the tokenLevelLA attribute and updates the info attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the posTag attribute.

        Returns
        -------
        None
        '''
        if e == 0 and 'POS_TAG' in self.tokenLevelLA:
            self.tokenLevelLA.remove('POS_TAG')
        elif 'POS_TAG' not in self.tokenLevelLA:
            self.tokenLevelLA.append('POS_TAG')
        self.info.tokenLevelLA = self.tokenLevelLA
        self.info.updateInfo()