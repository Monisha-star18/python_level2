
#string functions 
text = "Python Program"
words = ["Python", "Program"]

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

print(text.strip())

print(text.replace("Python", "Java"))
text_lower = text.lower()
text_lower.replace("p", "e")	#Replaces all matching p characters
text_lower.replace("p", "e", 1)	#Replaces only the first matching p


print(text.split()) # default Splits using spaces or whitespace

date_text = "24/09/2026"
result1 = date_text.split("/") #Splits at the slash 
result2 = date_text.split("/",1) #Splits at the first slash only

print(result1)
print(result2) 

print("-".join(words))

print(text.startswith("Python"))

print(text.endswith("Program"))



# Math Functions

import math

number = 25
print(math.sqrt(number))

power = 3
print(math.pow(5, power))

decimal = 5.4
print(math.ceil(decimal)) #Rounds a number upward

print(math.floor(decimal)) #Rounds a number downward

integer = 5
print(math.factorial(integer))

negative_number = -25.5
print(math.fabs(negative_number))

number1 = 18
number2 = 24

print(math.gcd(number1, number2))

print(math.log(10))

angle = 0
print(math.sin(angle))

print(math.pi)


#Date Functions
import datetime as dt

todays_date = dt.date.today() #give todays date 
print("Get today's date",todays_date)

now_date = dt.datetime.now()
print("Get the current date and time",now_date)

create_date = dt.date(2026,9,30)
create_date_time = dt.datetime(2026,9,30,23,30,1)

print("Create a specific date" , create_date)
print("Create a specific date time" , create_date_time)

print("year :", todays_date.year)        # year
print("month :",todays_date.month)       # month
print("day :",todays_date.day)         # day

"""
weekday() returns:

Monday    → 0
Tuesday   → 1
Wednesday → 2
Thursday  → 3
Friday    → 4
Saturday  → 5
Sunday    → 6

"""
print("normal weekday :",todays_date.weekday())   # day of week

"""
1: Monday2: Tuesday 3: Wednesday 4: Thursday 5: Friday 6: Saturday 7: Sunday
"""
print("iso weekday :",todays_date.isoweekday())   # day of week iso standard 


"""
%d	Day of the month	
%m	Month number
%Y	Four-digit year	
%y	Two-digit year	
%D	Shortcut for %m/%d/%y	
%M	Minute
"""

#Formats a date as text
print( "formated date with %D", todays_date.strftime("%D") )
print( "formated date with %d %m % Y", todays_date.strftime("%m-%d-%Y") )
print( "formated date with %d %m % y", todays_date.strftime("%y-%m-%d") )

