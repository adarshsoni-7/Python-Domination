# File detection in Python is the process of checking whether a file exists, determining its type, or verifying its properties before performing operations such as reading, writing, or deleting it.

# The main purpose of file detection is to avoid errors like FileNotFoundError and ensure that the program works with valid files.

import os

relative_file_path = "45. File Detection/data.txt"

if os.path.exists(relative_file_path):
    print("File found!")
else:
    print("File does not exist.")

# We can also add the absolute path of the file

absolute_file_path = "C:\\Users\\adars\\Documents\\New folder\\test" # make sure to replace this with the actual path to your file

if os.path.exists(absolute_file_path):
    print("File found!")
    
    if os.path.isfile(absolute_file_path): # checks if the path is a file
        print("It is a file.")

    elif os.path.isdir(absolute_file_path): # checks if the path is a directory or folder
        print("It is a directory.")

else:
    print("File does not exist.")