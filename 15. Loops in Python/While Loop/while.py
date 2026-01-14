# While Loops is Python: It's defined the particular piece of code that is repeatedly executed until a certain condition is met. Iteration is the process of repeating a set of instructions a certain number of times or until a specific condition is met. Most importantly, when we don't know the number of iterations in advance, we use while loops.

# Let's have some examples of while loops in Python.


# Let's see a code where until the user types "exit", the program will keep adding two numbers.


user_input = input("Enter the command: ")


while user_input.lower() != "exit":
    print(f"The sum of 5 and 3 is {5 + 3}")
    user_input = input("Enter the command: ")


print("Exited the loop. Goodbye!")

#                                                    =============================== Explanation ===============================

# In this code, we start by asking the user to enter a command. Then we wrote a while loop that checked if user enter exit, we will exit the loop and print the message otherwise we'll keep adding 5 and 3 and printing the result.


unique_num = int(input("Please enter a number: "))


while unique_num > 0:
    print(f"Your number is greater than zero: {unique_num}")
    unique_num = int(input("Please enter a number: "))

print("You entered a number which is less than or equal to zero.")


#                                                    =============================== Explanation ===============================

# In this code, we start by asking the user to enter a number. Then we wrote a while loop that checked if user enter a number which is greater than zero, we will exit the loop and print the message otherwise we'll keep asking for a number and printing the result.


# Let's see another example where we use a while loop to count down from 5 to 1.


num = int(input("Enter a number to start countdown: "))

while num > 0:
    print(f"Num is still greater than zero: {num}")
    num -= 1  # num = num - 1

print("Countdown finished!")


#                                                   =============================== Explanation ===============================
# Here, we start with taking user input a number to start the countdown. The while loop continues as long as num is greater than 0, printing the current value of num and  decrementing it by 1 in each iteration. When num reaches 0, the loop ends and we print "Countdown finished!"


#                                                   =============================== Explanation ===============================

# 1. Print the numbers from 1 to 10 using a while loop.
# 2. Print the even numbers between 1 and 10 using a while loop. (Hint: Use the modulus operator % to check for even numbers)
# 3. Print the numbers from 1 to 50 by jumping 5 numbers at each iteration using a while loop. (Hint: Use the += operator)
# 4. Print the multiplication table of a 5 or you can  take your desired one using a while loop. (Hint: Multiply the number by the iteration count)
