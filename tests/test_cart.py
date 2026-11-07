import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(20):
            result = cart.add_dvd(DigitalVideoDisc(f"DVD {i}"))
            self.assertTrue(result)

        result_21 = cart.add_dvd(DigitalVideoDisc("DVD 21"))
        self.assertFalse(result_21)


if __name__ == "__main__":
    unittest.main()
