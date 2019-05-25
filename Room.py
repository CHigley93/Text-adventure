global_rooms = {}

class Room:
    def __init__(self, location, exits, desc):
        self.exits = exits
        self.description = desc
        self.location = location
        global_rooms[self.location] = self
