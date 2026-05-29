# Class Method =  A class method is a method that works with the class itself rather than with a specific object of the class.

# It uses cls instead of self.

# self → refers to the current object.
# cls → refers to the class itself.

# Instance methods are best for operations on instances of the class (objects). 
# Static methods are best for utility functions that don't need access to class data. 
# Class methods are best for class-level data or require access to the class itself. 




class Student:
    student_cnt = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.student_cnt += 1
        Student.total_gpa += gpa


# INSTANCE METHOD

    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"


    # Here we are using a class method to get the count of students. We use the @classmethod decorator to indicate that this method is a class method, and we use cls to access the class variable student_cnt. This allows us to get the total number of students without needing to create an instance of the Student class.

    @classmethod
    def get_count(cls):
        return f"There are {cls.student_cnt} students"

    @classmethod
    def get_total_gpa(cls):
        return f"Total GPA of all students: {cls.total_gpa}"

    @classmethod
    def get_average_gpa(cls):
        if cls.student_cnt == 0:
            return 0
        return f"Average GPA of all students: {(cls.total_gpa / cls.student_cnt):.2f}"



student1 =  Student("Alice", 3.2)
student2 =  Student("Bob", 2.0)
student3 =  Student("Charlie", 4.0)
 


print(Student.get_count()) # We can call the class method directly on the class without creating an instance. This will return the total number of students that have been created 

print(Student.get_total_gpa()) # We can also call the class method to get the total GPA of all students.

print(Student.get_average_gpa()) # Finally, we can call the class method to get the average GPA of all students. This will calculate the average by dividing the total GPA by the number of students.