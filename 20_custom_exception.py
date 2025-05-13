"""Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception 
if age < 18. Handle it with try...except.

"""


class InvalidAgeError(Exception):
    def __init__(self,age,):
        self.age=age
        super().__init__ (f"Invalid Age:{self.age} .Age must  be 18 or older")
        # function to check age
def check_age(age):
        if age <18:
            raise InvalidAgeError(age)
        else:
            print("You are eligible!")

# Try-except block to handle the exception
try:
    my_age = int(input("Enter your age: "))  # User se age input li
    check_age(my_age)  # Function call
except InvalidAgeError as e:
    print(f"Error: {e}")  # Agar exception raise hota hai, toh error message print hoga


