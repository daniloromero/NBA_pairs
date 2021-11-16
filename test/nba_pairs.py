#!/usr/bin/python3
"""Unittest for nba_pairs"""
import unittest
import pep8
nba_pairs = __import__('nba_pairs')
module_doc = nba_pairs.__doc__


class TestNbaPairs(unittest.TestCase):
    """Unittest class for style and docstring compliance"""

    def test_pep8_conformance(self):
        """Test that nba_pairs.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['nba_pairs.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test(self):
        """Test that tests/nba_pairs.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['test/nba_pairs.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "nba_pairs.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "nba_pairs.py needs a docstring")


class TestsUserInput(unittest.TestCase):
    """Unittest class to test input handling"""

    def test_integer(self):
        """Test for integer input"""
        original_raw_input = __builtins__['input']
        __builtins__['input'] = lambda _: '139'
        self.assertEqual(nba_pairs.get_input(), 139)
        __builtins__['input'] = original_raw_input

    def test_string(self):
        """Test for string input"""
        original_raw_input = __builtins__['input']
        __builtins__['input'] = lambda _: 'abc'
        self.assertEqual(nba_pairs.get_input(), None)
        __builtins__['input'] = original_raw_input
