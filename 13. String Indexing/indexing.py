# String Indexing is defined as the process of accessing individual characters within a string using their position with the help of [] in Python. Always remember, in every language including Python, the indexing starts from 0. Let's  have a glance at some examples to understand it better:

# Syntax: var_name[start: end: step]. If we only mention var_name[index], it will be considered as first and return the character at that specific index.


my_num = "89433-21442"

print(my_num[0]) # Output: '8'
print(my_num[1]) # Output: '9'
print(my_num[2]) # Output: '4' and so on...




print(my_num[0: 4]) # Here, always remember that the 'end' index is exclusive, so it will return characters from index 0 to 3. Output: '8943'
print(my_num[:4]) # If we don't specify the 'start' index, it will consider it as 0 by default. Output: '8943'


print(my_num[6: ]) # If we don't specify the 'end' index, it will consider it as the length of the string by default. Output: '21442'


print(my_num[-1]) # Negative indexing starts from the end of the string. Here, -1 refers to the last character. Output: '2'




# Let's have a look at step indexing now:

print(my_num[0: 11: 2]) # Here, it will return every 2nd character from index 0 to 9. Output: '843244'
print(my_num[::2]) # If we don't specify 'start' and 'end', it will consider the whole string. Output: '843244'

# Let's print last 5 digits using negative indexing with step:
print(my_num[-5:]) # Output: '21442'


# Let's reverse the string:

print(my_num[:: -1]) # Output: '24412-33498'