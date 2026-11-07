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

    def test_remove_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD")
        cart.add_dvd(dvd)
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertFalse(cart.remove_dvd(dvd))

    def test_discount_calculation(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD Test", cost=100.0))
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_invalid_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD Test", cost=100.0))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
