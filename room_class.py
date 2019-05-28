global_rooms = {}

def make_exits(n=None, s=None, w=None, e=None):
    exits = {"n": n,
             "s": s,
             "w": w,
             "e": e}
    return exits

class Room:

    def __init__(self, location, exits, desc, items=None):
        self.exits = exits
        self.description = desc
        self.location = location
        self.items = items
        global_rooms[self.location] = self

    def unlock(self, direction):
        self.exits[direction] = 'unlocked'

    def lock(self, direction):
        self.exits[direction]='locked'

    def lock_status(self, direction):
        return self.exits[direction]
