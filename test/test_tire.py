import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn = [0, 0.8, 0.9, 0.3]
        tire = CarriganTire(tire_worn)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_worn = [0, 0.8, 0.89, 0.3]
        tire = CarriganTire(tire_worn)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_worn = [0.6, 0.8, 0.9, 0.7]
        tire = OctoprimeTire(tire_worn)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_worn = [0, 0.8, 0.89, 0.3]
        tire = OctoprimeTire(tire_worn)
        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()
