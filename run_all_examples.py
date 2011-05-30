#!/usr/bin/env python
import doctest
import unittest
import os
import sys
import glob


def test_suite():
    flags = doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS
    if sys.version_info >= (3,):
        flags |= doctest.IGNORE_EXCEPTION_DETAIL
    doctests_path = os.path.join('matcher_crowd', 'doctests')

    suite = unittest.TestSuite()

    for doctest_file in os.listdir(doctests_path):
        if doctest_file.endswith('.txt'):
            suite.addTest(doctest.DocFileSuite(os.path.join(doctests_path,
                                                            doctest_file),
                                               optionflags=flags))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite())
    sys.exit(int(bool(result.failures or result.errors)))

