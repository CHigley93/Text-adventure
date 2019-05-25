import room

room1_exits = room.make_exit(n='unlocked')
room2_exits = room.make_exit(s='unlocked', e='locked')
#make a dictionary for global rooms that will contain every room as they are instanciated
room1 = room.Room((0,0), room1_exits, 'This is the starting room')
room2 = room.Room((0,1), room2_exits, 'This is a bathroom')
#create rooms with locations in tuple format, exits as either n, s, e, or w, and a description of the room
curr_room = room.global_rooms
for k, v in room1.exits.iteritems():
    if v:
        print("the room has an exit to the {direction}. It is {lock_status}.".format(direction=k,lock_status=v))
