# What is Exception Handling in Python?

# Definition:

# Exception handling is a mechanism used to handle runtime errors gracefully so that the program doesn't crash unexpectedly.

# In Python, we use:

# try:
#     # Risky code
# except:
#     # Handle error
# finally:
#     # Always executes

# JavaScript vs Python

# JavaScript
# try {
#     let result = 10 / 0;
# }
# catch(error) {
#     console.log(error);
# }
# finally {
#     console.log("Done");
# }


# Python
try:
    result = 10 / 0
except Exception as e:
    print(e)
finally:
    print("Done")


# We have some common types of Errors in Python :

# ZeroDivisionError = Occurs when a number is divided by zero. try 5 / 0

# ValueError = Occurs when the correct data type is used, but the value is inappropriate. try age = int("twenty")

# TypeError = Occurs when an operation is performed on incompatible data types. try "5" + 5

# IndexError = Occurs when accessing an index that doesn't exist.

# NameError = Occurs when using a variable that has not been defined. try score which is not defined yet

# FileNotFoundError = Occurs when opening a file that doesn't exist. open file.txt which doesn't exist

# AttributeError = Occurs when an object doesn't have the requested attribute or method. try num = 9 then num.append(5), possible on arrays





#                                   =============================== Task todo  =============================== 

# Try to do unexpected operations by wrapping them under try, catch and finally blocks. You may fully eliminate finally block as it executes regardless of there is a error or not