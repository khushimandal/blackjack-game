import random

us = input("Do you want to play BlackJack? (y/n) ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

ourCards = []
computerCards = []
continueGame = True
exitGame = False


def deal_cards():
    chosen = random.choice(cards)
    return chosen


while continueGame and not exitGame:
    if us.lower() == "y":
        print("Your cards are: ")
        for i in range(2):
            dealt = deal_cards()
            ourCards.append(dealt)
            print(dealt)

        comp = deal_cards()
        computerCards.append(comp)
        print(f"Computer's first card is: {comp}")

        again = input("Do you want to hit? (y/n) ")
        while again.lower() == "y":
            newest = deal_cards()
            ourCards.append(newest)
            print(f"Your new card is: {newest}")

            ourTotal = sum(ourCards)
            again = input("Do you want to hit? (y/n) ")

        compTotal = sum(computerCards)
        while compTotal < 17:
            newest = deal_cards()
            computerCards.append(newest)
            compTotal = sum(computerCards)

        print(f"Your cards are: {ourCards} and the total is {ourTotal}")
        print(f"Computer's cards are: {computerCards} and the total is {compTotal}")

        if ourTotal > 21:
            print("You lose")
        elif compTotal > 21:
            print("You win")
        elif ourTotal > compTotal:
            print("You win")
        elif ourTotal < compTotal:
            print("You lose")
        else:
            print("Draw")

        gameAgain = input("Do you want to play again? (y/n) ")
        if gameAgain == "y":
            ourCards = []
            computerCards = []
            continueGame = True
        else:
            continueGame = False

    elif us.lower() == "n":
        exitGame = True
    else:
        print("Invalid input")
        us = input("Do you want to play BlackJack? (y/n) ")
