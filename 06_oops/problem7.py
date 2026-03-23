# Static method is a method that belongs to class rather than an instance of a class
# property decorator
# first for private things use __

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand
    
            
    def set_brand(self, new_brand):
        self.__brand = new_brand
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
my_car = Car("Toyota", "Corolla")
# my_car.model = "city"
# print(Car.general_description())

print(my_car.general_description())
# print(my_car.model)