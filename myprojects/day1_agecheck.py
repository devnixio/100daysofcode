#!python3

from datetime import datetime
from datetime import timedelta
from datetime import date


 # Obtain users birthyear
def get_birthyear():
    print("Let's see how old you are!:  ")
    birthyear = int(input("What year were your born?  "))
    return birthyear

    # print("So you were born in " + birthyear + "!")      # Test for valid input

# Get current year
def get_currentdate():
    currentdate = datetime.today()
    return currentdate.year

# Return user age based on previous input!

#  print age function
def current_age():
    age = get_currentdate() - get_birthyear()
    days_alive = age * 365
    print ("I am guessing you are " + str(age) + " years old!")
    print("You have been alive for " + str(days_alive) + " days!")

#    return age

# calculate and print additional information about age


# how may days alive
# def days_old(days):
#    age = current_age()
#    days = int(age) *int(365)
#    print("You have also been alive for " + str(days)  + "!")
#    return days


# how many months
# def months(current_age):
#    current_age = age
#    months_old = int(age)  * int(12)
#  return months_old

# how many minutes, etc


def main():
    current_age()
#    days_old()

main()
