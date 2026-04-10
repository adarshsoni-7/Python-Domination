def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))


    print(f"The addition of both the numbers is: {a + b}")

if(__name__ == '__main__'):
    main()





# 🧠 Core Concept: __name__ (Understand This First)
# __name__ is a special built-in variable in Python
# It tells how your file is being used
# If you run the file directly:
# __name__ becomes "__main__"
# If you import the file into another file:
# __name__ becomes the file name


# 🚪 Why we use if __name__ == "__main__"
# It acts like a control switch / gate
# It decides whether the main code should run or not
# Prevents code from running automatically when imported

# Allows the same file to be used as:
# a standalone program
# a reusable module


# ⚡ Key Idea (Very Important)
# This condition controls execution, not access
# Functions are always available (can be imported)
# Only automatic running is controlled


# 💡 Now Understanding Our Code
# A function main() is defined
# Inside it:
# User is asked to input two numbers
# Inputs are converted into integers
# Both numbers are added
# Result is printed

# 🔄 What happens when you run this file directly
# Python sets __name__ = "__main__"
# Condition becomes true
# main() function is called
# User sees input prompts and result

# 🔄 What happens when this file is imported somewhere else
# Python sets __name__ = "filename"
# Condition becomes false
# main() does NOT run automatically
# But:
# You can still use the functions from this file

# 🧠 Mental Model (Easy Way to Remember)
# __name__ == "__main__" → entry gate 🚪
# main() → controller 🧠
# functions → reusable tools ⚙️


# 🔥 One-Line Memory Trick
# “Run this file → execute main”
# “Import this file → don’t execute main”