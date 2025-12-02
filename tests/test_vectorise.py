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
    test_tokeniserNameError()
        Tests that providing an invalid tokeniser raise an exception.
    test_preLANameError()
        Tests that providing invalid pre LA techniques raises an exception.
    test_tokenLevelLANameError()
        Tests that providing invalid token LA techniques raises an exception.
    test_textLevelLANameError()
        Tests that providing invalid text LA techniques raises an exception.
    test_corpusLevelLANameError()
        Tests that providing invalid corpus LA techniques raises an exception.
    test_ngramRangeError()
        Tests that providing invalid ngramRange input raises an exception.
    test_buildVectorPreLA()
        Tests that building a vector with preLA produces vectors of the same 
        length.
    test_buildVectorTokeniser()
        Tests that building a vector with tokenisers produces vectors of the 
        same length.
    test_buildVectorTokenLevel()
        Tests that building a vector with token level LA produces vectors of the 
        same length.
    test_buildVectorTextLevel()
        Tests that building a vector with text level LA produces vectors of the 
        same length.
    test_buildVector()
        Tests that build vector produces vectors of the same length.
    test_recordToVector()
        Tests that recordToVector produces vectors of the same length.
    test_vectorise()
        Tests that vectorise produces the correct number of vectors and vectors 
        of the same length.
    '''
    
    def test_noError(self):
        vc = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '',
                         ngramRange= (1,3))
        text = 'The-quick brown, fox "jumps" over the lazy dog.'
        _ = vc.buildVector(text)
        record = ['The quick brown','fox jumps over',0]
        _ = vc.recordToVector(record)

        args = {
            'tokeniser' : 'WORD_TOKENISER',
            'preLAChanges' : ['REMOVE_STOPWORDS'],
            'tokenLevelLA' : [],
            'textLevelLA' : ['KEYWORDS'],
            'corpusLevelLA' : '',
            'ngramRange' : (1, 3)
        }
        vc = v.Vectorise(arg_dict= args)
        text = 'The-quick brown, fox "jumps" over the lazy dog.'
        _ = vc.buildVector(text)
        record = ['The quick brown','fox jumps over',0]
        _ = vc.recordToVector(record)

    def test_noTechniquesError(self):
        with self.assertRaises(e.PreLAException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= [],
                         corpusLevelLA= '')

    def test_tokLAWithNoTok(self):
        with self.assertRaises(e.TokeniserException):
            _ = v.Vectorise(tokeniser= '', 
                         preLAChanges= [],
                         tokenLevelLA= ['POS_TAG'],
                         textLevelLA= [],
                         corpusLevelLA= '')

    def test_tokeniserNameError(self):
        with self.assertRaises(e.TokeniserException):
            _ = v.Vectorise(tokeniser= 'invalid',
                            preLAChanges= ['REMOVE_STOPWORDS'],
                            tokenLevelLA= [],
                            textLevelLA= ['KEYWORDS'],
                            corpusLevelLA= '')
        with self.assertRaises(e.TokeniserException):
            _ = v.Vectorise(tokeniser= 0,
                            preLAChanges= ['REMOVE_STOPWORDS'],
                            tokenLevelLA= [],
                            textLevelLA= ['KEYWORDS'])

    def test_preLANameError(self):
        with self.assertRaises(e.PreLAException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['invalid'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '')
        with self.assertRaises(e.PreLAException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= [0],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '')
        with self.assertRaises(e.PreLAException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= 0,
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '')
        with self.assertRaises(e.PreLAException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= [''],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '')

    def test_tokenLevelLANameError(self):
        with self.assertRaises(e.TokenLevelException):
            _ = v.Vectorise(tokeniser='WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= ['invalid'],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '')
        with self.assertRaises(e.TokenLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [''],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '')
        with self.assertRaises(e.TokenLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= ['POS_TAG', 'invalid'],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '')
        with self.assertRaises(e.TokenLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [0],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '')
        with self.assertRaises(e.TokenLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= 0,
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '')

    def test_textLevelLANameError(self):
        with self.assertRaises(e.TextLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['invalid'],
                         corpusLevelLA= '')
        with self.assertRaises(e.TextLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['invalid','ASCII_CONVERSION'],
                         corpusLevelLA= '')
        with self.assertRaises(e.TextLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= [0],
                         corpusLevelLA= '')
        with self.assertRaises(e.TextLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= 0,
                         corpusLevelLA= '')
        with self.assertRaises(e.TextLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= [''],
                         corpusLevelLA= '')
            
    def test_corpusLevelLANameError(self):
        with self.assertRaises(e.CorpusLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= 'invalid')
        with self.assertRaises(e.CorpusLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= [''])
        with self.assertRaises(e.CorpusLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= [0])
        with self.assertRaises(e.CorpusLevelException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= 0)
            
    def test_ngramRangeError(self):
        with self.assertRaises(e.NGramException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '',
                         ngramRange= (0, 0))
        with self.assertRaises(e.NGramException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '',
                         ngramRange= (-1, 0))
        with self.assertRaises(e.NGramException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '',
                         ngramRange= (2, 1))
        with self.assertRaises(e.NGramException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '',
                         ngramRange= (1, -1))
        with self.assertRaises(e.NGramException):
            _ = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= [],
                         textLevelLA= ['KEYWORDS'],
                         corpusLevelLA= '',
                         ngramRange= (-1, 1))
    
    def test_buildVectorPreLA(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise(preLAChanges= ['REMOVE_STOPWORDS'],
                         textLevelLA= ['KEYWORDS'])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
        vc = v.Vectorise(preLAChanges= ['STEMMING'],
                         textLevelLA= ['KEYWORDS'])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))

    def test_buildVectorTokeniser(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         textLevelLA= ['ASCII_CONVERSION'])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
        vc = v.Vectorise(tokeniser= 'PUNC_TOKENISER', 
                         textLevelLA= ['ASCII_CONVERSION'])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
        vc = v.Vectorise(tokeniser= 'TWEET_TOKENISER',
                         textLevelLA= ['ASCII_CONVERSION'])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))

    def test_buildVectorTokenLevel(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         tokenLevelLA= ['POS_TAG'])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))

    def test_buildVectorTextLevel(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise(textLevelLA= ['KEYWORDS'])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
        vc = v.Vectorise(textLevelLA= ['ASCII_CONVERSION'])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))

    def test_buildVector(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        text2 = 'She sells sea shells by the sea shore'
        vc = v.Vectorise(tokeniser= 'WORD_TOKENISER', 
                         preLAChanges= ['REMOVE_STOPWORDS'],
                         tokenLevelLA= ['POS_TAG'],
                         textLevelLA= ['KEYWORDS'])
        vector1 = vc.buildVector(text1)
        vector2 = vc.buildVector(text2)
        self.assertEqual(len(vector1), len(vector2))
    
    def test_recordToVector(self):
        vect = v.Vectorise(tokeniser= 'WORD_TOKENISER',
                           textLevelLA= ['ASCII_CONVERSION'])
        record1 = ['','',0]
        record2 = ['The quick brown','fox jumps over the lazy dog',0]
        record3 = ['She sells sea','shells by the sea shore',0]
        self.assertEqual(len(vect.recordToVector(record1)),
                        len(vect.recordToVector(record2)),
                        len(vect.recordToVector(record3)))     

    def test_vectorise(self):
        trainRecords = [['','',0],
                        ['The quick brown',
                         'fox jumps over the lazy dog',0],
                        ['She sells sea','shells by the sea shore',0]]
        testRecords = [['Peter piper picked a peck',
                        'of pickled peppers',0],
                       ['Red leather','yellow leather',0]]
        vect = v.Vectorise(corpusLevelLA= 'BAG_OF_WORDS_C')
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise(corpusLevelLA= 'MOD_BAG_OF_WORDS_C')
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise(corpusLevelLA= 'BAG_OF_WORDS_F')
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise(corpusLevelLA= 'MOD_BAG_OF_WORDS_F')
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise(tokeniser= 'WORD_TOKENISER',
                           textLevelLA= ['ASCII_CONVERSION'],
                           corpusLevelLA= 'BAG_OF_WORDS_C')
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise(tokeniser= 'WORD_TOKENISER',
                           textLevelLA= ['ASCII_CONVERSION'],
                           corpusLevelLA= 'MOD_BAG_OF_WORDS_C')
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise(tokeniser= 'WORD_TOKENISER',
                           textLevelLA= ['ASCII_CONVERSION'],
                           corpusLevelLA= 'BAG_OF_WORDS_F')
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

        vect = v.Vectorise(tokeniser= 'WORD_TOKENISER',
                           textLevelLA= ['ASCII_CONVERSION'],
                           corpusLevelLA= 'MOD_BAG_OF_WORDS_F')
        trainVects, testVects = vect.vectorise(trainRecords, testRecords)
        self.assertEqual(trainVects.shape[0], len(trainRecords))
        self.assertEqual(testVects.shape[0], len(testRecords))

if __name__ == '__main__':
    unittest.main()