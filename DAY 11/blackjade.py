import module

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

userCards = module.generateTwoRandomCard(cards)
dealerCards = module.generateTwoRandomCard(cards)
print(userCards)
print(dealerCards)

if userCards.count(10) != 0 and userCards.count(11) != 0:
    if dealerCards.count(10) != 0 and dealerCards.count(11) != 0:
        print("It's a draw")
    else:
        print("User Wins")
elif dealerCards.count(10) != 0 and dealerCards.count(11) != 0:
    print("Dealer Wins")
