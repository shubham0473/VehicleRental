from rental_service import RentalService


bs = RentalService()

bs.add_branch("B1", ["Car", "Bike", "Van"])

print(bs.add_vehicle("B1", "Car", "V1", 500))
print(bs.add_vehicle("B1", "Car", "V2", 1000))
print(bs.add_vehicle("B1", "Bike", "V3", 250))
print(bs.add_vehicle("B1", "Bike", "V4", 300))
print(bs.add_vehicle("B1", "Bus", "V5", 2500))

print(bs.book_vehicle("B1", "Van", 1, 5))
print(bs.book_vehicle("B1", "Car", 1, 3))
print(bs.book_vehicle("B1", "Bike", 2, 3))
print(bs.book_vehicle("B1", "Bike", 2, 5))
print(bs.book_vehicle("B1", "Bike", 2, 5))
print(bs.display_vehicles("B1", 1, 5))