import room_class
global_rooms = room_class.global_rooms

#make a dictionary for global rooms that will contain every room as they are instanciated
room1 = room_class.Room((0,0), {'n': 'locked', 'w':''}, 'The starting room')
room2 = room_class.Room((0,1), {'s':'locked', 'w':''}, 'A bathroom')
room3 = room_class.Room((-1,1), {'n':'', 's':'', 'e':'', 'w':''}, 'A room full of weapons')
room4 = room_class.Room((-1,2), {'s':''}, 'An office')
room5 = room_class.Room((-2,1), {'e':''}, 'A storage closet')
room6 = room_class.Room((-1,0), {'n':'', 'e':''}, 'A room with metal walls and floor')
#create rooms with locations in tuple format, exits as either n, s, e, or w, and a description of the room
curr_room = global_rooms[(0,0)]
#set starting room

go_commands = ['go', 'move', 'walk', 'run', 'exit']
north_commands = ['n', 'north', 'up', 'forward']
south_commands = ['s', 'south', 'down', 'backward']
east_commands = ['e', 'east', 'right']
west_commands = ['w', 'west', 'left']
dir_commands = north_commands.copy()
dir_commands.extend(south_commands)
dir_commands.extend(east_commands)
dir_commands.extend(west_commands)
#Sets commands that can be used to move the player and words that can be used as directions for the player to go
def lock_resolve(room, direction):
  if room.lock_status(direction) == 'unlocked':
    return 1
  else:
    print('===============\nThis exit is locked\n===============')
    return 0

def go_dir(direction, room):
  location = room.location
  x = location[0]
  y = location[1]
  if direction in north_commands and room.exits['n']:
    y += lock_resolve(room, 'n')
  elif direction in south_commands and room.exits['s']:
    y -= lock_resolve(room, 's')
  elif direction in east_commands and room.exits['e']:
    x += lock_resolve(room, 'e')
  elif direction in west_commands and room.exits['w']:
    x -= lock_resolve(room, 'w')
  elif direction in dir_commands:
    print('===============\nThere is no exit to the {}\n==============='.format(direction))
  else:
    print('===============\nThere is no exit that way\n===============')
  return (x,y)

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
    if len(curr_input) == 0:
        print('you have to enter something buddy\n')
    elif word_split[0] in go_commands:
      curr_room = global_rooms[go_dir(direction=word_split[1], room=curr_room)]
    elif word_split[0] in dir_commands:
      curr_room = global_rooms[go_dir(direction=word_split[0],room=curr_room)]
    else:
        print('===============\nI don\'t understand please try again\n===============')