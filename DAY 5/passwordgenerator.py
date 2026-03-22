import random

alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "$", "(", ")", "<", ">", "@", "/", ":", ";", "[", "]", "=", "#", "&"]
print("Welcome to my password Generator")

letterInPassword = int(input("How Many letters would you like in your password?\n"))

symbolInPassword = int(input("How many symbols would you like in your password?\n"))

numberInPassword = int(input("How many numbers would you like in your password?\n"))

passwordList = []

for i in range(0, letterInPassword):
    passwordList.append(random.choice(alphabet))

for i in range(0, symbolInPassword):
    passwordList.append(random.choice(symbols))

for i in range(0, numberInPassword):
    passwordList.append(random.choice(number))

print(passwordList)
randomPasswordList = []

for i in range(0, len(passwordList)):
    randomPass = random.choice(passwordList)
    randomPasswordList.append(randomPass)
    passwordList.remove(randomPass)

print(randomPasswordList)
passwordInString = ""

for i in randomPasswordList:
    passwordInString += i

print(passwordInString)
