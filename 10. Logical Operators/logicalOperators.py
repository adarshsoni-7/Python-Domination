# There are three main logical operators in Python: and, or, and not.

# and = returns True if both statements are true as well as False if both statements are false. But if one of the statement is false then it returns False.

# Let's have some examples:

condition1 = int(input("Enter True or False for condition1: "))
condition2 = int(input("Enter True or False for condition2: "))


if condition1 and condition2:
    print("Both conditions are True")

elif (not condition1 and not condition2):
    print("Both conditions are False")
else:
    print("Both conditions should be True")


# Explaination:
# In the above code, if both condition1 and condition2 are True (non-zero values), the first block will execute.

# If both are False (zero values), the second block will execute. Here not is used to negate the conditions simply. For e.g. if the condition1 is False, then not condition1 will be True and same for condition2.

# If one of them is True and the other is False, the else block will execute.


# or  = returns True if one of the conditions is true otherwise false. If both conditions are true or false then it returns true and false respectively also.

if condition1 or condition2:
    print("At least one condition is True")
else:
    print("Both conditions are False")


# Explaination:
# In the above code, if either condition1 or condition2 is True (non-zero value), the first block will execute. If both are False (zero values), the else block will execute.


# not = reverses the logical state of its operand. If a condition is True, then not operator will make it False and vice-versa.

if condition1:
    condition1 = not condition1
    print("Condition1 is now False")
else:
    condition1 = not condition1
    print("Condition1 is now True")


if condition2:
    condition2 = not condition2
    print("Condition2 is now False")
else:
    condition2 = not condition2
    print("Condition2 is now True")




#                                              =======================      Some more examples to understood         =========================


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


# for and operaotor

if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest number")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest number")
else:
    print(f"{num3} is the largest number")
    
    
    
    
    
# for or operator

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's a holiday")


# for not operator, I do not think that you need an example for this since it's very simple to understand.



#                                              =======================      Your task to do        =========================

# 1. Create a program that checks if a user is eligible to vote. The user must be at least 18 years old and a citizen of the country.
# 2. Create a program that checks if a number is within a specific range (e.g., between 10 and 50) or is equal to a specific value (e.g., 100).
# 3. Create a program that toggles the state of a boolean variable (e.g., from True to False or from False to True) using the not operator.