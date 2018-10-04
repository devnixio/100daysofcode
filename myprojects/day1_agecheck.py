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

def main():
    age = get_currentdate() - get_birthyear()
    print ("I am guessing you are " + str(age) + " years old!")

main()
