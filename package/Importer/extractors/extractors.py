'''
Contains classes and helper functions to be used in 
package/Importer/importer.py to extract data.

Classes:

    Extractor
    NewestBlock
    RandomBlock
    Uniform

Functions:

    indexSet(int, function) -> str
    splitter(list) -> tuple[list, list]

Misc variables:

    None

Exceptions:

    MoreDataThanRecordsException
'''
import random
from abc import ABC, abstractmethod
from collections import deque
from ... import exceptions as e

class Extractor(ABC):
    '''
    An abstract class used to create instances classes to extract data with 
    different sampling distributions.

    ...

    Attributes
    ---------
        None
    
    Methods
    -------
    extractData(list) -> tuple[list, list]
        An abstract method that returns specified data and leftover data.
    changeAmount(int)
        Changes the amount attribute.
    '''

    @abstractmethod
    def extract(self, 
                takeFrom: list) -> tuple[list, list]:
        '''
        An abstract method that returns specified data and leftover data.

        Parameters
        ----------
        takeFrom : list
            A list of records to extract data from.

        Returns
        ------
        specified : list
            The desired records from takeFrom.
        leftover : list
            All records in takeFrom which aren't in the specified data.
        '''
        specified = []
        leftover = []
        return (specified, leftover)

    def changeAmount(self, 
                     newAmount : int):
        '''
        Changes the amount attribute.

        Parameters
        ----------
        newAmount : int
            The new amount.

        Returns
        -------
        None
        '''
        self.amount = newAmount
 
class NewestBlock(Extractor):
    '''
    Can be used to extract the newest block of available records. Is an instance
    of the abstract Extractor class.

    ...

    Attributes
    ----------
    amount : int
        The number of records to extract.
    
    Methods
    -------
    extract(list) -> tuple[list, list]
        Splits the input list into specified data and leftover data.
    '''

    def __init__(self, 
                 amount: int):
        '''
        Constructs attributes for the NewestBlock object.

        Parameters
        ----------
        amount : int
            The number of records to extract.
        '''
        self.amount = amount

    def extract(self, 
                takeFrom: list) -> tuple[list, list]:
        '''
        Splits the input list into specified data and leftover data.

        Parameters
        ----------
        takeFrom : list
            List of records to extract data from.
        
        Returns
        -------
        output : tuple[list, list]
            The desired records (first) and the leftover records (second).
        '''
        if len(takeFrom) < self.amount:
            raise e.MoreDataThanRecordsException(
                f'Data size of {self.amount} is greater than the '
                f'available number of records {len(takeFrom)}.'
                )
        inBlock = takeFrom[0:self.amount]
        outBlock = takeFrom[self.amount: len(takeFrom) - 1]
        output = (inBlock, outBlock)
        return output

class RandomBlock(Extractor):
    '''
    Can be used to extract a random block of available records. Is an instance
    of the abstract Extractor class.

    ...

    Attributes
    ----------
    amount : int
        The number of records to extract.
    
    Methods
    -------
    extract(list) -> tuple[list, list]
        Splits the input list into specified data and leftover data.
    '''

    def __init__(self, 
                 amount: int):
        '''
        Constructs attributes for the RandomBlock object.

        Parameters
        ----------
        amount : int
            The number of records to extract.
        '''
        self.amount = amount

    def extract(self, 
                takeFrom: list) -> tuple[list, list]:
        '''
        Splits the input list into specified data and leftover data.

        Parameters
        ----------
        takeFrom : list
            A list of records to extract data from.
        
        Returns
        -------
        output : tuple[list, list]
            The desired records (first) and the leftover records (second).
        '''
        if len(takeFrom) < self.amount:
            raise e.MoreDataThanRecordsException(
                'Data size is greater than the available number of records'
                )
        
        start = random.randint(0,len(takeFrom) - self.amount - 1)

        inBlock = takeFrom[start: start + self.amount]
        outBlock = (
            takeFrom[0: start] + takeFrom[start + self.amount: len(takeFrom) -1]
        )
        output = (inBlock, outBlock)
        return output

class Uniform(Extractor):
    '''
    Can be used to extract a uniformly distributed selection of available 
    records. Is an instance of the abstract Extractor class.

    ...

    Attributes
    ----------
    amount : int
        The number of records to extract.
    
    Methods
    -------
    extract(list) -> tuple[list, list]
        Splits the input list into specified data and leftover data.
    '''

    def __init__(self, 
                 amount: int):
        '''
        Constructs attributes for the Uniform object.

        Parameters
        ----------
        amount : int
            The number of records to extract.
        '''
        self.amount = amount
    
    def extract(self, 
                takeFrom: list) -> tuple[list, list]:
        '''
        Splits the input list into specified data and leftover data.

        Parameters
        ----------
        takeFrom : list
            A list of records to extract data from.
        
        Returns
        -------
        output : tuple[list, list]
            The desired records (first) and the leftover records (second).
        '''
        if len(takeFrom) < self.amount:
            raise e.MoreDataThanRecordsException(
                'Data size is greater than the available number of records'
                )
        indexGen = lambda x : random.randint(0,len(takeFrom) - 1)
        indicies = indexSet(self.amount, indexGen)
        output = splitter(indicies,takeFrom)
        return output
        
def indexSet(size : int, 
             indexGen) -> list:
    '''
    Produces a list of unique indices to be used in the splitter function.

    Parameters
    ----------
    size : int
        The desired length of the output list.
    indexGen : function
        When called on any argument, produces an index.
    
    Returns
    -------
    indicies : list
        A list of unique indicies.
    '''
    indicies = set()
    while len(indicies) < size:
        index = indexGen(0)
        indicies.add(index)
    return indicies

def splitter(indicies : list, 
             takeFrom : list) -> tuple[list, list]:
    '''
    Splits one list into two based on a set of indicies.

    Parameters
    ----------
    takeFrom : list
        the list to split.
    indicies : list
        the list of indicies upon which to base the split.

    Returns
    -------
    samp : list
        The elements of takeFrom whose indicies are in the indicies list.
    left : list
        The elements of takeFrom whose indicies are not in the indicies list.
    ''' 
    sample = deque([])
    leftover = deque([])
    index = 0
    while index < len(takeFrom):
        if index in indicies:
            sample.append(takeFrom[index])
        else:
            leftover.append(takeFrom[index])
        index += 1
    samp = list(sample)
    left = list(leftover)
    return (samp, left)