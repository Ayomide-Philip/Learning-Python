import random

word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)

blank_dash = ""
for i in range(0, len(random_word)):
    blank_dash += "_"

startGame = True
totalLife = 6

random_word_to_list = []
for word in random_word:
    random_word_to_list.append(word)

blank_dash_to_list = []

for dash in blank_dash:
    blank_dash_to_list.append(dash)


def convertListToString(inputtedList):
    listToWord = ""
    for i in inputtedList:
        listToWord += i
    return listToWord


while startGame:
    if totalLife > 0:
        print(
            f"*******************************{totalLife}/6*********************************"
        )
        if blank_dash_to_list.count("_") != 0:
            userInput = input("Guess a letter?\n")
            if (
                random_word_to_list.count(userInput) > 0
                and blank_dash_to_list.count(userInput) == 0
            ):
                for i in range(0, len(random_word_to_list)):
                    if random_word_to_list[i] == userInput:
                        blank_dash_to_list[i] = userInput
                print(convertListToString(blank_dash_to_list))
            else:
                totalLife -= 1
                print(f"You have {totalLife} live left.")
        else:
            print(
                f"You Won, the correct word is {convertListToString(blank_dash_to_list)}. Game Over!"
            )
            startGame = not startGame
    else:
        if totalLife == 0:
            print("Game Over, you loss")
            startGame = not startGame
