# https://www.ssa.gov/oact/STATS/table4c6.html

# import collections
import random
from multiprocessing import Process

import file_handler
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
# The simulation takes the lowest number that is higher or same as the current age.
# Example of age brackets where you can fine-tune birth rate for each bracket:
"""
births_per_1000 = {
    19: 5,  # 15-19
    24: 40,  # 20-24
    29: 80,  # 25-29
    34: 80,  # 30-34
    39: 30,  # 35-39
    44: 10,  # 40-44
    49: 3  # 45-49
}
"""

births_per_1000 = {
    # The number on the left is the oldest age (44) that a person is fertile in this simulation.
    # Simulation expects that the youngest fertile person is 15, and it doesn't need to be stated.
    # Right number is the number of births per 1000 for 15-44 age bracket.
    # For example US birthrate for fertile people between ages of 15-44 is 56.0 for year 2020.
    44: 56,
}


if __name__ == '__main__':
    print("Explanations: ")
    print("Mean (Average)")
    print("Median (Middle value of the dataset)")
    print("Mode (Value that occurs the highest number of times)\n")
    autoplay_turns = 0
    population = []
    # population_history = []
    print("Choose 1 for generating your own population range")
    # print("Choose 2 for pre-made population range")
    print("Choose 3 for previously user-generated population range")
    ask_for_choice = input()
    try:
        choice = int(ask_for_choice)
        if choice == 1:
            # Create a human cohort
            print("Enter size of the population:")
            size_of_pop = input()
            for x in range(int(size_of_pop)):
                population.append(Human(human_data))
                print(x)
        # if choice == 2:
        #    population = file_handler.load_object("pref.pickle")
        if choice == 3:
            population = file_handler.load_object("user.pickle")
    except ValueError:
        print("Just one more turn...\n")


    def make_older(p, r):
        # Make everyone in the cohort a year older
        for p in range(r):
            population[p].get_older()
            # Birthrate randomizer
            if population[p].is_fertile:  # Check that the person is fertile
                for b in births_per_1000:  # Loop if user wanted to simulate birthrates more accurately
                    if random.randint(0, 1000) <= births_per_1000.get(b):  # If a birth happens, add a new human
                        population.append(Human(human_data))
                    break


    def make_older2(p, r):
        # Make everyone in the cohort a year older
        for p in range(r):
            population[p].get_older()
            # Birthrate randomizer
            if population[p].is_fertile:  # Check that the person is fertile
                for b in births_per_1000:  # Loop if user wanted to simulate birthrates more accurately
                    if random.randint(0, 1000) <= births_per_1000.get(b):  # If a birth happens, add a new human
                        population.append(Human(human_data))
                    break


    # save_object(population)
    # range == years
    for y in range(100_000):
        prc1 = Process(target=make_older(0, int(population.__len__() / 2 - 1)))
        prc2 = Process(target=make_older2(int(population.__len__() / 2), int(population.__len__() / 2)))
        prc1.start()
        prc2.start()
        prc1.join()
        prc2.join()
        # for z in range(population.__len__()):
        #    if not population[z].is_alive:
        #        population[z].death_year = y
        #        population_history.append(population[z])
        if autoplay_turns > 0:
            # population[:] = (h for h in population if h.is_alive)
            print("Year: ", y, "\n")
            print("Total number of alive people: ", population.__len__())

        autoplay_turns = autoplay_turns - 1
        if autoplay_turns < 0:
            ages_now = []
            ages_at_death = []
            fertile_people = []

            for z in population:
                if not z.is_alive:
                    ages_at_death.append(z.age)
                    population.remove(z)
            for z in range(population.__len__()):
                ages_now.append(population[z].age)
                if population[z].is_fertile:
                    fertile_people.append(population[z])

            # counter = collections.Counter(age_list)
            print("Year: ", y, "\n")
            print("Total number of alive people: ", population.__len__())
            print("Mean age of population: ", statistics.mean(ages_now))
            print("Median age of population: ", statistics.median(ages_now))
            print("Mode age of population: ", statistics.mode(ages_now), "\n")
            if ages_at_death:
                print("Mean age at death: ", statistics.mean(ages_at_death))
                print("Median age at death: ", statistics.median(ages_at_death))
                print("Mode age at death: ", statistics.mode(ages_at_death), "\n")
            # print("Total number of alive people: ", population.__len__())
            print("Total number of alive fertile people: ", fertile_people.__len__(), "\n")
            print("Enter 's' for saving the current situation or")
            print("Enter number of autoplay turns or")
            print("Press <ENTER> to end turn...")
            input_a = input()
            try:
                if input_a == "s":
                    file_handler.save_object(population, "user.pickle")
                autoplay_turns = int(input_a)
            except ValueError:
                print("Just one more turn...\n")
            print("Loading...")

        """
        figure, axis = plt.subplots(2, 2)
        axis[0, 0].plot(counter.keys(), counter.items())
        axis[0, 1].plot(age_list, mortality_list)
        plt.show()
        """
