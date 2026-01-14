# Compound Interest Calculator: This program calculates the compound interest on an investment over a specified number of years in which we'll use while loop, may be some new concepts.


# principle = float(input("Enter the principal amount (initial investment): "))

# while principle <= 0:
#     principle = float(input("Enter the principal amount (initial investment): "))
#     if principle <= 0:
#         print("Principal amount must be greater than zero. Please try again.")

# print(principle)


# For this code:
# The Issue:

# The if statement inside the while loop is redundant!

# The while loop already checks principle <= 0

# The if inside also checks the same condition

# The if only prints a message but doesn't prevent re-entry into the loop effectively.

# Result: After printing the error message, it loops back to the while condition without actually re-prompting effectively.

# Corrected Code:

principle = float(input("Enter the principal amount (initial investment): "))

while principle <= 0:
    print("Principal amount must be greater than zero. Please try again.")
    principle = float(
        input("Enter the principal amount (initial investment): "))


rate = float(input("Enter the annual interest rate (in %): "))
time = int(input("Enter the number of years the money is invested: "))

amount = principle * (1 + (rate / 100)) ** time

compund_interest = amount - principle


print(f"The compound interest after {time} years is: {compund_interest:.2f}")


#                                                 =============================== Explanation ===============================

# In this code, we first prompt the user to enter the principal amount. We use a while loop to ensure that the principal amount is greater than zero. If the user enters a value less than or equal to zero, we print an error message and prompt them to enter the amount again. Once we have a valid principal amount, we proceed to ask for the annual interest rate and the number of years the money will be invested. Finally, we calculate the compound interest using the formula and display the result formatted to two decimal places.

#                                                =============================== Important Concepts to learn ===============================

# ** : Exponentiation operator in Python, used to raise a number to the power of another number.

# Let's say you want to calculate 2 raised to the power of 3:
# result = 2 ** 3  # This means 2 raised to the power of 3



#                                                 =============================== Task to do ===============================

# Modify the program to allow the user to choose between compound interest and simple interest calculations.