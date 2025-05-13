'''
Combines all test cases into one test suite and runs that test suite.
'''
import unittest

from . import test_base
from . import test_evaluate
from . import test_importer
from . import test_mlearn
from . import test_nltk
from . import test_vectorise

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_base))
suite.addTests(loader.loadTestsFromModule(test_evaluate))
suite.addTests(loader.loadTestsFromModule(test_importer))
suite.addTests(loader.loadTestsFromModule(test_mlearn))
suite.addTests(loader.loadTestsFromModule(test_nltk))
suite.addTests(loader.loadTestsFromModule(test_vectorise))

runner = unittest.TextTestRunner(verbosity=3)

if __name__ == "__main__":
    result = runner.run(suite)