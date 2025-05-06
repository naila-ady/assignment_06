"""Create a class Dog with instance variables name and breed. Add an instance method bark() that prints
a message including the dog's name."""

class Dog:
    def __init__ (self , name , breed):
        self.name= name
        self.breed = breed
    def bark(self):
        
        print(f"The {self.name} says woof woof!" )
        
animal1=Dog("Puppy" ,"BullDog")
animal2=Dog("Maxi" ,"German Shepered")

animal1.bark()
animal2.bark()