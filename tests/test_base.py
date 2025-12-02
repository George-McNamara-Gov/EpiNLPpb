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
deldir = cwd + '\\EpiNLPpb_dev\\model'

class TestBase(unittest.TestCase):
    '''
    A class of tests to check the operation of the package/base.py module.

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
    test_columnLabelError()
        Tests that invalid column label inputs raise exceptions.
    test_ageError()
        Tests that invalid ageBounds inputs raise exceptions.
    test_hospitalError()
        Tests that invalid hospital inputs raise exceptions.
    test_sexError()
        Tests that invalid sex inputs raise exceptions.
    test_yearError()
        Tests that invalid yearBounds inputs raise exceptions.
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
    test_crossValidate()
        Tests that invalid nFold inputs raise exceptions and the correct number
        of measurements are recorded.
    test_rec()
        Tests that startRec and stopRec record the correct time.
    '''

    def test_noError(self):
        os.chdir(cwd)
        nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
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

        nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= '',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= '',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= '',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= '',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        nlp.create()
        nlp.evaluateNLP()

        nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        nlp.create()
        nlp.evaluateNLP()

        i_arg_dict = {
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
        v_arg_dict = {
            'tokeniser' : 'WORD_TOKENISER', 
            'preLAChanges' : ['REMOVE_STOPWORDS'],
            'tokenLevelLA' : [],
            'textLevelLA' : ['KEYWORDS'],
            'corpusLevelLA' : ''
        }
        m_arg_dict = {
            'mlAlgType' : 'DECISIONTREE',
            'macLearnInput' : {'impurity' : 'gini'}
        }
        nlp = b.NLP(imp_arg_dict= i_arg_dict,
                    vect_arg_dict= v_arg_dict,
                    ml_arg_dict= m_arg_dict)
        nlp.create()
        nlp.evaluateNLP()

        
    def test_fileNameDuplicate(self):
        nlp = b.NLP(name= 'Testing',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        nlp.create()
        nlp.evaluateNLP()
        nlp.exportNLP()
        with self.assertRaises(e.NameExistsException):
            nlp = b.NLP(name= 'Testing',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
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
        
    def test_columnLabelError(self):
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'invalid',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'invalid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'invalid',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'invalid',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['invalid','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
            nlp.create()
        with self.assertRaises(e.ColumnLabelException):
            nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'invalid',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
            nlp.create()

    def test_ageError(self):
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (-1, 15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,-1),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (15,0),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_hospitalError(self):
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'invalid',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= '',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_sexError(self):
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 'invalid',
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 4,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_yearError(self):
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (1899,2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015,2013),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.BoundsException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2020,2015),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_trainSizeError(self):
        with self.assertRaises(e.NegTrainSizeException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= -1,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.MoreDataThanRecordsException):
            nlp = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 10000000,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
            nlp.create()

    def test_trainDistError(self):
        with self.assertRaises(e.TrainDistException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    trainDist= 'invalid',
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.TrainDistException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    trainDist= '',
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_testSizeError(self):
        with self.assertRaises(e.NegTestSizeException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= -1,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.MoreDataThanRecordsException):
            nlp = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 10000000,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
            nlp.create()

    def test_testDistError(self):
        with self.assertRaises(e.TestDistException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    testDist= 'invalid',
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.TestDistException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    testDist= '',
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_tokeniserError(self):
        with self.assertRaises(e.TokeniserException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'invalid',
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_preLAError(self):
        with self.assertRaises(e.PreLAException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    preLAChanges= ['invalid'],
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.PreLAException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    preLAChanges= ['REMOVE_STOPWORDS', 'invalid'],
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_tokenLAError(self):
        with self.assertRaises(e.TokenLevelException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    tokenLevelLA= ['invalid'],
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.TokenLevelException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    tokenLevelLA= ['POS_TAG','invalid'],
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_textLAError(self):
        with self.assertRaises(e.TextLevelException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['invalid'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.TextLevelException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS', 'invalid'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
    
    def test_corpusLAError(self):
        with self.assertRaises(e.CorpusLevelException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'invalid',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})

    def test_mlAlgError(self):
        with self.assertRaises(e.MLAlgTypeException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'invalid',
                    macLearnInput= {'impurity' : 'gini'})
        with self.assertRaises(e.MLAlgTypeException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= '',
                    macLearnInput= {'impurity' : 'gini'})
    
    def test_macLearnError(self):
        with self.assertRaises(e.ImpurityException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'invalid'})
        with self.assertRaises(e.KernelException):
            _ = b.NLP(name= 'Test',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    textLevelLA= ['KEYWORDS'],
                    mlAlgType= 'SVMACHINE',
                    macLearnInput= {'kernel' : 'invalid'})

    def test_create(self):
        nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 500,
                    testSize= 100,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        nlp.create()
        self.assertEqual(len(nlp.actualFlags), 100)
        self.assertEqual(len(nlp.predictedFlags), 100)
        for flag in nlp.actualFlags:
            self.assertTrue(flag in [0,1])
        for flag in nlp.predictedFlags:
            self.assertTrue(flag in [0,1])
        self.assertEqual(len(nlp.times), len(nlp.spaces))

    def test_crossValidate(self):
        nlp = b.NLP(name= 'Tester',
                    fileLocations= ['EpiNLPpb_dev/data/KEYWORD1.csv', 'EpiNLPpb_dev/data/KEYWORD2.csv'],
                    dateColumnLabel= 'EDPresentationDTTM',
                    hospitalColumnLabel= 'hospid',
                    sexColumnLabel= 'Sex',
                    ageColumnLabel= 'AgeAtPresentation',
                    textFieldColumnLabels= ['TriageObject','TriageDescription'],
                    flagColumnLabel= 'SSH_Flag',
                    ageBounds= (0,15),
                    hospital= 'CHHS',
                    sex= 1,
                    yearBounds= (2015, 2020),
                    trainSize= 5000,
                    testSize= 1000,
                    tokeniser= 'WORD_TOKENISER',
                    preLAChanges= ['REMOVE_STOPWORDS', 'STEMMING'],
                    tokenLevelLA= ['POS_TAG'],
                    textLevelLA= ['KEYWORDS'],
                    corpusLevelLA= 'BAG_OF_WORDS_C',
                    mlAlgType= 'DECISIONTREE',
                    macLearnInput= {'impurity' : 'gini'})
        nlp.crossValidate()
        with self.assertRaises(e.CrossValidateException):
            nlp.crossValidate(nFolds= [])
        with self.assertRaises(e.CrossValidateException):
            nlp.crossValidate(nFolds= 0)
        
        results = nlp.crossValidate(nFolds= 7)
        self.assertEqual(len(results['Train F1']), 7)
        self.assertEqual(len(results['Train Precision']), 7)
        self.assertEqual(len(results['Train Recall']), 7)
        self.assertEqual(len(results['Test F1']), 7)
        self.assertEqual(len(results['Test Precision']), 7)
        self.assertEqual(len(results['Test Recall']), 7)
        self.assertEqual(len(results['Fold Times']), 7)

    def test_rec(self):
        time0 = b.startRec()
        time.sleep(5)
        time1, _ = b.stopRec(time0)
        self.assertGreaterEqual(time1, 5)
        self.assertLess(time1, 6)

if __name__ == '__main__':
    unittest.main()