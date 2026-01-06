# This is the simple task where we will take a username and check some appropriate conditions to validate it.


unique_username = input("Enter your username: ")


if len(unique_username) > 12:
    print("Username should not be greater than 12 characters.")
elif not unique_username.find(" ") == -1:
    print("Username should not contain spaces.")

elif not unique_username.isalpha():
    print("Username should not contain digits.")
    
else:
    print("Username is valid.")