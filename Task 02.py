"""
name = Task 02
student name = b01888722
date start = 02/10/2026
date finish = 02/10/2026
"""


"""Start of code"""
"""asking the user for time inputs"""
def getin():
    timehour = input("Please input your time in hours: ") # getting the hour from the user
    while int(timehour) > 24 or int(timehour) < 0: # validating the users input
        timehour = input("Invalid hour, please try again: ")
    timeminute = input("What minute into the hour is it: ") # getting the minute from the user
    while int(timeminute) > 60 or int(timeminute) < 0: # validating the number given
        timeminute = input("Invalid minutes, please try again: ")
    return timehour, timeminute # returning both inputs given

"""function for calculating"""
def calculations(timehour):
    
    pst = (timehour - 8) % 24 # converting the hours given to pst time
    cet = (timehour + 1) % 24 # converting the hours given to cet time
    
    return pst, cet # returning both calculations
    
"""Start of main code"""
"""main function"""
def main():

    timehour, timeminute = getin() # calling function for getting inputs
    pst, cet = calculations(int(timehour)) # calling function for calculating

    print("This is the current time in pst")
    print(f"{pst}:{timeminute}") # printing pst time
    print("This is the current time in cet")
    print(f"{cet}:{timeminute}") # printing cet time

main()