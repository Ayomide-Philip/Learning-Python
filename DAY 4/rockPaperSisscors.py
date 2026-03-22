import random

userInput = int(input("Type 0 for Rock , 1 for Paper, 2 for Scissors \n"))

shape = ["Rock", "Paper", "Scissors"]

randomGuess = int(random.random() * len(shape))

randomShape = shape[randomGuess]

if shape[userInput] == "Rock" and randomShape == "Scissors":
    print(
        f"""You picked {shape[userInput]} while Computer Picked {randomShape}.
          You Won."""
    )
elif randomShape == "Rock" and shape[userInput] == "Scissors":
    print(
        f"""You picked {shape[userInput]} while Computer Picked {randomShape}.
           Computer Won."""
    )
elif shape[userInput] == "Scissors" and randomShape == "Paper":
    print(
        f"""You picked {shape[userInput]} while Computer picked {randomShape}.
          You Won."""
    )
elif shape[userInput] == "Paper" and randomShape == "Scissors":
    print(
        f"""You Picked {shape[userInput]} while Computer Picked {randomShape}.
          Computer Won"""
    )
elif shape[userInput] == "Paper" and randomShape == "Rock":
    print(
        f"""You Picked {shape[userInput]} while Computer Picked {randomShape}.
          You Won"""
    )
elif randomShape == "Paper" and shape[userInput] == "Rock":
    print(
        f"""You Picked {shape[userInput]} while Computer Picked {randomShape}.
               \nComputer Won"""
    )
elif randomShape == shape[userInput]:
    print(
        f"""You Picked {shape[userInput]} while Computer Picked {randomShape}.
          Its a tie"""
    )
