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

    def test_discount_calculation(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD Test", cost=100.0))
        # 100$ giảm 20% kết quả mong đợi là 80$
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80.0)

    def test_discount_invalid_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("DVD Test", cost=100.0))
        # percent ngoài khoảng 0-100 phải ném ngoại lệ ValueError
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()
