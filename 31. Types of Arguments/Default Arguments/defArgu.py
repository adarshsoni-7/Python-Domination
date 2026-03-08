# In previous module, we learned the functions, parameters, arguments. 
# Default argument = A default value for certain parameters. It is used when that argument is omitted.
# There are four types of default arguments => 1. Positional(what we have been using) 2. default(w eunderstood how it works) 3. keyword and 4. arbitrary 

# Let's see some example


def addition(num1, num2, num3 = 0):
    return num1 + num2 + num3



print(addition(2, 3))


# Think for a while that what if you want two numbers and ignore num3. That's exactly
# where the default arguments are really for.



# Let's make tax telling machine.


# def tax(price, discount = 0, tax = 3.5):
#     after_tax = (int)(price * (1 - discount) * (1 + 50))
#     return after_tax


# res_price = tax(300000)
# print(f"My car's total price after tax is : {res_price}")


#                                           ============================= EXPLAINATION ====================================

# We told that for car's price, there's no discount there and 3.5% tax will be applied everytime when we pass the price to it. Later, we can also set the discount and tax manually but but but here most important thing is when you don't pass the value manually, it consider its default value we set.





 