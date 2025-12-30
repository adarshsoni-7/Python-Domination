# Important Note: We don't cover the data types section yet, but as of now, think it as your Mathematical numbers which are in int, decimal(float in Python). In alphabets, 'a-z' considered as characters.

# In every language, Type-Casting is simply defined as the conversion of the data type into another one like as int to float, float to string, string to int. Let's understand by some examples.

num1 = 13
num2 = 14

result  = (num1 / num2)
print(result)

# Here, the ans is 0.9285 something..... and which is 'float' data type.

# If you have to convert this into a int type result\
    
result = int(num1 / num2)
print(result)


first_name = 1
last_name = 5

very_last_name = str(first_name + last_name)
print(very_last_name) # 6
print(type(very_last_name)) # class 'str'