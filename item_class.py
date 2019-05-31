class Item:
    def __init__(self, name, desc, location=None):
        self.name = name
        self.desc = desc
        location.items.append(self)
class Key(Item):
    def __init__(self, name, desc, location, room, lock):
        self.name = name
        self.description = desc
        self.room = room
        self.lock = lock
        location.items.append(self)
        self.get_names = [self.name.lower(), 'key', 'the key', 'a key','keys']
     #keys have a name description, and the lock they are for is determined by room and lock- lock being the direction of the exit
    def unlock(self, atmp_room):
        if self.room == atmp_room:
            atmp_room.unlock(self.lock)
            print('===============\nYou unlock the {} exit\n==============='.format(self.lock))
        else:
            print('===============\nThat lock doesn\'t fit there\n===============')
        #checks to see if the lock the player is trying the key with is the correct lock for that key