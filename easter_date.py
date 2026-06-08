# File: easter_date.py
# Description: Calculates the month and day of Easter Sunday for any given year using Gauss's Computus algorithm.
# Assignment Number: 3
#
# Name: DOTSE SELORM
# SID:  2425402027
# Email: DOTSES444@GMAIL.COM
# Grader: AUGUSTUS BUCKMAN
# Slip days used this assignment: 0
#
# On my honor, DOTSE SELORM, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    year = int(input("Enter a year: "))
    month_of_easter, day_of_easter = computus(year)
    print("In " + str(year) + " Easter Sunday is on " + str(month_of_easter) + "/" + str(day_of_easter) + "/" + str(year) + ".")

def computus(year):
    lunar_year_cycle_position = year % 19 
    weekday_slide_part_1 = year % 4 
    weekday_slide_part_2 = year % 7 
    leap_year_100 = year // 100 
    leap_year_400 = leap_year_100 // 4 

    lunar_orbit_correction = (13 + 8 * leap_year_100) // 25 

    century_start = (15 - lunar_orbit_correction + leap_year_100 - leap_year_400) % 30 
    sunday_offset = (4 + leap_year_100 - leap_year_400) % 7 

    days_added = (19 * lunar_year_cycle_position + century_start) % 30 

    day_of_week_offset = (2 * weekday_slide_part_1 + 4 * weekday_slide_part_2 + 6 * days_added + sunday_offset) % 7 

    total_days_added = 22 + days_added + day_of_week_offset

    day_of_easter = total_days_added % 31 
    month_of_easter = 3 + (total_days_added // 31) 
    
    return month_of_easter, day_of_easter

main()