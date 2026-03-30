import module
import random

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

    def letUserDrawAnotherCardOrNot():
        newCard = input("Enter 'y' to draw another card, and 'n' to skip?:").lower()
        if newCard == "y":
            userCards.append(random.choice(cards))
            return True
        elif newCard == "n":
            return False


userHasNewCard = True
while userHasNewCard:
    totalUserScore = module.calculateTotalCards(userCards)
    totalDealerScore = module.calculateTotalCards(dealerCards)
    print(f"Total User Score: {totalUserScore}")
    print(f"Dealer Total Score:{totalDealerScore}")
    if totalUserScore > 21:
        if userCards.count(11) != 0:
            totalUserAceScore = module.calculateTotalCardIfAce(userCards)
            if totalUserAceScore > 21:
                print(f"User Cards: {userCards}")
                print(f"Dealer Cards:{dealerCards}")
                print("User Busts, Dealer Wins")
                userHasNewCard = not userHasNewCard
            else:
                userHasNewCard = letUserDrawAnotherCardOrNot()
        else:
            print("User Burst, Dealer Wins")
            userHasNewCard = False
    else:
        userHasNewCard = letUserDrawAnotherCardOrNot()
