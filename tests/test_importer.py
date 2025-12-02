'''
Test module for the package/importer package.

Classes:

    TestImporter

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
import unittest

from ..package.Importer import importer as i
from ..package.Importer import base as b
from ..package import exceptions as e

class TestImporter(unittest.TestCase):
    '''
    A class of tests to check the operation of the package/Importer package.

    Attributes
    ----------
    None

    Methods
    -------
    test_noError_csv()
        Tests that data can be imported without error from a csv file.
    test_noError_noBounds_csv()
        Test that data can be imported without error from a csv file when
        no bounds are provided.
    test_noError_noLabels_csv()
        Test that data can be imported without error from a csv file when
        no column labels are provided.
    test_noError_noBounds_noLables_csv()
        Test that data can be imported without error from a csv file when
        no bounds or column labels are provided.
    test_noError_custom_csv()
        Test that data can be imported without error from a csv file when
        custom bounds and column labels are provided.
    test_noError_custom_noBounds_csv()
        Test that data can be imported without error from a csv file when
        custom labels but no custom bounds are provided.
    test_noError_custom_noLabels_csv()
        Test that data can be imported without error from a csv file when
        custom bounds but no custom labels are provided.
    test_noError_xlsx()
        Test that data can be imported without error from a xlsx file.
    test_noError_noBounds_xlsx()
        Test that data can be imported without error from a xlsx file when
        no bounds are provided.
    test_noError_noLables_xlsx()
        Test that data can be imported without error from a xlsx file when
        no column labels are provided.
    test_noError_noBounds_noLables_xlsx()
        Test that data can be imported without error from a xlsx file when
        no bounds or column labels are provided.
    test_noError_custom_xlsx()
        Test that data can be imported without error from a xlsx file when
        custom bounds and column labels are provided.
    test_noError_custom_noBounds_xlsx()
        Test that data can be imported without error from a xlsx file when
        custom labels but no custom bounds are provided.
    test_noError_custom_noLabels_xlsx()
        Test that data can be imported without error from a xlsx file when
        custom bounds but no custom labels are provided.
    test_fileTypeError()
        Tests that invalid file type inputs cause exceptions.
    test_trainDistError()
        Tests that invalid trainDist inputs cause exceptions. 
    test_testDistError()
        Tests that invalid testDist inputs cause exceptions. 
    test_ageError()
        Tests that invalid ageBounds inputs cause exceptions.
    test_hospitalError()
        Tests that invalid hospital inputs cause exceptions.
    test_sexError()
        Tests that invalid sex inputs cause exceptions.
    test_yearError()
        Tests that invalid yearBounds inputs cause exceptions.
    test_dataExtractorSizeError()
        Tests that invalid trainSize and testSize inputs cause exceptions.
    test_dataSizes()
        Tests that all exctractors extract the correct amount of data.
    test_Demographic()
        Tests that the imported data satisfies the given demographic and the 
        data contains the correct amount of data fields.
    test_invalidColumnLabel()
        Tests that invalid column labels cause exceptions.
    '''
    
    def test_noError_csv(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (0,150),
                            hospital= 'ALL',
                            sex= 0,
                            yearBounds= (2015,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()
        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (0,150),
                            hospital= 'ALL',
                            sex= 0,
                            yearBounds= (2015,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (20,90),
                            hospital= 'ALL',
                            sex= 0,
                            yearBounds= (2015,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (0,150),
                            hospital= 'ALL',
                            sex= 0,
                            yearBounds= (2021,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (0,150),
                            hospital= 'CHHS',
                            sex= 0,
                            yearBounds= (2015,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (0,150),
                            hospital= 'ALL',
                            sex= 1,
                            yearBounds= (2015,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (20,90),
                            hospital= 'CHHS',
                            sex= 1,
                            yearBounds= (2021,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()
        
        arg_dict = {
            'fileLocations' : ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
            'dateColumnLabel' : 'EDPresentationDTTM',
            'hospitalColumnLabel' : 'hospid',
            'sexColumnLabel' : 'Sex',
            'ageColumnLabel' : 'AgeAtPresentation',
            'textFieldColumnLabels' : ['TriageObject','TriageDescription'],
            'flagColumnLabel' : 'SSH_Flag',
            'ageBounds' : (0,150),
            'hospital' : 'ALL',
            'sex' : 0,
            'yearBounds' : (2015,2022),
            'trainSize' : 10,
            'trainDist' : 'NEWESTBLOCK',
            'testSize' : 10, 
            'testDist' : 'UNIFORM'
        }
        importer = i.Importer(arg_dict= arg_dict)
        importer.importData()

    def test_noError_noBounds_csv(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()
        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

    def test_noError_noLabels_csv(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (0,150),
                            hospital= 'ALL',
                            sex= 0,
                            yearBounds= (2015,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()
        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (0,150),
                            hospital= 'ALL',
                            sex= 0,
                            yearBounds= (2015,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

    def test_noError_noBounds_noLables_csv(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()
        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()

    def test_noError_custom_csv(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            customColumnLabels= ['AgeAtPresentation'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription', 'Sex', 'hospid'],
                            customBounds= [(20, 90), 1, 'CHHS'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        
        importer.importData()
        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            customColumnLabels= ['AgeAtPresentation', 'Sex', 'hospid'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            customBounds= [(20, 90), 1, 'CHHS'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()

    def test_noError_custom_noBounds_csv(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            customColumnLabels= ['AgeAtPresentation', 'Sex', 'hospid'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()
        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            customColumnLabels= ['AgeAtPresentation', 'Sex', 'hospid'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()

    def test_noError_custom_noLabels_csv(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            customBounds= [(2016, 2019), (20, 90), 1, 'CHHS'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()
        importer = i.Importer(trainFile= 'EpiNLPpb_dev/data/KEYWORD1.csv', 
                            testFile= 'EpiNLPpb_dev/data/KEYWORD2.csv',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            customBounds= [(2016, 2019), (20, 90), 1, 'CHHS'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()

    def test_noError_xlsx(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUALXLSXTEST.xlsx'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (0,150),
                            hospital= 'ALL',
                            sex= 0,
                            yearBounds= (2015,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

    def test_noError_noBounds_xlsx(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUALXLSXTEST.xlsx'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

    def test_noError_noLables_xlsx(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUALXLSXTEST.xlsx'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (0,150),
                            hospital= 'ALL',
                            sex= 0,
                            yearBounds= (2015,2022),
                            trainSize= 10,
                            trainDist= 'NEWESTBLOCK',
                            testSize=10, 
                            testDist= 'UNIFORM')
        importer.importData()

    def test_noError_noBounds_noLables_xlsx(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUALXLSXTEST.xlsx'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()

    def test_noError_custom_xlsx(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUALXLSXTEST.xlsx'],
                            customColumnLabels= ['AgeAtPresentation', 'Sex', 'hospid'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            customBounds= [(20, 90), 1, 'CHHS'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()

        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUALXLSXTEST.xlsx'],
                            customColumnLabels= ['AgeAtPresentation'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription', 'Sex', 'hospid'],
                            customBounds= [(20, 90), 1, 'CHHS'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()

    def test_noError_custom_noBounds_xlsx(self):      
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUALXLSXTEST.xlsx'],
                            customColumnLabels= ['AgeAtPresentation', 'Sex', 'hospid'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()

    def test_noError_custom_noLabels_xlsx(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUALXLSXTEST.xlsx'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            customBounds= [(20, 90), 1, 'CHHS'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize=10)
        importer.importData()

    def test_fileTypeError(self):
        with self.assertRaises(e.UnsupportedFileTypeException):
            importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize= 10)
            importer.importData()
        with self.assertRaises(e.UnsupportedFileTypeException):
            importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.py'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10,
                            testSize= 10)
            importer.importData()

    def test_trainDistError(self):
        with self.assertRaises(e.TrainDistException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        trainSize= 10,
                        trainDist= 'not a distriubtion', 
                        testSize= 10)

    def test_testDistError(self):
        with self.assertRaises(e.TestDistException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        trainSize= 10,
                        testSize= 10, 
                        testDist= 'not a distribution')

    def test_ageError(self):
        with self.assertRaises(e.BoundsException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        ageColumnLabel= 'AgeAtPresentation',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        ageBounds= (-1,150),
                        trainSize= 10,
                        testSize= 10)
        with self.assertRaises(e.BoundsException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        ageColumnLabel= 'AgeAtPresentation',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        ageBounds= (-2,-1),
                        trainSize= 10,
                        testSize= 10)
        with self.assertRaises(e.BoundsException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        ageColumnLabel= 'AgeAtPresentation',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag', 
                        ageBounds= (10,9),
                        trainSize= 10,
                        testSize= 10)
        with self.assertRaises(e.BoundsException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        ageColumnLabel= 'AgeAtPresentation',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag', 
                        ageBounds= (0,-1),
                        trainSize= 10,
                        testSize= 10)
    
    def test_hospitalError(self):
        with self.assertRaises(e.BoundsException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        hospitalColumnLabel= 'hospid',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        hospital= 'not a hospital',
                        trainSize= 10, 
                        testSize= 10)

    def test_sexError(self):
        with self.assertRaises(e.BoundsException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        sexColumnLabel= 'Sex',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        sex= 'not a sex',
                        trainSize= 10,
                        testSize= 10)

    def test_yearError(self):    
        with self.assertRaises(e.BoundsException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        dateColumnLabel= 'EDPresentationDTTM',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        yearBounds= (1899, 2022),
                        trainSize=10, testSize= 10)
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        dateColumnLabel= 'EDPresentationDTTM',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        yearBounds= (2015, 2101),
                        trainSize=10, testSize= 10)

        with self.assertRaises(e.BoundsException):
            _ = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                        dateColumnLabel= 'EDPresentationDTTM',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        yearBounds= (2017, 2016),
                        trainSize=10, testSize= 10)

    def test_dataExtractorSizeError(self):
        importerTrain = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10000000, 
                            testSize= 10)
        importerTest= i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 10, 
                            testSize=10000000)
        with self.assertRaises(e.MoreDataThanRecordsException):
            importerTrain.importData()
        with self.assertRaises(e.MoreDataThanRecordsException):
            importerTest.importData()

    def test_dataSizes(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 20,
                            trainDist= 'NEWESTBLOCK', 
                            testSize= 10,
                            testDist= 'NEWESTBLOCK')
        data = importer.importData()
        train = data[0]
        test = data[1]
        self.assertEqual(len(train),20)
        self.assertEqual(len(test),10)

        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 20,
                            trainDist= 'RANDOMBLOCK', 
                            testSize= 10,
                            testDist= 'RANDOMBLOCK')
        data = importer.importData()
        train = data[0]
        test = data[1]
        self.assertEqual(len(train),20)
        self.assertEqual(len(test),10)

        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            trainSize= 20,
                            trainDist= 'UNIFORM', 
                            testSize= 10,
                            testDist= 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        self.assertEqual(len(train),20)
        self.assertEqual(len(test),10)
    
    def test_Demographic(self):
        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (18,21),
                            hospital= 'CHHS',
                            sex= 1,
                            yearBounds= (2017,2020),
                            trainSize= 20,
                            trainDist= 'NEWESTBLOCK', 
                            testSize= 10, 
                            testDist= 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        for _, record in train.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual('CHHS', record['hospid'])
            self.assertEqual(1, record['Sex'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        for _, record in test.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual('CHHS', record['hospid'])
            self.assertEqual(1, record['Sex'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (18,21),
                            hospital= 'ALL',
                            sex= 1,
                            yearBounds= (2017,2020),
                            trainSize= 20,
                            trainDist= 'NEWESTBLOCK', 
                            testSize= 10, 
                            testDist= 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        for _, record in train.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual(1, record['Sex'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        for _, record in test.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual(1, record['Sex'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (18,21),
                            hospital= 'CHHS',
                            sex= 0,
                            yearBounds= (2017,2020),
                            trainSize= 20,
                            trainDist= 'NEWESTBLOCK', 
                            testSize= 10, 
                            testDist= 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        for _, record in train.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual('CHHS', record['hospid'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        for _, record in test.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual('CHHS', record['hospid'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (18,21),
                            hospital= 'CHHS',
                            sex= 1,
                            yearBounds= (2017,2020),
                            trainSize= 20,
                            trainDist= 'NEWESTBLOCK', 
                            testSize= 10, 
                            testDist= 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        for _, record in train.iterrows():
            self.assertEqual('CHHS', record['hospid'])
            self.assertEqual(1, record['Sex'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        for _, record in test.iterrows():
            self.assertEqual('CHHS', record['hospid'])
            self.assertEqual(1, record['Sex'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            sexColumnLabel= 'Sex',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (18,21),
                            hospital= 'CHHS',
                            sex= 1,
                            yearBounds= (2017,2020),
                            trainSize= 20,
                            trainDist= 'NEWESTBLOCK', 
                            testSize= 10, 
                            testDist= 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        for _, record in train.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual(1, record['Sex'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        for _, record in test.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual(1, record['Sex'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            ageColumnLabel= 'AgeAtPresentation',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (18,21),
                            hospital= 'CHHS',
                            sex= 1,
                            yearBounds= (2017,2020),
                            trainSize= 20,
                            trainDist= 'NEWESTBLOCK', 
                            testSize= 10, 
                            testDist= 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        for _, record in train.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual('CHHS', record['hospid'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        for _, record in test.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual('CHHS', record['hospid'])
            self.assertTrue(18 <= record['AgeAtPresentation'] <= 21)

        importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                            dateColumnLabel= 'EDPresentationDTTM',
                            hospitalColumnLabel= 'hospid',
                            sexColumnLabel= 'Sex',
                            textFieldColumnLabels= ['TriageObject','TriageDescription'],
                            flagColumnLabel= 'SSH_Flag',
                            ageBounds= (18,21),
                            hospital= 'CHHS',
                            sex= 1,
                            yearBounds= (2017,2020),
                            trainSize= 20,
                            trainDist= 'NEWESTBLOCK', 
                            testSize= 10, 
                            testDist= 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        for _, record in train.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual('CHHS', record['hospid'])
            self.assertEqual(1, record['Sex'])

        for _, record in test.iterrows():
            self.assertTrue(2017 <= b.getYear(record['EDPresentationDTTM']) <= 2020)
            self.assertEqual('CHHS', record['hospid'])
            self.assertEqual(1, record['Sex'])

    def test_invalidColumnLabel(self):
        with self.assertRaises(e.ColumnLabelException):
            importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUAL.csv'],
                        dateColumnLabel= 'invalid',
                        hospitalColumnLabel= 'hospid',
                        sexColumnLabel= 'Sex',
                        ageColumnLabel= 'AgeAtPresentation',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        ageBounds= (0,150),
                        hospital= 'ALL',
                        sex= 0,
                        yearBounds= (2015,2022),
                        trainSize= 10,
                        testSize=10)
            _, _ = importer.importData()
        with self.assertRaises(e.ColumnLabelException):
            importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUAL.csv'],
                        dateColumnLabel= 'EDPresentationDTTM',
                        hospitalColumnLabel= 'invalid',
                        sexColumnLabel= 'Sex',
                        ageColumnLabel= 'AgeAtPresentation',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        ageBounds= (0,150),
                        hospital= 'ALL',
                        sex= 0,
                        yearBounds= (2015,2022),
                        trainSize= 10,
                        testSize=10)
            _, _ = importer.importData()
        with self.assertRaises(e.ColumnLabelException):
            importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUAL.csv'],
                        dateColumnLabel= 'EDPresentationDTTM',
                        hospitalColumnLabel= 'hospid',
                        sexColumnLabel= 'invalid',
                        ageColumnLabel= 'AgeAtPresentation',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        ageBounds= (0,150),
                        hospital= 'ALL',
                        sex= 0,
                        yearBounds= (2015,2022),
                        trainSize= 10,
                        testSize=10)
            _, _ = importer.importData()
        with self.assertRaises(e.ColumnLabelException):
            importer = i.Importer(fileLocations= ['EpiNLPpb_dev/data/MANUAL.csv'],
                        dateColumnLabel= 'EDPresentationDTTM',
                        hospitalColumnLabel= 'hospid',
                        sexColumnLabel= 'Sex',
                        ageColumnLabel= 'invalid',
                        textFieldColumnLabels= ['TriageObject','TriageDescription'],
                        flagColumnLabel= 'SSH_Flag',
                        ageBounds= (0,150),
                        hospital= 'ALL',
                        sex= 0,
                        yearBounds= (2015,2022),
                        trainSize= 10,
                        testSize=10)
            _, _ = importer.importData()

if __name__ == '__main__':
    unittest.main()