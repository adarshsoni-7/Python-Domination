#  Scope resolution is the process Python uses to decide where to look for a variable when it is used in a program.
# When Python sees a variable, it searches for it in a specific order called LEGB rule.

# L => Local, E => Enclosing, G => Global, B => Built-in

# Python first search for local variable followed by other. If there is not any local, it will print the value of the enclosed one and so on...


# Let's have some examples:

# def func1():
#     x = 1
#     print(x)
    
# def func2():
#     x = 2
#     print(x)
    
    
# func1()
# func2()


# Here, since 'x' is in the local variable, value of both 'x' printed here.



# def func1():
#     x = 5
    
#     def func2():
#         print(x)
#     func2()
    
# func1()

#  Saw the magic, what did this happen ? Because func2 is declared under func1 whose intial value is 5 and then same value can be easily accessible to This is known an enclosed one.

# In this code, Python first search for local varibale which it could not be find, then it started search for enclosed one and track it, print it.




# Let's have some instances of built-in scope resolution:

from math import e 

# def func1():
#     print(e) 
    
    
# e = 10
    
# func1()

# Here, you'll see that 3 is printed. Because we have global version of e and local version of e. Since global is come before built-in that's why we ended up the value 3.       Don't panic, try to understand precisely, look at each line of code using your eagle's eyes.


# Always remeber Local => Enclosed => Global => Built-in
# Even if there is a local variable so even if there is a global variable too, value of 'local' one will be printed.