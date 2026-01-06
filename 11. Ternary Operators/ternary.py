"""
Author: Adarsh Soni
Email: soniadarsh487@gmail.com
LinkedIn: https://www.linkedin.com/in/adarsh-soni-881b4139a/
Motto: Stay disciplined, practice daily, and keep improving.
"""

# Ternary Operators in Python are just simple one-liner conditional statements. They are used to evaluate something based on a condition being true or false.


age = int(input("Enter your age: "))

# Using Ternary Operator

status = "Eligible to vote" if age >= 18 else "You are over age" if age > 60 else "Not eligible to vote"


print(status)