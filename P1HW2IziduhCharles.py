# Charles Iziduh
# 2/18/26
# P1HW2 Assignment
# Python program that does some basic math on numbers that are entered.
# This program calculates and displays travel expenses
print("This program calculates and displays travel expenses")
# Get Budget from user 
Initial_Budget = int(input("Enter Budget: "))
# Get travel destination from user
Location = input("Enter your travel destination: ") 
# Get expence on gas 
Fuel = int(input("How much do you think you will spend on gas? "))
# Get Approximately, how muuch will you need for accmodation/hotel?
Accomodation = int(input("Approximately, how muuch will you need for accmodation/hotel? "))
# Get Last, how much do you need for food?
Food = int(input("Last, how much do you need for food? "))

print("-------------Travel Expenses--------------")
print(f"location: {Location}")
print(f"Initial_Budget: {Initial_Budget}")
print(f"Fuei: {Fuel}")
print(f"Accomodation: {Accomodation}")
print(f"Food:{Food}")

# Get Remaining Balance
Remaining_Balance =  Initial_Budget - Fuel - Accomodation - Food
print(f"Remaning Balance: {Remaining_Balance}")
