import unittest
from src.rental_service import RentalService

class RentalSystemTest(unittest.TestCase):
    
    rs = RentalService()
    
    def test_1_add_branch(self):
        self.rs.add_branch("B1", ['Car', "Bike"])
        self.assertIn("B1", self.rs.branches)