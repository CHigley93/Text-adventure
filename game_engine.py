
import room_class
global_rooms = room_class.global_rooms

#make a dictionary for global rooms that will contain every room as they are instanciated
room1 = room_class.Room((0,0), ['n', 'w'], 'The starting room')
room2 = room_class.Room((0,1), ['s', 'w'], 'A bathroom')
room3 = room_class.Room((-1,1), [ 'n', 's', 'e', 'w'], 'A room full of weapons')
room4 = room_class.Room((-1,2), ['s'], 'An office')
room5 = room_class.Room((-2,1), ['e'], 'A storage closet')
room6 = room_class.Room((-1,0), ['n', 'e'], 'A room with metal walls and floor')
#create rooms with locations in tuple format, exits as either n, s, e, or w, and a description of the room
curr_room = global_rooms[(0,0)]
#set starting room

go_commands = ['go', 'move', 'walk', 'run', 'exit']
north_commands = ['n', 'north', 'up', 'forward']
south_commands = ['s', 'south', 'down', 'backward']
east_commands = ['e', 'east', 'right']
west_commands = ['w', 'west', 'left']
dir_commands = [north_commands, south_commands, east_commands, west_commands]
#Sets commands that can be used to move the player and words that can be used as directions for the player to go

while True:
    print('You look around and see:\n')
    print(curr_room.description+'\n')
    print('This room has the following exits:')
    for exit in curr_room.exits:
        print(exit)
    curr_input = input('What do you do? \n')
    # print the description, exits, and ask for input
    word_split = curr_input.split()
    #splits the input into words for sorting so we can deal with each word one by one in order
    if word_split[0] in go_commands: 
        curr_xy = curr_room.location
        new_x = curr_xy[0]
        new_y = curr_xy[1]
        #This sets up our current location and breaks it into x and y coordinates
        if word_split[1] in north_commands and 'n' in curr_room.exits: 
            new_y += 1
        elif word_split[1] in south_commands and 's' in curr_room.exits:
            new_y -= 1
        elif word_split[1] in east_commands and 'e' in curr_room.exits:
            new_x += 1         
        elif word_split[1] in west_commands and 'w' in curr_room.exits:
            new_x -= 1           
        elif word_split[1] in [word for directions in dir_commands for word in directions]:
            print('There is no exit to the {}\n'.format(' '.join(word_split[1:])))
        #this determines what direction was chosen and if that exit exists it alters the x y coordinates of the player
        new_xy = (new_x, new_y)
        curr_room = global_rooms[new_xy]
        #This updates the xy coordinates then uses those to change the room that  the player is in      
    else:
        print('I don\'t understand please try again\n')