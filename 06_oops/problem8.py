# @property decorator used for read only first we need to make it private and we can access it by using as a variable not as a model function 


class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand
            
    def set_brand(self, new_brand):
        self.__brand = new_brand
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    @property
    def model(self):
        return self.__model
    
    
my_car = Car("Toyota", "Corolla")
# my_car.model = "City"

print(my_car.model())