'''
Main module of the package/vectorise package to be used in package/base.

Classes:

    Vectorise

Functions:

    None

Misc Variables:

    None

Exceptions:

    NoLATechniquesException
    NoTokeniserException
    TokeniserException
    PreLAException
    TokenLevelException
    TextLevelException
    CorpusLevelException
'''
from . import base as b
from . import constants as c
from . import nltkvectorise as n
from scipy import sparse
from scipy.sparse import hstack
from .. import exceptions as e

class Vectorise:
    '''
    A class to be consturcted in package/base to vectorise records.

    ...

    Attributes
    ----------
    tokeniser : str
        The name of the tokeniser to use.
    preLAChanges : list
        A list of the names of pre LA changes to use.
    tokenLevelLA : list
        A list of the names of token level LA techniques to use.
    textLevelLA : list
        A list of the names of text level LA techniques to use.
    corpusLevelLA : str
        The name of the corpus level LA technique to use.
    textIndices : list
        A list of indices of free text fields in a record.

    Methods
    -------
    buildVector(str) -> list
        Creates a vector, of consistent length, representing some input text.
    recordToVector(list) -> list
        Creates a vector, of consistent length, representing some input record.
    vectorise(list) -> list
        Vectorises the input training and testing data.
    vectoriseSingle(list) -> sparse.crs_matrix
        Vectorises a single record after the algorithm has been trained.
    vectoriseList(list)
        Converts a list of records into a list of vectors.
    setTextIndices(list)
        Changes the textIndices attribute.
    '''

    def __init__(self, 
                 tokeniser : str, 
                 preLAChanges : list, 
                 tokenLevelLA : list, 
                 textLevelLA : list,
                 corpusLevelLA : str,
                 textIndices : list):
        '''
        Checks inputs are valid and constructs attributes for Vectorise object.

        Parameters
        ----------
        tokeniser : str
            The name of the tokeniser to use.
        preLAChanges : list
            A list of the names of pre LA Changes to use.
        tokenLevelLA : list
            A list of the names of token level LA techniques to use.
        textLevelLA : list
            A list of the names of text level LA techniques to use.
        corpusLevelLA : str
            The name of the corpus level LA technique to use.
        textIndicies : list
            List of indicies of the text fields to be processed.
        '''
        if tokenLevelLA == [] and textLevelLA == [] and corpusLevelLA == '':
            raise e.NoLATechniquesException(
                'Must have at least one token, text or corpus level LA '
                'technique level LA technique to construct a vector.'
                )
        if tokenLevelLA != [] and (tokeniser == ''):
            raise e.NoTokeniserException(
                'Cannot use token level techniques without a tokeniser.'
                )
        if tokeniser not in c.TOKENISER_NAMES:
            raise e.TokeniserException(
                f'Tokensier must be one of {c.TOKENISER_NAMES}.'
                )
        for preLA in preLAChanges:
            if preLA not in c.PRE_LA_CHANGES:
                raise e.PreLAException(
                    f'{preLA} is not in {c.PRE_LA_CHANGES}.'
                    )
        for tokenLev in tokenLevelLA:
            if tokenLev not in c.TOKEN_LEVEL:
                raise e.TokenLevelException(
                    f'{tokenLev} is not in {c.TOKEN_LEVEL}.'
                    )
        for textLev in textLevelLA:
            if textLev not in c.TEXT_LEVEL:
                raise e.TextLevelException(
                    f'{textLev} is not in {c.TEXT_LEVEL}.'
                    )
        if corpusLevelLA not in c.CORPUS_LEVEL:
            raise e.CorpusLevelException(
                f'{corpusLevelLA} is not in {c.CORPUS_LEVEL}.'
                )
        self.tokeniser = tokeniser
        self.preLAChanges = preLAChanges
        self.tokenLevelLA = tokenLevelLA
        self.textLevelLA = textLevelLA
        self.corpusLevelLA = corpusLevelLA
        self.textIndices = textIndices

    def buildVector(self, 
                    text : str) -> list:
        '''
        Creates a vector, of consistent length, representing some input text.

        Parameters
        ----------
        text : str
            The text to be represented as a vector.
        
        Returns
        -------
        vector : list
            The vector representing the input text.
        '''
        if 'REMOVE_STOPWORDS' in self.preLAChanges:
            text = n.stopwordRemoval(text)
        if 'STEMMING' in self.preLAChanges:
            text = n.stemming(text)
        
        match self.tokeniser:
            case 'WORD_TOKENISER':
                tokens = n.wordTokeniser(text)
            case 'PUNC_TOKENISER':
               tokens = n.puncTokeniser(text)
            case 'TWEET_TOKENISER':
                tokens = n.tweetTokeniser(text)
        
        vector = []
        if 'POS_TAG' in self.tokenLevelLA:
            vector += n.posTag(tokens)

        if 'KEYWORDS' in self.textLevelLA:
            vector = vector + b.keyWordCheck(text)
        if 'ASCII_CONVERSION' in self.textLevelLA:
            vector += b.asciiConversion(text)

        return vector
    
    def recordToVector(self, 
                       record : list) -> list:
        '''
        Creates a vector, of consistent length, representing some input record.

        Parameters
        ----------
        record : list
            The record to be represented as a vector.
        
        Returns
        -------
        vector : list
            The vector representing the input record.
        '''
        vector = []
        for index in self.textIndices:
            vector = vector + self.buildVector(str(record[index]))
        return vector

    def vectorise(self, 
                  trainRecords : list, 
                  testRecords : list) -> tuple[sparse.csr_matrix, sparse.csr_matrix]:
        '''
        Vectorises the input training and testing data.

        Parameters
        ----------
        trainRecords : list
            The list of training records to be vectorised.
        testRecords : list
            The list of testing records to be vectorised.

        Returns
        -------
        outTrainVecs : csr_matrix
            The vectorised training records.
        outTestVectors : crs_matrix
            The vectorised testing records.
        '''
        self.vectoriser = None
        if 'BAG_OF_WORDS_C' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.bagOfWordsC(
                trainRecords, 
                testRecords,
                self.textIndices
                )
        if 'MOD_BAG_OF_WORDS_C' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.modBagOfWordsC(
                trainRecords, 
                testRecords,
                self.textIndices
                )
        if 'BAG_OF_WORDS_F' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.bagOfWordsF(
                trainRecords, 
                testRecords,
                self.textIndices
                )
        if 'MOD_BAG_OF_WORDS_F' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.modBagOfWordsF(
                trainRecords, 
                testRecords,
                self.textIndices
                )
        if 'BAG_OF_WORDS_H' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.bagOfWordsH(
                trainRecords, 
                testRecords,
                self.textIndices
                )
        if 'MOD_BAG_OF_WORDS_H' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.modBagOfWordsH(
                trainRecords, 
                testRecords,
                self.textIndices
                )
        outTrainVecs = sparse.csr_matrix(
            [self.recordToVector(record) for record in trainRecords]
            )
        outTestVecs = sparse.csr_matrix(
            [self.recordToVector(record) for record in testRecords]
            )

        if self.corpusLevelLA != '':
            outTrainVecs = hstack((trainVecs, outTrainVecs))
            outTestVecs = hstack((testVecs, outTestVecs))
 
        return (outTrainVecs, outTestVecs)
    
    def vectoriseSingle(self, 
                        record : list):
        '''
        Vectorises a single record after the algorithm has been trained.

        Parameters
        ----------
        record : list
            The record to be vectorised

        Returns
        -------
        vectorList : sparse.crs_matrix
            A sparse matrix containing a single vector. 
        '''
        text = n.recordToCorpusText(record, self.textIndices)
        if self.corpusLevelLA in ['MOD_BAG_OF_WORDS_C', 
                                  'MOD_BAG_OF_WORDS_F', 
                                  'MOD_BAG_OF_WORDS_H']:
            text = n.prepareTexts([text])[0]
        vectPart1 = self.vectoriser.transform([text])
        vectPart2 = sparse.csr_matrix([self.recordToVector(record)])
        if self.corpusLevelLA == '':
            vectorList = vectPart2
        else:
            vectorList = hstack((vectPart1, vectPart2))
        
        return vectorList

    def vectoriseList(self, records : list):
        '''
        Converts a list of records into a list of vectors.

        Parameters
        ----------
        records : list
            The list of records to be converted.

        Returns
        -------
        vectorList : list
            The list of vectors corresponding to the input records.
        '''
        texts = [n.recordToCorpusText(rec, self.textIndices) for rec in records]
        if self.corpusLevelLA in ['MOD_BAG_OF_WORDS_C', 
                                  'MOD_BAG_OF_WORDS_F', 
                                  'MOD_BAG_OF_WORDS_H']:
            texts = n.prepareTexts(texts)
        vectPart1 = self.vectoriser.transform(texts)
        vectPart2 = sparse.csr_matrix([self.recordToVector(rec) for rec in records])
        if self.corpusLevelLA == '':
            vectorList = vectPart2
        else:
            vectorList = hstack((vectPart1, vectPart2))
        
        return vectorList
    
    def setTextIndices(self, newTextIndices : list):
        '''
        Changes the textIndices attribute.

        Parameters
        ----------
        newTextIndices : list
            The new value for the textIndices attribute.

        Returns
        -------
        None
        '''
        self.textIndices = newTextIndices