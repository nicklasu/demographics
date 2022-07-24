# https://www.ssa.gov/oact/STATS/table4c6.html

import collections
import random

import matplotlib.pyplot as plt
import statistics
from human import Human

# Mortality and infant mortality for the US, 2019 hazard function for Denmark, 2006
human_data = {
    'mortality': 0.0001,
    'infant_mortality': 0.0065,
    'hazard_function': 1.085
}
births_per_1000 = {
    19: 10,
    24: 10,
    29: 10,
    34: 10,
    39: 10,
    44: 10,
    49: 10
}

if __name__ == '__main__':

    all_people = []
    # Create a human cohort
    for x in range(100):
        human = Human(human_data)
        all_people.append(human)

    # range == years
    for y in range(100):
        # Make everyone in the cohort a year older
        for x in range(all_people.__len__()):
            all_people[x].get_older()
            if all_people[x].is_female:
                for z in births_per_1000:
                    if z >= all_people[x].age:
                        if random.randint(0, 1000) <= births_per_1000.get(z):
                            all_people.append(Human(human_data))
                        break

    all_people.sort(key=lambda h: h.age)

    alive_people = []
    alive_female = []
    age_list = []
    mortality_list = []
    all_female_list = []
    for y in range(all_people.__len__()):
        age_list.append(all_people[y].age)
        mortality_list.append(all_people[y].mortality)
        if all_people[y].is_female:
            all_female_list.append(all_people[y])
        if all_people[y].is_alive:
            alive_people.append(all_people[y])
            if all_people[y].is_female:
                alive_female.append(all_people[y])
    counter = collections.Counter(age_list)
    print(counter)
    # for key in counter:
    #    print(key.real)

    print("Mean (Average): ", statistics.mean(age_list))
    print("Median (Middle value of the dataset): ", statistics.median(age_list))
    print("Mode (Value that occurs the highest number of times): ", statistics.mode(age_list))
    print("Total number of all people: ", all_people.__len__())
    print("Total number of alive people: ", alive_people.__len__())
    print("Total number of all females: ", all_female_list.__len__())
    print("Total number of alive females: ", alive_female.__len__())

    figure, axis = plt.subplots(2, 2)
    axis[0, 0].plot(counter.keys(), counter.items())
    axis[0, 1].plot(age_list, mortality_list)

    plt.show()
