from src.vehicle import VehicleFactory
from src.branch import Branch
from src.pricing import PricingFactory
from src.selection import CheapestVehicleSelector

class RentalService():
    def __init__(self) -> None:
        self.branches = {}
        self.vehicle_factory = VehicleFactory()
        self.pricing_factory = PricingFactory()
    
    def book_vehicle(self, bname, vtype, start_time, end_time):
        if bname in self.branches:
            return self.branches[bname].book_vehicle(vtype, start_time, end_time)
        else:
            return -1
    
    def add_branch(self, bname, vtypes, strat="Simple"):
        if bname in self.branches:
            return False
        
        pricing_strat = self.pricing_factory.create_strategy(strat)
        branch = Branch(bname, vtypes, pricing_strat, CheapestVehicleSelector())
        self.branches[branch.name] = branch
        return True
        
    def display_vehicles(self, bname, start_time, end_time):
        return self.branches[bname].get_available_vehicles(start_time, end_time)
        
    def add_vehicle(self, bname, vtype, vid, price):
        if bname in self.branches:
            if vtype in self.branches[bname].vtypes:
                v = self.vehicle_factory.create_vehicle(vtype=vtype, vid=vid, price=price)
                if v is not None:
                    self.branches[bname].add_vehicle(v, vtype)
                    return True
                else:
                    # raise VehicleAddException()
                    return False
            else:
                # raise VehicleTypeNotFoundException()
                return False
        else:
            # raise BranchNotFoundException()
            return False