"""Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during
initialization. Access a method of the Engine class via the Car class.

"""
class Engine:
    def __init__(self,engine_type):
        self.engine_type= engine_type
    def start(self):
        return f"The {self.engine_type} engine is starting."
    

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return f"The {self.make} {self.model} is ready to go. {self.engine.start()}"

# Example usage
engine = Engine("V8")  # Create an Engine object
car = Car("Ford", "Mustang", engine)  # Create a Car object and pass the Engine object

print(car.start_car())
        