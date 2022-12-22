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
        expected = [('Bytedance', 180, 'Artificial intelligence', 'China', 'Sequoia Capital China, SIG Asia Investments, Sina Weibo, Softbank Group', 8), ('SpaceX', 100, 'Other', 'United States', 'Founders Fund, Draper Fisher Jurvetson, Rothenberg Ventures', 7), ('SHEIN', 100, 'E-commerce & direct-to-consumer', 'China', 'Tiger Global Management, Sequoia Capital China, Shunwei Capital Partners', 2), ('Stripe', 95, 'Fintech', 'United States', 'Khosla Ventures, LowercaseCapital, capitalG', 2), ('Klarna', 46, 'Fintech', 'Sweden', 'Institutional Venture Partners, Sequoia Capital, General Atlantic', 4)]
        self.assertDictEqual(actual_result, expected)

    def test_get_valuation_last_2(self):
        """Test using nba_last_2.txt."""
        input_file = "unicorn_last_2.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_valuation()
        expected_result = [('Gemini', 7, 'Fintech', 'United States', 'Morgan Creek Digital, Marcy Venture Partners, 10T Fund', 0.42), ('Zopa', 1, 'Fintech', 'United Kingdom', 'IAG Capital Partners, Augmentum Fintech, Northzone Ventures', 0.79)]
        self.assertDictEqual(actual_result, expected_result)



if __name__ == '__main__':
    unittest.main()
