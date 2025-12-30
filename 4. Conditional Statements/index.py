# If we try to understand by taking the real analogy, conditional statement is nothing but if the given condition for e.g 2 == 2 & so on.... is true then perform it's addition or else perform it's multiplication. Let's try to understand by some instances:


num1 = 13
num2 = 15

if(num1 == num2):
    print(num1 + num2)
else:
    print(num1 * num2)
    
    
# The result was 195 because 13 is not equal to 15

# Let's take one more little bit big instance


# Since we didn't cover the strings but as of now just remember that the group of characters is known as string.

name1 = "Seth Adarsh"  
name2 = "Seth Anamika"
lenOfName1 = len(name1)
lenOfName2 = len(name2)

if(lenOfName1 == lenOfName2):
    print("The length of both strings is equal.")
elif (lenOfName1 > lenOfName2):
    print("The length of the first name is greater than second one.") 
else:
    print("The length of both strings isn't equal.")