"""Test Unicorn methods."""

import unittest
from unittest import TestCase
from src.unicorn import Unicorn

class TestPlayerValuation(TestCase):
    """Test get_valuation() method."""

    def test_get_valuation_empty(self):
        """Test using unicorn_empty.txt."""
        input_file = "unicorn_empty.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_valuation()
        self.assertDictEqual(actual_result, {})

    def test_get_valuation_first_5(self):
        """Test using unicorn_first_5.txt."""
        input_file = "unicorn_first_5.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_valuation()
        expected =
        self.assertDictEqual(actual_result, expected)

    def test_get_valuation_last_2(self):
        """Test using nba_last_2.txt."""
        input_file = "unicorn_last_2.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_valuation()
        expected_result =
        self.assertDictEqual(actual_result, expected_result)



if __name__ == '__main__':
    unittest.main()
