'''
Main module of the gui package. When run, this modules displays the NLP program 
builder GUI.

Classes:

    MainWindow

Functions:

    None

Misc Variables:

    app : QApplication
        The application which runs the GUI.
    window : MainWindow
        The main window of the GUI.

Exceptions:

    None
'''
import sys
from PyQt6.QtWidgets import (QApplication,
                            QMainWindow,
                            QTabWidget,
                            QHBoxLayout,
                            QWidget,
                            QLabel,
                            QVBoxLayout)

from .build import build as bu
from .build import info as inf
from . import data as da

class MainWindow(QMainWindow):
    '''
    A widget which displays the GUI for the NLP program builder.

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
        Construction attributes and adds tabs to a MainWindow object.

        Parameters
        ----------
        None
        '''
        super(MainWindow, self).__init__()

        self.setWindowTitle('NLP Program Builder')

        menu = self.menuBar()

        fileMenu = menu.addMenu("&File")
        helpMenu = menu.addMenu("&Help")

        info = inf.Info()
        build = bu.Build(info)
        
        buildLayout = QHBoxLayout()
        buildLayout.addWidget(info)
        buildLayout.addWidget(build)

        buildWidget = QWidget()
        buildWidget.setLayout(buildLayout)

        data = da.Data()

        tab = QTabWidget(self)
        tab.addTab(buildWidget, 'Build NLP Program')
        tab.addTab(data, 'Annotate Data')

        incompleteLabel = QLabel(
            'This GUI is not yet complete and will be finalised in a future rel'
            'ease.')
        font = incompleteLabel.font()
        font.setPointSize(15)
        incompleteLabel.setFont(font)

        incompleteLayout = QVBoxLayout()
        incompleteLayout.addWidget(incompleteLabel)
        incompleteLayout.addWidget(tab)

        incompleteWidget = QWidget()
        incompleteWidget.setLayout(incompleteLayout)

        self.setCentralWidget(incompleteWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()