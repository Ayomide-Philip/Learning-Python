import random

from game_data import data


def generate_starting_two_question():
    return random.choices(data, k=2)


print(generate_starting_two_question())
startingQuestionData = generate_starting_two_question()
print(
    f"""
Compare A: {startingQuestionData[0]["name"]}, a {startingQuestionData[0]["description"]}, from {startingQuestionData[0]["country"]}.
vs
Against B: {startingQuestionData[1]["name"]}, a {startingQuestionData[1]["description"]}, from {startingQuestionData[1]["country"]}.
"""
)

userInput = input("Who has more followers? Type 'A' or 'B':")
