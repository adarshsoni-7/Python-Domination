# In Python, scope refers to the region or part of a program where a variable can be accessed or used.
# In simpler words, it tells a variable is visible and usable in the program.


# Python mainly has two common scopes you see first: 1. Local Scope and 2. Global Scope
# Local Scope = a variable which can be used inside of the function only.
# Global Scope = a variable which can be used 'anywhere' in the program -- under function, making lists, tuple etc.

# Let's have some example to understand the local scopes:


# def func():
#     x = 4 <== here x is in local scope inside the function
#     print(x)

# func()

# print(x)  end up with error: NameError: name 'x' is not defined

# In the function, 'x' is in a local scope means it can be used only inside of the function and if we try to use it in outside, it will give the NameError:'x' is not defined.


# def greet():
#     message = "Happy Birthday"
#     print(message)

# greet()
# print(message) same error because 'message' is inside of 'greet' and we are trying to print it outside of the function.


# Let's have some example to understand the global scopes:


# x = 10 here x is declared as global variable not inside anything so it can be used anywhere in anyway.

# def show():
# print(x) print the value of global variable x


# show()


#                                               ====================== Task to do ===============================

# Putting your reasoning, answer these questions:

# 1:

# x = 10

# def show():
#     print(x)


# show() What will be the printed and why ?


# 2:

# def test():
#     a = 10

#     print(a)


# test() What type of scope does 'a' have ?


# 3:

# def dispaly():
#     msg = "Hello!"

# dispaly()
# print(msg) Will this code run or give an error ? Explain why.


# 4:


# value = 20

# def change():
#     value = 50
#     print(value)

# change()

# print(value) What will be the output and tell yourself why these values printed like this.


# 5:

# num = 50

# def test():
#     print(num)
#     num = 20
    
# test() Will this code run successfully ? If not, why ?

