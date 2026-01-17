# In Python, Sets are same as lists but there are some key differences them. Sets are unordered and cannot contain duplicates. We can add, remove the elements from it.
# Elements are surrounded by '{}'
# We cannot modify the values in Sets in Python.
# We cannot check the element position by indexing as we used to do in the lists.



fruits = {"apple", "orange", "banana", "coconut"}
print(fruits) # Here output can be seen in any random way becasue we know that set is unordered in Python.
 

 
# print(fruits[0]) # You will get the error: TypeError: 'set' object is not subscriptable


# fruits.add("guavava") # In sets, we can add the new elements in it with the help of the 'add'.
# print(fruits)


# fruits.pop() # It delete the first element but don't confuse the random output again in again in Sets.
# print(fruits)

# fruits.clear() # It delete the first element but don't confuse the random output again in again in Sets.
# print(fruits)




#                ================================================ Important Note =====================================================
# Rest all the methods are same as lists. But remember the output might be different in order. Best to way to see practically, I will recommend that use them with sets yourslef too.



# Let's have a glance to a small project which is storing mobile numbers.

mobile_num_list = set()
how_many_num = int(input("How many numbers you've: "))

for num in range(how_many_num):
    mobile_num = input('Ente your mobile number: ')
    mobile_num_list.add(mobile_num)
   
print(mobile_num_list)



#               ================================================ Explaination =====================================================

# Initially, we declared mobile_num_list and said that okay you contain as of now a empty set.
# We took input from how_many_num
# We ran a loop times how many number the user have. Along with it, we keep asking for input and adding the element in the set also.



#              ===================================================== Task to do ====================================================


# Make a phone directory of 10 numbers and store it in a set.
# Once ready, add, remove the values from the set.
# try to change the values which is not possible.