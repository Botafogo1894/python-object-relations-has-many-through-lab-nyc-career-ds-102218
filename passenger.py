from trip import Trip

class Passenger:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def age(self):
        return self._age


    def trips(self):
        empty = []
        for trip in Trip.all():
                if trip.passenger.name == self.name:
                    empty.append(trip)
        return empty

    def drivers(self):
        empty = []
        for trip in Trip.all():
                if trip.passenger.name == self.name:
                    empty.append(trip.driver)
        return empty

    def trip_count(self):
        count = 0
        for trip in Trip.all():
                if trip.passenger.name == self.name:
                    count += 1
        return count
