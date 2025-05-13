'''
Helper functions and classes to support gui/build/vectorise.

Classes:

    TechniqueCheck
    CustomDialog

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QLabel,
                            QWidget,
                            QHBoxLayout,
                            QCheckBox,
                            QPushButton,
                            QDialog,
                            QVBoxLayout
                            )
from PyQt6.QtCore import QSize

class TechniqueCheck(QWidget):
    '''
    A widget for selecting a general linguistic analysis technique.

    ...

    Attributes
    ----------
    check : QCheckBox
        A widget to select whether or not to use the technique.
    message : str
        The text displayed in a help pop-up window linked to the technique.

    Methods
    -------
    helpPopUp()
        Displays a pop-up window with a help message.
    '''
    def __init__(self, technique : str, message : str):
        '''
        Constructs attributes and sets the layout for a TechniqueCheck object.

        Parameters
        ----------
        technique : str
            The name of the technique.
        message : str
            The text displayed in a help pop-up window linked to the technique.
        '''
        super(TechniqueCheck, self).__init__()

        tech = QLabel()
        tech.setText(technique)

        self.check = QCheckBox()

        self.message = message

        help = QPushButton('?')
        help.setFixedSize(QSize(20,20))
        help.pressed.connect(self.helpPopUp)

        layout = QHBoxLayout()
        layout.addWidget(self.check)
        layout.addWidget(tech)
        layout.addWidget(help)

        self.setLayout(layout)

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
        dlg = CustomDialog(self.message)
        dlg.exec()

class CustomDialog(QDialog):
    '''
    A pop-up window to display a help message.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    None
    '''
    def __init__(self, message : str):
        '''
        Creates a label for the pop-up window and sets the layout.

        Parameters
        ----------
        message : str
            The text to be displayed in the pop-up window.
        '''
        super().__init__()

        self.setWindowTitle('Help')

        help = QLabel(message)

        layout = QVBoxLayout()
        layout.addWidget(help)
        self.setLayout(layout)