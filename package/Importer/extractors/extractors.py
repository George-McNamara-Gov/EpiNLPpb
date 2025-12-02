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

Misc variables:

    None

Exceptions:

    MoreDataThanRecordsException
'''
import random
from abc import ABC, abstractmethod
import pandas as pd
from ... import exceptions as e

class Extractor(ABC):
    '''
    An abstract class used to create instances classes to extract data with 
    different sampling distributions.

    ...

    Attributes
    ---------
    amount : int
        The number of records to extract.
    
    Methods
    -------
    extract(pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]
        An abstract method that returns specified data and leftover data.
    changeAmount(int)
        Changes the amount attribute.
    '''

    @abstractmethod
    def extract(self, 
                takeFrom: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        '''
        An abstract method that returns specified data and leftover data.

        Parameters
        ----------
        takeFrom : pd.DataFrame
            A data frame of records to extract data from.

        Returns
        ------
        specified : pd.DataFrame
            The desired records from takeFrom.
        leftover : pd.DataFrame
            All records in takeFrom which aren't in the specified data.
        '''
        specified = None
        leftover = None
        return specified, leftover

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
    extract(pd.DataFrame) -> tuple[pd.DateFrame, pd.DataFrame]
        Splits the input data into specified data and leftover data.
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
                takeFrom: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        '''
        Splits the input data into specified data and leftover data.

        Parameters
        ----------
        takeFrom : pd.DataFrame
            A data frame of records to extract data from.
        
        Returns
        -------
        specified : pd.DataFrame
            The desired records from takeFrom.
        leftover : pd.DataFrame
            All records in takeFrom which aren't in the specified data.
        '''
        if len(takeFrom) < self.amount:
            raise e.MoreDataThanRecordsException(
                f'Data size of {self.amount} is greater than the '
                f'available number of records {len(takeFrom)}.'
                )
        specified = takeFrom.iloc[0:self.amount]
        leftover = takeFrom.iloc[self.amount: len(takeFrom) - 1]
        return specified, leftover

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
    extract(pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]
        Splits the input data into specified data and leftover data.
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
                takeFrom: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        '''
        Splits the input data into specified data and leftover data.

        Parameters
        ----------
        takeFrom : pd.DataFrame
            A data frame of records to extract data from.
        
        Returns
        -------
        specified : pd.DataFrame
            The desired records from takeFrom.
        leftover : pd.DataFrame
            All records in takeFrom which aren't in the specified data.
        '''
        if len(takeFrom) < self.amount:
            raise e.MoreDataThanRecordsException(
                'Data size is greater than the available number of records'
                )
        
        start = random.randint(0,len(takeFrom) - self.amount - 1)

        specified = takeFrom.iloc[start: start + self.amount]
        outBlock1 = takeFrom.iloc[0: start]
        outBlock2 = takeFrom.iloc[start + self.amount: len(takeFrom) -1]
        leftover = pd.concat([outBlock1, outBlock2], axis= 0)
        return specified, leftover

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
    extract(pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]
        Splits the input data into specified data and leftover data.
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
                takeFrom: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
        '''
        Splits the input data into specified data and leftover data.

        Parameters
        ----------
        takeFrom : pd.DataFrame
            A data frame of records to extract data from.
        
        Returns
        -------
        specified : pd.DataFrame
            The desired records from takeFrom.
        leftover : pd.DataFrame
            All records in takeFrom which aren't in the specified data.
        '''
        if len(takeFrom) < self.amount:
            raise e.MoreDataThanRecordsException(
                'Data size is greater than the available number of records'
                )
        indexGen = lambda x : random.randint(0,len(takeFrom) - 1)
        indices = indexSet(self.amount, indexGen)
        specified = takeFrom.iloc[list(indices)]
        remainingIndicies = list(range(0,len(takeFrom) - 1))
        for ind in indices:
            try:
                remainingIndicies.remove(ind)
            except ValueError:
                pass
        leftover = takeFrom.iloc[remainingIndicies]
        return specified, leftover
        
def indexSet(size : int, 
             indexGen) -> list:
    '''
    Produces a list of unique indices to be used in the Uniform extractor.

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