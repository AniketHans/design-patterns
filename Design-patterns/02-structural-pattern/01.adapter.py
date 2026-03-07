"""
    This is used to convert data from one format to other
"""

from dataclasses import dataclass
# Third Party library

@dataclass
class Datatype1:
    index: float
    data: str
    
class DisplayDataOfType1:
    def __init__(self, display_data: Datatype1):
        self.display_data1 = display_data
    def show_data(self):
        print(f"3rd party functionality: {self.display_data1.index} - {self.display_data1.data}")


# Our code
@dataclass
class Datatype2:
    position: int
    amount: int

class DisplayDataOfType2:
    def __init__(self, display_data: Datatype2):
        self.display_data2 = display_data
    
    def store_data(self):
        print(f"Data stored: {self.display_data2.position} - {self.display_data2.amount}")


# Adapter to convert data from Type2 to Type1

class DisplayDataOfType2AsType1(DisplayDataOfType1, DisplayDataOfType2):
    def __init__(self, data):
        self.data = data
    def store_data(self):
        print("Call this but use third party code")
        for item in self.data:
            ddt1 = Datatype1(float(item.position), str(item.amount))
            self.display_data1 = ddt1
            self.show_data()

def generate_data():
    data = []
    data.append(Datatype2(2,3))
    data.append(Datatype2(3,4))
    data.append(Datatype2(4,5))
    return data

if __name__ == "__main__":
    d = DisplayDataOfType2AsType1(generate_data())
    d.store_data()
    
        
        
    