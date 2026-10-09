"""
name = Task 06
student name = b01888722
date start = 09/10/2026
date finish = 09/10/2026
"""

"""start of code"""
"""function for getting input"""
def getin(password, inter):
    usin = input("Welcome\nPlease input your password: ") #asking the user for their password
    while usin != password: #loop for checking if the users input matches the password
        usin = input("Invalid password, please try again: ") #asking the user for another attempt
        inter = inter + 1 #adding a number to show how many attempts the user has made
        if inter == 3: #checking if the user has made the maximum number of attempts
            print("You have reached the maximum number of attempts, please try again later.") #printing a message to the user
            exit() #exiting the program

"""main function"""
def main():
    password = "password123!" #setting the password
    inter = 1 #setting the number of attempts to 1
    getin(password, inter) #calling the function to get the users input
    print("Access granted, you have entered the correct password.") #printing a success message

"""calling main function"""
if __name__ == "__main__":
    main()