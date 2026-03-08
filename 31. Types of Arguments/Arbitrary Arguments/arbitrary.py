# In Python, arbitrary arguments are => *args & **kwargs means arguments and keyword arguments.



# Let's understand why we need *args even though we have enough resource to use:


# def add(*args):
#     print(type(args))
#     return sum(args)

# print(add(1, 2))
# print(add(1, 2, 3))


# Here, when we tried to pass more than declared parameters in the function, we were given a error of "add() takes 2 positional arguments but 3 were given". To by pass the problem where we have to pass only those much arguments as the function signature have, we use *args.

# With *args we don't need to worry about how many arguments we give to the function.
# *args store all the passed arguments in the form of a tuple.




# Working of *kwargs is same as *args but in **kwargs you can pass keywords as arguments and **kwargs store all these keyword in the form of a dictionary.


# def student_info(**kwargs):
#     print(type(kwargs))
    
#     for key, value in kwargs.items():
#         print(key, "", value)
        


# student_info(name = "Adarsh", section = "13", city = "Noida")



#                                           ============================= CLEAR DIFFERENCE ===================================


# *args => Tuple    Input style => positional usually what we use very first while passing the arguments to the function. Example func(1, 2, 3)
# **kwargs => Dictionary  iInput style => Keywords. Example func(a = 1, b = 2)


# Le's use both in one place

def demo(*args, **kwargs):
    print("Args", args, "<=== see it's in a form of tuple")
    print("Kwargs", kwargs, "<=== see it's in a form of dictionary")
    
demo(1, 2, 3, name = "Adarsh", role = "Engineer")