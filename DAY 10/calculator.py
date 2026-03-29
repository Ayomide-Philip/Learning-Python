import platform
import subprocess


def performAnOperation(firstNum, operator, lastNum):
    if operator == "+":
        return float(firstNum) + float(lastNum)
    elif operator == "-":
        return float(firstNum) - float(lastNum)
    elif operator == "*":
        return float(firstNum) * float(lastNum)
    elif operator == "/":
        return float(firstNum) / float(lastNum)
    return None


def clearScreen():
    if platform.system().lower() == "windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


calculationInProgress = True
firstNumber = 0
while calculationInProgress:
    if firstNumber == 0:
        firstNumber = input("What's the first number?:")
    print(
        """
    +
    -
    *
    /
    """
    )
    pickAnOperator = input("Pick an Operator:")
    nextNumber = input("Whats the next number?:")
    answerFromOperation = performAnOperation(firstNumber, pickAnOperator, nextNumber)
    if answerFromOperation is None:
        print("Invalid Operation")
        calculationInProgress = not calculationInProgress
    else:
        print(f"{firstNumber} {pickAnOperator} {nextNumber} = {answerFromOperation}")
    wouldYouContinue = input(
        "Type 'y' to continue calculating with , or type 'n' to start a new calculation:"
    ).lower()

    if wouldYouContinue == "y":
        firstNumber = answerFromOperation
    elif wouldYouContinue == "n":
        firstNumber = 0
        clearScreen()
    else:
        print("Invalid Input, Quitting!")
