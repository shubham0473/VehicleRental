import unittest
import unittest
from src.vehicle import Car

class VehicleTest(unittest.TestCase):
    
    car = Car("Car", "C1", 1000)
    
    def test_1_set_vid(self):
        self.assertEqual("C1", self.car.vid)
    
    def test_2_set_base_price(self):
        self.assertEqual(1000, self.car.base_price)
    
    def test_3_set_vtype(self):
        self.assertEqual("Car", self.car.vtype)
            
    def test_4_book(self):
        val = self.car.book(1, 5)
        self.assertEqual(val, 4000)
        self.assertEqual(self.car.start_time, 1)
        self.assertEqual(self.car.end_time, 5)
        self.assertEqual(self.car.available, False)

    def test_5_failed_book(self):
        val = self.car.book(2, 7)
        self.assertEqual(val, -1)
        self.assertEqual(self.car.available, False)
    
    def test_6_end_booking(self):
        self.car.end_booking()
        self.assertEqual(self.car.start_time, -1)
        self.assertEqual(self.car.end_time, -1)
        self.assertEqual(self.car.available, True)
