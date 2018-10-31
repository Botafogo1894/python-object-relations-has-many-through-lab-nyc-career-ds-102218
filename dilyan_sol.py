from driver import Driver
from passenger import Passenger
from trip import Trip
#create drivers
daniel = Driver("Daniel", "fast and furious")
alice = Driver("Alice", "faster and furiouser")
jeff = Driver("Jeff", "defensive")
#create passengers
jake = Passenger("Jake", 29)
anna = Passenger("Anna", 25)
katie = Passenger("Katie", 20)
# create trip instances here using the above passenger and driver instance objects
trip_one = Trip(daniel, jake)
trip_two = Trip(alice, jake)
trip_three = Trip(jeff, anna)
trip_four = Trip(alice, katie)
