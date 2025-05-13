'''
Creates a widget for selecting text level techniques in the vectorise tab.

Classes:

    Text

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

class Text(QWidget):
    '''
    A widget for selecting text level techniques in the vectorise tab.

    ...

    Attributes
    ----------
    info : Info
        A scroll area displaying the parameters of the program being built.
    textLevelLA : list
        A list of names of text level techniques to use.

    Methods
    -------
    keywordInput(QEvent)
        Alters the textLevelLA attribute and updates the info attribute.
    asciiInput(QEvent)
        Alters the textLevelLA attribute and updates the info attribute.
    '''
    def __init__(self, info : Info):
        '''
        Constructs attributes and sets the layout for a Text object.

        Parameters
        ----------
        info : Info
            A scroll area displaying the parameters of the program being built.
        '''
        super(Text, self).__init__()

        self.info = info

        displayLabel = QLabel()
        displayLabel.setText('Text Display')
        displayLayout = QVBoxLayout()
        displayLayout.addWidget(displayLabel)
        display = QWidget()
        display.setLayout(displayLayout)

        techLabel = QLabel()
        techLabel.setText('Text Level Techniques')

        keywords = vb.TechniqueCheck('Keyword Searching',
                                     '')
        keywords.check.stateChanged.connect(self.keywordInput)
        asciiConversion = vb.TechniqueCheck('ASCII Conversion',
                                            '')
        asciiConversion.check.stateChanged.connect(self.asciiInput)

        frame = b.InputFrame([techLabel,
                              keywords,
                              asciiConversion])

        layout = QHBoxLayout()
        layout.addWidget(display)
        layout.addWidget(frame)

        self.setLayout(layout)

        self.textLevelLA = []

    def keywordInput(self, e : QEvent):
        '''
        Alters the textLevelLA attribute and updates the info attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the keywords widget.

        Returns
        -------
        None
        '''
        if e == 0 and 'KEYWORDS' in self.textLevelLA:
            self.textLevelLA.remove('KEYWORDS')
        elif 'KEYWORDS' not in self.textLevelLA:
            self.textLevelLA.append('KEYWORDS')
        self.info.textLevelLA = self.textLevelLA
        self.info.updateInfo()

    def asciiInput(self, e : QEvent):
        '''
        Alters the textLevelLA attribute and updates the info attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the asciiConversion widget.

        Returns
        -------
        None
        '''
        if e == 0 and 'ASCII_CONVERSION' in self.textLevelLA:
            self.textLevelLA.remove('ASCII_CONVERSION')
        elif 'ASCII_CONVERSION' not in self.textLevelLA:
            self.textLevelLA.append('ASCII_CONVERSION')
        self.info.textLevelLA = self.textLevelLA
        self.info.updateInfo()