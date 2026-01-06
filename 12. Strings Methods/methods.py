"""
Author: Adarsh Soni
Email: soniadarsh487@gmail.com
LinkedIn: https://www.linkedin.com/in/adarsh-soni-881b4139a/
Motto: Stay disciplined, practice daily, and keep improving.
"""

# Before we dive deep into the string methods, let's have a glance of what is a string and what is the method in Python.

# A string is a sequence of characters enclosed within single quotes, double quotes, or triple quotes. For example: 'Hello', "World", '''Python'''.
# A method is a function that is associated with an object. In Python, strings have built-in methods that allow you to perform various operations on them.

# Important Note: Don't worry for objects, functions since we have covered them in the upcoming chapters.



# Let's explore the factories of the string methods in Python since there are a lot of them. We will cover the most commonly used string methods here.


 # 1. len: returns the length of the string.
string1 = "Hello, World!"
print(f"The length of the string is: {len(string1)}")  # Output: 13


# 2. find: returns the first index of the substring if found, otherwise -1.
string2 = "Hello, World!"   
print(f"The first index of 'o' is: {string2.find('o')}")  # Output: 4


# 3. rfind: returns the first index of the substring from the end if found, otherwise -1.
string2 = "Hello, World!"   
print(f"The last index of 'o' is: {string2.rfind('o')}")  # Output: 8



#4. capitalize: capitalizes the first character of the string.
string3 = "hello, world!"
print(f"The capitalized string is: {string3.capitalize()}")  # Output: "Hello, world!"


# 5. upper: converts all characters in the string to uppercase.
string4 = "hello, world!"
print(f"The uppercase string is: {string4.upper()}")  # Output: "HELLO, WORLD!"


# 6. lower: converts all characters in the string to lowercase.
string5 = "HELLO, WORLD!"
print(f"The lowercase string is: {string5.lower()}")  # Output: "hello, world!"


#7. isdigit: checks if all characters in the string are digits and returns True when all are digits otherwise False.
string6 = "12345"
print(f"The string is a digit: {string6.isdigit()}")  # Output: True

string6 = "Adarsh Soni"
print(f"The string is a digit: {string6.isdigit()}")  # Output: False


# 8. isalpha: checks if all characters in the string are alphabetic and returns True when all are alphabetic otherwise False.
string7 = "Adarsh Soni"
print(f"The string is alphabetic: {string7.isalpha()}")  # Output: False Wait..... 🤨Why? Because there is a space in between the name which isn't an alphabetic character.

string7 = "AdarshSoni"
print(f"The string is alphabetic: {string7.isalpha()}")  # Output: True


# 9. count: returns the number of occurrences of a substring in the string.
string8 = "Hello, World! Hello, Universe!"
print(f"The number of occurrences of 'Hello' is: {string8.count('Hello')}")  # Output: 2


phone_num = "123-456-7890"
print(f"The number of occurrences of '-' is: {phone_num.count('-')}")  # Output: 2


# 10. replace: replaces all occurrences of a substring with another substring.
string9 = "Hello, World!"
print(f"The replaced string is: {string9.replace('World', 'Python')}")  # Output: "Hello, Python!"


# These are the some of the most commonly used string methods in Python. There are many more methods available that you can explore in the official Python documentation or you can refer to:
print(help(str))