'''
Creates a widget for displaying the parameters of the program being built.

Classes:

    Info

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
from PyQt6.QtWidgets import (QWidget,
                            QLabel,
                            QVBoxLayout,
                            QScrollArea
                            )

class Info(QScrollArea):
    '''
    A widget for displaying the parameters of the program being built.

    ...

    Attributes
    ----------
    fileLocations : list
        A list of file locations where data is stored.
    fileType : str
        The type of file in which the data is stored.
    dateColumnLabel : str
        The title of the column containing the date data.
    hospitalColumnLabel : str
        The title of the column containing the hospital data.
    sexColumnLabel : str
        The title of the column containing the sex data.
    ageColumnLabel : str
        The title of the column containing the age data.
    textFieldColumnLabels : list
        The titles of the columns containing the free text data.
    flagColumnLabel : str
        The title of the column containing the data annotations.
    minAge : int
        The minimum age of patients to include.
    maxAge : int
        The maximum age of patients to include.
    hospital : str
        The hospitals to include data from.
    sex : str
        The sex(es) of patients to include.
    minYear : int
        The minimum year to include data from.
    maxYear : int
        The maximum year to include data before.
    trainTestRatio : str
        The ratio of training to testing records to use.
    numberOfRecords : int
        The number of records to use for training and testing data.
    trainDist : str
        The distribution to use when extracting training records.
    testDist : str
        The distribution to use when extracting testing records.
    trainPosPercent : float
        The percentage of positively flagged training records to extract.
    testPosPercent : float
        The percentage of positively flagged testing records to extract.
    tokeniser : str
        The name of the tokeniser to use.
    preLAChanges : list
        A list of names of pre LA techniques to use.
    tokenLevelLA : list
        A list of names of token level techniques to use.
    textLevelLA : list
        A list of names of text level techniques to use.
    corpusLevelLA : str
        The name of the corpus level technique to use.
    mlAlgType : str
        The type of machine learning algorithm to use.
    impurity : str
        The impurity measure to use for a decision tree algorithm.
    kernel : str
        The kernel to use for an SVM algorithm.
    gamma : Union[float, str]
        The gamma parameter to use for an SVM kernel.
    r : float
        The r parameter to use for an SVM kernel.
    degree : float
        The degree parameters to use for an SVM kernel.
    precision : float
        The precision of an NLP program.
    recall : float
        The recall of an NLP program.
    totalTime : float
        The total time taken to build an NLP program.
    totalSpace : float
        The peak memory used to build an NLP program.
    fileLocationsDisp : QLabel
        A widget to display the fileLocations attribtute.
    fileTypeDisp : QLabel
        A widget to display the fileType attribute.
    textFieldColumnLabelsDsip : QLabel
        A widget to display the textFieldColumnLabel attribute.
    flagColumnLabelDisp : QLabel
        A widget to display the flagColumnLabel attribute.
    dateColumnLabelDisp : QLabel
        A widget to display the dateColumnLabel attribute.
    hospitalColumnLabelDisp : QLabel
        A widget to display the hospitalColumnLabel attribute.
    sexColumnLabelDisp : QLabel
        A widget to display the sexColumnLabel attribute.
    ageColumnLabelDisp : QLabel
        A widget to display the ageColumnLabel attribute.
    minAgeDisp : QLabel
        A widget to display the minAge attribute.
    maxAgeDisp : QLabel
        A widget to display the maxAge attribute.
    hospitalDisp : QLabel
        A widget to display the hospital attribute.
    sexDisp : QLabel
        A widget to display the sex attribute.
    minYearDisp : QLabel
        A widget to display the minYear attribute.
    maxYearDisp : QLabel
        A widget to display the maxYear attribute.
    trainTestRatioDisp : QLabel
        A widget to display the trainTestRatio attribute.
    numberOfRecordsDisp : QLabel
        A widget to display the numberOfRecords attribute.
    trainDistDisp : QLabel
        A widget to display the trainDist attribute.
    testDistDisp : QLabel
        A widget to display the testDist attribute.
    trainPosPercentDisp : QLabel
        A widget to display the trainPosPercent attribute.
    testPosPercentDisp : QLabel
        A widget to display the testPosPercent attribute.
    preLAChangesDisp : QLabel
        A widget to display the preLAChanges attribute.
    tokeniserDisp : QLabel
        A widget to display the tokeniser attribute.
    tokenLevelLADisp : QLabel
        A widget to display the tokenLevelLA attribute.
    textLevelLADisp : QLabel
        A widget to display the textLevelLA attribute.
    corpusLevelLADisp : QLabel
        A widget to display the corpusLevelLA attribute.
    mlAlgTypeDisp : QLabel
        A widget to display the mlAlgType attribute.
    impurityDisp : QLabel
        A widget to display the impurity attribute.
    kenrelDisp : QLabel
        A widget to display the kernel attribute.
    gammaDisp : QLabel
        A widget to display the gamma attribute.
    rDisp : QLabel
        A widget to display the r attribute.
    degreeDisp : QLabel
        A widget to display the degree attribute.
    precisionDisp : QLabel
        A widget to display the precision attribute.
    recallDisp : QLabel
        A widget to display the recall attribute.
    totalTimeDisp : QLabel
        A widget to display the totalTime attribute.
    totalSpaceDisp : QLabel
        A widget to display the totalSpace attribute.

    Methods
    -------
    updateInfo()
        Updates all display attributes based on the values of data attributes.
    '''
    def __init__(self):
        '''
        Constructs attributes and sets the layout of an Info object.

        Parameters
        ----------
        None
        '''
        super(Info, self).__init__()

        self.fileLocations = []
        self.fileType = ''
        self.dateColumnLabel = ''
        self.hospitalColumnLabel = ''
        self.sexColumnLabel = ''
        self.ageColumnLabel = ''
        self.textFieldColumnLabels = []
        self.flagColumnLabel = ''

        self.minAge = 0
        self.maxAge = 150
        self.hospital = 'ALL'
        self.sex = 'ALL'
        self.minYear = 2015
        self.maxYear = 2022

        self.trainTestRation = '60:40'
        self.numberOfRecords = 0
        self.trainDist = 'UNIFORM'
        self.testDist = 'UNIFORM'
        self.trainPosPercent = -1
        self.testPosPercent = -1

        self.tokeniser = ''
        self.preLAChanges = []
        self.tokenLevelLA = []
        self.textLevelLA = []
        self.corpusLevelLA = ''

        self.mlAlgType = 'DECISIONTREE'
        self.impurity = 'GINI'
        self.kernel = None
        self.gamma = 0
        self.r = 0
        self.degree = 0

        self.precision = None
        self.recall = None
        self.totalTime = None
        self.totalSpace = None

        importInfo = QLabel()
        importInfo.setText('Import')
        font = importInfo.font()
        font.setPointSize(15)
        importInfo.setFont(font)
        self.fileLocationsDisp = QLabel(
            f'File Locations:\n{self.fileLocations}')
        self.fileTypeDisp = QLabel(
            f'File Type:\n{self.fileType}')
        self.textFieldColumnLabelsDisp = QLabel(
            f'Text Field Column Label(s):\n'
            f'{self.textFieldColumnLabels}')
        self.flagColumnLabelDisp = QLabel(
            f'Flag Column Label:\n{self.flagColumnLabel}')
        self.dateColumnLabelDisp = QLabel(
            f'Date Column Label:\n{self.dateColumnLabel}')
        self.hospitalColumnLabelDisp = QLabel(
            f'Hospital Column Label:\n{self.hospitalColumnLabel}')
        self.sexColumnLabelDisp = QLabel(
            f'Sex Column Label:\n{self.sexColumnLabel}')
        self.ageColumnLabelDisp = QLabel(
            f'Age Column Label:\n{self.ageColumnLabel}')
        
        filterInfo = QLabel()
        filterInfo.setText('Filter')
        font = filterInfo.font()
        font.setPointSize(15)
        filterInfo.setFont(font)
        self.minAgeDisp = QLabel(f'Minimum Age:\n{self.minAge}')
        self.maxAgeDisp = QLabel(f'Maximum Age:\n{self.maxAge}')
        self.hospitalDisp = QLabel(f'Hospital(s):\n{self.hospital}')
        self.sexDisp = QLabel(f'Sex(es):\n{self.sex}')
        self.minYearDisp = QLabel(f'Earliest Year:\n{self.minYear}')
        self.maxYearDisp = QLabel(f'Latest Year:\n{self.maxYear}')
        
        extractInfo = QLabel()
        extractInfo.setText('Extract')
        font = extractInfo.font()
        font.setPointSize(15)
        extractInfo.setFont(font)
        self.trainTestRationDisp = QLabel(
            f'Train:Test Ratio:\n{self.trainTestRation}')
        self.numberOfRecordsDisp = QLabel(
            f'Number of Record:\n{self.numberOfRecords}')
        self.trainDistDisp = QLabel(
            f'Training Data Distribution:\n{self.trainDist}')
        self.testDistDisp = QLabel(
            f'Testing Data Distribution:\n{self.testDist}')
        self.trainPosPercentDisp = QLabel(
            f'Percentage of Positive Training Records:\n'
            f'{self.trainPosPercent}')
        self.testPosPercentDisp = QLabel(
            f'Percentage of Positive Testing Records:\n'
            f'{self.testPosPercent}')
        
        vectoriseInfo = QLabel()
        vectoriseInfo.setText('Vectorise')
        font = vectoriseInfo.font()
        font.setPointSize(15)
        vectoriseInfo.setFont(font)
        self.preLAChangesDisp = QLabel(
            f'Pre Linguistic Analysis Changes:\n'
            f'{self.preLAChanges}')
        self.tokeniserDisp = QLabel(f'Tokeniser:\n{self.tokeniser}')
        self.tokenLevelLADisp = QLabel(
            f'Token Level Techniques:\n{self.tokenLevelLA}')
        self.textLevelLADisp = QLabel(
            f'Text Level Techniques:\n{self.textLevelLA}')
        self.corpusLevelLADisp = QLabel(
            f'Corpus Level Techniques:\n{self.corpusLevelLA}')
        
        mlearnInfo = QLabel()
        mlearnInfo.setText('Machine Learning')
        font = mlearnInfo.font()
        font.setPointSize(15)
        mlearnInfo.setFont(font)
        self.mlAlgTypeDisp = QLabel(
            f'Machine Learning Algorithm Type:\n{self.mlAlgType}')
        self.impurityDisp = QLabel(f'Impurity Criterion:\n{self.impurity}')
        self.kernelDisp = QLabel(f'Kernel:\n{self.kernel}')
        self.gammaDisp = QLabel(f'Gamma Parameter:\n{self.gamma}')
        self.rDisp = QLabel(f'r Parameter:\n{self.r}')
        self.degreeDisp = QLabel(f'Degree Parameter:\n{self.degree}')
        
        evaluateInfo = QLabel()
        evaluateInfo.setText('Evaluate')
        font = evaluateInfo.font()
        font.setPointSize(15)
        evaluateInfo.setFont(font)
        self.precisionDisp = QLabel(f'Precision:\n{self.precision}')
        self.recallDisp = QLabel(f'Recall:\n{self.recall}')
        self.totalTimeDisp = QLabel(f'Total Time Taken:\n{self.totalTime}')
        self.peakMemoryDisp = QLabel(f'Peak Memory Used:\n{self.totalSpace}')

        layout = QVBoxLayout()
        layout.addWidget(importInfo)
        layout.addWidget(self.fileLocationsDisp)
        layout.addWidget(self.fileTypeDisp)
        layout.addWidget(self.textFieldColumnLabelsDisp)
        layout.addWidget(self.flagColumnLabelDisp)
        layout.addWidget(self.dateColumnLabelDisp)
        layout.addWidget(self.hospitalColumnLabelDisp)
        layout.addWidget(self.sexColumnLabelDisp)
        layout.addWidget(self.ageColumnLabelDisp)
        layout.addWidget(filterInfo)
        layout.addWidget(self.minAgeDisp)
        layout.addWidget(self.maxAgeDisp)
        layout.addWidget(self.hospitalDisp)
        layout.addWidget(self.sexDisp)
        layout.addWidget(self.minYearDisp)
        layout.addWidget(self.maxYearDisp)
        layout.addWidget(extractInfo)
        layout.addWidget(self.trainTestRationDisp)
        layout.addWidget(self.numberOfRecordsDisp)
        layout.addWidget(self.trainDistDisp)
        layout.addWidget(self.testDistDisp)
        layout.addWidget(self.trainPosPercentDisp)
        layout.addWidget(self.testPosPercentDisp)
        layout.addWidget(vectoriseInfo)
        layout.addWidget(self.preLAChangesDisp)
        layout.addWidget(self.tokeniserDisp)
        layout.addWidget(self.tokenLevelLADisp)
        layout.addWidget(self.textLevelLADisp)
        layout.addWidget(self.corpusLevelLADisp)
        layout.addWidget(mlearnInfo)
        layout.addWidget(self.mlAlgTypeDisp)
        layout.addWidget(self.impurityDisp)
        layout.addWidget(self.kernelDisp)
        layout.addWidget(self.gammaDisp)
        layout.addWidget(self.rDisp)
        layout.addWidget(self.degreeDisp)
        layout.addWidget(evaluateInfo)
        layout.addWidget(self.precisionDisp)
        layout.addWidget(self.recallDisp)
        layout.addWidget(self.totalTimeDisp)
        layout.addWidget(self.peakMemoryDisp)

        info = QWidget()
        info.setLayout(layout)

        self.setWidget(info)

    def updateInfo(self):
        '''
        Updates all display attributes based on the values of data attributes.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        self.fileLocationsDisp.setText(
            f'File Locations:\n{self.fileLocations}')
        self.fileTypeDisp.setText(
            f'File Type:\n{self.fileType}')
        self.dateColumnLabelDisp.setText(
            f'Date Column Label:\n{self.dateColumnLabel}')
        self.hospitalColumnLabelDisp.setText(
            f'Hospital Column Label:\n{self.hospitalColumnLabel}')
        self.sexColumnLabelDisp.setText(
            f'Sex Column Label:\n{self.sexColumnLabel}')
        self.ageColumnLabelDisp.setText(
            f'Age Column Label:\n{self.ageColumnLabel}')
        self.textFieldColumnLabelsDisp.setText(
            f'Text Field Column Label(s):\n'
            f'{self.textFieldColumnLabels}')
        self.flagColumnLabelDisp.setText(
            f'Flag Column Label:\n{self.flagColumnLabel}')
        self.minAgeDisp.setText(f'Minimum Age:\n{self.minAge}')
        self.maxAgeDisp.setText(f'Maximum Age:\n{self.maxAge}')
        self.hospitalDisp.setText(f'Hospital(s):\n{self.hospital}')
        self.sexDisp.setText(f'Sex(es):\n{self.sex}')
        self.minYearDisp.setText(f'Earliest Year:\n{self.minYear}')
        self.maxYearDisp.setText(f'Latest Year:\n{self.maxYear}')
        self.trainTestRationDisp.setText(
            f'Train:Test Ratio:\n{self.trainTestRation}')
        self.numberOfRecordsDisp.setText(
            f'Number of Record:\n{self.numberOfRecords}')
        self.trainDistDisp.setText(
            f'Training Data Distribution:\n{self.trainDist}')
        self.testDistDisp.setText(
            f'Testing Data Distribution:\n{self.testDist}')
        self.trainPosPercentDisp.setText(
            f'Percentage of Positive Training Records:\n'
            f'{self.trainPosPercent}')
        self.testPosPercentDisp.setText(
            f'Percentage of Positive Testing Records:\n'
            f'{self.testPosPercent}')
        self.preLAChangesDisp.setText(
            f'Pre Linguistic Analysis Changes:\n'
            f'{self.preLAChanges}')
        self.tokeniserDisp.setText(f'Tokeniser:\n{self.tokeniser}')
        self.tokenLevelLADisp.setText(
            f'Token Level Techniques:\n{self.tokenLevelLA}')
        self.textLevelLADisp.setText(
            f'Text Level Techniques:\n{self.textLevelLA}')
        self.corpusLevelLADisp.setText(
            f'Corpus Level Techniques:\n{self.corpusLevelLA}')
        self.mlAlgTypeDisp.setText(
            f'Machine Learning Algorithm Type:\n{self.mlAlgType}')
        self.impurityDisp.setText(f'Impurity Criterion:\n{self.impurity}')
        self.kernelDisp.setText(f'Kernel:\n{self.kernel}')
        self.gammaDisp.setText(f'Gamma Parameter:\n{self.gamma}')
        self.rDisp.setText(f'r Parameter:\n{self.r}')
        self.degreeDisp.setText(f'Degree Parameter:\n{self.degree}')
        self.precisionDisp.setText(f'Precision:\n{self.precision}%')
        self.recallDisp.setText(f'Recall:\n{self.recall}%')
        self.totalTimeDisp.setText(f'Total Time Taken:\n{self.totalTime} (s)')
        self.peakMemoryDisp.setText(
            f'Peak Memory Used:\n{self.totalSpace} (MB)')