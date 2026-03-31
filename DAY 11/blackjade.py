import module
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
doYouWantToPlayBlackJade = True


def checkComputerTotalScore(computerCards, totalUserAceCards):
    while module.calculateTotalCards(computerCards) < 17:
        computerCards.append(random.choice(cards))

    if module.calculateTotalCards(computerCards) > 21:
        if computerCards.count(11) > 0:
            totalComputerAceCards = module.calculateTotalCardIfAce(computerCards)
            if totalComputerAceCards > 21:
                print(f"User Card: {userCards}")
                print(f"Computer Card: {computerCards}")
                print("User Wins, Computer loose")
            else:
                module.announce_winner(
                    userScore=totalUserAceCards,
                    computerScore=totalComputerAceCards,
                    computerCards=computerCards,
                    userCards=userCards,
                )
        else:
            print(f"User Card: {userCards}")
            print(f"Computer Card: {computerCards}")
            print("Computer Loose, User Wins")
    else:
        totalComputerAceCards = module.calculateTotalCards(computerCards)
        module.announce_winner(
            userScore=totalUserAceCards,
            computerScore=totalComputerAceCards,
            computerCards=computerCards,
            userCards=userCards,
        )


while doYouWantToPlayBlackJade:
    playBlackJack = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if playBlackJack == "y":
        module.clear_screen()
        print(art.logo)
        userCards = module.generateTwoRandomCard(cards)
        computerCard = module.generateTwoRandomCard(cards)
        print(
            f"Your Current Card {userCards}, current total {module.calculateTotalCards(userCards)}"
        )
        print(f"Computer first card:{computerCard[0]}")
        if userCards.count(10) > 0 and userCards.count(11) > 0:
            if computerCard.count(10) == 0 or computerCard.count(11) == 0:
                print(f"User Card: {userCards}")
                print(f"Computer Card: {computerCard}")
                print("User Won")
            else:
                print(f"User Card: {userCards}")
                print(f"Computer Card: {computerCard}")
                print("It's a Draw")
        elif computerCard.count(10) > 0 and computerCard.count(11) > 0:
            if userCards.count(10) == 0 or userCards.count(11) == 0:
                print(f"User Card: {userCards}")
                print(f"Computer Card: {computerCard}")
                print("Computer Wins")
            else:
                print(f"User Card: {userCards}")
                print(f"Computer Card: {computerCard}")
                print("Its a draw")
        else:
            userNewCards = True
            while userNewCards:
                if module.calculateTotalCards(userCards) > 21:
                    if userCards.count(11) > 0:
                        totalUserAceCard = module.calculateTotalCardIfAce(userCards)
                        if totalUserAceCard > 21:
                            print(f"User Card: {userCards}")
                            print(f"Computer Card: {computerCard}")
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
                                checkComputerTotalScore(
                                    computerCards=computerCard,
                                    totalUserAceCards=totalUserAceCard,
                                )
                    else:
                        print(f"User Card: {userCards}")
                        print(f"Computer Card: {computerCard}")
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
                        checkComputerTotalScore(
                            computerCards=computerCard,
                            totalUserAceCards=module.calculateTotalCards(userCards),
                        )

    else:
        doYouWantToPlayBlackJade = not doYouWantToPlayBlackJade
        print("Quitting!")
