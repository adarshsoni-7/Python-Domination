# In Pyhton, list comprehension is defined as the short-form of how we write the for loop and under some conditions, we do something.
# Syntax: [ {:expression} for {:item} in {:list} if {:conditional} ]

# Let's see the key difference between both:



# doubles = []
# for num in range(1, 11):
#     doubles.append(num * 2)
    
# print(doubles) 
    
    
# Above was a traditional way of how we write loops. But let's see now shortcut but right now we won't use conditional for better understanding:

# doubles = [num *2 for num in range(1, 11)]
# print(doubles)


# We can see clearly here that how only 2 lines of code did the same for which we need 3-5 lines. Well... this is a power of list comprehension.
# Now, we see by writing the code by following full syntax by applying some condition: 


# grades = [89, 90, 21, 32]
# passing_grades = [grade for grade in grades if grade >= 33]

# print(passing_grades)
 
# Above, we can clearly see that the grades >= 33 has filtered out and stored in passing_grades list and when we print it, it will give me the list of it.



# Let's see more examples:


# even_numbers = [even_num for even_num in range(2, 21) if even_num % 2 == 0]
# print(even_numbers) we will have all the even numbers between 2 and 20






# natural_with_squares = [num * num for num in range(1, 21)]
# print(natural_with_squares) we will have the squares of all the numbers from 1 to 20 (remember 21 is exclusive)






#                                       ===================================== Task to do =========================================

# 1. Try to make a list of odd numbers using list comprehension method.
# 2. Try  to make a list of prime numbers using list comprehension method.
# 3. Try to make a list by applying logical operators.
# 4. Try to make a list in which from 1 to 100 the numbers which are divisible by 5 or 7 should be in the list.