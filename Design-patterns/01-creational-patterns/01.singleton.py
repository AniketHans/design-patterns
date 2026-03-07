import threading
import time

class Network:
    _instances = {} # static property
    _lock = threading.Lock() # locks for multi threading
    
    def __new__(self, *args, **kwargs):
            with self._lock:
                if self not in self._instances:
                    time.sleep(1)
                    instance = super().__new__(self, *args, **kwargs)
                    self._instances[self] = instance
            return self._instances[self]
    
    def log(self):
        print(f"{self}")
        
def createSingleton():
    s = Network()
    s.log()
     

if __name__ == "__main__":
    
    n1= Network()
    n2= Network()
    n1.log()
    n2.log()
    
    p1 = threading.Thread(target=createSingleton)
    p2 = threading.Thread(target=createSingleton)
    p1.start()
    p2.start()


    