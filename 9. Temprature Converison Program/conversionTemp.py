"""
Author: Adarsh Soni
Email: soniadarsh487@gmail.com
LinkedIn: https://www.linkedin.com/in/adarsh-soni-881b4139a/
Motto: Stay disciplined, practice daily, and keep improving.
"""

# In this program, we will convert temperature between Celsius and Kelvin based on user input.
# Before we dive deep further, let's understand the conversion formulas:
# 1 °C = 273.15 K
# 1 K = -273.15 °C

# Celsius to Kelvin: K = C + 273.15
# Kelvin to Celsius: C = K - 273.15


initial_temp = float(input("Enter the temperature: "))
unit = input(
    "Is this temperature in Celsius or Kelvin? (C/K): ").strip().upper() # .upper is optional


if (unit == 'C'):
    kelvin_temp = initial_temp + 273.15
    print(f"{initial_temp} °C is equal to {kelvin_temp} K")
elif (unit == 'K'):
    celsius_temp = initial_temp - 273.15
    print(f"{initial_temp} K is equal to {celsius_temp} °C")
else:
    print("Invalid input! Please enter 'C' for Celsius or 'K' for Kelvin.")


# =======================================            Important Concepts to learn          ===========================================


# 1. .strip() is used to remove any leading or trailing whitespace from the input string for e.g if the I/O is "   c" then it is converted to "c".

# 2. .upper() is used to convert the input string to uppercase for e.g if the I/O is "c" then it is converted to "C". (optional)
