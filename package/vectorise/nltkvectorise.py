'''
Helper functions using NLTK package to support package/vectorise/vectorise.py.

Classes:

    None

Functions:

    wordTokeniser(str) -> list
    puncTokeniser(str) -> list
    tweetTokeniser(str) -> list
    stopwordRemoval(str) -> str
    stemming(str) -> str
    posTag(list) -> list
    bagOfWordsC(list, list, tuple) -> 
        tuple[sparse.csr_matrix, sparse.csr_matrix, CountVectorizer]
    modBagOfWordsC(list, list, tuple) -> 
        tuple[sparse.csr_matrix, sparse.csr_matrix, CountVectorizer]
    bagOfWordsF(list, list, tuple) -> 
        tuple[sparse.csr_matrix, sparse.csr_matrix, TfidfVectorizer]
    modBagOfWordsF(list, list, tuple) -> 
        tuple[sparse.csr_matrix, sparse.csr_matrix, TfidfVectorizer]
    tagToIndex(tuple) -> int
    prepareTexts(list) -> list
    removeStop(list) -> list
    stem(list) -> list
    reconstruct(list) -> str
    bagOfWords(list, list, str, bool, tuple) -> 
        tuple[sparse.csr_matrix, 
              sparse.csr_matrix, 
              Union[CountVectorizer, 
                    TfidfVectorizer]]
    recordToCorpusText(list) -> str

Misc variables:

    None

Exceptions:

    None
'''
from . import constants as vc
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import word_tokenize 
from nltk.tokenize import TweetTokenizer
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import Union

def wordTokeniser(text : str) -> list:
    '''
    Tokenises a text using NLTK's word tokeniser.

    Parameters
    ----------
    text : str
        The text to be tokenised.

    Returns
    -------
    tokens : list
        A list of tokens.
    '''
    tokens = word_tokenize(str(text))
    return tokens

def puncTokeniser(text  : str) -> list:
    '''
    Tokenises a text using NLTK's punctuation tokeniser.

    Parameters
    ----------
    text : str
        The text to be tokenised.

    Returns
    -------
    tokens : list
        A list of tokens.
    '''
    tokens = wordpunct_tokenize(str(text))
    return tokens

def tweetTokeniser(text : str) -> list:
    '''
    Tokenises a text using NLTK's tweet tokeniser.

    Parameters
    ----------
    text : str
        The text to be tokenised.

    Returns
    -------
    tokens : list
        A list of tokens.
    '''
    tknzr = TweetTokenizer()
    tokens = tknzr.tokenize(str(text))
    return tokens

def stopwordRemoval(text : str) -> str:
    '''
    Removes the stopwords from a piece of text.

    Parameters
    ----------
    text : str
        The text to have the stopwords removed from.

    Returns
    -------
    newText : str
        The input text with stopwords removed.
    '''
    newText = reconstruct(removeStop(word_tokenize(text)))
    return newText

def stemming(text : str) -> str:
    '''
    Tokenises, stems and reconstructs an input text.

    Parameters
    ----------
    text : str
        The text to be stemmed.

    Returns
    -------
    newText : str
        The text tokenised, stemmed and reconstructed.
    '''
    tokens = word_tokenize(text)
    tokens = stem(tokens)
    newText = reconstruct(tokens)
    return newText

def posTag(tokens : list) -> list:
    '''
    Outputs a list of indices associated with the POS tags of each token.

    Parameters
    ----------
    tokens : list
        The tokens to extract the POS tags of.
    
    Returns
    -------
    vector : list
        List of indices associated with the POS tags of each token.
    '''
    tags = pos_tag(tokens)
    vector = [tagToIndex(tag) for tag in tags]
    while len(vector) < vc.MAX_TOKENS:
        vector += [-2] 
    return vector

