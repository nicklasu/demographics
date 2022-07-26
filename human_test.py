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

    # Test fertility ages
    def test_fertility(self):
        human_data = {
            'mortality': 0.0000,
            'infant_mortality': 0.0000,
            'hazard_function': 0
        }
        human = Human(human_data)
        human.is_woman = True
        for x in range(15):
            self.assertEqual(human.is_fertile, False)
            human.get_older()
        print("Test 1 for fertility passed...")
        for x in range(40):
            if human.age <= 44:
                self.assertEqual(human.is_fertile, True)
            human.get_older()
        print("Test 2 for fertility passed...")
        for x in range(40):
            self.assertEqual(human.is_fertile, False)
        print("Test 3 for fertility passed...")


if __name__ == '__main__':
    unittest.main()
