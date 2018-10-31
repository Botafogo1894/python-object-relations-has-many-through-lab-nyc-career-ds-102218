# remeber to import the Song class here
from song import Song

class Artist:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def songs(self):
        empty = []
        for song in Song._all:
            if song.artist.name == self.name:
                empty.append(song)
        return empty

    def genres(self):
        empty = []
        for song in Song._all:
            if song.artist.name == self.name:
                empty.append(song.genre)
        return empty
