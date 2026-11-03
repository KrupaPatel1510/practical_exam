import os
import datetime
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# def isleapyear():
#     year=int(input("enter the year"))
#     if(year %4 == 0 and year % 100!=0) or(year % 400 == 0):
#         print(year, "is a leap year / true")
#     else:
#         print(year, "is not a leap year / false")
        
# isleapyear()


# def dayofweek(text):
#     date=datetime.datetime.strptime(text,'%Y-%m-%d')
#     return date.strftime('%A')

# print(dayofweek('2026-12-04'))


# date1 = datetime.datetime(2026, 2, 1)
# date2 = datetime.datetime(2026, 11, 30)

# difference = date2 - date1

# print("Number of days:", difference.days)


# now = datetime.datetime(2026, 7, 19, 9, 5, 30)
# print(now.strftime("%d-%m-%Y"), now.strftime("%m/%d/%Y"))
# print(now.strftime("%H:%M:%S"), now.strftime("%I:%M:%S %p"))



# new_date = datetime.datetime.now() + datetime.timedelta(weeks=3, days=2, hours=7)

# print(new_date.strftime("%Y-%m-%d %H:%M:%S"))