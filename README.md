# Vehicle Rental System

This repository demonstrates a simple implementation of Vehicle rental system using python.

## Features

- Rental service has multiple branches throughout the city.
- Each branch has a limited number of different kinds of vehicles.
- Each vehicle can be booked with a predefined fixed price.
- Each vehicle can be booked in multiples of 1-hour slots each. (For simplicity, assume slots of a single day)

## Getting Started

```bash
https://github.com/shubham0473/VehicleRental.git
cd VehicleRental
```

This system works on native python (3.9) packages so no dependency installation is required

## Run the code

The code takes input from a text file located in `src` folder where the input format is specified. To run the code, execute the following command from the top folder:

```bash
python src/main.py --input_file src/input.txt
```

## Future Improvements

- Dynamic pricing can be implemented
- Since vehicle id and branch name are supplied by the user, there can be a clash and create inconsistency, so that can be automated
- A clock can be incorporated as a feature to track bookings and fare