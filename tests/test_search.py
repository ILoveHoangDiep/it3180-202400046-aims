import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95),
            DigitalVideoDisc("Aladdin", "Animation", cost=18.99),
        ]

    def test_search_by_title_case_insensitive(self):
        results = search_by_title(self.items, "lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()
