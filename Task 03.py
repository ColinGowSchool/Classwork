"""
name = Task 03
student name = b01888722
date start = 02/10/2026
date finish = 02/10/2026
"""

"""start of the code"""

"""Function for getting input"""
def getin():
    usin = input("Please input how many eggs you have: ") # getting user input
    return usin

"""function for doing calculations"""
def calculations(a, b, c):

    gross = a // b # getting the gross number of eggs
    remain = a % b # getting the remainder
    dozen = remain // c # getting the dozen number of eggs
    remain = a % c # getting the remaining number of eggs
    
    return gross, dozen, remain


"""main code"""
"""main function"""
def main():
    grossegg = 144 # number for gross eggs
    dozenegg = 12 # number for dozen eggs
    

    usin = getin() # calling function to get user input
    gross, dozen, remain = calculations(int(usin), int(grossegg), int(dozenegg)) # calling function for doing calculations

    """displaying all numbers calculated"""
    print("You have:")
    print(f"{gross} grosseggs")
    print(f"{dozen} dozen eggs")
    print(f"{remain} eggs")

main() # calling main function