import module
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
doYouWantToPlayBlackJade = True
while doYouWantToPlayBlackJade:
    playBlackJack = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if playBlackJack == "y":
        userCards = module.generateTwoRandomCard(cards)
        computerCard = module.generateTwoRandomCard(cards)
        print(
            f"Your Current Card {userCards}, current total {module.calculateTotalCards(userCards)}"
        )
        print(f"Computer first card:{computerCard[0]}")
        if userCards.count(10) > 0 and userCards.count(11) > 0:
            if computerCard.count(10) == 0 or computerCard.count(11) == 0:
                print("User Won")
            else:
                print("It's a Draw")
        elif computerCard.count(10) > 0 and computerCard.count(11) > 0:
            if userCards.count(10) == 0 or userCards.count(11) == 0:
                print("Computer Wins")
            else:
                print("Its a draw")
        else:
            userNewCards = True
            while userNewCards:
                if module.calculateTotalCards(userCards) > 21:
                    print("User Card Greater than 21")
                    if userCards.count(11) > 0:
                        print("There is an Ace in user Card")
                        totalUserAceCard = module.calculateTotalCardIfAce(userCards)
                        if totalUserAceCard > 21:
                            print("Computer Wins")
                            userNewCards = False
                        else:
                            newCard = input(
                                "Type 'y' to get another card, type 'n' to pass:"
                            )
                            if newCard == "y":
                                userCards.append(random.choice(cards))
                                print(
                                    f"Your Current Card {userCards}, current total {module.calculateTotalCards(userCards)}"
                                )
                            else:
                                userNewCards = False
                    else:
                        print("User Has No Ace")
                        print("Computer wins")
                        userNewCards = False
                else:
                    newCard = input("Type 'y' to get another card, type 'n' to pass:")
                    if newCard == "y":
                        userCards.append(random.choice(cards))
                        print(
                            f"Your Current Card {userCards}, current total {module.calculateTotalCards(userCards)}"
                        )
                    else:
                        userNewCards = False
    else:
        doYouWantToPlayBlackJade = not doYouWantToPlayBlackJade
        print("Quitting!")
