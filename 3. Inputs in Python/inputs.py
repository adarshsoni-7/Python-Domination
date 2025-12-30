# In Python, "taking inputs" is simply defined as the input which we request to a user to give and then based upon what that user want, we'll perform the operations such as: User give 2 and 3 and say do addition of this numbers. 

# Let's understand by some examples:

# Let's have a interview of Rahul

name = input("Please enter your name: ")
standard = int(input("Please enter your class: "))
roll_num = int(input("Please enter your roll no.: "))

# 'input' is used to take the user info in Python.
# Important Note: Since 'input' returns string everytime in result that's why we use 'int' to convert the given info into another data type based upon what we need.

print("My name is", name, "and I read in", standard, "My roll no is", roll_num)