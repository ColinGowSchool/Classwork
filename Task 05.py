"""
name = Task 05
student name = b01888722
date start = 09/10/2026
date finish = 09/10/2026
"""

"""start of code"""
"""function for getting input"""
def getin():
    usin = input("Please input a number: ") #asking the user for an input
    while True: #loop for validation
        try: #trying to convert users input to an integer
            usin = int(usin) #changing input to an integer
            return usin #returning the value
            break #breaking the loop after returning value
        except ValueError: #incase user inputs something other than a integer 
            usin = input("Invalid input, please enter a number: ") #asking the user for another input
            
"""function for doing calculations"""
def calculations(a):
    for i in range(1, 11): print(f"{a} x {i} = {a * i}") #printing the multiplication table from the number given

"""main function"""
def main():
    usin = getin() #calling the function to get the users input
    print(f"The multiplication table for {usin} from x1 - 10:") #printing a message before the multiplication table
    calculations(usin) #calling the function to do the calculations

"""calling main function"""
if __name__ == "__main__":
    main()