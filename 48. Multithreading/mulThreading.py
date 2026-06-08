# Multithreading is commonly used in programming to improve the efficiency of tasks that can be performed concurrently, such as handling user input, performing background tasks, or processing data in parallel.

import threading
import time

# def eat_ice():
#     time.sleep(4)
#     print("The ice-cream is eaten !")


# def trash_waste():
#     time.sleep(2)
#     print("Trashing done !")


# def get_email():
#     time.sleep(1)
#     print("We get the email !")



# chore1 = threading.Thread(target = eat_ice)
# chore1.start()

# chore2 = threading.Thread(target = trash_waste)
# chore2.start()

# chore3 = threading.Thread(target = get_email)
# chore3.start()


# chore1.join()
# chore2.join()
# chore3.join()

# print("All chores are done !")

# Here, we have three tasks: eating ice-cream, trashing waste, and getting email. These tasks will run concurrently with the help of chore1, chore2 and chore3.start() but in the time taken to complete each task will be different. The output will be printed in the order of completion, which may not necessarily be the order in which the threads were started. get_email will likely print first, followed by trash_waste, and finally eat_ice, due to the different sleep durations. These happened because get_email has minimum sleep time, so it will complete first, while eat_ice has the longest sleep time, so it will complete last. That's how multithreading allows tasks to run concurrently, improving efficiency and responsiveness in applications.



# chore1.join(), chore2.join(), and chore3.join() are used to ensure that the main thread waits for all the child threads to complete before printing "All chores are done !". This is important to ensure that the program does not exit before all tasks have finished executing.





def sending_marks_to_parents(student_name, marks):
    time.sleep(2)
    print(f"Marks of {student_name} are sent to parents: {marks}")


def sending_goodies_to_students(student_name, goodies):
    time.sleep(1)
    print(f"{goodies} are sent to {student_name}  ")


chore1 = threading.Thread(target = sending_marks_to_parents, args = ("Alice", 85))
chore2 = threading.Thread(target = sending_goodies_to_students, args = ("Alice", "toy"))

chore1.start()
chore2.start()




# If we have to send the parameters to the target function, we can use the args parameter of the Thread constructor. The args parameter takes a tuple of arguments that will be passed to the target function when the thread is started. In this example, we are passing the student name and marks to the sending_marks_to_parents function, and the student name and goodies to the sending_goodies_to_students function.