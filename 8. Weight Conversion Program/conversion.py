"""
Author: Adarsh Soni
Email: soniadarsh487@gmail.com
LinkedIn: https://www.linkedin.com/in/adarsh-soni-881b4139a/
Motto: Stay disciplined, practice daily, and keep improving.
"""

# In this program, we will convert weight between kilograms and pounds based on user input.

weight = float(input("Enter weight: "))
unit = input("Enter the unit in (k) g or (l) bs: ")

if(unit.lower() == 'k'):
    weight_in_pounds = weight * 2.20462
    print(f"{weight} kilograms is equal to {weight_in_pounds:.2f} pounds.")
    
elif(unit.lower() == 'l'):
    weight_in_kilograms = weight / 2.20462
    print(f"{weight} pounds is equal to {weight_in_kilograms:.2f} kilograms.")
    


# ===============================            Important Concepts to learn           ===============================

# 1. We took input in float because weight can be a decimal value (in lbs).
# 2. We used ':.2f' which is called format specifiers, in formatted string to limit the output to 2 decimal places for better readability. 

# Let's have some instances:
# Output is 23.2221233 lbs  --> formatted to 2 decimal places --> 23.22 lbs