def bagOfWordsC(trainRecords : list, 
                testRecords : list,
                ngramRange : tuple) -> tuple[sparse.csr_matrix, 
                                             sparse.csr_matrix, 
                                             CountVectorizer]:
    '''
    Applies bag of words pipeline without modification using count vectorising.

    Parameters
    ----------
    trainRecords : list
        The training records provided to the bag of words pipeline.
    testRecords : list
        The testing records provided to the bag of words pipeline.
    ngramRange : tuple
        Lower and upper bound for n-gram sizes (inclusive).

    Returns
    -------
    trainVectors : sparse.csr_matrix
        The training vectors returned from the bag of words pipeline.
    testVectors : sparse.csr_matrix
        The testing vectors returned from the bag of words pipeline.
    vectoriser : CountVectoriser
        Vectoriser to convert text to a bag of words vector.
    '''
    trainVecotrs, testVectors, vectoriser = bagOfWords(trainRecords, 
                                           testRecords, 
                                           'COUNT', 
                                           False,
                                           ngramRange)
    return (trainVecotrs, testVectors, vectoriser)

def modBagOfWordsC(trainRecords : list, 
                   testRecords : list,
                   ngramRange : tuple) -> tuple[sparse.csr_matrix, 
                                                sparse.csr_matrix, 
                                                CountVectorizer]:
    '''
    Applies bag of words pipeline with modification using count vectorising.

    Parameters
    ----------
    trainRecords : list
        The training records provided to the bag of words pipeline.
    testRecords : list
        The testing records provided to the bag of words pipeline.
    ngramRange : tuple
        Lower and upper bound for n-gram sizes (inclusive).

    Returns
    -------
    trainVectors : sparse.csr_matrix
        The training vectors returned from the bag of words pipeline.
    testVectors : sparse.csr_matrix
        The testing vectors returned from the bag of words pipeline.
    vectoriser : CountVectoriser
        Vectoriser to convert text to a bag of words vector.
    '''
    trainVecotrs, testVectors, vectoriser = bagOfWords(trainRecords, 
                                           testRecords, 
                                           'COUNT', 
                                           True,
                                           ngramRange)
    return (trainVecotrs, testVectors, vectoriser)

def bagOfWordsF(trainRecords : list, 
                testRecords : list,
                ngramRange : tuple) -> tuple[sparse.csr_matrix, 
                                             sparse.csr_matrix, 
                                             TfidfVectorizer]:
    '''
    Applies bag of words pipeline without modification using tfidf vectorising.

    Parameters
    ----------
    trainRecords : list
        The training records provided to the bag of words pipeline.
    testRecords : list
        The testing records provided to the bag of words pipeline.
    ngramRange : tuple
        Lower and upper bound for n-gram sizes (inclusive).

    Returns
    -------
    trainVectors : sparse.csr_matrix
        The training vectors returned from the bag of words pipeline.
    testVectors : sparse.csr_matrix
        The testing vectors returned from the bag of words pipeline.
    vectoriser : TfidfVectoriser
        Vectoriser to convert text to a bag of words vector.
    '''
    trainVecotrs, testVectors, vectoriser = bagOfWords(trainRecords, 
                                           testRecords, 
                                           'FREQ', 
                                           False,
                                           ngramRange)
    return (trainVecotrs, testVectors, vectoriser)

def modBagOfWordsF(trainRecords : list, 
                   testRecords : list,
                   ngramRange : tuple) -> tuple[sparse.csr_matrix, 
                                                sparse.csr_matrix, 
                                                TfidfVectorizer]:
    '''
    Applies bag of words pipeline with modification using tfidf vectorising.

    Parameters
    ----------
    trainRecords : list
        The training records provided to the bag of words pipeline.
    testRecords : list
        The testing records provided to the bag of words pipeline.
    ngramRange : tuple
        Lower and upper bound for n-gram sizes (inclusive).

    Returns
    -------
    trainVectors : sparse.csr_matrix
        The training vectors returned from the bag of words pipeline.
    testVectors : sparse.csr_matrix
        The testing vectors returned from the bag of words pipeline.
    vectoriser : TfidfVectoriser
        Vectoriser to convert text to a bag of words vector.
    '''
    trainVecotrs, testVectors, vectoriser = bagOfWords(trainRecords, 
                                           testRecords, 
                                           'FREQ', 
                                           True,
                                           ngramRange)
    return (trainVecotrs, testVectors, vectoriser)

