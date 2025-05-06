"""Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance 
variables should be used.
"""
class MathUtils:
    @staticmethod #This decorator tells Python that the method doesn’t depend on self (instance) or cls (class).
    def add(a,b):
        return(a+b)
result=MathUtils.add(10,9)#Can be called directly using the class name, like MathUtils.add(...)
print(result)
    