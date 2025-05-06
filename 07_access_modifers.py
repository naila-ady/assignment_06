"""Create a class Employee with:a public variable name,a protected variable _salary, anda private variable __ssn.
Try accessing all three variables from an object of the class and document what happens.
SSN stands for Social Security Number. It is a unique identifier used by the United States government for social security 
and tax purposes.
"""
class Employee:
    def __init__(self,name ,_salary,_ssn):
        self.name = name #public var
        self._salary = _salary #protected var
        self.__ssn = _ssn  #private var
        
emp = Employee("Adnan" ,89000,"1234-675-2487")

print("Public variable (name):", emp.name)           # ✅ Works fine (Public)
print("Protected variable (_salary):", emp._salary)  # ✅ Works, but protected by convention
# print("Private variable (__ssn):", emp.__ssn)      # ❌ This will raise an error

 #Accessing private variable via name mangling
print("Private variable via name mangling (_Employee__ssn):", emp._Employee__ssn)

        
