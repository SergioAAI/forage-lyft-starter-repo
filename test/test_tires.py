import unittest
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires_status = [0.9, 0, 0, 0]

        tires = CarriganTires(tires_status)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires_status = [0.89, 0, 0, 0]

        tires = CarriganTires(tires_status)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires_status = [1, 1, 1, 0]

        tires = OctoprimeTires(tires_status)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires_status = [1, 1, 0.9, 0]

        tires = OctoprimeTires(tires_status)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()