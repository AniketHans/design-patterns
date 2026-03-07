class Equipment:
    def __init__(self, name:str, price: int):
        self.name = name
        self.price = price
    
class Composite:
    def __init__(self, name:str):
        self.name=name
        self.equipments = []
    
    def addEquipment(self, equipment:Equipment):
        self.equipments.append(equipment)
        return self

    @property
    def price(self):
        return sum([x.price for x in self.equipments])

if __name__ == "__main__":
    pc = Composite("pc")
    
    processor = Equipment("processor", 1000)
    hard_disk = Equipment("Harddisk", 800)
    
    memory = Composite("memory")
    ram = Equipment("RAM", 600)
    rom = Equipment("ROM", 400)
    
    memory.addEquipment(ram).addEquipment(rom)
    pc.addEquipment(memory).addEquipment(hard_disk).addEquipment(processor)
    
    print(pc.price)
    print(memory.price)
        