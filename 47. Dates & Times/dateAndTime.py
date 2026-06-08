import datetime

# date = datetime.date(2025, 6, 8)
# today = datetime.date.today()


# print(today)


# time = datetime.time(12, 30, 0)
# print(time)
 


# now = datetime.datetime.now()
# print(f"{now:%d-%m-%y %H:%M:%S}") # here %Y is for year, %m is for month, %d is for day, %H is for hour, %M is for minute and %S is for second.
# print(now.strftime("%d-%m-%y %H:%M:%S")) # this is another way to format the date and time.



# We are here checking whether our future date and time has passed or not. 

targeted_time = datetime.datetime(2050, 1, 2, 12, 50, 1)
current_time = datetime.datetime.now()


if current_time < targeted_time:
    print("Targetted time is about to come.")
else:
    print("Targetted time has passed.")