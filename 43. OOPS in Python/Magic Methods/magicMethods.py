# Magic methods are special methods with double underscores (__) that Python automatically calls when we use built-in operations like creating objects, printing, comparing, adding, or finding length.


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author


#     def __str__(self):
#         return f"{self.title} is written by {self.author}"

    # When I write print(book1), Python automatically looks for the __str__() magic method in the Book class. If it finds it, it calls that method and prints the returned string.

    # What if __str__() doesn't exist?
    # Output will look something like: <__main__.Book object at 0x000001F...> because Python falls back to its default object representation.

    # __str__() is a magic method that Python automatically calls when an object is printed using print(object) to get a human-readable string representation of that object.





# book1 = Book("The Psychology of Money", "Morgan Housel")
# book2 = Book("Hands on Machine Learning", "Aureily")


# print(book1)



# class Student:
#     def __init__(self, roll):
#         self.roll = roll


#     def __eq__(self , other):
#         return self.roll == other.roll


# s1 = Student(1)
# s2 = Student(1)

# print(s1 == s2) # Here, Python automatically calls the __eq__() magic method to compare s1 and s2. Since both have the same roll number, it returned True.



# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __gt__(self, other):
#         return self.value > other.value

# num1 = Number(20)
# num2 = Number(10)
# print(num1 > num2) # Here, Python automatically calls the __gt__() magic method to compare num1 and num2. Since 20 is greater than 10, it returned True.


class Search:
    def __init__(self, number):
        self.number = number

    def __contains__(self, item):
        return item in self.number


search = Search([1, 2, 3, 4, 5])
print(0 in search) # Here, Python automatically calls the __contains__() magic method to check if 0 is in the search object. Since 0 is not in the list, it returned False.