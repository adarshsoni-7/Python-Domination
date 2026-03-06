# In Python, dictionaries are basically collection of a pairs of {key: value} (which is object in JS). They are ordered and changeable but here only unique key value pairs are allowed.

# Let's have some examples to understand more precisely.


capitals = {"India": "New Delhi",
            "Jammu & Kashmir": "Srinagar",
            "Bangladesh": "Dhaka"
            }

# Here capitals is a variable in which all the key:value pairs are stored.
# Here, India = key and New Delhi = value.


# print(dir(capitals)) tells us many of the dictionaries's methods 
# print(dir(capitals)) tells us syntax of the dictionaries's methods 


# print(capitals.get("India"))  Here, we use .get("my_key") to find the value of our key which is in this case "New Delhi"
# print(capitals.get("Bangladesh")) Here, we use .get("my_key") to find the value of our key which is in this case "Dhaka"


# What if we try to access that key which has not any value...... Well, in that case, we'll have None in Python.

# print(capitals.get("Sri Lankaa")) We'll have None.

# if capitals.get("Sri Lanka"):
#     print("Capital is present.")
    
# else: 
#     print("Capital isn't present") 


# What if we try to change the values of keys under some meaningful condition.... We use .update({our_key: new_value}) ! Carefull! about "{}" 
# capitals.update({"India": "Sri Lanka"}) # {'India': 'Sri Lanka', 'Jammu & Kashmir': 'Srinagar', 'Bangladesh': 'Dhaka'}



# What if we try to change the delete a key:value.... We use a famous method .pop({our_key}) to delete the key:value pairs. 
# capitals.pop("Bangladesh")  {'India': 'New Delhi', 'Jammu & Kashmir': 'Srinagar'}

# capitals.popitem() deletes the latest key:value pair

# capitals.clear() vanished your all declared key:value pairs and gives you {}.

# What if you want only the keys from all the pairs... Well, we use .keys() to access all keys from the pairs.
# keys = capitals.keys()
# print(keys) dict_keys(['India', 'Jammu & Kashmir', 'Bangladesh']). It's array of keys so we can iterate in it and have keys.

# for key in keys:
#     print(key) 

    
# What if you want only the values from all the pairs... Well, we use .values() to access all values from the pairs.
# values = capitals.values()
# print(values) dict_values(['India', 'Jammu & Kashmir', 'Bangladesh']). It's array of values so we can iterate in it and have values.

# for value in values:
#     print(value)

# items = capitals.items()  .items() gives us the entire dictionary object in the form of array of 2D tuples.

# We can have a loop in order to access all the key:value pairs.
# for key, value in items:
#     print(f"Key: {key}", end=" ")
#     print(f"Value: {value}")
#     print()

# print(capitals)



#       =========== Have a practise project in next folder. But before we do that, let's have some exercise for you. =============

# Make a dictionary of students and their grade, also based on grade configuration, print remark for the student like A => Excellent and so on.
# Make a dictionary of mobile phones and their storage or with their price.

#                             =========== Make sure after completing these exercise, you will come to the project.   ==========