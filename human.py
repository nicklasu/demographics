import random


# Object which makes a check every time get_older is called and dies if the check fails.
# Based on https://en.wikipedia.org/wiki/Gompertz%E2%80%93Makeham_law_of_mortality
class Human:
    age = 0
    mortality = 0
    is_alive = bool
    is_female = bool

    def __init__(self, human_data):
        self.hazard_function = human_data['hazard_function']
        self.mortality = human_data['mortality']
        if human_data['infant_mortality'] > random.random():
            self.is_alive = False
        if random.random() > 0.50:
            self.is_female = False

    # Check and increase mortality.
    def get_older(self):
        if self.is_alive:
            if self.mortality > random.random():
                self.is_alive = False
                return  # If a human dies while trying to get older, we don't want to raise their age.
            self.age += 1
            self.mortality *= self.hazard_function
