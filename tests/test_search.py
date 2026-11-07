import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95),
            DigitalVideoDisc("Aladdin", "Animation", cost=18.99),
        ]

    def test_search_by_category(self):
        results = search_by_category(self.items, "animation")
        self.assertEqual(len(results), 2)

    def test_search_by_title_exact(self):
        results = search_by_title(self.items, "The Lion King")
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()
