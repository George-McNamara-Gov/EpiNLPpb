'''
Helper functions and classes to support gui/build.

Classes:

    InputFrame
    DemographicCheck
    CustomDialog

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QVBoxLayout, 
                             QFrame, 
                             QLabel, 
                             QDialog,
                             QHBoxLayout,
                             QWidget,
                             QCheckBox,
                             QComboBox,
                             QPushButton
                            )
from PyQt6.QtCore import (QSize,
                          QEvent)

class InputFrame(QFrame):
    '''
    A frame to hold a series of related widgets to organised the interface.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    None
    '''
    def __init__(self, widgets : list):
        '''
        Creates and sets the layout for the frame.

        Parameters
        ----------
        widgets : list
            A list of widgets to be held in the frame.
        '''
        super(InputFrame, self).__init__()

        frameLayout = QVBoxLayout()
        for widget in widgets:
            frameLayout.addWidget(widget)

        self.setLayout(frameLayout)
        self.setFrameShape(QFrame.Shape.StyledPanel)

class DemographicCheck(QWidget):
    '''
    A widget for selecting a data column containing particular demographic data.

    ...

    Attributes
    ----------
    frame : InputFrame
        The frame containing the corresponding widgets in the filter tab.
    filter : Filter
        The filter tab widget.
    message : str
        The text displayed in a help pop-up window linked to the demographic.
    check : QCheckBox
        A widget for selecting whether to filter by the demographic.
    columns : QComboBox
        A widget for selecting which data column contains the data.

    Methods
    -------
    helpPopUp()
        Displays a pop-up window with a help message.
    addColumns(list)
        Add column names to the columns attribute.
    emptyColumns()
        Removes all column names from the columns attribute.
    chooseColumn(QEvent)
        Activates or deactivates the columns attribute based on the state of the
        check attribute.
    activateDemo(QEvent)
        Activates or deactivates the frame attribute in the filter widget.
    value() -> str
        Returns the currently selected column name.
    '''
    def __init__(self, 
                 demographic : str, 
                 frame : InputFrame, 
                 filter : QWidget,
                 message : str):
        '''
        Constructs attributes and sets the layout for a DemographicCheck object.

        Parameters
        ----------
        demographic : str
            The name of the demographic.
        frame : InputFrame
            The frame containing the corresponding widgets in the filter tab.
        filter : Filter
            The filter tab widget.
        message : str
            The text displayed in a help pop-up window linked to the demographic.
        '''
        super(DemographicCheck, self).__init__()

        self.frame = frame
        self.filter = filter

        self.message = message

        demo = QLabel()
        demo.setText(demographic)

        self.check = QCheckBox()
        self.check.stateChanged.connect(self.chooseColumn)

        self.columns = QComboBox()
        self.columns.addItem('None')
        self.columns.setEnabled(False)

        help = QPushButton('?')
        help.setFixedSize(QSize(20,20))
        help.pressed.connect(self.helpPopUp)

        errorLabel = QLabel()

        layout = QHBoxLayout()
        layout.addWidget(demo)
        layout.addWidget(self.check)
        layout.addWidget(self.columns)
        layout.addWidget(help)
        layout.addWidget(errorLabel)

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

    def addColumns(self, newColumns : list):
        '''
        Adds column names to the columns attribute.

        Parameters
        ----------
        newColumns : list
            The column names to be added.

        Returns
        -------
        None
        '''
        self.columns.addItems(newColumns)

    def emptyColumns(self):
        '''
        Removes all column names from the columns attribute.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.columns.clear()
        self.columns.addItem('None')
        if self.check.isChecked():
            self.columns.setEnabled(True)
        else:
            self.columns.setEnabled(False)

    def chooseColumn(self, e : QEvent):
        '''
        Activates or deactivates the columns attribute based on the state of the
        check attribute.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the check attribute.

        Returns
        -------
        None
        '''
        if e == 2:
            self.columns.setEnabled(True)
        else:
            self.columns.setCurrentIndex(0)
            self.columns.setEnabled(False)

    def activateDemo(self, e : QEvent):
        '''
        Activates or deactivates the frame attribute in the filter widget.

        Parameters
        ----------
        e : QEvent
            The event passed by changing the state of the DemographicCheck
            attribute in gui/build/importer.py.
        
        Returns
        -------
        None
        '''
        if e == 0:
            self.frame.setEnabled(False)
            match self.frame:
                case self.filter.aFrame:
                    self.filter.aFrameDefault()
                case self.filter.hFrame:
                    self.filter.hFrameDefault()
                case self.filter.sFrame:
                    self.filter.sFrameDefault()
                case _:
                    self.filter.dFrameDefault()
        else:
            self.frame.setEnabled(True)

    def value(self) -> str:
        '''
        Returns the currently selected column name.

        Parameters
        ----------
        None

        Returns
        -------
        name: str
            The currently selected column name.
        '''
        if self.columns.isEnabled() and self.columns.currentText() != 'None':
            name = self.columns.currentText()
            return name
        else:
            name = ''
            return name

class CustomDialog(QDialog):
    '''
    A pop-up window to display a help message

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