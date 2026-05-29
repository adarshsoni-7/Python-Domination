# Static methods = A method that belongs to a class rather than any instance of the class. 
#                  Usually used for general utility functions. 
# Instance methods = Best for operations on an instance of the class. 

# def get_info(self):
#     return f"{self.name} is {self.age} years old."

# Here we can see that the get_info method is an instance method because it uses the self parameter to access instance attributes.


# Static methods = Best for utility functions that don't need access to class data. 

# @staticmethod
# def kmm_to_miles(km):
#     return km * 0.621371

# Here we can see that the kmm_to_miles method is a static method because it doesn't use the self parameter and doesn't access any instance attributes. It simply performs a conversion from kilometers to miles.




class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position


    def get_info(self):
        return f"{self.name} is a {self.position}."


    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Analyst"]
        
        if position in valid_positions:
            return (f"{position} is a valid position. Apply now!")

        else :
            return (f"{position} is not a valid position. Please check the job listings for available positions.")


# employee1  = Employee("Alice", "Developer")
# print(employee1.get_info())  # Output: Alice is a Developer.


# For an instance method, you access an object then call the instance method. 

# We don't need to create an instance of the Employee class to use the static method is_valid_position. We can call it directly on the class itself.

print(Employee.is_valid_position("AI Engineer"))  
print(Employee.is_valid_position("Developer"))     

# With a static method, you only need to access that class. 



#                                            ======================== Explaiantion ========================


# In this code, we have an Employee class with an instance method get_info which used self parameter to access the instance attributes name and position while the static method is_valid_position doesn't use self.

# Instance methods require an object of the class to be created before they can be called, while static methods can be called directly on the class without creating an instance.  