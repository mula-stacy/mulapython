# create a pyhon program to check if the year is leap or not
# leap year divisible by 4 but not divisible by 100
# except if its also divisible by 400
year = int(input("enter the year:"))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is not a leap year")
else:
    print(year, "is a leap year")
