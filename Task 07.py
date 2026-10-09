"""
name = Task 07
student name = b01888722
date start = 09/10/2026
date finish = 09/10/2026
"""

"""start of code"""
"""printing the fibonacci sequence"""
def fibonacci(n):
    a, b = 0, 1 #setting the first two numbers for the fibonacci sequence
    for i in range(n): #looping for the amount the user inputed
        print(a, end=" ") # printing the current number in the fibonacci sequence
        a, b = b, a + b # making the next number in the fibonacci sequence by adding the previous two numbers together

"""main function"""
def main():
    print("This program will print the fibonacci sequence, your determine how far you want it to go:") #telling the user what the program is for
    n = int(input("Please input a number: ")) #asking the user how far they want the fibonacci sequence to go
    print(f"The fibonacci sequence for {n} is:") #show the users input, and telling them what the program is doing
    fibonacci(n) #calling the function to print the fibonacci sequence

"""calling main function"""
if __name__ == "__main__":
    main()