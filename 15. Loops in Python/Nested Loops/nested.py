# In Python, nesting of loops is defined as the loop under a loop which is when we'll use, it will automatically stick to your mind.


# Let's have some example:

for x in range(1, 10):
    print(x)
    
    
print("This is a simple loop.")
print("========================================")


for x in range(4):
    for y in range(1, 6):
        print(y, end="")
        
    print()
    


print("This is the nested loop.")
print("========================================")




# Let's try something else:


row = int(input("Enter the row: "))
column = int(input("Enter the column: "))
symbol = input("Enter the symbol: ")


for x in range(row):
    for y in range(column):
        print(symbol, end="")
        
    print()   
    print("Inner loop ended.")
    
print("Entire loop ended.")



# Let's print the some star patterns


for x in range(row):
    for y in range(column):
        print("*",end="")
    print()


print("===============================================")   
    
for x in range(row):
    for y in range(x + 1):
        print("*", end="")
    print()
    
    
    
print("===============================================")    




for x in range(row):
    for space in range(row - x - 1):
        print(" ", end="")
    for star in range(x + 1):
        print("*", end="")
    print()
  
  
  
print("===============================================") 