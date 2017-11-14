import nose
import glob
import locale
import unittest

testmodules = [
    'Sprint1.test_output_sprint1',
    'Sprint2.test_output_sprint2',
    'Sprint3.test_output_sprint3',
    'Sprint4.test_output_sprint4'
    ]

suite = unittest.TestSuite()

for t in testmodules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)