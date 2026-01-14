# This is a simple count-down program in Python.


import time

my_time = int(input("Please enter the time (in seconds): "))


for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) # optional but we can do here (x / 3600) % 24 to have days (if necessary)
    
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
    
    
print("TIME'S UP!")




#                                 ========================================   EXPLAINATION    ================================================

# We will import the 'time' from Python libraries. What is it ? ==> "The library is defined as some piece of code which has already written somewhere in the document. And if we want to use it, we have to only imprt it and now we have all access of code of that library".

# time.sleep(1) means for 1 (or more seconds as per your code), nothing won't be printed. After that, your code will start working.

# we calculate time in seconds, minutes, hours like this:
# 1. seconds = let's say if you want start the count-down from 65 then 65 % 60  = 5 seconds that's okay.
# 2. minutes = but we all know that in 60 sec = 1 min, that's why we did this x / 60 give how many minutes, and if minutes is greater than 60, it will be limit under 60 from (% 60). Example: 65 seconds is calculated as: 65 % 60 = 5 seconds and the minutes = 60 / 60 = 1 minute and 1 % 60 = 1. Eventually, we got 1 minute 5 seconds which is correct.