"""Create a class decorator add_greeting that modifies a class to add a greet() method returning 
"Hello from Decorator!". 
Apply it to a class Person"""

# Class decorator ka function jo class ko modify karega aur usmein greet method add karega
def add_greeting(cls):
    # Greet method jo class mein add karenge, yeh 'self' se class ka object access karega
    def greet(self):
        return f"Hello from Decorator, {self.name}"  # Yahan class ka 'name' attribute use ho raha hai
    
    cls.greet = greet  # Ab hum greet method ko class mein add kar rahe hain
    return cls  # Aur modified class ko return kar rahe hain

@add_greeting  # Yahan hum decorator ko Person class pe apply kar rahe hain
class Person:
    def __init__(self, name):
        self.name = name  # Class ke constructor mein name attribute ko initialize kar rahe hain

# Person class ka object banaya aur name 'Mr. Adnan' diya
person = Person("Mr.Adnan")

# Greet method ko call kiya jo ab decorator se add hua hai
print(person.greet())  # Yahan greet method ko print kar rahe hain
