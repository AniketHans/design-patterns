"""
    The Proxy Design Pattern is a structural design pattern where a proxy object acts as a substitute or placeholder for another real object to control access to it.
    
    Instead of directly accessing the real object, the client interacts with the proxy, which may add extra logic like:
        access control
        caching
        logging
        lazy loading
        security
    
    - It is different from facade pattern as the real and proxy object have the same interface, in facade we provide a simple interface for a complex interface
    - It is different from decorator pattern as the proxy controls the lifecycle of the real object. But in decorator pattern,we change some of the functionality of the real object
    
    User should not be able to know if he is interacting with real object or proxy object
"""

from abc import ABC, abstractmethod

class Image(ABC):
    
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename:str):
        self.filename = filename
        print(f"Real Image: Loading {self.filename}") # RealImage class loads image from disk

    def display(self):
        print(f"Real Image: Displaying {self.filename}\n\n")

class ProxyImage(Image):
    def __init__(self, filename:str):
        self.filename=filename
        self.real_image = None
    
    def display(self):
        # Here, the ProxyImage is helping us in preventing a disk operation for image fetch by caching it locally
        print(f"Proxy Image: Displaying {self.filename}\n")
        
        if self.real_image==None:
            self.real_image = RealImage(self.filename)
            print("From Disk") # Simulating fetching image from disk as initially it is nor present in cache
        else:
            print("From cache")
            
        self.real_image.display()

image = ProxyImage("test.png")

# From disk
image.display()

# From cache
image.display()