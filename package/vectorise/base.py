'''
Helper functions to support pakage/vectorise.vectorise.py

Classes:

    None

Functions:

    keywordCheck(str) -> list
    asciiConversion(str) -> list
    wordCheck(list, str) -> bool

Misc variables:

    None

Exceptions:

    None
'''
from . import constants as c

def keyWordCheck(text: str) -> list:
    '''
    Produces a vector detailing which keywords are present in the given text.

    Parameters
    ----------
    text : str
        The text to search for keywords in.

    Returns
    -------
    check : list
        A list of 0s and 1s corresponding to whether keywords are present.
    '''
    text = str(text).lower()
    check = [int(wordCheck(words,text)) for words in c.KEYWORDS]
    return check

def asciiConversion(text : str) -> list:
    '''
    Converts the text into a list of ascii codes for each character.

    Parameters
    ----------
    text : str
        The text to be converted into ascii characters.

    Returns
    -------
    codes : list
        The list of ascii codes associated with each character.
    '''
    chars = list(str(text))
    codes = [ord(char) for char in chars]
    while len(codes) < c.MAX_CHARS:
        codes.append(-1)
    return codes

def wordCheck(listOfWords: list, 
              string: str) -> bool:
    '''
    Determines if all the words in a list are present in a string.

    Parameters
    ----------
    listOfWords : list
        The words to determine the presence of.
    string : str
        The string to check for the presence of words.

    Returns
    -------
    output : bool
        Whether or not all words from listOfWords are present in string.
    '''
    for word in listOfWords:
        if word not in string:
            return False
    return True