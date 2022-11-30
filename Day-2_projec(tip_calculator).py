# Write a program that takes the total bill of a group of people and then ask them the tip they would like to give. Ask the number of people that are to split the bill and display the amount each of them is to pay

print("Welcome to the tip calculator.")
actual_bill = float(input("what was the actual bill?\nGHC "))

percentage_tip = float(input("What percentage tip would you like to give?\n"))
percentage_tip = (percentage_tip / 100) * actual_bill

number_of_people = int(input("How many people are to split the bill?\n"))

total_bill = actual_bill + percentage_tip
amount_for_each = "{:.2f}".format(total_bill / number_of_people)

print(f"Each person should pay: GHC {amount_for_each}")

