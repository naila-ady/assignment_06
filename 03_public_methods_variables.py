# """Create a class Car with a public variable brand and a public method start(). Instantiate the 
# class and access both from outside the class."""

class Car:
    
    def __init__(self, brand):  # Constructor to initialize the brand
        self.brand = brand  # Instance variable for the brand

    def start(self):  # Public method to start the car
        return f"The {self.brand} is starting."

# Instantiate the class and create objects
car1 = Car("Toyota")
car2 = Car("Honda")

# Access the public variable and method from outside the class
print(car1.brand)   # Accessing the 'brand' of car1
print(car2.brand)   # Accessing the 'brand' of car2

print(car1.start())  # Calling the 'start()' method for car1
print(car2.start())  # Calling the 'start()' method for car2
