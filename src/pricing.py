from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    
    @abstractmethod
    def getFare(self, base_fare, time, current_cap):
        raise NotImplementedError
    
    
class SimplePricingStrategy(PricingStrategy):
    
    def __init__(self) -> None:
        super().__init__()
        
    def getFare(self, base_fare, time, cap=1):
        return base_fare*time

class DynamicPricingStrategy(PricingStrategy):
    
    def __init__(self, premium=0.1, cap=0.8) -> None:
        self._premium = premium
        self._cap = cap
        
    @property
    def premium(self):
        return self._premium
    
    @premium.setter
    def premium(self, val):
        self._premium = val

    @property
    def cap(self):
        return self._cap
    
    @cap.setter
    def cap(self, val):
        self._cap = val

    def getFare(self, base_fare, time, current_cap):
        if current_cap >= self.cap:
            return (1+self.premium)*base_fare*time
        else:
            return base_fare*time
        
class PricingFactory(object):
    @staticmethod    
    def create_strategy(strat, **kwargs):
        strategies = {
            "SIMPLE" : SimplePricingStrategy,
            "DYNAMIC": DynamicPricingStrategy,
            "Simple" : SimplePricingStrategy,
            "Dynamic" : DynamicPricingStrategy,
            "simple": SimplePricingStrategy,
            "dynamic": DynamicPricingStrategy,
        }
        try:
            return strategies[strat](**kwargs)
        except:
            return None 