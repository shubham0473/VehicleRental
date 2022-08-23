from src.vehicle import VehicleFactory

class Branch():
    def __init__(self, name, vtypes) -> None:
        self._name = name
        self._vtypes = vtypes
        self.vehicles = {}
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, val):
        self._name = val
        
    @property
    def vtypes(self):
        return self._vtypes
    
    @vtypes.setter
    def set_vtypes(self, val):
        self._vtypes = val
        
    def get_available_vehicles(self, start_time, end_time):
        available_vehicles = {}
        for vtype in self.vehicles:
            for vehicle in self.vehicles[vtype]:
                if vehicle.available or start_time >= vehicle.end_time:
                    available_vehicles[vehicle.vid] = vehicle.base_price
        
        return {k: v for k, v in sorted(available_vehicles.items(), key=lambda item: item[1])}
    
    def add_vehicle(self, vehicle, vtype):
        if vtype not in self.vtypes:
            return False
        if vtype not in self.vehicles:
            self.vehicles[vtype] = [vehicle]
        else:
            self.vehicles[vtype].append(vehicle)
        return True
            
    def book_vehicle(self, vtype, start_time, end_time):
        if vtype in self.vehicles:
            for vehicle in self.vehicles[vtype]:
                if vehicle.available:
                    return vehicle.book(start_time, end_time)            
        else:
            return -1

    
    def end_booking(self, vid, vtype):
        for vehicle in self.vehicles[vtype]:
            if vehicle.vid == vid:
                vehicle.end_booking()
                return True
        return False
    
