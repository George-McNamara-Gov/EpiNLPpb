'''
Test module for the package/base module.

Classes:

    TestBase

Functions:

    None

Misc Variables:

    cwd : str
        A string containing the path to the current working directory when the
        module is first run.
    deldir : str
        A string containing the path from which to delete NLP programs.

Exceptions:

    None
'''
import unittest
import os
import time

from ..package import base as b
from ..package import exceptions as e

cwd = str(os.getcwd())
deldir = cwd + '\\EpiNLPpb\\model'

class TestBase(unittest.TestCase):
    '''
    A class of tests to check the operation of the package/base module.

    Attributes
    ----------
    None

    Methods
    -------
    test_noError()
        Tests that the NLP class can be constructed and the create, evaluateNLP
        and exportNLP methods run without error on valid inputs.
    test_fileNameDuplicate()
        Tests that creating a model with the same name as one already stored in
        project/model raises an exception.
    test_fileTypeError()
        Tests that invalid fileType inputs raise exceptions.
    test_columnLabelError()
        Tests that invalid column label inputs raise exceptions.
    test_ageError()
        Tests that invalid minAge or maxAge inputs raise exceptions.
    test_hospitalError()
        Tests that invalid hospital inputs raise exceptions.
    test_sexError()
        Tests that invalid sex inputs raise exceptions.
    test_yearError()
        Tests that invalid minYear or maxYear inputs raise exceptions.
    test_trainSizeError()
        Tests that invalid trainSize inputs raise exceptions.
    test_trainDistError()
        Tests that invalid trainDist inputs raise exceptions.
    test_testSizeError()
        Tests that invalid testSize inputs raise exceptions.
    test_testDistError()
        Tests that invalid testDist inputs raise exceptions.
    test_tokeniserError()
        Tests that invalid tokeniser inputs raise exceptions.
    test_preLAError()
        Tests that invalid preLAChanges inputs raise exceptions.
    test_tokenLAError()
        Tests that invalid tokenLevelLA inputs raise exceptions.
    test_textLAError()
        Tests that invalid textLevelLA inputs raise exceptions.
    test_corpusLAError()
        Tests that invalid corpusLevelLA inputs raise exceptions.
    test_mlAlgError()
        Tests that invalid mlAlgType inputs raise exceptions.
    test_macLearnError()
        Tests that invalid macLearnInput inputs raise exceptions.
    test_create()
        Tests that the create method can be called without error.
    test_predictSingle()
        Tests that the predictSingle method can be called without error.
    test_treeGraphError()
        Tests that viewTreeGraph raises an exception on SVMACHINE nlp objects.
    test_extractFlags()
        Tests that extractFlags function behaves as expected.
    test_rec()
        Tests that startRec and stopRec record the correct time.
    '''

    def test_noError(self):
        os.chdir(cwd)
        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        nlp.evaluateNLP()
        nlp.exportNLP()

        try:
            os.chdir(deldir)
            path = deldir + '\\Tester-NLP-Program'
            for name in os.listdir(path):
                file = path + '/' + name
                os.remove(file)
            os.rmdir(deldir + '\\Tester-NLP-Program')
            os.chdir(cwd)
        except Exception as ex:
            os.chdir(cwd)
            raise ex

        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    '',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    '',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    '',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    '',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        nlp.evaluateNLP()
        
    def test_fileNameDuplicate(self):
        nlp = b.NLP('Testing',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        nlp.evaluateNLP()
        nlp.exportNLP()
        with self.assertRaises(e.NameExistsException):
            nlp = b.NLP('Testing',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
            nlp.create()
            nlp.evaluateNLP()
            nlp.exportNLP()
        
        try:
            os.chdir(deldir)
            path = deldir + '/Testing-NLP-Program'
            for name in os.listdir(path):
                file = path + '/' + name
                os.remove(file)
            os.rmdir(deldir + '/Testing-NLP-Program')
            os.chdir(cwd)
        except Exception as ex:
            os.chdir(cwd)
            raise ex

    def test_fileTypeError(self):
        with self.assertRaises(e.UnsupportedFileTypeException):
            _ = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    '',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.UnsupportedFileTypeException):
            _ = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'invalid',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        
    def test_columnLabelError(self):
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'invalid',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'invalid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'invalid',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'invalid',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['invalid','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'invalid',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
            nlp.create()

    def test_ageError(self):
        with self.assertRaises(e.MinAgeException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    -1,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.MaxAgeException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    -1,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.MaxAgeException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    15,
                    0,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])

    def test_hospitalError(self):
        with self.assertRaises(e.HospitalException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'invalid',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.HospitalException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    '',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])

    def test_sexError(self):
        with self.assertRaises(e.SexException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'invalid',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.SexException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    '',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])

    def test_yearError(self):
        with self.assertRaises(e.MinYearException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2013,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.MaxYearException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2013,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.MinMaxYearException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2020,
                    2015,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])

    def test_trainSizeError(self):
        with self.assertRaises(e.NegTrainSizeException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    -1,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.MoreDataThanRecordsException):
            nlp = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    10000000,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
            nlp.create()

    def test_trainDistError(self):
        with self.assertRaises(e.TrainDistException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'invalid',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.TrainDistException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    '',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])

    def test_testSizeError(self):
        with self.assertRaises(e.NegTestSizeException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    -1,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.MoreDataThanRecordsException):
            nlp = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    10000000,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
            nlp.create()

    def test_testDistError(self):
        with self.assertRaises(e.TestDistException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'invalid',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.TestDistException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    '',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])

    def test_tokeniserError(self):
        with self.assertRaises(e.TokeniserException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'invalid',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])

    def test_preLAError(self):
        with self.assertRaises(e.PreLAException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    ['invalid'],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.PreLAException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    ['REMOVE_STOPWORDS', 'invalid'],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])

    def test_tokenLAError(self):
        with self.assertRaises(e.TokenLevelException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    [],
                    ['invalid'],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.TokenLevelException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    [],
                    ['POS_TAG','invalid'],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])

    def test_textLAError(self):
        with self.assertRaises(e.TextLevelException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['invalid'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
        with self.assertRaises(e.TextLevelException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS', 'invalid'],
                    '',
                    'DECISIONTREE',
                    ['GINI'])
    
    def test_corpusLAError(self):
        with self.assertRaises(e.CorpusLevelException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    [],
                    [],
                    ['KEYWORDS'],
                    'invalid',
                    'DECISIONTREE',
                    ['GINI'])

    def test_mlAlgError(self):
        with self.assertRaises(e.MLAlgTypeException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'invalid',
                    ['GINI'])
        with self.assertRaises(e.MLAlgTypeException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    '',
                    ['GINI'])
    
    def test_macLearnError(self):
        with self.assertRaises(e.ImpurityException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'DECISIONTREE',
                    ['invalid'])
        with self.assertRaises(e.KernelException):
            _ = b.NLP('Test',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    '',
                    [],
                    [],
                    ['KEYWORDS'],
                    '',
                    'SVMACHINE',
                    ['invalid'])

    def test_create(self):
        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        self.assertEqual(len(nlp.actualFlags), 100)
        self.assertEqual(len(nlp.predictedFlags), 100)
        for flag in nlp.actualFlags:
            self.assertTrue(flag in [0,1])
        for flag in nlp.predictedFlags:
            self.assertTrue(flag in [0,1])
        self.assertEqual(len(nlp.times), len(nlp.spaces))
    
    def test_predictSingle(self):
        record1 = [0,0,0,0,0,'This is a test record.','Test test test',0]
        record2 = [0,0,0,0,0,'','',0]
        record3 = [0,0,0,0,0]
        record4 = [0,0,0,0,'Test']
        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    500,
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'DECISIONTREE',
                    ['GINI'])
        nlp.create()
        flag1 = nlp.predictSingle(record1)
        flag2 = nlp.predictSingle(record2)
        self.assertTrue(flag1 in [0,1])
        self.assertTrue(flag2 in [0,1])
        with self.assertRaises(IndexError):
            _ = nlp.predictSingle(record3)
        with self.assertRaises(IndexError):
            _ = nlp.predictSingle(record4)
    
    def test_treeGraphError(self):
        nlp = b.NLP('Tester',
                    ['EpiNLPpb/data/KEYWORD1.csv', 'EpiNLPpb/data/KEYWORD2.csv'],
                    'CSV',
                    'EDPresentationDTTM',
                    'hospid',
                    'Sex',
                    'AgeAtPresentation',
                    ['TriageObject','TriageDescription'],
                    'SSH_Flag',
                    0,
                    15,
                    'CHHS',
                    'MALE',
                    2015,
                    2020,
                    5000, #FIXME 
                    'NEWESTBLOCK',
                    100,
                    'NEWESTBLOCK',
                    'WORD_TOKENISER',
                    ['REMOVE_STOPWORDS', 'STEMMING'],
                    ['POS_TAG'],
                    ['KEYWORDS'],
                    'BAG_OF_WORDS_C',
                    'SVMACHINE',
                    ['LINEAR'])
        nlp.create()
        with self.assertRaises(e.TreeGraphException):
            nlp.viewTreeGraph()

    def test_extractFlags(self):
        records = [[0,0,0,0,0,'','',0],
                   [0,0,0,0,0,'','',1],
                   [0,0,0,0,0,'','',9]]
        self.assertEqual(b.extractFlags(records), [0,1,9])

    def test_rec(self):
        time0 = b.startRec()
        time.sleep(5)
        time1, _ = b.stopRec(time0)
        self.assertGreaterEqual(time1, 5)
        self.assertLess(time1, 6)

if __name__ == '__main__':
    unittest.main()