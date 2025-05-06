"""Create a class Logger that prints a message when an object is created (constructor) and another
message when it is destroyed (destructor).

"""
class Logger:
    def __init__(self,name):
        self.name=name
        print(f"The object {self.name} is created")
    def __del__(self):
        print(f"The object {self.name} created is deleted")
log1=Logger("Quarter 1")
log2=Logger("Quarter 2")
del log1
del log2
"""In Python, when a script finishes executing, all remaining objects are automatically destroyed.
So, even if you don't explicitly del log1, the Python garbage collector will delete the objects 
at the end of the program.
Thats when the __del__() destructor is automatically called.
"""