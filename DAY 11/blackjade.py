import random
import module

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

userCards = module.generateTwoRandomCard(cards)
dealerCards = module.generateTwoRandomCard(cards)
print(userCards)
print(dealerCards)
