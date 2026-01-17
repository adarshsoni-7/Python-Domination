# In Python, lists are the collection of different values in which we can add values of any data-type. Think it of a real life lists of any heading in which you add your goals, your exercise routines, your journaling and more......

# In lists, we can add, remove and modify any value. We can also add duplicates in the lists.

# Let's dive deep more into it:


# fruits = ["apple", "banana", "grapes", "pineapple"] # This is a simple collection(lists) of fruits.

# print(fruits[0]) # Output: apple since indexing is always starting from zero.
# print(fruits) # ['apple', 'banana', 'grapes', 'pineapple']


# fruits[0] = "peach"
# print(fruits) # Output: ['peach', 'banana', 'grapes', 'pineapple'] apple is replaced by peach at 1st index.


# print(fruits[:3]) # Output: ['peach', 'banana', 'grapes'] first 3 elements
# print(fruits[::-1]) # Output: ['pineapple', 'grapes', 'banana', 'peach'] in reverse fashion



# fruits.append("pomegranate") # append is used to add the elements in the lists.
# print(fruits) # Output: ['peach', 'banana', 'grapes', 'pineapple', 'pomegranate']


# fruits.remove("pomegranate") # remove is basically used to remove the elements from the end. Remember (from end) is important.
# print(fruits) # Output: ['peach', 'banana', 'grapes', 'pineapple']


# fruits.insert(3, "mango")
# print(fruits) # Output: ['peach', 'banana', 'grapes', 'mango', 'pineapple']


# fruits.pop() # delete the element from the end. Remember (from end) is important
# print(fruits) # Output: ['peach', 'banana', 'grapes', 'mango']



vegetables = ["Guard", "Reddish", "Capsicum", "Onion", "Coriander", "Beet-root"] 
# vegetables.reverse() # Output is basically in a reverse fashion of the index in which the values placed in.
# print(vegetables)
# vegetables.sort() # Output: ['Beet-root', 'Capsicum', 'Coriander', 'Guard', 'Onion', 'Reddish'] based upon the alphabet position.
# print(vegetables)

# # If we want to reverse the lists based on the alphabets, we should sort the lists. Now every is in the order of English alphabets, after reversing it, we'll have a list which is reversed in terms of alphabets.

# vegetables.sort()
# vegetables.reverse()
# print(vegetables) # Output: ['Reddish', 'Onion', 'Guard', 'Coriander', 'Capsicum', 'Beet-root']


# vegetables.clear() # Output: [] 

# print(vegetables.index("Onion")) # Output: The index of given element which is 3



# print("Reddish" in vegetables) # gives a Boolean result True or False. True this time since Reddish is present in the lists at 1st index.

# vegetables.pop() # delete the elements from the end


# print(vegetables.count("Reddish")) # Output: number times of that element is present in the list which is as of now 1.  
# print(help(vegetables)) # You'll see tons of methods and its usage.




# Let's have a list in which firstly we have nothing and based on the input we will have some movie names.


# movie_name = input("Enter the movie name: ")
# bollywood_movies = []

# for x in movie_name:
#     bollywood_movies.append(x)
    
    
# print(bollywood_movies)



# these_much_movies = int(input("Enter how much movies you like: "))
# bollywood_movies = []

# for movie in range(these_much_movies):
#     my_movie = input("Enter the movie name: ")
#     bollywood_movies.append(my_movie)

# print(bollywood_movies)



#                                                       =============================== Explaination  ============================================


# We took input from user for how many movies do they like to watch.
# Initially, we have a empty list.
# We ran a loop the these_much_movie times to have a input for all the movies.
# Under the loop, we have to ask the user for movie.
# We add that movie in the list one by one.
# Eventually, we printed out bollywood movies list.




#                                                       =============================== Task to do   ============================================

# 1. Add a feature which skips the movie which are older than 2000. Research these topics in ChatGPT or refer my demo prompts.


# Make a students list in which students are in the list by following these:
# a. who have marks <= 15 should be in fail list. 
# b. who have marks <= 33 should be in pass list. 
# c. who have marks >= 50 should be in average list. 
# d. who have marks >= 70 should be in good list. 
# e. who have marks >= 85 should be in excellent list. 
# f. who have marks >= 95 should be in outstanding list. 

 
# Before having a look at the solution, trying yourself not only build your confidence but also you have that capability to understand how code works.  


# student = input("Enter the student name: ")
# marks = int(input("Enter the student's marks: "))


# if marks <= 15:
#     fail_list = []
#     fail_list.append(student)
#     print("You are fail.")
#     print(fail_list)
    
# elif marks <= 33:
#     pass_list = []
#     pass_list.append(student)
#     print("You are pass.")   
#     print(pass_list)
    
# elif marks <= 50:
#     average_list = []
#     average_list.append(student)
#     print("You are average.") 
#     print(average_list)
    
    
# elif marks <= 70:
#     good_list = []
#     good_list.append(student)
#     print("You are good.") 
#     print(good_list)
    
# elif marks <= 85:
#     excellent_list = []
#     excellent_list.append(student) 
#     print("You are excellent.")
#     print(excellent_list)
    
# else:
#     outstanding_list = []
#     outstanding_list.append(student)
#     print("You are outstanding.")
#     print(outstanding_list)








#                                       ======================= Thinks to add in this project =============================

# a. Reduce the line of code by logical operators (and, or, not)
# b. Eventually, make the lists of every student whether he is pass or not and print it.