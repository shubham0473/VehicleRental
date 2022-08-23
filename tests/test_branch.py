import unittest
import unittest
from src.branch import Branch
from src.vehicle import Bike, Car, Van

class BranchTest(unittest.TestCase):
    
    branch = Branch("B1", ["Car", "Bike", "Bus"])
    
    def test_1_set_name(self):
        self.assertEqual("B1", self.branch.name)
    
    def test_2_set_vtypes(self):
        self.assertCountEqual(['Car', "Bike", "Bus"], self.branch.vtypes)
    
    def test_3_add_vehicle(self):
        c = Car("Car", "C1", 1000)
        val = self.branch.add_vehicle(c, "Car")
        self.assertEqual(val, True)

        
    def test_4_failed_add_vehicle(self):
        v = Van("Van", "V1", 1000)
        val = self.branch.add_vehicle(v, "Van")
        self.assertEqual(val, False)       
            
    def test_5_get_available_vehicles(self):
        c1 = Car("Car", "C2", 1250)
        c2 = Car("Car", "C3", 2000)
        c3 = Car("Car", "C4", 3000)
        b = Bike("Car", "B1", 250)
        
        self.branch.add_vehicle(c1, "Car")
        self.branch.add_vehicle(c2, "Car")
        self.branch.add_vehicle(c3, "Car")
        self.branch.add_vehicle(b, "Bike")
        
        val = self.branch.get_available_vehicles(1, 5)
        print(val)

        result = {
            'B1' : 250,
            'C1': 1000,
            'C2': 1250,
            'C3': 2000,
            'C4': 3000
        }
        self.assertDictEqual(result, val)