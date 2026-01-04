# This is a simple calculator program that performs basic arithmetic operations.

operand = input("Enter the operation you want to perform (+, -, *, /): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if operand == '+':
    result = num1 + num2
    print(f"The addition of both numbers is {result}")
elif operand == '-':
    result = num1 - num2
    print(f"The subtraction of both numbers is {result}")

elif operand == '*':
    result = num1 * num2
    print(f"The multiplication of both numbers is {result}")
elif operand == '/':
    result = num1 / num2
    print(f"The division of both numbers is {result}")
else:
    print("Invalid operation! Please enter one of +, -, *, /.")
    
    
    


# ===============================      Task to do    ===============================
# 1. Handle zeroes while division.
# 2. Handle subtraction resulting in negative numbers.
# 3. Most importantly, what can we do in this code very firstly so that later on we don't need to check the conditions while division or multiplication or any other operation? Think and implement it.
