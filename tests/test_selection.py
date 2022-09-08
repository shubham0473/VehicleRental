import unittest
from src.selection import CheapestVehicleSelector
from src.vehicle import Car
class VehicleSelectionTest(unittest.TestCase):
    
    cheapest = CheapestVehicleSelector()
    
    def test_1_cheapest_selection(self):
        cars = [
            Car("CAR", "C1", 3), 
            Car("CAR", "C2", 10), 
            Car("CAR", "C3", 1), 
            Car("CAR", "C4", 9), 
            Car("CAR", "C5", 5)
                 ]
        cheapest_car = self.cheapest.select_vehicle(cars)
        self.assertEqual(cheapest_car, Car("CAR", "C3", 1))
        
        cars[2].book(1, 3)
        
        cheapest_car = self.cheapest.select_vehicle(cars)
        self.assertEqual(cheapest_car, Car("CAR", "C1", 3))