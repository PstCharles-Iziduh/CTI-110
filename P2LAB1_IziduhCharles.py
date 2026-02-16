# Charles Iziduh
# 2/16/26
# P2LAB1
# Using a library with formulas of circle

import math
# print(math.pi)
# Get a radius from the user as a float

radius = float(input("What is the radius of the circle?: "))
print()

# Calculate Diameter
diameter = 2 * radius

#Display diameter 8.75


print(f"The diameter of the circle is {diameter}")

# Calculate circumference
circumference = 2 * math.pi * radius

# Display circumference
print(f"The circumference of the circle is {circumference:.2f}")

print()

# Calculate area
area = math.pi * math.pow(radius, 2)

# Display the area
print(f"The area of the circle is {area:.3f}")
