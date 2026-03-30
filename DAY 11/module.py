import random


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
