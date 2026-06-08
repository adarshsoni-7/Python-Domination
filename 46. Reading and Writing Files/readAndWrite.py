#   =========================================================    Writing Files ==================================================


import json


txt_data = "I like Soya Chaap"

file_path = "output.txt"

absolute_file_path = "C:\\Users\\adars\\Documents\\output.txt"

# with open(file_path, 'w') as file:
#     file.write(txt_data)

# print(f"Data has been written to {file_path}")





# with open(absolute_file_path, 'w') as file:
#     file.write("Variable are containers which stores the data in Python.")

# print(f"Data has been written to {absolute_file_path}")





# Here, we use 'x' which creates the new file if the file doesnot exist, in our case it does that's why the error comes "This file already exists !"


# try:
#     with open(absolute_file_path, 'x') as file:
#         file.write("Variable are containers which stores the data in Python.")
    
# except FileExistsError as e:
#     print("This file already exists !")
    

# # Here, we can also add the new info or append the content in the existing file by using 'a' which append the given content in the file.

# try:
#     with open(absolute_file_path, 'a') as file:
#         file.write("\n" + "The name of the variables should be valid, not start with keywords or special characters.")
# except:
#     print("Something wenrt wrong !")


#                                       ======================== Explaiantion ===============================


# 1. We define a string variable `txt_data` that contains the text we want to write to a file.

# 2. We specify the file path where we want to save the data, in this case, "output.txt".

# 3. We use a `with` statement to open the file in write mode ('w'). This ensures that the file is properly closed after we are done writing to it.


# Why use with?

# Without with:

# file = open("output.txt", "w")
# file.write(txt_data)
# file.close()

# You must remember:
# file.close()

# 4. Inside the `with` block, we call the `write()` method on the file object to write the contents of `txt_data` to the file.

# 5. Finally, we print a message to the console indicating that the data has been written to the specified file.

# We can also use the absolute path of the file and write the contents for it.


# Let's add some contents in .txt file:

# employees = ["Squidword", "Spongebob", "Patrick", "Luther"]

absolute_txt_file_path = "C:\\Users\\adars\\Documents\\output.txt"

# with open(absolute_txt_file_path, "w") as file:
#     try:
#         for employee in employees:
#             file.write(employee + " ")

#         print(f"Data has been transferred to {absolute_txt_file_path}")
#     except FileExistsError:
#         print("File doesn't exist !")




# Let's add some contents in .json file:
# import json
# absolute_json_file_path = "C:\\Users\\adars\\Documents\\output.json"

# employee = {
#     "Name": "Patrick",
#     "Role": "Hacker",
#     "Age": 29,
#     "Salary": 10000,

#     "Name": "Luther",
#     "Role": "SDE",
#     "Age": 34,
#     "Salary": 100000,

#     "Name": "Aliana",
#     "Role": "SRE",
#     "Age": 23,
#     "Salary": 1000,
# }

 
# try:
#         with open(absolute_json_file_path, "w") as file:
#             json.dump(employee, file, indent = 2) # json.dump() is used to write the data in json file and indent is used to make the json file more readable by adding indentation to the data.
#         print(f"Data has been transferred to {absolute_json_file_path}")
# except FileExistsError:
#         print("File doesn't exist !")




# Let's add some contents in .csv file:

# import csv

# employees = [["Name", "Role", "Age", "Salary"],
#              ["Squidward", "Kelpie", 30, 50000],
#              ["Spongebob", "Cook", 25, 40000],
#              ["Patrick", "Hacker", 29, 10000],
#              ["Luther", "SDE", 34, 100000],
#              ["Aliana", "SRE", 23, 1000]]


# absolute_csv_file_path = "C:\\Users\\adars\\Documents\\output.csv"

# try:
#     with open(absolute_csv_file_path, "w", newline = '') as file:
#         writer = csv.writer(file) # csv.writer() is used to create a writer object which is used to write the data in csv file and newline = '' is used to avoid adding extra new line after each row in the csv file.

#         writer.writerows(employees) # writer.writerows() is used to write the data in csv file and it takes a list of lists as an argument where each inner list represents a row in the csv file.

#     print(f"Data has been transferred to {absolute_csv_file_path}")
# except FileExistsError:
#     print("File doesn't exist !")












#   =========================================================    Reading Files ==================================================


# Let's read the contents in .txt file:

# absolute_txt_file_path = "C:\\Users\\adars\\Documents\\output.txt"

# try:
#     with open(absolute_txt_file_path, "r") as file:
#         content = file.read() # file.read() is used to read the data from txt file.
#         print(content)
# except FileNotFoundError:
#     print("File doesn't exist !")

# except PermissionError:
#     print("You don't have permission to read this file !")



# Let's read the contents in .json file:

# absolute_json_file_path = "C:\\Users\\adars\\Documents\\output.json"

# import json

# try:
#     with open(absolute_json_file_path, "r") as file:
#         data = json.load(file) # json.load() is used to read the data from json file and it returns a dictionary.
#         print(data)
        
# except FileNotFoundError:
#     print("File doesn't exist !")

# except PermissionError:
#     print("You don't have permission to read this file !")




# Let's read the contents in .csv file:

absolute_csv_file_path = "C:\\Users\\adars\\Documents\\output.csv"

import csv

try:
    with open(absolute_csv_file_path, "r") as file:
        data = csv.reader(file) # csv.reader() is used to read the data from csv file and it returns a reader object.
        for row in data:
            print(row)


except FileNotFoundError:
    print("File doesn't exist !")

except PermissionError:
    print("You don't have permission to read this file !")