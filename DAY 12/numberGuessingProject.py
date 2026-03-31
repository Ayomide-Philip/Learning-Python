import random
import art

print(art.logo)
print("Welcome To the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
chooseLevel = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
randomNumberChosen = random.randint(1, 100)
numberOfAttempt = 0
gameStarted = False
if chooseLevel == "easy":
    numberOfAttempt = 10
    gameStarted = not gameStarted
elif chooseLevel == "hard":
    numberOfAttempt = 5
    gameStarted = not gameStarted

while gameStarted:
    if numberOfAttempt > 0:
        print(
            f"************************{numberOfAttempt} attempt**************************"
        )
        guessedNumber = int(input("Make a guess:"))
        if guessedNumber == randomNumberChosen:
            gameStarted = False
            print(f"You won, the correct number is {guessedNumber}")
        elif guessedNumber > randomNumberChosen:
            print(f"The number {guessedNumber} is too high")
            numberOfAttempt -= 1
        elif guessedNumber < randomNumberChosen:
            print(f"The number {guessedNumber} is too low")
            numberOfAttempt -= 1
    else:
        print("Game Over, You have used your total attempt available")
        gameStarted = not gameStarted
