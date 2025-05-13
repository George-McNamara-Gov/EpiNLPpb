'''
Test module for the package/vectorise package.

Classes:

    TestVectorise

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
import unittest

from ..package.vectorise import vectorise as v
from ..package.vectorise import base as b
from ..package import exceptions as e

class TestVectorise(unittest.TestCase):
    '''
    A class of tests to check the operation of the package/mlearn package.

    Attributes
    ----------
    None

    Methods
    -------
    test_noError()
        Tests that the vectorise class can be constructed and the buildVector 
        and vectorise methods can be run on valid inputs.
    test_noTechniquesError()
        Tests that giving no token, text or corpus level LA techniques raises an 
        exception.
    test_tokLAWithNoTok()
        Tests that providing a token level LA technique without a tokeniser
        raises an exception.
    test_keyWordCheck()
        Tests that keyWordCheck identifies the correct terms.
    test_tokeniserNameError()
        Tests that providing an invalid tokeniser raise an exception.
    test_preLANameError()
        Tests that providing invalid preLA techniques raises an exception.
    test_tokenLevelLANameError()
        Tests that providing invalid token LA techniques raises an exception.
    test_textLevelLANameError()
        Tests that providing invalid text LA techniques raises an exception.
    test_corpusLevelLANameError()
        Tests that providing invalid corpus LA techniques raises an exception.
    test_builderVectorPreLA()
        Tests that building a vector with preLA produces vectors of the same 
        length.
    test_builderVectorTokeniser()
        Tests that building a vector with tokenisers produces vectors of the 
        same length.
    test_builderVectorTokenLevel()
        Tests that building a vector with token level LA produces vectors of the 
        same length.
    test_builderVectorTextLevel()
        Tests that building a vector with text level LA produces vectors of the 
        same length.
    test_buildVector()
        Tests that build vector produces vectors of the same length.
    test_recordToVector()
        Tests that recordToVecotr produces vectors of the same length.
    test_vectorise()
        Tests that vectorise produces the correct number of vectors and vectors 
        of the same length.
    '''
    
    def test_noError(self):
        vc = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        text = 'The-quick brown, fox "jumps" over the lazy dog.'
        _ = vc.buildVector(text)
        record = [0,0,0,0,0,'The quick brown','fox jumps over',0]
        _ = vc.recordToVector(record)

    def test_noTechniquesError(self):
        with self.assertRaises(e.NoLATechniquesException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         [],
                         '',
                         [4,5])

    def test_tokLAWithNoTok(self):
        with self.assertRaises(e.NoTokeniserException):
            _ = v.Vectorise('', 
                         [],
                         ['POS_TAG'],
                         [],
                         '',
                         [4,5])
            
    def test_keyWordCheck(self):
        text1 = 'Example text 1 with no key words'
        text2 = 'Example text 2 with one key word tos'
        text3 = 'monox Example text 3 with multiple key words od.'
        text4 = 'cutting Example text 4 with split key word self harm'
        for value in b.keyWordCheck(text1):
            self.assertEqual(value,0)
        self.assertEqual(b.keyWordCheck(text2)[8], 1)
        self.assertEqual(b.keyWordCheck(text3)[15], 1)
        self.assertEqual(b.keyWordCheck(text3)[13], 1)
        self.assertEqual(b.keyWordCheck(text4)[20], 1)

    def test_tokeniserNameError(self):
        _ = v.Vectorise('',
                        ['REMOVE_STOPWORDS'],
                        [],
                        ['KEYWORDS'],
                        '',
                        [4,5])
        with self.assertRaises(e.TokeniserException):
            _ = v.Vectorise('invalid',
                            ['REMOVE_STOPWORDS'],
                            [],
                            ['KEYWORDS'],
                            '',
                            [4,5])
        with self.assertRaises(e.TokeniserException):
            _ = v.Vectorise(0,
                            ['REMOVE_STOPWORDS'],
                            [],
                            ['KEYWORDS'],
                            '',
                            [4,5])

    def test_preLANameError(self):
        _ = v.Vectorise('WORD_TOKENISER', 
                        [],
                        [],                         
                        ['KEYWORDS'],
                        '',
                        [4,5])
        with self.assertRaises(e.PreLAException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['invalid'],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(e.PreLAException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         [0],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(TypeError):
            _ = v.Vectorise('WORD_TOKENISER', 
                         0,
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(e.PreLAException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         [''],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])

    def test_tokenLevelLANameError(self):
        _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         ['POS_TAG'],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(e.TokenLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         ['invalid'],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(e.TokenLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [''],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(e.TokenLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         ['POS_TAG', 'invalid'],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(e.TokenLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [0],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(TypeError):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         0,
                         ['KEYWORDS'],
                         '',
                         [4,5])

    def test_textLevelLANameError(self):
        _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         ['POS_TAG'],
                         [],
                         '',
                         [4,5])
        _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(e.TextLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['invalid'],
                         '',
                         [4,5])
        with self.assertRaises(e.TextLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['invalid','ASCII_CONVERSION'],
                         '',
                         [4,5])
        with self.assertRaises(e.TextLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         [0],
                         '',
                         [4,5])
        with self.assertRaises(TypeError):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         0,
                         '',
                         [4,5])
        with self.assertRaises(e.TextLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         [''],
                         '',
                         [4,5])
            
    def test_corpusLevelLANameError(self):
        _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         ['POS_TAG'],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        with self.assertRaises(e.CorpusLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['KEYWORDS'],
                         'invalid',
                         [4,5])
        with self.assertRaises(e.CorpusLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['KEYWORDS'],
                         [''],
                         [4,5])
        with self.assertRaises(e.CorpusLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['KEYWORDS'],
                         [0],
                         [4,5])
        with self.assertRaises(e.CorpusLevelException):
            _ = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['KEYWORDS'],
                         0,
                         [4,5])
    
    def test_buildVectorPreLA(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise('', 
                         ['REMOVE_STOPWORDS'],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
        vc = v.Vectorise('', 
                         ['STEMMING'],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))

    def test_buildVectorTokeniser(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise('WORD_TOKENISER', 
                         [],
                         [],
                         ['ASCII_CONVERSION'],
                         '',
                         [4,5])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
        vc = v.Vectorise('PUNC_TOKENISER', 
                         [],
                         [],
                         ['ASCII_CONVERSION'],
                         '',
                         [4,5])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
        vc = v.Vectorise('TWEET_TOKENISER', 
                         [],
                         [],
                         ['ASCII_CONVERSION'],
                         '',
                         [4,5])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))

    def test_buildVectorTokenLevel(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise('WORD_TOKENISER', 
                         [],
                         ['POS_TAG'],
                         [],
                         '',
                         [4,5])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))

    def test_buildVectorTextLevel(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise('', 
                         [],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
        vc = v.Vectorise('', 
                         [],
                         [],
                         ['ASCII_CONVERSION'],
                         '',
                         [4,5])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
        vc = v.Vectorise('', 
                         [],
                         [],
                         ['KEYWORDS'],
                         '',
                         [4,5])

    def test_buildVector(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise('WORD_TOKENISER', 
                         ['REMOVE_STOPWORDS'],
                         ['POS_TAG'],
                         ['KEYWORDS'],
                         '',
                         [4,5])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
    
    def test_recordToVector(self):
        vect = v.Vectorise('WORD_TOKENISER',
                           [],
                           [],
                           ['ASCII_CONVERSION'],
                           '',
                           [4,5])
        record1 = [0,0,0,0,0,'','',0]
        record2 = [0,0,0,0,0,'The quick brown','fox jumps over the lazy dog',0]
        record3 = [0,0,0,0,0,'She sells sea','shells by the sea shore',0]
        self.assertEqual(len(vect.recordToVector(record1)),
                        len(vect.recordToVector(record2)),
                        len(vect.recordToVector(record3)))     

    def test_vectorise(self):
        trainRecords = [[0,0,0,0,0,'','',0],
                        [0,0,0,0,0,'The quick brown',
                         'fox jumps over the lazy dog',0],
                        [0,0,0,0,0,'She sells sea','shells by the sea shore',0]]
        testRecords = [[0,0,0,0,0,'Peter piper picked a peck',
                        'of pickled peppers',0],
                       [0,0,0,0,0,'Red leather','yellow leather',0]]
        vect = v.Vectorise('',
                           [],
                           [],
                           [],
                           'BAG_OF_WORDS_C',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('',
                           [],
                           [],
                           [],
                           'MOD_BAG_OF_WORDS_C',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('',
                           [],
                           [],
                           [],
                           'BAG_OF_WORDS_F',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('',
                           [],
                           [],
                           [],
                           'MOD_BAG_OF_WORDS_F',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('',
                           [],
                           [],
                           [],
                           'BAG_OF_WORDS_H',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('',
                           [],
                           [],
                           [],
                           'MOD_BAG_OF_WORDS_H',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('WORD_TOKENISER',
                           [],
                           [],
                           ['ASCII_CONVERSION'],
                           'BAG_OF_WORDS_C',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('WORD_TOKENISER',
                           [],
                           [],
                           ['ASCII_CONVERSION'],
                           'MOD_BAG_OF_WORDS_C',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('WORD_TOKENISER',
                           [],
                           [],
                           ['ASCII_CONVERSION'],
                           'BAG_OF_WORDS_F',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('WORD_TOKENISER',
                           [],
                           [],
                           ['ASCII_CONVERSION'],
                           'MOD_BAG_OF_WORDS_F',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('WORD_TOKENISER',
                           [],
                           [],
                           ['ASCII_CONVERSION'],
                           'BAG_OF_WORDS_H',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise('WORD_TOKENISER',
                           [],
                           [],
                           ['ASCII_CONVERSION'],
                           'MOD_BAG_OF_WORDS_H',
                           [4,5])
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

if __name__ == '__main__':
    unittest.main()