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
from ..package.Importer import constants as c
from ..package import exceptions as e

class TestImporter(unittest.TestCase):
    '''
    A class of tests to check the operation of the package/Importer package.

    Attributes
    ----------
    None

    Methods
    -------
    test_noError()
        Tests that the importer class can be constructed and the importData 
        method can run without errors on valid inputs.
    test_fileTypeError()
        Tests that invalid file type inputs cause exceptions.
    test_columnLabelIndices()
        Tests that column label indices are assigned correctly.
    test_trainDistError()
        Tests that invalid trainDist inputs cause exceptions. 
    test_testDistError()
        Tests that invalid testDist inputs cause exceptions. 
    test_ageError()
        Tests that invalid minAge and maxAge inputs cause exceptions.
    test_hospitalError()
        Tests that invalid hospital inputs cause exceptions.
    test_sexError()
        Tests that invalid sex inputs cause exceptions.
    test_yearError()
        Tests that invalid minYear and maxYear inputs cause exceptions.
    test_dataExtractorSizeError()
        Tests that invalid trainSize and testSize inputs cause exceptions.
    test_dataSizes()
        Tests that all exctractors extract the correct amount of data.
    test_Demographic()
        Tests that the imported data satisfies the given demographic and the 
        data contains the correct amount of data fields.
    test_posPercentError()
        Tests that invalid trainPosPercent or testPosPercent inputs cause 
        exceptions.
    test_PosPercent()
        Tests that the correct percentages of positively and negatively flagged
        records are extracted.
    test_splitPosAndNegFlags()
        Tests the splitPosAndNegFlags accurately divide the input data.
    testInvalidColumnLabel()
        Tests that invalid column labels cause exceptions.
    '''
    
    def test_noError(self):
        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        importer.importData()
        importer = i.Importer(['EpiNLPpb/data/MANUALXLSXTEST.xlsx'],
                            'XLSX',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        importer.importData()

    def test_fileTypeError(self):
        with self.assertRaises(e.UnsupportedFileTypeException):
            importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            '',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
            importer.importData()
        with self.assertRaises(e.UnsupportedFileTypeException):
            importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'invalid',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
            importer.importData()

    def test_columnLabelIndices(self):
        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        self.assertEqual(importer.dataSet.dateIndex, 0)
        self.assertEqual(importer.dataSet.hospIndex, 1)
        self.assertEqual(importer.dataSet.sexIndex, 2)
        self.assertEqual(importer.dataSet.ageIndex, 3)
        self.assertEqual(importer.dataSet.textIndices, [4,5])
        self.assertEqual(importer.dataSet.flagIndex, 6)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            '',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        self.assertEqual(importer.dataSet.dateIndex, -1)
        self.assertEqual(importer.dataSet.hospIndex, 0)
        self.assertEqual(importer.dataSet.sexIndex, 1)
        self.assertEqual(importer.dataSet.ageIndex, 2)
        self.assertEqual(importer.dataSet.textIndices, [3,4])
        self.assertEqual(importer.dataSet.flagIndex, 5)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            '',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        self.assertEqual(importer.dataSet.dateIndex, 0)
        self.assertEqual(importer.dataSet.hospIndex, -1)
        self.assertEqual(importer.dataSet.sexIndex, 1)
        self.assertEqual(importer.dataSet.ageIndex, 2)
        self.assertEqual(importer.dataSet.textIndices, [3,4])
        self.assertEqual(importer.dataSet.flagIndex, 5)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            '',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        self.assertEqual(importer.dataSet.dateIndex, 0)
        self.assertEqual(importer.dataSet.hospIndex, 1)
        self.assertEqual(importer.dataSet.sexIndex, -1)
        self.assertEqual(importer.dataSet.ageIndex, 2)
        self.assertEqual(importer.dataSet.textIndices, [3,4])
        self.assertEqual(importer.dataSet.flagIndex, 5)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            '',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        self.assertEqual(importer.dataSet.dateIndex, 0)
        self.assertEqual(importer.dataSet.hospIndex, 1)
        self.assertEqual(importer.dataSet.sexIndex, 2)
        self.assertEqual(importer.dataSet.ageIndex, -1)
        self.assertEqual(importer.dataSet.textIndices, [3,4])
        self.assertEqual(importer.dataSet.flagIndex, 5)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        self.assertEqual(importer.dataSet.dateIndex, 0)
        self.assertEqual(importer.dataSet.hospIndex, 1)
        self.assertEqual(importer.dataSet.sexIndex, 2)
        self.assertEqual(importer.dataSet.ageIndex, 3)
        self.assertEqual(importer.dataSet.textIndices, [4])
        self.assertEqual(importer.dataSet.flagIndex, 5)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            '',
                            '',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        self.assertEqual(importer.dataSet.dateIndex, -1)
        self.assertEqual(importer.dataSet.hospIndex, -1)
        self.assertEqual(importer.dataSet.sexIndex, 0)
        self.assertEqual(importer.dataSet.ageIndex, 1)
        self.assertEqual(importer.dataSet.textIndices, [2,3])
        self.assertEqual(importer.dataSet.flagIndex, 4)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            '',
                            '',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        self.assertEqual(importer.dataSet.dateIndex, 0)
        self.assertEqual(importer.dataSet.hospIndex, 1)
        self.assertEqual(importer.dataSet.sexIndex, -1)
        self.assertEqual(importer.dataSet.ageIndex, -1)
        self.assertEqual(importer.dataSet.textIndices, [2,3])
        self.assertEqual(importer.dataSet.flagIndex, 4)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            '',
                            'hospid',
                            '',
                            'AgeAtPresentation',
                            ['TriageObject'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,10,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        self.assertEqual(importer.dataSet.dateIndex, -1)
        self.assertEqual(importer.dataSet.hospIndex, 0)
        self.assertEqual(importer.dataSet.sexIndex, -1)
        self.assertEqual(importer.dataSet.ageIndex, 1)
        self.assertEqual(importer.dataSet.textIndices, [2])
        self.assertEqual(importer.dataSet.flagIndex, 3)
        
    def test_trainDistError(self):
        with self.assertRaises(e.TrainDistException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'not a distriubtion', 10, 'UNIFORM')
        _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,150,'ALL','ALL',2015,2022,10,
                    'NEWESTBLOCK', 10, 'UNIFORM')

    def test_testDistError(self):
        with self.assertRaises(e.TestDistException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'not a distribution')
        _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,150,'ALL','ALL',2015,2022,10,
                    'NEWESTBLOCK', 10, 'UNIFORM')

    def test_ageError(self):
        with self.assertRaises(e.MinAgeException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        -1,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM')
        with self.assertRaises(e.MinAgeException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        -2,-1,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM')
        with self.assertRaises(e.MaxAgeException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag', 
                        10,9,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM')
        with self.assertRaises(e.MaxAgeException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag', 
                        0,-1,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM')
        _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    9,9,'ALL','ALL',2015,2022,10,
                    'NEWESTBLOCK', 10, 'UNIFORM')
        _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,0,'ALL','ALL',2015,2022,10,
                    'NEWESTBLOCK', 10, 'UNIFORM')
    
    def test_hospitalError(self):
        with self.assertRaises(e.HospitalException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'not a hospital','ALL',2015,
                        2022,10, 'NEWESTBLOCK', 10, 'UNIFORM')

    def test_sexError(self):
        with self.assertRaises(e.SexException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','not a sex',2015,
                        2022,10, 'NEWESTBLOCK', 10, 'UNIFORM')

    def test_yearError(self):
        with self.assertRaises(e.MinYearException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2014,
                        2022,10, 'NEWESTBLOCK', 10, 'UNIFORM')
        with self.assertRaises(e.MaxYearException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,
                        2023,10, 'NEWESTBLOCK', 10, 'UNIFORM')
        with self.assertRaises(e.MinMaxYearException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2017,
                        2016,10, 'NEWESTBLOCK', 10, 'UNIFORM')
        _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,150,'ALL','ALL',2016,
                    2016,10, 'NEWESTBLOCK', 10, 'UNIFORM')

    def test_dataExtractorSizeError(self):
        importerTrain = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,
                            2022,10000000, 'NEWESTBLOCK', 10, 'UNIFORM')
        importerTest = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,
                            2022,10, 'NEWESTBLOCK', 10000000, 'UNIFORM')
        with self.assertRaises(e.MoreDataThanRecordsException):
            importerTrain.importData()
        with self.assertRaises(e.MoreDataThanRecordsException):
            importerTest.importData()

    def test_dataSizes(self):
        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',0,150,'ALL','ALL',2015,2022,20,
                            'NEWESTBLOCK', 10, 'NEWESTBLOCK')
        data = importer.importData()
        train = data[0]
        test = data[1]
        self.assertEqual(len(train),20)
        self.assertEqual(len(test),10)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,20,
                            'RANDOMBLOCK', 10, 'RANDOMBLOCK')
        data = importer.importData()
        train = data[0]
        test = data[1]
        self.assertEqual(len(train),20)
        self.assertEqual(len(test),10)

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            0,150,'ALL','ALL',2015,2022,20,
                            'UNIFORM', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        self.assertEqual(len(train),20)
        self.assertEqual(len(test),10)
    
    def test_Demographic(self):
        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            18,21,'CHHS','MALE',2017,2020,20,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        testRecords = train + test
        for record in testRecords:
            self.assertTrue(2017 <= b.getYear(record[0]) <= 2020)
            self.assertEqual('CHHS', record[1])
            self.assertEqual(1, record[2])
            self.assertTrue(18 <= record[3] <= 21)
            self.assertEqual(7, len(record))

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            18,21,'ALL','MALE',2017,2020,20,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        testRecords = train + test
        for record in testRecords:
            self.assertTrue(2017 <= b.getYear(record[0]) <= 2020)
            self.assertEqual(1, record[2])
            self.assertTrue(18 <= record[3] <= 21)
            self.assertEqual(7, len(record))

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            18,21,'CHHS','ALL',2017,2020,20,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        testRecords = train + test
        for record in testRecords:
            self.assertTrue(2017 <= b.getYear(record[0]) <= 2020)
            self.assertEqual('CHHS', record[1])
            self.assertTrue(18 <= record[3] <= 21)
            self.assertEqual(7, len(record))

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            '',
                            'hospid',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            18,21,'CHHS','MALE',2017,2020,20,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        testRecords = train + test
        for record in testRecords:
            self.assertEqual('CHHS', record[0])
            self.assertEqual(1, record[1])
            self.assertTrue(18 <= record[2] <= 21)
            self.assertEqual(6, len(record))

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            '',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            18,21,'CHHS','MALE',2017,2020,20,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        testRecords = train + test
        for record in testRecords:
            self.assertTrue(2017 <= b.getYear(record[0]) <= 2020)
            self.assertEqual(1, record[1])
            self.assertTrue(18 <= record[2] <= 21)
            self.assertEqual(6, len(record))

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            '',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            18,21,'CHHS','MALE',2017,2020,20,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        testRecords = train + test
        for record in testRecords:
            self.assertTrue(2017 <= b.getYear(record[0]) <= 2020)
            self.assertEqual('CHHS', record[1])
            self.assertTrue(18 <= record[2] <= 21)
            self.assertEqual(6, len(record))

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            'EDPresentationDTTM',
                            'hospid',
                            'Sex',
                            '',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            18,21,'CHHS','MALE',2017,2020,20,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        testRecords = train + test
        for record in testRecords:
            self.assertTrue(2017 <= b.getYear(record[0]) <= 2020)
            self.assertEqual('CHHS', record[1])
            self.assertEqual(1, record[2])
            self.assertEqual(6, len(record))

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            '',
                            '',
                            'Sex',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            18,21,'CHHS','MALE',2017,2020,20,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        testRecords = train + test
        for record in testRecords:
            self.assertEqual(1, record[0])
            self.assertTrue(18 <= record[1] <= 21)
            self.assertEqual(5, len(record))

        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                            'CSV',
                            '',
                            '',
                            '',
                            'AgeAtPresentation',
                            ['TriageObject','TriageDescription'],
                            'SSH_Flag',
                            18,21,'CHHS','MALE',2017,2020,20,
                            'NEWESTBLOCK', 10, 'UNIFORM')
        data = importer.importData()
        train = data[0]
        test = data[1]
        testRecords = train + test
        for record in testRecords:
            self.assertTrue(18 <= record[0] <= 21)
            self.assertEqual(4, len(record))
    
    def test_posPercentError(self):
        with self.assertRaises(e.TrainPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM', trainPosPercent= -2)
        with self.assertRaises(e.TrainPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM',trainPosPercent= 100)
        with self.assertRaises(e.TrainPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM',trainPosPercent= 0)
        with self.assertRaises(e.TestPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM', testPosPercent= -2)
        with self.assertRaises(e.TestPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM', testPosPercent= 100)
        with self.assertRaises(e.TestPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM', testPosPercent= 0)
        with self.assertRaises(e.TrainPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM', 
                        trainPosPercent= -2,
                        testPosPercent= -2)
        with self.assertRaises(e.TrainPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM', 
                        trainPosPercent= -2,
                        testPosPercent= 100)
        with self.assertRaises(e.TrainPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM', 
                        trainPosPercent= 100,
                        testPosPercent= -2)
        with self.assertRaises(e.TrainPosPercentException):
            _ = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM', 
                        trainPosPercent= 100,
                        testPosPercent= 100)
        with self.assertRaises(e.MoreDataThanRecordsException):
            imp = i.Importer(['EpiNLPpb/data/MANUAL.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,100000,
                        'NEWESTBLOCK', 40000, 'UNIFORM',trainPosPercent=80)
            imp.importData()
        with self.assertRaises(e.MoreDataThanRecordsException):
            imp = i.Importer(['EpiNLPpb/data/MANUAL.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,40000,
                        'NEWESTBLOCK', 100000, 'UNIFORM',testPosPercent=80)
            imp.importData()

    def test_PosPercent(self):
        importer = i.Importer(['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM', 
                        trainPosPercent= 20, 
                        testPosPercent= 70)
        trainData, testData = importer.importData()
        trainCount = 0
        for rec in trainData:
            if rec[len(rec) - 1] == 1:
                trainCount += 1
        testCount = 0
        for rec in testData:
            if rec[len(rec) - 1] == 1:
                testCount += 1
        self.assertEqual(trainCount, 2)
        self.assertEqual(testCount, 7)
        
    def test_splitPosAndNegFlags(self):
        importer = i.Importer(['EpiNLPpb/data/MANUAL.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM')
        trainData, testData = importer.importData()
        data = trainData + testData
        posList, negList = i.splitPosAndNegFlags(data)
        for rec in posList:
            self.assertEqual(rec[6], 1)
        for rec in negList:
            self.assertEqual(rec[6], 0)

    def test_invalidColumnLabel(self):
        with self.assertRaises(e.ColumnLabelException):
            importer = i.Importer(['EpiNLPpb/data/MANUAL.csv'],
                        'CSV',
                        'invalid',
                        'hospid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM')
            _, _ = importer.importData()
        with self.assertRaises(e.ColumnLabelException):
            importer = i.Importer(['EpiNLPpb/data/MANUAL.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'invalid',
                        'Sex',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM')
            _, _ = importer.importData()
        with self.assertRaises(e.ColumnLabelException):
            importer = i.Importer(['EpiNLPpb/data/MANUAL.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'invalid',
                        'AgeAtPresentation',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM')
            _, _ = importer.importData()
        with self.assertRaises(e.ColumnLabelException):
            importer = i.Importer(['EpiNLPpb/data/MANUAL.csv'],
                        'CSV',
                        'EDPresentationDTTM',
                        'hospid',
                        'Sex',
                        'invalid',
                        ['TriageObject','TriageDescription'],
                        'SSH_Flag',
                        0,150,'ALL','ALL',2015,2022,10,
                        'NEWESTBLOCK', 10, 'UNIFORM')
            _, _ = importer.importData()

if __name__ == '__main__':
    unittest.main()