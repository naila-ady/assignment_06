"""Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject 
field, and use super() to call the base class constructor.

"""
class Person:
    def __init__ (self ,name):
        self.name = name
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__ (name)
        self.subject =subject
teacher = Teacher ("Miss Hifza" ,"Python") 
teacher1=Teacher("Miss Ayesha" ,"AI")
print(f"My teacher name is {teacher.name} and she teaches us {teacher.subject}")
print(f"My teacher name is {teacher1.name} and she teaches us {teacher1.subject}")

"""You pass name again in Teacher.__init__() so that super().__init__(name) can initialize the base class’s
part of the object.It's necessary if you override the constructor — otherwise, the base class attributes
like name won’t be set."""