# Let's have a timer program using fucntion, 'time' module and 'default arguments' concepts at one place.


# import time


# def count(end, start = 0):
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("Time Up!")


# count(1,  5)


# Now, who doesn't know time start from 0 second, that's why we set the start = 0 as default argument because we don't need to tell again and again that start from 0. 
# And yepp! don't confuse with the position of start and end because by the rules those who have default arguments should be declared at last.




#                                                           =================== Task to do =========================



# 1. Try to make the student group and say that whose marks are more than 100 have grade 'A' otherwise default grade will be as 'C'.
# 2. Generate the random numbers between 1 and 20 and print the numbers if num > 10 then print "Greater than 10" otherwise print a default statement as you want when there is no random num passed to the argument. (I solved this question personally and felt like it would be tough, so I gave the source code but after trying yourselves so hard, refer to this code and after seeing it, write on your own again.)


# import random
# res = random.randint(1, 20)

# def printState(res = 20):
#     if(res > 10):
#         print("Greater than 10")
#     else:
#         print("Lesser than 10")

# printState() <== we can here pass the argument if we want but according to the question this would be your solution.