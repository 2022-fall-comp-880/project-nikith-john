"""Test Unicorn methods."""

import unittest
from unittest import TestCase
from src.unicorn import Unicorn

class TestUnicornInvestors(TestCase):
    """Test get_investors() method."""

    def test_get_investors_first_5(self):
        """Test using unicorn_first_5.txt."""
        input_file = "unicorn_first_5.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_investors()
        expected = ["'Founders Fund;Draper Fisher Jurvetson;Rothenberg Ventures'",
 "'Institutional Venture Partners; Sequoia Capital; General Atlantic'",
 "'Khosla Ventures; LowercaseCapital; capitalG'",
 "'Sequoia Capital China;SIG Asia Investments;Sina Weibo;Softbank Group'",
 "'Tiger Global Management; Sequoia Capital China; Shunwei Capital Partners'"]
        self.assertEqual(actual_result, expected)

    def test_get_investors_last_2(self):
        """Test using nba_last_2.txt."""
        input_file = "unicorn_last_2.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_investors()
        expected = ["'IAG Capital Partners'", "'Morgan Creek Digital'"]
        self.assertEqual(actual_result, expected)



if __name__ == '__main__':
    unittest.main()
