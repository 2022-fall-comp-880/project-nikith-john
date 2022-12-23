"""Test Unicorn methods."""

import unittest
from unittest import TestCase
from src.unicorn import Unicorn

class TestUnicornValuation(TestCase):
    """Test get_valuation() method."""

    def test_get_valuation_first_5(self):
        """Test using unicorn_first_5.txt."""
        input_file = "unicorn_first_5.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_valuation()
        expected = [
            ('Bytedance', '180', 'Artificial intelligence', 'China', '8',
             "'Sequoia Capital China;SIG Asia Investments;Sina Weibo;Softbank Group'"),
            ('SpaceX', '100', 'Other', 'United States', '7',
             "'Founders Fund;Draper Fisher Jurvetson;Rothenberg Ventures'"), (
            'SHEIN', '100', 'E-commerce direct-to-consumer', 'China', '2',
            "'Tiger Global Management; Sequoia Capital China; Shunwei Capital Partners'"),
            ('Stripe', '95', 'Fintech', 'United States', '2',
             "'Khosla Ventures; LowercaseCapital; capitalG'"), (
            'Klarna', '46', 'Fintech', 'Sweden', '4',
            "'Institutional Venture Partners; Sequoia Capital; General Atlantic'")
        ]
        self.assertListEqual(actual_result, expected)

    def test_get_valuation_last_2(self):
        """Test using nba_last_2.txt."""
        input_file = "unicorn_last_2.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_valuation()
        expected_result = [
            ('Gemini', '7', 'Fintech', 'United States', '0.42',
             "'Morgan Creek Digital'"), (
            'Zopa', '1', 'Fintech', 'United Kingdom', '0.79',
            "'IAG Capital Partners'")
        ]
        self.assertListEqual(actual_result, expected_result)



if __name__ == '__main__':
    unittest.main()
