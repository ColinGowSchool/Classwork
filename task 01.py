"""
name = Task 01
student name = b01888722
date start = 02/10/2026
date finish = 02/10/2026
"""

"""Start of program"""

"""Making the function for getting the users input"""
def getin():
    firstin = input("What is your first input: ")
    print(f"Your first number is: {firstin}")
    secondin = input("What is your second input: ")
    print(f"Your first number is: {secondin}")
    return firstin, secondin

"""Making a function for making the calculations"""
def calculations(a, b):
    devnum1 = a / b
    devnum2 = b / a
    print(f"This is the first number devided by the second number: {devnum1}")
    print(f"This is the second number devided by the first number: {devnum2}")
    modnum = a % b
    print(f"this is the modulus: {modnum}")
    numup = a ** b
    print(f"This is the first value raised by the second: {numup}")

"""Main section of the code starts here"""
def main():
    """Calling function for getting input"""
    firstin, secondin = getin()
    """Calling function for calculating everything"""
    calculations(int(firstin), int(secondin))
main()