import unittest
import os
from apps.main import Main, Valuation


class TestGetValuation(unittest.TestCase):
    """Test `get_valuation()` method."""

    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        df_10 = Main(f"{data_dir}/ten.csv").get_data()
        self.tasks_10 = Valuation(df_10)
        df_50 = Main(f"{data_dir}/fifty.csv").get_data()
        self.tasks_50 = Valuation(df_50)
        df = Main(f"{data_dir}/full_data.csv").get_data()
        self.tasks_all = Valuation(df)

    def test_multiple_entries(self):
        """Test case 1 using full_data.csv."""
        actual_result = self.tasks_all.get_valuation()
        expected_result = [
            "Bytedance",
            "SpaceX",
            "Stripe",
            "Klarna",
            "Epic Games",
            "Canva",
            "Checkout.com",
            "Instacart",
            "Databricks",
            "Revolut",
        ]
        self.assertEqual(actual_result, expected_result)

    def test_fifty_entries(self):
        """Test case 2 using fifty.csv with fifty rows."""
        actual_result = self.tasks_50.get_valuation()
        expected_result = [
            "Bytedance",
            "SpaceX",
            "Stripe",
            "Klarna",
            "Epic Games",
            "Canva",
            "Checkout.com",
            "Instacart",
            "Databricks",
            "Revolut",
        ]
        self.assertEqual(actual_result, expected_result)

    def test_ten_entries(self):
        """Test case 3 using ten.csv with ten rows."""
        actual_result = self.tasks_10.get_valuation()
        expected_result = [
            "Bytedance",
            "SpaceX",
            "Stripe",
            "Klarna",
            "Epic Games",
            "Canva",
            "Checkout.com",
            "Instacart",
            "Databricks",
        ]
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
