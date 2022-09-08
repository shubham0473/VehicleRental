import unittest
from src.pricing import DynamicPricingStrategy, SimplePricingStrategy

class PricingTest(unittest.TestCase):
    
    dynamic = DynamicPricingStrategy()
    simple = SimplePricingStrategy()
    
    def test_1_simple_pricing(self):
        fare = self.simple.getFare(base_fare=10, time=10)
        self.assertEqual(fare, 100)
    
    def test_2_dynamic_pricing(self):
        fare = self.dynamic.getFare(base_fare=10, time=10, current_cap=0.3)
        self.assertEqual(fare, 100)
        fare = self.dynamic.getFare(base_fare=10, time=10, current_cap=0.9)
        self.assertEqual(fare, 110)