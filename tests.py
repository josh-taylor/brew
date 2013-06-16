import unittest

tests = unittest.defaultTestLoader.discover('tests')
testRunner = unittest.TextTestRunner()
testRunner.run(tests)