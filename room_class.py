global_rooms = {}
class Room:
    def __init__(self, location, exits, desc, items=None):
        self.exits = exits
        self.description = desc
        self.location = location
        self.items = items
        global_rooms[self.location] = self
        if 'n' in self.exits and self.exits['n'] == '':
            self.unlock('n')
        elif 's' in self.exits and self.exits['s'] == '':
            self.unlock('s')
        elif 'e' in self.exits and self.exits['e'] == '':
            self.unlock('e')
        elif 'w' in self.exits and self.exits['w'] == '':
            self.unlock('w')
    def unlock(self, direction):
        self.exits[direction] = 'unlocked'
    def lock(self, direction):
        self.exits[direction]='locked'
    def lock_status(self, direction):
        return self.exits[direction]