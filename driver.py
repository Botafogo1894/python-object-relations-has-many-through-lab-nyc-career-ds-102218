from trip import Trip

class Driver:

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style

    @property
    def name(self):
        return self._name

    @property
    def driving_style(self):
        return self._driving_style
    @driving_style.setter
    def driving_style(self, driving_style):
        self._driving_style = driving_style


    def trips(self):
        empty = []
        for trip in Trip.all():
                if trip.driver.name == self.name:
                    empty.append(trip)
        return empty

    def passengers(self):
        empty = []
        for trip in Trip.all():
                if trip.driver.name == self.name:
                    empty.append(trip.passenger)
        return empty

    def trip_count(self):
         count = 0
         for trip in Trip.all():
                 if trip.driver.name == self.name:
                     count += 1
         return count
