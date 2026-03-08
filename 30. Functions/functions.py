# In Python, functions are nothing but a piece of code which prevents the repetitive code in the entire file and make our file more readable. In other words, we can say that the functions are defined as the block of code in which reuseable code is written.
# 1. We use 'def' to declare the function which is read as 'definition'.

# 2. Then we pass one, two or more than two parameters to 'function' that tells the 'function' that you have perform operations in them ---- simply print it, add it, subtract it or anything based on what you told to do under the 'function'.

# 3. Then we call it. Basically it means that we tell the function that "Yess! Now run!" with passing our arguments to it -- with what values our cod gonna use to perform the operations. 

# Let's see the wrong way to code and how the "functions" make them right and your code cleaner:

# Wrong way:

# print("Hey Steve! Happy Diwali!")  
# print("Hey Mark! Happy Diwali!")  
# print("Hey John! Happy Diwali!")  

# We had to write the same sentence three times, it doesn't matter you copy or paste because it take equal time too. Now.. what if I want you to write this same message to your all 50 friends. You cooked! Let's see the right and efficient way: 


# Right way:

# def func(name, greetings):
#     print(f"Hey! {name} {greetings}")
    
# func("Steve", "Happy Diwali!")


# Now, here you have to only put your friends' name and this will send the greeting messages on your behalf faster. Well, this is the crystal clear example of why we use function over repeated print statement.



# Let's make a cafe_menu again but this time, we'll use functions to do everything :

# def menu(name, price):   <== here two parameters
#    print(f"Have some {name} of {price}")  we simply print them here as our greeting message.
    
# print("============     YOUR MENU       ============")
# print() # This skip a line. Nothing more than this.
    
# menu("coffee", 99)  <== here we call the function with passing the arguments to it. Arguments are the values that we pass to the function when we call it. Here, "coffee" is the argument for the parameter 'name' and 99 is the argument for the parameter 'price'.
# menu("tea", 39)
# menu("pizza", 199)





# Let's see a very useful keyword 'return' you can assume as of now only a return statement at end of the function. Well... Let's see some examples:


# def add(num1, num2):  <== parameters
    # res = num1 + num2 add two values
    # return res return the 'res' as final value

# result = add(20, 30)
# print(f"Addition of 20 and 30 is: {result}")

# We have to store the result and then print because function returns something





#                                                               ======================= CALCULATOR =====================================


# def calculate(num1, num2):
#     addition = num1 + num2
#     subtraction = max(num1, num2) - min(num1, num2)
#     multplication = num1 * num2 if num1 > 0 and num2 > 0 else print("Either of the number should be non-zero.")
#     division = (num1 // num2)
    
#     return addition, subtraction, multplication, division



# print(f"All the arithmatic operations are: {calculate(10, 5)}")
 
 
 
#                                                              ======================= Task to do =====================================


# 1. Try to make the functions for every arithmatic operation seperately and print the result.
# 2. Try to make the function in which you have to perform the all lists, sets and tuples methods we have discussed so far.
# 3. Try to make a card shuffling machine using function and 'random' module.
# 4. Try to make a function which returns your full name in capital letters.