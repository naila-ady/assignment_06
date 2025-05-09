"""Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during
initialization. Access a method of the Engine class via the Car class.

"""
class Engine:
    def __init__(self,engine_type):
        self.engine_type = engine_type
    def start(self):
        return f"The {self.engine_type} engine is starting."
    

class Car:
    def __init__(self, make, model, engine_type):
        self.make = make
        self.model = model
        self.engine = Engine(engine_type)  # Composition: Car has an Engine

    def start_car(self):
        return f"The {self.make} {self.model} is ready to go. {self.engine.start()}"

# Example usage
car = Car("Ford", "Mustang", "v8")  # Create a Car object and pass the make and model arguments along with
print(car.start_car())              #Engine object bcz instance/engine object is ceated at line 16 and this 
                                    # is called composition

        