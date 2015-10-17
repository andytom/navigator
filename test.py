import unittest
import os
import sys


if __name__ == '__main__':
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(parent_dir, 'navigator', 'tests')

    tests = unittest.TestLoader().discover(test_dir)
    results = unittest.TextTestRunner(verbosity=2, buffer=True).run(tests)

    ret = not results.wasSuccessful()
    sys.exit(ret)
