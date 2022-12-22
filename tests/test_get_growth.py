"""Test Unicorn methods."""

import unittest
from unittest import TestCase
from src.unicorn import Unicorn

class TestUnicornGrowth(TestCase):
    """Test get_growth() method."""

    def test_get_growth_first_5(self):
        """Test using unicorn_first_5.txt."""
        input_file = "unicorn_first_5.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_growth()
        expected = ['Bytedance', 'SpaceX', 'SHEIN', 'Stripe', 'Klarna']
        self.assertEqual(actual_result, expected)

        input_file = "unicorn_last_2.txt"
        unicorn_data = Unicorn.read_dataset(input_file)
        actual_result = unicorn_data.get_growth()
        expected = ['Gemini']
        self.assertEqual(actual_result, expected)


if __name__ == '__main__':
    unittest.main()
