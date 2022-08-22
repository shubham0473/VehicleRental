from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty
from sys import base_prefix
import enum

# class VehicleTypes(enum.Enum):
class Vehicle(ABC):
    def __init__(self) -> None:
        pass
        
    
    @property
    @abstractmethod
    def base_price():
        pass
    
    
    @property
    @abstractmethod
    def vid():
        pass
    
    
    @property
    @abstractmethod
    def vtype():
        pass
    
    @property
    @abstractmethod
    def start_time():
        pass   
    
    @property
    @abstractmethod
    def end_time():
        pass

class Car(Vehicle):
    def __init__(self, vtype, vid, price):
        self._base_price = price
        self._vtype = vtype
        self._vid = vid
        self._available = True
        self._start_time = -1
        self._end_time = -1
        
    @property
    def base_price(self):
        return self._base_price
    
    @base_price.setter
    def set_base_price(self, base_price):
        self._base_price = base_price
    
    @property
    def vid(self):
        return self._vid
    
    @vid.setter
    def vid(self, val):
        self._vid = val
    
    @property
    def vtype(self):
        return self._vtype
    
    @vtype.setter
    def vtype(self, val):
        self._vtype = val
        
    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, val):
        self._available = val
        
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, val):
        self._start_time = val
    
    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, val):
        self._end_time = val
        
    def book(self, start_time, end_time):
        if self.available:
            self.start_time = start_time
            self.end_time = end_time
            self.available = False
            return self.base_price*(end_time-start_time)
        else:
            return -1
        
    def end_booking(self):
        self.start_time = -1
        self.end_time = -1
        self.available = True
        
class Bike(Vehicle):
    def __init__(self, vtype, vid, price):
        self._base_price = price
        self._vtype = vtype
        self._vid = vid
        self._available = True
        self._start_time = -1
        self._end_time = -1
        
    @property
    def base_price(self):
        return self._base_price
    
    @base_price.setter
    def set_base_price(self, base_price):
        self._base_price = base_price
    
    @property
    def vid(self):
        return self._vid
    
    @vid.setter
    def vid(self, val):
        self._vid = val
    
    @property
    def vtype(self):
        return self._vtype
    
    @vtype.setter
    def vtype(self, val):
        self._vtype = val
        
    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, val):
        self._available = val
        
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, val):
        self._start_time = val
    
    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, val):
        self._end_time = val
        
    def book(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.available = False
        return self.base_price*(end_time-start_time)
        
    def end_booking(self):
        self.set_start_time(-1)
        self.set_end_time(-1)
        self.available = True
        
class Van(Vehicle):
    def __init__(self, vtype, vid, price):
        self._base_price = price
        self._vtype = vtype
        self._vid = vid
        self._available = True
        self._start_time = -1
        self._end_time = -1
        
    @property
    def base_price(self):
        return self._base_price
    
    @base_price.setter
    def set_base_price(self, base_price):
        self._base_price = base_price
    
    @property
    def vid(self):
        return self._vid
    
    @vid.setter
    def vid(self, val):
        self._vid = val
    
    @property
    def vtype(self):
        return self._vtype
    
    @vtype.setter
    def vtype(self, val):
        self._vtype = val
        
    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, val):
        self._available = val
        
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, val):
        self._start_time = val
    
    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, val):
        self._end_time = val
        
    def book(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.available = False
        return self.base_price*(end_time-start_time)
        
    def end_booking(self):
        self.set_start_time(-1)
        self.set_end_time(-1)
        self.available = True
        
class Bus(Vehicle):
    def __init__(self, vtype, vid, price):
        self._base_price = price
        self._vtype = vtype
        self._vid = vid
        self._available = True
        self._start_time = -1
        self._end_time = -1
        
    @property
    def base_price(self):
        return self._base_price
    
    @base_price.setter
    def set_base_price(self, base_price):
        self._base_price = base_price
    
    @property
    def vid(self):
        return self._vid
    
    @vid.setter
    def vid(self, val):
        self._vid = val
    
    @property
    def vtype(self):
        return self._vtype
    
    @vtype.setter
    def vtype(self, val):
        self._vtype = val
        
    @property
    def available(self):
        return self._available
    
    @available.setter
    def available(self, val):
        self._available = val
        
    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, val):
        self._start_time = val
    
    @property
    def end_time(self):
        return self._end_time
    
    @end_time.setter
    def end_time(self, val):
        self._end_time = val
        
    def book(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.available = False
        return self.base_price*(end_time-start_time)
        
    def end_booking(self):
        self.set_start_time(-1)
        self.set_end_time(-1)
        self.available = True

class VehicleFactory(object):
    @staticmethod    
    def create_vehicle(vtype, **kwargs):
        vehicles = {
            "Car" : Car,
            "Bike": Bike,
            "Van" : Van,
            "Bus" : Bus
        }
        try:
            return vehicles[vtype](vtype=vtype, **kwargs)
        except:
            return None
    
    
# c = Car(1, 2, 300)

