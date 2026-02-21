from abc import ABC, abstractmethod

#------------------------ Vehicle Types ----------------------
class Car(ABC):
    @abstractmethod
    def engine(self):
        pass

class Bike(ABC):
    @abstractmethod
    def engine(self):
        pass

#------------------------ Concrete Products --------------------------
class BMW(Car):
    def engine(self):
        return "V6 twin turbo"
    
class RoyalEnfield(Bike):
    def engine(self):
        return "650cc twin exhaust"
    
class Tata(Car):
    def engine(self):
        return "1.5 diesel"

class Honda(Bike):
    def engine(self):
        return "250cc unit"
    

#------------------ Abctract Factory --------------------------

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass
    
    @abstractmethod
    def create_bike(self) -> Bike:
        pass

class LuxuryVehicle(VehicleFactory):
    def create_car(self):
        return BMW()
    def create_bike(self):
        return RoyalEnfield()

class EconomyVehicle(VehicleFactory):
    def create_car(self):
        return Tata()
    def create_bike(self):
        return Honda()    


#-------------- client function --------------------------
def getVehicle(vehicleCategory) -> VehicleFactory:
    if vehicleCategory=="luxury":
        return LuxuryVehicle()
    elif vehicleCategory=="economy":
        return EconomyVehicle()
    else:
        return None
    

luxuryVehicles = getVehicle("luxury")
car = luxuryVehicles.create_car()
print(car.engine())

bike = luxuryVehicles.create_bike()
print(bike.engine())


economyVehicles = getVehicle("economy")
car = economyVehicles.create_car()
print(car.engine())

bike = economyVehicles.create_bike()
print(bike.engine())

