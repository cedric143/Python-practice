class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def kuanzisha(self):
        print(f"{self.make} {self.model} {self.year} started")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def kuanzisha(self):
        print(f"{self.make}{self.model}{self.year} model with {self.engine_size}cc started")


Motorcycle=Motorcycle("Nissan ","WRXT ","2023","10")
Motorcycle.kuanzisha()

