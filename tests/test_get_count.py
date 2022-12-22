"""Test Unicorn methods."""

import unittest
from unittest import TestCase
from src.unicorn import Unicorn

class TestGetCount(TestCase):
    """Test get_count() method."""

    def test_get_count_last2(self):
        """Test using unicorn_first_5.txt."""
        input_file = "unicorn_last_2.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_top_countries()
        expected = {'United States': 1, 'United Kingdom': 1}
        self.assertDictEqual(actual_result, expected)

    def test_get_count_first5(self):
        """Test using unicorn_first_5.txt."""
        input_file = "unicorn_first_5.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_top_countries()
        expected = {'United States': 2, 'China': 2, 'Sweden': 1}
        self.assertDictEqual(actual_result, expected)


if __name__ == '__main__':
    unittest.main()
