# Vehicle Rental System

This repository demonstrates a simple implementation of Vehicle rental system using python. 

## Design Pattern

The code follows **Strategy** pattern complemented with **Factory** pattern to create different types of objects at runtime. 

### Vehicle Interface

A Vehicle interface is designed which can be implemented to extend functionalities for different types of vehicles. With the vehicle module, Factory pattern is also used to create objects of the required concrete implementation


### Pricing Interface

A Pricing interface is designed to implement different types of pricing strategy. This interface can be extended to implement fare calculation logic. Factory is also included to create required object. There are two example strategies implemented in this code:

- SimplePricing: This is the vanilla price calculator (base_price * duration)
- DynamicPricing: This takes in two arguments, the premium (ex: for 10% it is 0.1) and the booked_cap after which this pricing kicks in. In this example, values for these two params are using their default values (0.1, 0.8)


### Selection Interface

A Selection interface is designed to implement different types of vehicle selection paradigms. An exmaple concrete implementation of selecting cheapest available vehicle is implemented in this code.

## Features

- Rental service has multiple branches throughout the city.
- Each branch has a limited number of different kinds of vehicles.
- Each vehicle can be booked with a predefined fixed price.
- Each vehicle can be booked in multiples of 1-hour slots each. (For simplicity, assume slots of a single day)
- Dynamic pricing applied if 80% vehicles in a particular branch are booked

## Getting Started

```bash
https://github.com/shubham0473/VehicleRental.git
cd VehicleRental
export PYTHONPATH="${PYTHONPATH}:`pwd`"
```

This system works on native python (3.9) packages so no dependency installation is required

## Run the code

The code takes input from a text file located in `src` folder where the input format is specified. To run the code, execute the following command from the top folder:

```bash
python src/main.py src/input.txt
```

To run the unit tests, execute the following command:

```bash
python -m unittest
```

In the test file, there are two Branches, one that follows a SimplePricingStrategy and the other follows DynamicPricingStrategy

## Future Improvements

- A vehicle cannot have a queue of bookings as of now, just a single booking even if the next booking is outside the current booking period. This can be implemented
- Functionality for returning vehicle can be enhanced, right now it is defined but not in use.
- Since vehicle id and branch name are supplied by the user, there can be a clash and create inconsistency, so that can be automated
- A clock can be incorporated as a feature to track bookings and fare
- Unit tests with mocked objects of different dependencies can be implemented

## Links
- [Strategy Pattern in Python](https://refactoring.guru/design-patterns/strategy/python/example#example-0)
- [Factory Pattern in Python](https://refactoring.guru/design-patterns/abstract-factory/python/example#example-0)