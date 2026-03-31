import random
import platform
import subprocess


def generateTwoRandomCard(cards):
    randomCard = []
    for _ in range(2):
        randomCard.append(random.choice(cards))
    return randomCard


def calculateTotalCards(cards):
    totalCard = 0
    for card in cards:
        totalCard += card
    return totalCard


def calculateTotalCardIfAce(cards):
    totalCard = 0
    for card in cards:
        if card == 11:
            totalCard += 1
        else:
            totalCard += card
    return totalCard


def clear_screen():
    if platform.system().lower() == "windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)



def announce_winner(userScore, computerScore, userCards, computerCards):
    if computerScore == userScore:
        print(f"User Card: {userCards}, Total User Card :{userScore}")
        print(f"Computer Card: {computerCards}, Total Computer Score: {computerScore}")
        print("Its a draw")
    elif computerScore > userScore:
        print(f"User Card: {userCards}, Total User Card :{userScore}")
        print(f"Computer Card: {computerCards}, Total Computer Score: {computerScore}")
        print("Computer Won, User Loose")
    elif userScore > computerScore:
        print(f"User Card: {userCards}, Total User Card :{userScore}")
        print(f"Computer Card: {computerCards}, Total Computer Score: {computerScore}")
        print("User Won, Computer Loose")
