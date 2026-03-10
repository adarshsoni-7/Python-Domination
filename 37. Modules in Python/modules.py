# A module is simply a file that contains Python code (functions, variables, classes) which you can reuse in another program.
# Think it as a tool-box, Instead of writing everythign again, you import the toolbox and use its tools.


# Let's see some important modules with examples:

# math - Python's basic operators (+, -, *, /) are not enough for advanced calculations like sq. roots, trignometry, factorials, logarithms, etc.

# random - which we used earlier when we were generating random numbers. (Refer Folder. 27)

# datetime - it helps manage the date and time easily.

# os - program often needs to interact with the system, such as: accessing files, navigating directories, creating folders, automating tasks. This module lets Python communicate with the operating system.

# sys - sometimes, we need info about the Python runtime environment, such as: command-line arguments, system configuration, Python version. This module provides system-level interactions.


# collections - sometimes normal lists and dictionaries are not powerful enough. The collection module provides specialized data structures like: Counter, defaultdict, deque # end match

# itertools - when working with large datasets, writing loops manually becomes inefficient. This module provides powerful looping utilities.

# json - most web APIs and databases allows Pyhton to convert data to and from JSON(Java Script Object Notation).



# Now, it's time to feel real with some examples of each of them here:



# import math

# print(math.sqrt(25)) # square root
# print(math.factorial(5)) # factorial
# print(math.pi) # value of pi


# import random
# print(random.randint(1, 10)) # random number
# print(random.choice(["A", "B", "C"])) # random choice
    

# import datetime

# now = datetime.datetime.now()

# print(now) # today's info
# print(now.year) # current year
# print(now.month) # current month
# print(now.day) # current day



# import os

# print(os.getcwd()) # tells us currently which directory we are in
# # print(os.listdir()) # tells us how many folders with their name


# from collections import Counter # <=== It means from the collections module, use Counter method. By using this we don't need to later say like "collections.Counter"

# data = ["apple", "banana", "grapes", "papaya", "apple", "pomegranate", "grapes"]
# count = Counter(data)

# print(count)





#                                             ==================== Follow Up Message ==============================

# The modules for which I did not provide the examples are advanced. At this stage, it's not necessary for you to learn them in detail. We'll assurely discuss in upcoming modules.

# Also, don't feel overwhelmed by seeing all these modules together since you are entering in a intemediate phase of Python. The key is to learn things step by step. Python modules are actually very easy to understand; we just need consistent practise of try everyday one new method from any module to become comfortable with them.


