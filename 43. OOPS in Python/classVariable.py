# Class Variable = A variable that is shared among all instances of a class. It is defined within the class but outside of any instance methods. Class variables are accessed using the class name or through an instance of the class.


class Student:

    class_year  = 2024  # This is a class variable that is shared among all instances of the Student class.
    num_students = 0 
   
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1  # Increment the class variable num_students by 1 each time a new instance of the Student class is created. This keeps track of the total number of students created.


student1 = Student("Hayato", 24)
student2 = Student("Yuki", 21)
student3 = Student("Sakura", 26)

print(student1.name)  # Output: Hayato
print(student2.age)  # Output: 21
print(Student.class_year)  # Output: 2024
print(student1.class_year)  # Output: 2024

print(Student.num_students)  # Output: 3 because three instances of the Student class have been created.

print(f"{student1.name} is graduated in the {student1.class_year} and currently he is {student1.age}.")  # Output: Hayato is graduated in the year 2024 and currently he is 24 years old.

# Student.class_year and student1.class_year both are same because class_year is a class variable that is shared among all instances of the Student class. Therefore, both student1 and student2 can access the class variable class_year through the class name Student or through their own instance.