# Polymorphism - setting properties to private

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
          
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charge"
    
my_car = Car("Toyota", "Corolla")


elec_car = ElectricCar("Tesla", "truck", "85kWh")
print(elec_car.fuel_type())