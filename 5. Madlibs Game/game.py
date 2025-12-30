# In this game, we'll create a short story about someone, something, etc. in which we gonna use all the concepts we learned and have amateur knowledge about so far.


# Important Concept to Learn - String Literals - 'f' is used to print the values directly. It means that we don't need to mention again and again seperate variables in braces. Let's have a instance:

name1 = "Seth Adarsh"
name2 = "Seth Anamika"

print(f"My name is {name1} and her name is {name2}")

# I hope you understood this concept clearly. Now let's have our story.

my_name = input("Please enter your: ")
print(f"Hello, Everyone! Myself {my_name}")

my_city = input("Please enter your city: ")
print(f"I'm from {my_city}")

my_school = input("Please enter your school name: ")
print(f"I have completed my 10 + 2 from {my_school}")

my_degree = input("Please enter your pursuing degree: ")
my_clg_unvst = input("Please enter your college or university: ")
print(f"I'm pursing {my_degree} from {my_clg_unvst}")

CGPA = int(input("Please enter your current CGPA(in digits): "))
print(f"My current CGPA is {CGPA}")



print(f"Hello, Everyone! Myself, {my_name}. I'm from {my_city}. I have completed my 10 + 2 from {my_school}. I'm pursing {my_degree} from {my_clg_unvst}. My current CGPA is {CGPA}")



if(CGPA >= 6.5):
    print("You're a average student.")
elif(CGPA > 7):
    print("You're a good student.")
elif(CGPA > 8):
    print("You're an excellent student.")
elif(CGPA > 9) :
    print("You're an outstanding student.")
else:
    print("You are a poor student and you have to do hard-work day & night.")
 