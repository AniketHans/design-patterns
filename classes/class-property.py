class Car:
    total_cars = 0 #class property
    
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_cars +=1

class ElectricCar(Car):
    pass

nexon = Car("Tata","Nexon")
baleno = Car("Maruti", "Baleno")
tesla = Car("Tesla", "Model Y")
print(Car.total_cars)
# print(baleno.__model)
# print(tesla.__model)