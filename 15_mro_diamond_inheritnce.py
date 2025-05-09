"""Create four classes:A with a method show(),B and C that inherit from A and override show(),D that inherits
from both B and C.Create an object of D and call show() to observe MRO.
"""

class A:
    def show(self):
        return "Hello I am A"
class B(A):
    def show(self):
        return "Hello I am B"
    
class C(A):
    def show(self):
        return "Hello I am C"
    
class D(B,C):# Multiple inheritance from B and C yani D child hy B ur C ka aur ye dono parents hn,aur jo kuch
       pass         
            #DB aur C k pass hy mehods/Functions aur attributes wo sb kuch D ko mil skty hn
            # aur kyun k D k parents B,C ka parent A hy to isko A ki bhi  
    
d=D()#yahan pr D class k object bna rhy hn
print (D.mro())# Method Resolution Order dekhna
print(d.show())# show() method kis class ka chalega? B ka bcz D class k pass


"""If we want to inherit from A, we would have to pass it through class I, and since I is the child of H, 
H's parent is A. Therefore, the show function of A will be called in H. 
Python will look in H and find the show method of A, so it prints 'Hello from A'."""
    
class H(A):
    pass
class I(H):
    pass
i=I()
print(I.mro())
print(i.show())