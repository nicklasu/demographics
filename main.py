# https://www.ssa.gov/oact/STATS/table4c6.html

# import collections
import random

# import matplotlib.pyplot as plt
import statistics
from human import Human

# Mortality and infant mortality for the US, 2019 hazard function for Denmark, 2006
human_data = {
    'mortality': 0.0001,
    'infant_mortality': 0.0065,
    'hazard_function': 1.085
}
# https://www.oecd.org/els/soc/SF_2_3_Age_mothers_childbirth.pdf
# Can be expanded if wanted to include age brackets.
# Example of age brackets where you can fine-tune birth rate:
""""
births_per_1000 = {
    19: 10,
    24: 10,
    29: 10,
    34: 10,
    39: 10,
    44: 10,
    49: 10
}
"""

births_per_1000 = {
    # Oldest age is 44 and the second number is for 16-44 age bracket.
    # For example US birthrate for Women ages 15-44 is 56.0 for year 2020.
    44: 56,
}

if __name__ == '__main__':
    print("Explanations: ")
    print("Mean (Average)")
    print("Median (Middle value of the dataset)")
    print("Mode (Value that occurs the highest number of times)\n")
    autoplay_turns = 0
    all_people = []
    # Create a human cohort
    for x in range(100):
        human = Human(human_data)
        all_people.append(human)

    # range == years
    for y in range(10_000):
        # Make everyone in the cohort a year older
        for x in range(all_people.__len__()):
            all_people[x].get_older()
            # Birthrate randomizer
            if all_people[x].is_fertile:  # Check that the person is fertile
                for z in births_per_1000:  # Loop if user wanted to simulate birthrates more accurately
                    if random.randint(0, 1000) <= births_per_1000.get(z):  # If a birth happens, add a new human
                        all_people.append(Human(human_data))
                    break
        all_people.sort(key=lambda h: h.age)

        alive_people = []
        alive_women = []
        age_list = []
        death_list = []
        all_women_list = []
        fertile_people = []

        # TODO increase efficiency of this loop
        for z in range(all_people.__len__()):
            if all_people[z].is_alive:
                age_list.append(all_people[z].age)
            if not all_people[z].is_alive:
                death_list.append(all_people[z].age)
            if all_people[z].is_woman:
                all_women_list.append(all_people[z])
            if all_people[z].is_alive:
                alive_people.append(all_people[z])
                if all_people[z].is_woman:
                    alive_women.append(all_people[z])
                if all_people[z].is_fertile:
                    fertile_people.append(all_people[z])
        # counter = collections.Counter(age_list)
        print("Year: ", y, "\n")
        print("Mean age of population: ", statistics.mean(age_list))
        print("Median age of population: ", statistics.median(age_list))
        print("Mode age of population: ", statistics.mode(age_list), "\n")
        if death_list:
            print("Mean age at death: ", statistics.mean(death_list))
            print("Median age at death: ", statistics.median(death_list))
            print("Mode age at death: ", statistics.mode(death_list), "\n")
        print("Total number of alive people: ", alive_people.__len__())
        print("Total number of alive women: ", alive_women.__len__())
        print("Total number of alive fertile people: ", fertile_people.__len__(), "\n")
        autoplay_turns = autoplay_turns - 1
        if autoplay_turns < 0:
            print("Enter number of autoplay turns or")
            print("Press <ENTER> to end turn...")
            input_a = input()
            try:
                autoplay_turns = int(input_a)
            except ValueError:
                print("Just one more turn...\n")

        """
        figure, axis = plt.subplots(2, 2)
        axis[0, 0].plot(counter.keys(), counter.items())
        axis[0, 1].plot(age_list, mortality_list)
        plt.show()
        """
