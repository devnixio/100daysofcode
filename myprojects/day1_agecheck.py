#!python3

from datetime import datetime
from datetime import timedelta
from datetime import date


 # Obtain users birthyear
def get_birthyear():
    print("Let's see how old you are!:  ")
    birthyear = int(input("What year were your born?  "))
    return birthyear

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




def main():
    current_age()
#    days_old()

main()
