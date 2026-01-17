# For Loops in Python is very concept to understand. It is defined as -- "When we know that okay, the loop gonna iterate 5, 6, as per our requirement, we use for loops.


# Let's have a glance on some instanes:

# 1. Let's print the numbers from 1 to 10 using for loop


# for count in range(1, 11):
#   print(count)

#                                         ================================= Explaiantion   =============================================


# count is a iterator in this loop which will iterate 10 times because 11 is exclusive for which we discussed in while loops. range(start, end, step) qnd the count is starting from 1 to 10. If there not exixts the steps, by default a single will be conisdered in Python.

# 1. Let's print the numbers from 10 to 1 using for loop


for count in reversed(range(1, 11)):
    print(count)


for count in range(10, 0, -1):
    print(count)


#                                         ================================= Explaiantion   =============================================


# We can use reversed range in order to print the numbers in reverse fashion.
# We can do one more thing that looks better than any in-built function which is we can start the loop from 10 finish at 1 and put a -1 in order to make steps backwards in theb loop.


for i in range(10, 0, -1):
    print(5 * i)
