import random

from game_data import data


def generate_starting_two_question():
    return random.choices(data, k=2)


print(generate_starting_two_question())
