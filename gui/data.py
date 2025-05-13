'''
Creates a tab in gui/gui.py for annotating data using an NLP program.

Classes:

    Data

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QWidget
                            )

class Data(QWidget):
    '''
    A widget to annotate data using an NLP program.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    None
    '''
    def __init__(self):
        '''
        Constructs attributes for a Data object.

        Parameters
        ----------
        None
        '''
        super(Data, self).__init__()