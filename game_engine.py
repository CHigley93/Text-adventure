
import room_class
global_rooms = room_class.global_rooms

#make a dictionary for global rooms that will contain every room as they are instanciated
room1 = room_class.Room((0,0), ['n'], 'The starting room')
room2 = room_class.Room((0,1), ['s'], 'A bathroom')
#create rooms with locations in tuple format, exits as either n, s, e, or w, and a description of the room
curr_room = global_rooms[(0,0)]
#set starting room


while True:
    print('You look around and see:')
    print(curr_room.description)
    print('This room has the following exits:')
    for exit in curr_room.exits:
        print(exit)
    curr_input = input('What do you do? \n')
    # print the description, exits, and ask for input
    if curr_input == 'n' and 'n' in curr_room.exits:
        curr_xy = curr_room.location
        new_x = curr_xy[0]
        new_y = curr_xy[1] + 1
        new_xy = (new_x, new_y)
        curr_room = global_rooms[new_xy]
        
    if curr_input == 's' and 's' in curr_room.exits:
        curr_xy = curr_room.location
        new_x = curr_xy[0]
        new_y = curr_xy[1] - 1
        new_xy = (new_x, new_y)
        curr_room = global_rooms[new_xy]
        
    if curr_input == 'e' and 'e' in curr_room.exits:
        curr_xy = curr_room.location
        new_x = curr_xy[0] + 1
        new_y = curr_xy[1] 
        new_xy = (new_x, new_y)
        curr_room = global_rooms[new_xy]
        
    if curr_input == 'w' and 'w' in curr_room.exits:
        curr_xy = curr_room.location
        new_x = curr_xy[0] - 1
        new_y = curr_xy[1] 
        new_xy = (new_x, new_y)
        curr_room = global_rooms[new_xy]

