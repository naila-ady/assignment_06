"""Create a class Counter that keeps track of how many objects have been created. Use a class
variable and a class method with cls to manage and display the count.
"""
class Counter:
    count = 0 #class level variable
    def __init__ (self):
        Counter.count +=1
    @classmethod
    def display_count(cls):
        return f"Total objects created: {cls.count}"  # Returning the count
# When you create an object of the Counter class:
obj1=Counter()# Calls the __init__ method, incrementing Counter.count
obj2=Counter()
obj3=Counter()

result=Counter.display_count()
print(result)

