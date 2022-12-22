"""Test Unicorn methods."""

import unittest
from unittest import TestCase
from src.unicorn import Unicorn

class TestPlayerInvestors(TestCase):
    """Test get_investors() method."""

    def test_get_investors_first_5(self):
        """Test using unicorn_first_5.txt."""
        input_file = "unicorn_first_5.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_investors()
        expected = ['Sequoia Capital China;SIG Asia Investments;Sina Weibo;Softbank Group']
        self.assertDictEqual(actual_result, expected)

    def test_get_investors_last_2(self):
        """Test using nba_last_2.txt."""
        input_file = "unicorn_last_2.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_investors()
        expected_result = ['Sequoia Capital China;SIG Asia Investments;Sina Weibo;Softbank Group']
        self.assertDictEqual(actual_result, expected_result)



if __name__ == '__main__':
    unittest.main()
