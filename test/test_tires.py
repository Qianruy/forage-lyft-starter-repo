import unittest

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestTires(unittest.TestCase):
    def test_carrigan_should_be_serviced(self):
        wear_array = [0.8, 0.8, 0.9, 0.7]

        tires = CarriganTires(wear_array)
        self.assertTrue(tires.needs_service())

    def test_carrigan_should_not_be_serviced(self):
        wear_array = [0.8, 0.8, 0.6, 0.7]

        tires = CarriganTires(wear_array)
        self.assertFalse(tires.needs_service())

    def test_octoprime_should_be_serviced(self):
        wear_array = [1, 1, 1, 0.6]

        tires = OctoprimeTires(wear_array)
        self.assertTrue(tires.needs_service())

    def test_octoprime_should_not_be_serviced(self):
        wear_array = [1, 1, 0.9, 0]

        tires = OctoprimeTires(wear_array)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()