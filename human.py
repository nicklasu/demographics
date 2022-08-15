import random


# Object which makes a check every time get_older is called and dies if the check fails.
# Based on https://en.wikipedia.org/wiki/Gompertz%E2%80%93Makeham_law_of_mortality
class Human:
    age = 0
    mortality = 0
    is_alive = bool
    # Gender identity
    # Further development: increase the amount of different gender identities
    is_woman = bool
    # Fertility check
    is_fertile = bool
    death_year = None

    def __init__(self, human_data):
        self.hazard_function = human_data['hazard_function']
        self.mortality = human_data['mortality']
        if human_data['infant_mortality'] > random.random():
            self.is_alive = False
        if random.random() > 0.50:
            self.is_woman = False
        self.is_fertile = False

    # Check and increase mortality and check for fertility etc.
    def get_older(self):
        if self.is_alive:
            if self.mortality > random.random():
                self.is_alive = False
                return  # If a human dies while trying to get older, we don't want to raise their age.
            self.age += 1
            self.mortality *= self.hazard_function
            # Women who are between ages 15 and 44 are fertile
            if self.is_woman:
                if self.age > 14:
                    self.is_fertile = True
                if self.age > 44:
                    self.is_fertile = False
