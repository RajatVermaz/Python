# An extra day is added to the calendar almost every four years as February 29, 
# and the day is called a leap day. It corrects the calendar for the fact that 
# our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, 
# otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. 
# It is only necessary to complete the is_leap function.

def leapYearBoolean(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(True) # This print statement shows if year is evenly divisible by 4, 100 and 400 then it is a leap year
            else:   #This else is showing that if year is evenly divisible by both 4 and 100 but not by 400 then return False
                print(False)
        else:   #This else is showing that if year is evenly divisible by 4 but not by 100 then return True
             print(True)       
    else:   #This else is showing that if year is not evenly divided by 4 then return false
         print(False)


def leapYear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(f"Year {year} is leap year.")
            else:
                print(f"Year {year} is not a leap year.")
        else:
            print(f"Year {year} is leap year.")
        
    else:
        print(f"Year {year} is not a leap year.")

def HackerLogicLeap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 100 == 0 and year % 400 != 0:
        leap = False
    elif year % 400 == 0:
        leap = True
    elif year % 4 != 0:
        leap = False
    return leap


if __name__ == "__main__":

    year = int(input("Enter the year from 1900 to 1000000 (FOR EXAMPLE: 1988,1992,1996 are leap year): ")) 
    print('**************************\n')
    print('Message print :)')   
    leapYear(year)
    print('**************************\n')
    print('Approach Bool 1 :)')
    leapYearBoolean(year)
    print('**************************\n')
    print('Hacker Rank Solution: ')
    print(HackerLogicLeap(year))