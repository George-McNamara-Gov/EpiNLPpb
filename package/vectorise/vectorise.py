'''
Main module of the package/vectorise package to be used in package/base.py.

Classes:

    Vectorise

Functions:

    None

Misc Variables:

    None

Exceptions:

    VectoriseException
    TokeniserException
    PreLAException
    TokenLevelException
    TextLevelException
    CorpusLevelException
    NGramException
'''
from . import base as b
from . import constants as c
from . import nltkvectorise as n
from scipy import sparse
from scipy.sparse import hstack
from .. import exceptions as e

class Vectorise:
    '''
    A class to be consturcted in package/base.py to vectorise records.

    ...

    Attributes
    ----------
    Constructed by running the initialise() method:
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
    ngramRange : tuple
        Lower and upper bound for n-gram sizes (inclusive).
    vectoriser : Union[CountVectorizer, TfidfVectorizer]
        The bag-of-words vectoriser.

    Methods
    -------
    initialise(str, list, list, list, str, tuple)
        Checks constructor inputs and creates attributes.
    buildVector(str) -> list
        Creates a vector, of consistent length, representing some input text.
    recordToVector(list) -> list
        Creates a vector, of consistent length, representing some input record.
    vectorise(list, list) -> tuple[sparse.csr_matrix, sparse.csr_matrix]
        Vectorises the input training and testing data.
    vectoriseList(list) -> sparse.csr_matrix
        Converts a list of records into a list of vectors. Can only
        be used after the vectorise() method has been run.
    '''

    def __init__(self,
                 arg_dict : dict = None, 
                 tokeniser : str = '',
                 preLAChanges : list = [], 
                 tokenLevelLA : list = [], 
                 textLevelLA : list = [],
                 corpusLevelLA : str = '',
                 ngramRange : tuple = (1, 1)):
        '''
        Passes inputs from either arg_dict or keyword arguments.

        Parameters
        ----------
        arg_dict : dict
            A dictionary containing constructor arguments.
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
        ngramRange : tuple
            Lower and upper bound for n-gram sizes (inclusive).
        '''
        if arg_dict is not None:
            if not isinstance(arg_dict, dict):
                raise e.VectoriseException(
                    'arg_dict must be a dictionary.'
                )
            
            if 'tokeniser' in arg_dict:
                tokeniser = arg_dict['tokeniser']
            if 'preLAChanges' in arg_dict:
                preLAChanges = arg_dict['preLAChanges']
            if 'tokenLevelLA' in arg_dict:
                tokenLevelLA = arg_dict['tokenLevelLA']
            if 'textLevelLA' in arg_dict:
                textLevelLA = arg_dict['textLevelLA']
            if 'corpusLevelLA' in arg_dict:
                corpusLevelLA = arg_dict['corpusLevelLA']
            if 'ngramRange' in arg_dict:
                ngramRange = arg_dict['ngramRange']
                
        self.initialise(tokeniser,
                        preLAChanges,
                        tokenLevelLA,
                        textLevelLA,
                        corpusLevelLA,
                        ngramRange)

    def initialise(self,
                   tokeniser : str = '', 
                   preLAChanges : list = [], 
                   tokenLevelLA : list = [], 
                   textLevelLA : list = [],
                   corpusLevelLA : str = '',
                   ngramRange : tuple = (1, 1)):
        '''
        Checks constructor inputs and creates attributes.

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
        ngramRange : tuple
            Lower and upper bound for n-gram sizes (inclusive).

        Returns
        -------
        None
        '''
        if not isinstance(tokeniser, str):
            raise e.TokeniserException(
                'tokeniser must be a string.'
            )
        if not isinstance(preLAChanges, list):
            raise e.PreLAException(
                'preLAChanges must be a list.'
            )
        if not isinstance(tokenLevelLA, list):
            raise e.TokenLevelException(
                'tokenLevelLA must be a list.'
            )
        if not isinstance(textLevelLA, list):
            raise e.TextLevelException(
                'textLevelLA must be a list.'
            )
        if not isinstance(corpusLevelLA, str):
            raise e.CorpusLevelException(
                'corpusLevelLA must be a string.'
            )
        if not isinstance(ngramRange, tuple):
            raise e.NGramException(
                'ngramRange must be a tuple.'
            )
        
        if tokenLevelLA == [] and textLevelLA == [] and corpusLevelLA == '':
            raise e.PreLAException(
                'Must have at least one token, text or corpus level LA '
                'technique level LA technique to construct a vector.'
                )
        if tokenLevelLA != [] and (tokeniser == ''):
            raise e.TokeniserException(
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
        if not isinstance(ngramRange[0], int):
            raise e.NGramException(
                'ngramRange lower bound must be an int.'
            )
        if not isinstance(ngramRange[1], int):
            raise e.NGramException(
                'ngramRange upper bound must be an int.'
            )
        if ngramRange[0] <= 0:
            raise e.NGramException(
                'ngramRange lower bound must be positive.'
            )
        if ngramRange[1] < ngramRange[0]:
            raise e.NGramException(
                'ngramRange upper bound must be greater than or equal to ',
                'ngramRange lower bound.'
            )
        self.tokeniser = tokeniser
        self.preLAChanges = preLAChanges
        self.tokenLevelLA = tokenLevelLA
        self.textLevelLA = textLevelLA
        self.corpusLevelLA = corpusLevelLA
        self.ngramRange = ngramRange
        self.vectoriser = None

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
        for text in record[0: len(record)]:
            vector = vector + self.buildVector(str(text))
        return vector

    def vectorise(self, 
                  trainRecords : list, 
                  testRecords : list) -> tuple[sparse.csr_matrix, 
                                               sparse.csr_matrix]:
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
        outTrainVecs : sparse.csr_matrix
            The vectorised training records.
        outTestVectors : sparse.crs_matrix
            The vectorised testing records.
        '''
        if 'BAG_OF_WORDS_C' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.bagOfWordsC(
                trainRecords, 
                testRecords,
                self.ngramRange
                )
        if 'MOD_BAG_OF_WORDS_C' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.modBagOfWordsC(
                trainRecords, 
                testRecords,
                self.ngramRange
                )
        if 'BAG_OF_WORDS_F' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.bagOfWordsF(
                trainRecords, 
                testRecords,
                self.ngramRange
                )
        if 'MOD_BAG_OF_WORDS_F' == self.corpusLevelLA:
            trainVecs, testVecs, self.vectoriser = n.modBagOfWordsF(
                trainRecords, 
                testRecords,
                self.ngramRange
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
    
    def vectoriseList(self, records : list) -> sparse.csr_matrix:
        '''
        Converts a list of records into a list of vectors. Can only
        be used after the vectorise() method has been run.

        Parameters
        ----------
        records : list
            The list of records to be converted.

        Returns
        -------
        vectorList : sparse.csr_matrix
            The list of vectors corresponding to the input records.
        '''
        texts = [n.recordToCorpusText(rec) for rec in records]
        if self.corpusLevelLA in ['MOD_BAG_OF_WORDS_C', 'MOD_BAG_OF_WORDS_F']:
            texts = n.prepareTexts(texts)
        vectPart1 = self.vectoriser.transform(texts)
        vectPart2 = sparse.csr_matrix([self.recordToVector(rec) for rec in records])
        if self.corpusLevelLA == '':
            vectorList = vectPart2
        else:
            vectorList = hstack((vectPart1, vectPart2))
        
        return vectorList