import random
import platform
import subprocess
from game_data import data
import art


def generate_starting_two_question():
    """Generating two dictionary from the game data"""
    return random.choices(data, k=2)


def is_user_answer_correct(user_answer, question_list):
    """Used To check if the user made the right choice or not"""
    if user_answer == "a":
        if question_list[0]["follower_count"] >= question_list[1]["follower_count"]:
            return True
        else:
            return False
    elif user_answer == "b":
        if question_list[1]["follower_count"] >= question_list[0]["follower_count"]:
            return True
        else:
            return False
    else:
        return False


def appending_new_question_and_removing_first(formal_Question_list):
    """This function takes in the formal list and remove the first one and also making sure the new one added is not either the one removed or the one there"""
    first_formal_question = formal_Question_list[0]
    last_formal_question = formal_Question_list[-1]
    # pick a random question from the game data
    new_question = random.choice(data)
    while (
        new_question["name"] == first_formal_question["name"]
        or new_question["name"] == last_formal_question["name"]
    ):
        new_question = random.choice(data)

    return [last_formal_question, new_question]


def clear_screen():
    """Clear the screen"""
    if platform.system().lower() == "windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


score = 0
gameOver = False
startingQuestionData = []
while not gameOver:
    if score == 0:
        startingQuestionData = generate_starting_two_question()
    else:
        startingQuestionData = appending_new_question_and_removing_first(
            formal_Question_list=startingQuestionData
        )
    print(f"{art.logo}")
    print(
        f"""
    Compare A: {startingQuestionData[0]["name"]}, a {startingQuestionData[0]["description"]}, from {startingQuestionData[0]["country"]}.
    {art.vs}
    Against B: {startingQuestionData[1]["name"]}, a {startingQuestionData[1]["description"]}, from {startingQuestionData[1]["country"]}.
    """
    )

    userInput = input("Who has more followers? Type 'A' or 'B':").lower()
    checkIfUserIsTrue = is_user_answer_correct(userInput, startingQuestionData)
    if not checkIfUserIsTrue:
        clear_screen()
        print({art.logo})
        gameOver = True
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        clear_screen()
        score += 1
        print(f"You're right! Current score: {score}")
