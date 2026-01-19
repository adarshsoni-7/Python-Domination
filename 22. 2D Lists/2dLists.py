# Two-dimensional lists are simply lists under list. It's not limited to lists instead we can also make sets of sets, tuples of tuples and even tuples of sets and more......
# You can think of 2D lists as real life matrix in Maths ---- rows and columns

# Let's have some example:


fruits = ["apple", "banana", "grapes"]
vegetables = ["guard", "spinach", "tomato"]
sweets = ["kaju-katli", "chenaa", "gud-jalebi"]


groceries = [fruits, vegetables, sweets]
print(groceries[0][0]) # Here, when we can access elements under list of lists by putting double []. Output: apple.


# Here, now groceries is the list of lists in which let's have a traversal:

# for collection in groceries:
#     print(collection, end= " ")
     
    
# Output:

# ['apple', 'banana', 'grapes']
# ['guard', 'spinach', 'tomato']
# ['kaju-katli', 'chenaa', 'gud-jalebi']



# Let's have one more loop to print the elements of the lists.

for collection in groceries:
    for element in collection:
        print(element, end= " ")
        
        
        
        
        
#                                   ==================================== Task to do =======================================

# 1. Access the random elements of the list by using [], [][].
# 2. Add, remove and modify the lists under list
# 3. Make a 2D list of row and column in which there should be 5 rows and columsn of students and their marks respectively.
