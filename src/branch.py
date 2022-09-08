class Branch():
    def __init__(self, name, vtypes, strategy, selector) -> None:
        self._name = name
        self._vtypes = vtypes
        self.vehicles = {}
        self._pricing_strat = strategy
        self._selector = selector
        self._total_vehicles = 0
        self._current_booked = 0
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, val):
        self._name = val
        
    @property
    def total_vehicles(self):
        return self._total_vehicles
    
    @total_vehicles.setter
    def total_vehicles(self, val):
        self._total_vehicles = val
        
    @property
    def current_booked(self):
        return self._current_booked
    
    @current_booked.setter
    def current_booked(self, val):
        self._current_booked = val
        
    @property
    def vtypes(self):
        return self._vtypes
    
    @vtypes.setter
    def vtypes(self, val):
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
        self.total_vehicles +=+ 1
        return True
            
    def book_vehicle(self, vtype, start_time, end_time):
        if vtype in self.vehicles:
            selected_vehicle = self._selector.select_vehicle(self.vehicles[vtype])
            if selected_vehicle is not None:
                selected_vehicle.book(start_time, end_time)
                fare = self._pricing_strat.getFare(selected_vehicle.base_price, end_time-start_time, self.current_booked/self.total_vehicles)
                self.current_booked += 1
                return fare
        return -1

    
    def end_booking(self, vid, vtype):
        for vehicle in self.vehicles[vtype]:
            if vehicle.vid == vid:
                vehicle.end_booking()
                return True
        return False
    
