import room


#make a dictionary for global rooms that will contain every room as they are instanciated
room1 = room.Room((0,0), 'n', 'This is the starting room')
room2 = room.Room((0,1), 's', 'This is a bathroom')
#create rooms with locations in tuple format, exits as either n, s, e, or w, and a description of the room
curr_room = room.global_rooms
