class Item:
    def __init__(self, name, desc, location=None):
        self.name = name
        self.desc = desc
        location.items.append(self)
class Key(Item):
    def __init__(self, name, desc, location, room, lock):
        self.name = name
        self.desc = desc
        self.room = room
        self.lock = lock
        location.items.append(self)
     #keys have a name description, and the lock they are for is determined by room and lock- lock being the direction of the exit
    def unlock(self, atmp_room, atmp_exit):
        if self.room == atmp_room and self.lock == atmp_exit:
            atmp_room.unlock(atmp_exit)
        else:
            print('===============\nThat lock doesn\'t fit there\n===============')
        #checks to see if the lock the player is trying the key with is the correct lock for that key