def tagToIndex(tag : tuple[str, str]) -> int:
    '''
    Converts a (token, POS tag) tuples into a POS tag index.

    Parameters
    ----------
    tag : tuple
        The (token, POS tag) tuple to be converted.

    Returns
    -------
    index : int
        The index associated with the POS tag.
    '''
    pos = tag[1]
    index = vc.UNIVERSAL_TAGS.get(pos)
    if index == None:
        index = -1
    return index

def prepareTexts(texts : list) -> list:
    '''
    Tokenises, removes stopwords and stems an input text.

    Parameters
    ----------
    texts : list
        The text to be modified.

    Returns
    -------
    newText : list
        The modified text.
    '''
    newText = (
        [reconstruct(stem(removeStop(word_tokenize(text)))) for text in texts]
    )
    return newText

def removeStop(tokens : list) -> list:
    '''
    Removes stopwords from a list of tokens.

    Parameters
    ----------
    tokens : list
        The list of tokens to remove the stopwords from.
    
    Returns
    -------
    newTokens : list
        The list of tokens with the stopwords removed.
    '''
    newTokens = [token for token in tokens if token.lower() not in vc.STOPWORDS]
    return newTokens

def stem(tokens : list) -> list:
    '''
    Stems a list of tokens.

    Parameters
    ----------
    tokens : list
        The tokens to be stemmed.

    Returns
    -------
    newTokens : list
        The stemmed tokens.
    '''
    newTokens = [vc.STEMMER.stem(token) for token in tokens]
    return newTokens

def reconstruct(tokens : list) -> str:
    '''
    Takes a list of tokens and converts them into a text.

    Parameters
    ----------
    tokens : list
        The tokens to be converted.

    Returns
    -------
    string : str
        The text constructed by combining the tokens.
    '''
    string = ''
    for token in tokens:
        string += token + ' '
    return string

def bagOfWords(trainRecords : list,
               testRecords : list,
               vect : str, 
               mod : bool,
               ngramRange : tuple) -> tuple[sparse.csr_matrix, 
                                            sparse.csr_matrix, 
                                            Union[CountVectorizer, 
                                                  TfidfVectorizer]]:
    '''
    Applies a customised bag of words pipeline to a set of training and testing
    records.

    Parameters
    ----------
    trainRecords : list
        A list of training records.
    testRecords : list
        A list of testing records.
    vect : str
        A choice of vectoriser, either "COUNT" or "FREQ".
    mod : bool
        Whether to modifiy the text before the pipeline or not.
    ngramRange : tuple
        Lower and upper bound for n-gram sizes (inclusive).

    Returns
    -------
    trainVectors : sparse.csr_matrix
        The training vectors.
    trainVectors : sparse.csr_matrix
        The testing vectors.
    vectoriser : Union[CountVectorizer, TfidfVectorizer]
        Vectoriser to convert text to bag of words vector.
    '''
    trainText = [
        recordToCorpusText(record) for record in trainRecords]
    testText = [
        recordToCorpusText(record) for record in testRecords]
    corpus = trainText + testText
    if mod:
        corpus = prepareTexts(corpus)
    if vect == 'COUNT':
        vectoriser = CountVectorizer(ngram_range= ngramRange)
        vectorized_corpus = vectoriser.fit_transform(corpus)
    if vect == 'FREQ':
        vectoriser = TfidfVectorizer(ngram_range= ngramRange)
        vectorized_corpus = vectoriser.fit_transform(corpus)
    
    trainVectors = vectorized_corpus[0:len(trainRecords),:]
    testVectors = vectorized_corpus[len(trainRecords):len(corpus),:]

    return (trainVectors, testVectors, vectoriser)

def recordToCorpusText(record : list) -> str:
    '''
    Converts a record into one string containing all of the relavant text.
    Helper function for bagOfWords.

    Parameters
    ----------
    record : list
        The record to extract corpus text from.

    Returns
    -------
    text : str
        All of the relavant text in record in one string.
    '''
    text = ''
    for field in record[0: len(record)]:
        text = text + str(field)
    return text