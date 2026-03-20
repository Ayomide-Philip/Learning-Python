print("Welcome to the tip calculator!!")

total_bill = float(input("What is the total bill? \n $"))

tip_amount = int(input("How much tip do you want to give? \n"))

number_of_people = int(input("How many people is sharing the bill? \n"))

# get the tip amount
total_tip_amount_payed = (tip_amount / 100) * total_bill
total_tip_amount_payed = total_bill + total_tip_amount_payed

# each person amount to pay
amount_to_pay = total_tip_amount_payed / number_of_people

print(f"Each person should pay : ${round(amount_to_pay, 2)}")
