# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's 
# first name and last name. Both should be at least 2 characters long. If not, print an error message.


first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")

def full_name():
    first_last = first_name + last_name
    return len(first_last)

if full_name() < 2:
    print("Error: Full Name should be at least two characters long.")
else:
    print(f"The total lenght of {first_name} {last_name} is: {full_name()} characters.")
    