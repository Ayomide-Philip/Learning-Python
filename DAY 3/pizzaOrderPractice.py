print("Welcome to Pizza Deliveries!!")
size = input("What size do you want? S, M or L:\n").upper()
pepperoni = input("Do you want Pepperoni on your pizza? Y or N:\n").upper()
extra_cheese = input("Do you want Extra cheese? Y or N:\n").upper()

price = 0

# price based on the size they pick
if size == "S":
    price += 15
elif size == "M":
    price += 20
elif price == "L":
    price += 30

print(price)
