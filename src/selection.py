from abc import ABC, abstractmethod

class VehicleSelector(ABC):
    
    @abstractmethod
    def select_vehicle(self, vehicles):
        raise NotImplementedError
    
    
class CheapestVehicleSelector(VehicleSelector):
    
    def select_vehicle(self, vehicles):
        while True and len(vehicles) > 0:
            min_vehicle = min(vehicles)
            # print(f"Min vehicle = {min_vehicle}")
            if not min_vehicle.available:
                vehicles.remove(min_vehicle)
            else:
                return min_vehicle
        return None

