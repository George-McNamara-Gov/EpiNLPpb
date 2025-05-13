'''
Test module for the package/vectorise/nltkvectorise.py module.

Classes:

    TestNLTKVectorise

Functions:

    None

Misc Variables:

    None

Exceptions:

    None
'''
import unittest

from ..package.vectorise import nltkvectorise as nv
from ..package.vectorise import constants as c

class TestNLTKVectorise(unittest.TestCase):
    '''
    A class of tests to check the operation of the 
    package/vectorise/nltkvectorise.py module.

    Attributes
    ----------
    None

    Methods
    -------
    test_wordTokeniser()
        Tests that word tokeniser behaves as expected.
    test_puncTokeniser()
        Tests that punc tokeniser behaves as expected.
    test_tweetTokeniser()
        Tests that tweet tokeniser behaves as expected.
    test_stopwordRemoval()
        Tests that stopword removal behaves as expected.
    test_stemming()
        Tests that stemming behaves as expected.
    test_posTag()
        Tests that POS tag behaves as expected.
    test_tagToIndex()
        Tests that tag to index behaves as expected.
    test_prepareTexts()
        Tests that prepareTexts behaves as expected.
    test_removeStop()
        Tests that removeStop behaves as expected.
    test_stem()
        Tests that stem behaves as expected.
    test_reconstruct()
        Tests that reconstruct behaves as expected.
    test_bagOfWords()
        Tests that bagOfWords behaves as expected.
    '''
     
    def test_wordTokeniser(self):
        text = 'The-quick brown, fox "jumps" over the lazy dog.'
        tokens = nv.wordTokeniser(text)
        self.assertEqual(len(tokens), 12)
        self.assertEqual(tokens[0], 'The-quick')
        self.assertEqual(tokens[5], 'jumps')
        self.assertEqual(tokens[11],'.')

    def test_puncTokeniser(self):
        text = 'The-quick brown, fox "jumps" over the lazy dog.'
        tokens = nv.puncTokeniser(text)
        self.assertEqual(len(tokens), 14)
        self.assertEqual(tokens[0], 'The')
        self.assertEqual(tokens[5], 'fox')
        self.assertEqual(tokens[13],'.')

    def test_tweetTokeniser(self):
        text = 'The-quick brown, fox "jumps" over the lazy dog.'
        tokens = nv.puncTokeniser(text)
        self.assertEqual(len(tokens), 14)
        self.assertEqual(tokens[0], 'The')
        self.assertEqual(tokens[4], ',')
        self.assertEqual(tokens[13],'.')

    def test_stopwordRemoval(self):
        text = 'The quick brown fox jumps over the lazy dog'
        removedText = 'quick brown fox jumps lazy dog '
        self.assertEqual(nv.stopwordRemoval(text), removedText)
        text = 'The it and was of to'
        self.assertEqual(nv.stopwordRemoval(text), '')
        text = 'The it and was of to andrew'
        self.assertEqual(nv.stopwordRemoval(text), 'andrew ')

    def test_stemming(self):
        text1 = 'The quick brown fox jumps over the lazy dog'
        stemmed1 = 'the quick brown fox jump over the lazi dog '
        text2 = 'Peter piper picked a peck of pickled peppers'
        stemmed2 = 'peter piper pick a peck of pickl pepper '
        self.assertEqual(nv.stemming(text1), stemmed1)
        self.assertEqual(nv.stemming(text2), stemmed2)

    def test_posTag(self):
        text = 'The-quick brown, fox "jumps" over the lazy dog.'
        tokens = nv.wordTokeniser(text)
        tagVector1 = nv.posTag(tokens)
        text = 'The-quick brown, fox "jumps".'
        tokens = nv.wordTokeniser(text)
        tagVector2 = nv.posTag(tokens)
        self.assertEqual(len(tagVector1), len(tagVector2))
        self.assertEqual(tagVector1[0],tagVector2[0])
        self.assertEqual(tagVector1[2],tagVector2[2])
        self.assertNotEqual(tagVector1[7],tagVector2[7])
        self.assertEqual(len(tagVector1), c.MAX_TOKENS)
        self.assertEqual(tagVector1[1],10)
        self.assertEqual(tagVector1[6],-1)
        self.assertEqual(tagVector1[9],5)
        self.assertEqual(tagVector1[20],-2)

    def test_tagToIndex(self):
        self.assertEqual(nv.tagToIndex(('word','CC')),0)
        self.assertEqual(nv.tagToIndex(('','CC')),0)
        self.assertEqual(nv.tagToIndex(('word','JJ')),5)
        self.assertEqual(nv.tagToIndex(('word','.')),-1)
        self.assertEqual(nv.tagToIndex(('word','?')),-1)
        self.assertEqual(nv.tagToIndex(('word','NOK')),-1)

    def test_prepareTexts(self):
        texts = ['The quick brown',
                 'fox jumps over',
                 'the lazy dog.']
        prepTexts = ['quick brown ',
                     'fox jump ',
                     'lazi dog . ']
        self.assertEqual(len(texts), len(nv.prepareTexts(texts)))
        self.assertEqual(nv.prepareTexts(texts), prepTexts)
        self.assertEqual(nv.prepareTexts(['']),[''])

    def test_removeStop(self):
        tokens1 = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the',
                    'lazy', 'dog']
        remstop1 = ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog']
        tokens2 = ['She', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
        remstop2 = ['sells', 'sea', 'shells', 'sea', 'shore']
        self.assertEqual(nv.removeStop(tokens1), remstop1)
        self.assertEqual(nv.removeStop(tokens2), remstop2)

    def test_stem(self):
       tokens = ['running', 'jumping', 'leaping']
       self.assertEqual(len(tokens), len(nv.stem(tokens)))
       self.assertEqual(['run', 'jump', 'leap'], nv.stem(tokens))

    def test_reconstruct(self):
        tokens1 = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the',
                    'lazy', 'dog']
        recon1 = 'The quick brown fox jumps over the lazy dog '
        tokens2 = ['She', 'sells', '', 'sea', '.', 'shells']
        recon2 = 'She sells  sea . shells '
        tokens3 = []
        recon3 = ''
        tokens4 = ['']
        recon4 = ' '
        self.assertEqual(nv.reconstruct(tokens1), recon1)
        self.assertEqual(nv.reconstruct(tokens2), recon2)
        self.assertEqual(nv.reconstruct(tokens3), recon3)
        self.assertEqual(nv.reconstruct(tokens4), recon4)

    def test_bagOfWords(self):
        trainRecords = [[0,0,0,0,'','',0],
                        [0,0,0,0,
                         'The quick brown','fox jumps over the lazy dog',0],
                        [0,0,0,0,'She sells sea','shells by the sea shore',0]]
        testRecords = [[0,0,0,0,
                        'Peter piper picked a peck','of pickled peppers',0],
                       [0,0,0,0,'Red leather','yellow leather',0]]
        trainVecs, testVecs, _ = nv.bagOfWords(trainRecords, testRecords, 
                                               'COUNT', True, [4,5])
        self.assertEqual(len(trainRecords), trainVecs.shape[0])
        self.assertEqual(len(testRecords), testVecs.shape[0])

        trainVecs, testVecs, _ = nv.bagOfWords(trainRecords, testRecords, 
                                               'COUNT', False, [4,5])
        self.assertEqual(len(trainRecords), trainVecs.shape[0])
        self.assertEqual(len(testRecords), testVecs.shape[0])

        trainVecs, testVecs, _ = nv.bagOfWords(trainRecords, testRecords, 
                                               'FREQ', True, [4,5])
        self.assertEqual(len(trainRecords), trainVecs.shape[0])
        self.assertEqual(len(testRecords), testVecs.shape[0])

        trainVecs, testVecs, _ = nv.bagOfWords(trainRecords, testRecords, 
                                               'FREQ', False, [4,5])
        self.assertEqual(len(trainRecords), trainVecs.shape[0])
        self.assertEqual(len(testRecords), testVecs.shape[0])
        
        trainVecs, testVecs, _ = nv.bagOfWords(trainRecords, testRecords, 
                                               'HASH', True, [4,5])
        self.assertEqual(len(trainRecords), trainVecs.shape[0])
        self.assertEqual(len(testRecords), testVecs.shape[0])

        trainVecs, testVecs, _ = nv.bagOfWords(trainRecords, testRecords, 
                                               'HASH', False, [4,5])
        self.assertEqual(len(trainRecords), trainVecs.shape[0])
        self.assertEqual(len(testRecords), testVecs.shape[0])

if __name__ == '__main__':
    unittest.main()