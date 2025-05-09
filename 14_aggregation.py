# """Create a class Department and a class Employee. Use aggregation by having a Department object 
# store a reference to an Employee object that exists independently of it.
# """

            
            
# Employee class (can exist independently)
class Employee:
    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.emp_name}, ID: {self.emp_id}")


# Department class aggregates Employee
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: using an existing Employee object

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_info()
        
# Create an independent Employee object
emp1 = Employee("Alice", 101)

# Pass it to a Department object (aggregation)
dept1 = Department("HR", emp1)

# Display details
dept1.show_details()

"""Another example just for clarification of aggregation """
# class Chef:
#     def __init__(self, chef_name):
#         self.chef_name = chef_name  # Chef ka naam object mein store kiya
#         print(f"Chef {chef_name} is available")  # Jab chef ka object banta hai, message print hota hai

#     def cook(self):
#         return f"{self.chef_name} can cook food"  # cook() method chef ka naam ke sath message return karta hai

# class Restaurant:
#     def __init__(self, chef, res_name):
#         self.res_name = res_name  # Restaurant ka naam object mein store kiya
#         self.chef = chef  # Yeh chef object ko restaurant ke andar store karta hai (Aggregation)
#         print(f"Restaurant name is {self.res_name}")  # Jab restaurant ka object banta hai to us ka naam print hota hai

#     def chef_hire(self):
#         print(self.chef.cook())  # Restaurant ka chef cook() method call karta hai aur result print hota hai

# # Neechey 3 Chef objects banaye gaye hain alag alag names ke sath
# chef1 = Chef("Ali")       # Chef Ali available print hoga
# chef2 = Chef("Mustafa")   # Chef Mustafa available print hoga
# chef3 = Chef("Naila")     # Chef Naila available print hoga

# # Har chef ko aik alag restaurant mein hire kiya gaya
# restaurant1 = Restaurant(chef1, "Spicy Bites")  # Spicy Bites naam ka restaurant Chef Ali ke sath create hua
# restaurant2 = Restaurant(chef2, "Peri Bytes")   # Peri Bytes restaurant mein Chef Mustafa hire hua
# restaurant3 = Restaurant(chef3, "Ajwa Hotel")   # Ajwa Hotel mein Chef Naila hire hui

# # Har restaurant ka chef apna cook function chala raha hai
# restaurant1.chef_hire()  # Ali can cook food print hoga
# restaurant2.chef_hire()  # Mustafa can cook food print hoga
# restaurant3.chef_hire()  # Naila can cook food print hoga
