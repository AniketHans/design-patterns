import uuid
from enum import Enum
from typing import List

class LockerSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class LockerStatus(Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"

class User:
    def __init__(self):
        self.user_id = str(uuid.uuid4())[:6]
        
class Agent:
    def __init__(self):
        self.agent_id = str(uuid.uuid4())[:6]

class Package:
    def __init__(self, user_id, agent_id, size):
        self.package_id = str(uuid.uuid4())[:6]
        self.user_id = user_id
        self.agent_id = agent_id
        self.size = size
        self.otp = str(uuid.uuid4())[:4]

class Locker:
    def __init__(self, pincode, lockerSize):
        self.locker_pincode = pincode
        self.locker_id = str(uuid.uuid4())[:6]
        self.locker_status = LockerStatus.AVAILABLE
        self.locker_size = lockerSize
        self.package : Package | None = None
        
    def add_package(self, package:Package):
        self.package = package
        self.locker_status = LockerStatus.OCCUPIED
    
    def release(self):
        self.package = None
        self.locker_status = LockerStatus.AVAILABLE

class LockerLocation:
    def __init__(self, pincode):
        self.pincode = pincode
        self.lockers: List[Locker] = []
    
    def add_locker(self, lockerSize):
        locker = Locker(self.pincode, lockerSize)
        self.lockers.append(locker)
    
    def getAvailableLockers(self, locker_size) -> Locker:
        print(self.lockers)
        for locker in self.lockers:
            if locker.locker_size == locker_size and locker.locker_status == LockerStatus.AVAILABLE:
                return locker
        return None

class LockerService:
    def __init__(self):
        self.locations: dict[str,LockerLocation] = dict()
        self.package_locker: dict[str, Locker] = dict()
    
    def addLocation(self, lockerLoc: LockerLocation):
        self.locations[lockerLoc.pincode] = lockerLoc
    
    def assign_locker(self, pincode, package: Package):
        if pincode not in self.locations:
            raise f"Given pincode {self.pincode} is not servicable"

        if package.package_id in self.package_locker:
            return self.package_locker[package.package_id]
        
        locker = self.locations[pincode].getAvailableLockers(package.size)
        if not locker:
            raise Exception("No locker available")
        locker.add_package(package)
        self.package_locker[package.package_id] = locker
        
        print("Locker assigned successfully")
        return package.otp

    def pickup_package(self, package_id, otp):
        if package_id not in self.package_locker:
            raise Exception("No package present with the given id")
        locker = self.package_locker[package_id]
        
        if locker.package.otp != otp:
            raise Exception("Wrong OTP")

        package = locker.package
        locker.release()
        del self.package_locker[package_id]
        
        print("Package picked successfully!!")
        return package

if __name__ == "__main__":
    LS = LockerService()
    
    lockerLoc = LockerLocation("244001")
    lockerLoc.add_locker(LockerSize.SMALL)
    lockerLoc.add_locker(LockerSize.MEDIUM)
    lockerLoc.add_locker(LockerSize.MEDIUM)
    
    LS.addLocation(lockerLoc)
    
    u = User()
    d = Agent()
    
    p = Package(u.user_id, d.agent_id, LockerSize.LARGE)
    otp = LS.assign_locker("244001", p)
    
    LS.pickup_package(p.package_id, otp)
        
    
                
    
    
    
                
    