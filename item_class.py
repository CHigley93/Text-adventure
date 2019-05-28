class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
class Key(Item):
    def __init__(self, name, desc, room, lock):
        self.name = name
        self.desc = desc
        self.room = room
        self.lock = lock
        
    def unlock(self, atmp_room, atmp_exit):
        if self.room == atmp_room and self.lock == atmp_exit:
            atmp_room.unlock(atmp_exit)
        else:
            print('that lock doesn\'t fit there')