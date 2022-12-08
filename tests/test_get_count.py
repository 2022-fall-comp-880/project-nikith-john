import unittest
import os
from apps.main import Main, Count


class TestCount(unittest.TestCase):
    """Test `get_count()` method."""

    def setUp(self):
        """Create Tasks objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        df_10 = Main(f"{data_dir}/ten.csv").get_data()
        self.tasks_10 = Count(df_10)
        df_50 = Main(f"{data_dir}/fifty.csv").get_data()
        self.tasks_50 = Count(df_50)
        df = Main(f"{data_dir}/full_data.csv").get_data()
        self.tasks_all = Count(df)

    def test_multiple_entries(self):
        """Test case 1 using full_data.csv."""
        actual_result = self.tasks_all.get_count()
        expected_result = {
            "China": 168,
            "United States": 536,
            "Sweden": 6,
            "Australia": 6,
            "United Kingdom": 42,
            "Bahamas": 1,
            "India": 63,
            "Indonesia": 7,
            "Germany": 24,
            "Hong Kong": 6,
            "Mexico": 6,
            "Estonia": 2,
            "Canada": 19,
            "Turkey": 3,
            "South Korea": 12,
            "Netherlands": 6,
            "Israel": 20,
            "France": 24,
            "Finland": 3,
            "Colombia": 2,
            "Belgium": 3,
            "Brazil": 16,
            "Denmark": 2,
            "Lithuania": 1,
            "Austria": 2,
            "Ireland": 5,
            "Singapore": 12,
            "Vietnam": 2,
            "United Arab Emirates": 3,
            "Switzerland": 5,
            "Argentina": 1,
            "Spain": 3,
            "Japan": 6,
            "Luxembourg": 1,
            "Nigeria": 1,
            "Philippines": 2,
            "Senegal": 1,
            "Malaysia": 1,
            "Bermuda": 1,
            "Norway": 4,
            "South Africa": 2,
            "Chile": 2,
            "Thailand": 2,
            "Czech Republic": 1,
            "Croatia": 1,
            "Italy": 1,
        }
        self.assertEqual(actual_result, expected_result)

    def test_fifty_entries(self):
        """Test case 2 using fifty.csv with fifty rows."""
        actual_result = self.tasks_50.get_count()
        expected_result = {
            "China": 9,
            "United States": 30,
            "Sweden": 1,
            "Australia": 1,
            "United Kingdom": 3,
            "Bahamas": 1,
            "India": 2,
            "Indonesia": 1,
            "Germany": 1,
            "Hong Kong": 1,
        }
        self.assertEqual(actual_result, expected_result)

    def test_ten_entries(self):
        """Test case 3 using ten.csv with ten rows."""
        actual_result = self.tasks_10.get_count()
        expected_result = {
            "China": 1,
            "United States": 5,
            "Sweden": 1,
            "Australia": 1,
            "United Kingdom": 1,
        }
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
