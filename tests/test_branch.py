import unittest
import unittest
from src.branch import Branch

class Test(unittest.TestCase):
    
    branch = Branch("B1", ["Car", "Bike", "Bus"])
    
    def test_1_set_name(self):
        self.assertEqual("B1", self.branch.name)
    
    def test_2_set_vtypes(self):
        self.assertCountEqual(['Car', "Bike", "Bus"], self.branch.vtypes)
    
    def test_3_set_vtype(self):
        self.assertEqual("Car", self.branch.vtype)
            
    def test_4_book(self):
        val = self.branch.book(1, 5)
        self.assertEqual(val, 4000)
        self.assertEqual(self.branch.start_time, 1)
        self.assertEqual(self.branch.end_time, 5)
        self.assertEqual(self.branch.available, False)

    def test_5_failed_book(self):
        val = self.branch.book(2, 7)
        self.assertEqual(val, -1)
        self.assertEqual(self.branch.available, False)
    
    def test_6_end_booking(self):
        self.branch.end_booking()
        self.assertEqual(self.branch.start_time, -1)
        self.assertEqual(self.branch.end_time, -1)
        self.assertEqual(self.branch.available, True)
    
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()