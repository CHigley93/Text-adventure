global_rooms = {}

def make_exit(n=None, s=None, e=None, w=None):
    exits = {"n": n,
             "s": s,
             "e": e,
             "w": w}
    return exits

class Room:
    def __init__(self, location, exits, desc):
        self.exits = exits
        self.description = desc
        self.location = location
        global_rooms[self.location] = self
