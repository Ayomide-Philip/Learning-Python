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

print(f"Total User Score: {module.calculateTotalCards(userCards)}")
print(f"Dealer Total Score:{module.calculateTotalCards(dealerCards)}")

totalUserScore = module.calculateTotalCards(userCards)
totalDealerScore = module.calculateTotalCards(dealerCards)
userHasNewCard = True
while userHasNewCard:
    if totalUserScore > 21:
        if userCards.count(11) != 0:
            totalUserAceScore = module.calculateTotalCardIfAce(userCards)
            if totalUserAceScore > 21:
                print("User Busts, Dealer Wins")
                userHasNewCard = not userHasNewCard
            else:
                print(f"Total User Score: {totalUserAceScore}")
                newCard = input(
                    "Type 'y' to draw another card and 'n' to skip?:"
                ).lower()
