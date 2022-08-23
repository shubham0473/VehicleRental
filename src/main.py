import sys

from rental_service import RentalService

commands = []
with open(sys.argv[1]) as f:
    commands = [l.split() for l in f.readlines()]

bs = RentalService()

for command in commands:
    if command[0] == "ADD_BRANCH":
        print("Types = ", [x for x in command[2].split(",")])
        print(bs.add_branch(command[1], [x for x in command[2].split(",")]))
    elif command[0] == "ADD_VEHICLE":
        print(bs.add_vehicle(command[1], command[2], command[3], int(command[4])))
    elif command[0] == "BOOK":
        print(bs.book_vehicle(command[1], command[2], int(command[3]), int(command[4])))
    elif command[0] == "DISPLAY_VEHICLES":
        print(bs.display_vehicles(command[1], int(command[2]), int(command[3])))