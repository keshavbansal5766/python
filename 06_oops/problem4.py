# Encapsulation - setting properties to private

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand
    
            
    def set_brand(self, new_brand):
        self.__brand = new_brand
        
    def full_name(self):
        return f"{self.__brand} {self.model}" 


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
my_car = Car("Toyota", "Corolla")
#  - not accessible now and also inherited electric car class does not have
# direct access of brand which is private property now for access u will create a get_brand function in main class
print(my_car.__brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_car.get_brand())