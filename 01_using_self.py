"""Create a class Student with attributes name and marks. Use the self keyword to initialize these 
values via a constructor. Add a method display() that prints student details."""
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")

student1=Student("Mustafa" ,86)
student2=Student("Adnan" ,94)


student1.display()
student2.display()
