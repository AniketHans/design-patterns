from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    @abstractmethod
    def make_small_coffee(self):
        pass
    
    @abstractmethod
    def make_large_coffee(self):
        pass
    
class BasicCoffeeMachine(CoffeeMachine):
    def make_small_coffee(self):
        print("Basic Coffee machine making small coffee")
    def make_large_coffee(self):
        print("Basic Coffee machine making large coffee")
        
class EnhancedCoffeeMachine(CoffeeMachine):
    def __init__(self, basicCoffeeMachine: BasicCoffeeMachine):
        self.basicCoffeeMachine = basicCoffeeMachine
    def make_small_coffee(self):
        # using the same functionality
        self.basicCoffeeMachine.make_small_coffee()
    def make_large_coffee(self):
        # Changed the functionality
        print("Enhanced Coffee machine making large coffee")
    def make_milk_coffee(self):
        # Enhancing the existing functionality
        self.basicCoffeeMachine.make_small_coffee()
        print("Enhanced coffee machine adding milk to it")

if __name__=="__main__":
    bcm = BasicCoffeeMachine()
    ecm = EnhancedCoffeeMachine(bcm)
    
    ecm.make_small_coffee()
    print()
    ecm.make_large_coffee()
    print()
    ecm.make_milk_coffee()