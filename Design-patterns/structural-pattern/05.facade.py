'''
    The Facade Design Pattern is a structural design pattern that provides a simple interface to a complex subsystem.

    Instead of the client interacting with many classes, the facade exposes one simplified interface that internally coordinates the subsystem.
    
    Without Facade:
        Client  → ClassA
                → ClassB
                → ClassC
    
    With Facade:
        Client → Facade → ClassA
                        → ClassB
                        → ClassC
'''

# Simulating some complex systems
class CPU:
    def start(self):
        print("CPU start")

class Memory:
    def load(self):
        print("Memory loaded")

class HardDrive:
    def read(self):
        print("Hard Drive reading data")
        
# Facade layer
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def start_computer(self):
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()
        print("Computer started successfully")

# user

computer = ComputerFacade()
computer.start_computer()
        
