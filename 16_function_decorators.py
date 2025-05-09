"""Write a decorator function log_function_call that prints "Function is being called" before a function executes.
Apply it to a function say_hello().

"""
## Yeh aik class-based  function decorator hai jo function ke call hone se pehle message print karega
class log_function_call:
    def __init__(self,func):  # decorator func banany k ly is k andar __init__ must hy"Function ko decorator class
         self.func = func      # mein store karta hai"
                               # Constructor method — jab decorator kisi function par lagega to yeh chalay ga
    
                                            # Jab function call hoga, to yeh method run karega
    def __call__(self, *args, **kwargs):  # Jab function call ho, extra kaam kare (like logging, printing)
        print("Function is being called")
        return self.func(*args, **kwargs)  # phely print hua aur ab actual function call hoga

@log_function_call  # decorator
def say_hello(name):
    print(f"Hello ,{name}")

say_hello("ALI")  # Yeh asal mein __call__ method run karega
