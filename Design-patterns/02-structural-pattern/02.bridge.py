from abc import ABC, abstractmethod

# Abstract classes
class Device(ABC):
    volume = 0
    
    @abstractmethod
    def get_name(self):
        pass

class Remote(ABC):
    @abstractmethod
    def volume_up(self):
        pass
    
    @abstractmethod
    def volume_down(self):
        pass
    
# classes

class TV(Device):
    def get_name(self):
        return "TV"

class Radio(Device):
    def get_name(self):
        return "Radio"

class BasicRemote(Remote):
    def __init__(self, device:Device):
        self.device = device
    def volume_up(self):
        self.device.volume += 1
        print(f"{self.device.get_name()} volume up to {self.device.volume}")
    def volume_down(self):
        self.device.volume -= 1
        print(f"{self.device.get_name()} volume down to {self.device.volume}")

if __name__ == "__main__":
    tv = TV()
    radio = Radio()
    
    tvRemote = BasicRemote(tv)
    radioRemote = BasicRemote(radio)
    
    tvRemote.volume_up()
    tvRemote.volume_up()
    tvRemote.volume_down()
    
    radioRemote.volume_up()
    