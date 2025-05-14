#13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__ (self, horsepower):
        self.horsepower = horsepower
    def start(self):
            return f"Engine with {self.horsepower} horsepower started."
class  Car:
    def __init__ (self, make, model, engine: Engine):
        self.make = make
        self.model = model
        self.engine = engine
    def start(self):
        return f"{self.make} {self.model} is starting. {self.engine.start()}"
# Example usage
engine: Engine = Engine(150)
car: Car = Car("Toyota", "Camry", engine)
print(car.start())