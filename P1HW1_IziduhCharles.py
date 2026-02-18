# Charles Iziduh
# 2/15/2026
# Example similar to P1HW1
# Get user input and convert to a specific datatype


# Get 2 number from the user and make the first the base value and the second number the exponent.Then print the string showing the base, exponent, and the result.

print()
print (f"-----Calculating Exponents-----")
print()
base_value = int(input("Enter an integer as base value: "))
exponent = int(input("Enter an integer as the exponet: ")) 

# exponent = num2
# base_value and num1
# result = num1 * * num2
#result = base_value ** exponent
result = base_value ** exponent
print(f"{base_value} raised to the power of {exponent} is  {result} !!!")

# Get 3 numbers from the user and make the first the statng integer the 2nd the added integer and the 3rd the subtracted integer find their sum

print()
print(f"------Addition and Subtraction-----")
print()
val1 = int(input("Enter a starting integer: "))
val2 = int(input("Enter an integer to add: "))
val3 = int(input("Enter an integer to subract: "))
# Addition and Subtraction
# sum = val1 + val2 - val3

sum = val1 + val2 - val3

print()
print(f"{val1} + {val2} - {val3} is equal to {sum}")