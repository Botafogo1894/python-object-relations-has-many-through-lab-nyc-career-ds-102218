from trip import Trip

class Query:


    def trips(self):
        empty = []
        for trip in Trip.all():
            for person in trip:
                if person.name == self.name:
                    empty.append(trip)
        return empty
