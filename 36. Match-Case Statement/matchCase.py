# Think for a while that what if I would say that according to the numbers print the week days such as: if day = 1 then print("Monday") and so on... You would say "Ok! I can write." which is typically possible but your code doesn't look clean, readable and maintainable. Well.... That's exactly match statement is for.

# Let's have some example to understand the concept clearly :

# def day_of_week(day):
#     if day == 1:
#         print("Monday")
#     elif day == 2:
#         print("Tuesday")
#     elif day == 2:
#         print("Wednesday")
#     elif day == 2:
#         print("Thursday")
#     elif day == 2:
#         print("Friday")
#     elif day == 2:
#         print("Saturday")
#     elif day == 2:
#         print("Sunday")


# day_of_week(1)


# Above was a traditional if-elif logic we write in order to perform in a different condition. But now let's move to the optimal one which is match-case statement which is as same as switch statement in C++ if you studied it.


# def day_of_week(day):
#     match (day):
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wednesday")
#         case 4:
#             print("Thursday")
#         case 5:
#             print("Friday")
#         case 6:
#             print("Saturday")

#         case (_):
#             print("Not a valid day.")


# day_of_week(1)




def marks_of_students(marks):
    match marks:
        case _ if marks <= 33:
            print("Fail")
        case _ if marks <= 45:
            print("Average")
        case _ if marks <= 55:
            print("Good")
        case _ if marks <= 65:
            print("Better")
        case _ if marks <= 75:
            print("Excellent")
        case _ if marks <= 85:
            print("Outstanding")            
        case _ if marks <= 95:
            print("Topper")
        case (_):
            print("Invalid marks")


marks_of_students(56)
    
    


# Seeing above, you can clearly understand how if conditions can be written in match-case statement using _ before 'if' logic.

# We can clearly see 2 thing here : 1. The code works same as previous one did and 2. The code looks cleaner, more readable than previous one.
# ====> At last, the case(_) is our 'default' case or you can say our 'else' case. It's not necessary to put this in every code.


#                                                    ============================= Task to do ===============================


# 1. Write a match-case statement to print the numbers from 15 to 150 which should satisfy these conditions: numbers % 5 == 0 and  numbers % 10 == 0 and numbers % 20 == 0, number % 2 == 0 and number  % 2 == 1.

# 2.(After trying yourself so hard then only see the code and again try to write on your own again) Write a match-case statement for a student's marks which should satisfy these conditions: marks <= 33 print("Fail"), marks <= 45 print("Average"), marks >= 60 print("Good"), marks >= 75 print("Excellent"), marks >= 95 print("Outstanding")
