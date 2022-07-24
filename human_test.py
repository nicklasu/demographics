import unittest

from human import Human


# Class for testing human.py.
class TestHuman(unittest.TestCase):

    def test_get_older(self):
        human_data = {
            'mortality': 0.0000,
            'infant_mortality': 0.0000,
            'hazard_function': 1.085
        }
        human = Human(human_data)
        human.get_older()
        self.assertEqual(human.age, 1)

    def test_infant_mortality(self):
        human_data = {
            'mortality': 0.0000,
            'infant_mortality': 1.0000,
            'hazard_function': 1.085
        }
        human = Human(human_data)
        self.assertEqual(human.is_alive, 0)
        self.assertEqual(human.age, 0)

    def test_mortality(self):
        human_data = {
            'mortality': 1.0000,
            'infant_mortality': 0.0000,
            'hazard_function': 1.085
        }
        human = Human(human_data)
        human.get_older()
        self.assertEqual(human.is_alive, 0)
        self.assertEqual(human.age, 0)


if __name__ == '__main__':
    unittest.main()
