import random


def generateTwoRandomCard(cards):
    randomCard = []
    for card in range(2):
        randomCard.append(random.choice(cards))
    return randomCard
