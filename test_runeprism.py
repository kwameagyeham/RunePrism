# test_runeprism.py
"""
Tests for RunePrism module.
"""

import unittest
from runeprism import RunePrism

class TestRunePrism(unittest.TestCase):
    """Test cases for RunePrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RunePrism()
        self.assertIsInstance(instance, RunePrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RunePrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
