'''
Constants to support package/vectorise/vectorise.py and 
package/vectorise/base.py.

Classes:

    None

Functions:

    None

Misc variables:

    TOEKNISER_NAMES : list
        A list of names of available tokenisers.
    PRE_LA_CHANGES : list
        A list of the names of available pre-LA changes.
    TOKEN_LEVEL : list(str)
        A list of the names of available token level LA techniques.
    TEXT_LEVEL : list
        A list of the names of available text level LA techniques.
    CORPUS_LEVEL : list
        A list of the names of available text level LA techniques.
    MAX_CHARS : int
        The maximum number of characters in a text field.
    MAX_TOKENS : int
        The maximum number of tokens in a text field.
    KEYWORDS : list
        A list of Paul's SSH keyword search items.
    STOPWORDS : set
        A set of stopwords.
    STEMMER : SnowballStemmer
        An NLTK stemmer.
    COUNTV : CountVectorizer
        An NLTK CountVectorizer to be used for the bag of words approach.
    FREQV : TfidfVectorizer
        An NLTK TfidfVectorizer to be used for the bag of words approach.
    HASHV : HashingVectorizer
        An NLTK HashingVectorizer to be used for the bag of words approach.
    UNIVERSAL_TAGS : dict
        A dictionary indexing the possible POS tags.

Exceptions:

    None
'''
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

TOKENISER_NAMES = ['',
                   'WORD_TOKENISER',
                   'PUNC_TOKENISER',
                   'TWEET_TOKENISER']
PRE_LA_CHANGES = ['REMOVE_STOPWORDS', 'STEMMING']
TOKEN_LEVEL = ['POS_TAG']
TEXT_LEVEL = ['KEYWORDS', 'ASCII_CONVERSION']
CORPUS_LEVEL = ['',
                'BAG_OF_WORDS_C', 
                'MOD_BAG_OF_WORDS_C', 
                'BAG_OF_WORDS_F', 
                'MOD_BAG_OF_WORDS_F',
                'BAG_OF_WORDS_H',
                'MOD_BAG_OF_WORDS_H']

MAX_CHARS = 1571
MAX_TOKENS = 225
KEYWORDS = [['suic'], ['self harm'], ['self-harm'], ['selfharm'], 
            [' self inflicted'], [' self-inflicted'], [' tsh '], 
            [' tosh '], ['tos'], [' dsh '], ['overdos'], [' od '], [' o/d '],
            [' od.'], [' gas self'], ['monox'], ['lacerat', 'self harm'], 
            [' hanging', 'self harm'], [' hang', 'self'], 
            [' strangle', 'self'], ['cutting', 'self harm']]

STOPWORDS = set(stopwords.words('english'))
STEMMER = SnowballStemmer('english')
COUNTV = CountVectorizer(ngram_range=(1,3))
FREQV = TfidfVectorizer(ngram_range=(1,3))
HASHV = HashingVectorizer(ngram_range=(1,3))
UNIVERSAL_TAGS = dict(CC = 0,
                      CD = 1,
                      DT = 2,
                      EX = 3,
                      IN = 4,
                      JJ = 5,
                      JJR = 6,
                      JJS = 7,
                      LS = 8,
                      MD = 9,
                      NN = 10,
                      NNP = 11,
                      NNS = 12,
                      PDT = 13,
                      POS = 14,
                      PRP = 15,
                      RB = 16,
                      RBR = 17,
                      RBS = 18,
                      RP = 19,
                      T0 = 20,
                      UH = 21,
                      VB = 22,
                      VBD = 23,
                      VBG = 24,
                      VBN = 25,
                      VBP = 26,
                      VBZ = 27,
                      WDT = 28,
                      WP = 29,
                      WRB = 30)