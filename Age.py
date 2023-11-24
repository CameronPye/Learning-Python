# Main Python File

import datetime as dt # dt alias for datetime. 

yrnow = dt.datetime.now().year
userinput = input("Enter your date of birth (dd/mm/yyyy):\n")
# Problem 1 - We need to sanitize the input. (fixed)

day, month, year = userinput.split("/") # Splits up user input into three variables.

yrborn = int(year)
mtborn = int(month)
dyborn = int(day)

yrnow = dt.datetime.now().year
mtnow = dt.datetime.now().month
dynow = dt.datetime.now().day 

hashadbirthday = (mtnow > mtborn) or (mtnow == mtborn and dynow >= dyborn) # Calculates if the users birthday has passed.

age = yrnow - yrborn - (not hashadbirthday) # because python treats true as 1 and false as 0.

# Problem 2 - This may be wrong dependant on the month and day. (fixed)
print(f"You are {age} Years old.")
# print(f"You are {yrnow-dob} Years old.")