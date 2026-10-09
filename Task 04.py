"""
name = Task 04
student name = b01888722
date start = 09/10/2026
date finish = 09/10/2026
"""

"""start of code"""
"""function for getting input"""
def getin():
    usin = input("Please input a number between 1-100: ") #storing users input
    while True: #loop for validation
        try: #trying to convert users input to an integer
            usin = int(usin) #changing input to an integer
            if 1 <= usin <= 100: #checking if the inputed value is between 1 and 100
                return usin #returning the value
                break #breaking the loop after returning value
            else:
                usin = input("Please input a number between 1-100: ") #telling the user the number inputed wasn't within range asked for
        except ValueError: #incase user inputs something other than a integer 
            usin = input("Invalid input, please enter a number between 1-100: ") #asking the user for another input
"""function for doing all the calculations"""
def calculations(a):
    if a % 2 == 0: #checking the remainder of inputed variable and checking whether its even or odd
        return "even" 
    else:
        return "odd"

"""main function"""
def main():
    #calling both functions
    usin = getin()
    result = calculations(usin)
    print(f"The number {usin} is {result}.") #printing the users input and saying whether its even or odd
main() #calling main function