import room_class
import item_class
import player_class
#make a dictionary for global rooms that will contain every room as they are instanciated
global_rooms = room_class.global_rooms

hero = player_class.Player('hero')

#Rooms:
#create rooms with locations in tuple format, exits as either n, s, e, or w, :locked or :unlocked and a description of the room
room1 = room_class.Room((0,0), {'n': 'locked', 'w':''}, 'The starting room')
room2 = room_class.Room((0,1), {'s':'locked', 'w':''}, 'A bathroom')
room3 = room_class.Room((-1,1), {'n':'', 's':'', 'e':'', 'w':''}, 'A room full of weapons')
room4 = room_class.Room((-1,2), {'s':''}, 'An office')
room5 = room_class.Room((-2,1), {'e':''}, 'A storage closet')
room6 = room_class.Room((-1,0), {'n':'', 'e':''}, 'A room with metal walls and floor')
#Items:
rusty_key = item_class.Key('Rusty Key', 'An old rusty key',room1, room1, 'n')
#set starting room
curr_room = global_rooms[(0,0)]

#Sets commands that can be used by the player and words that can be used as directions for the player to go
look_commands = ['look', 'examine', 'inspect', 'l']
go_commands = ['go', 'move', 'walk', 'run', 'exit']
get_commands = ['take', 'get', 'grab']
use_commands = ['use']
inv_commands = ['i','inv','inventory','items']
north_commands = ['n', 'north', 'up', 'forward']
south_commands = ['s', 'south', 'down', 'backward']
east_commands = ['e', 'east', 'right']
west_commands = ['w', 'west', 'left']
dir_commands = north_commands.copy()
dir_commands.extend(south_commands)
dir_commands.extend(east_commands)
dir_commands.extend(west_commands)
#make any output from a command stand out
def output(words):
  print('===============')
  print(words)
  print('===============')
#a function to work with go_dir() to check if the exit is unlocked and returning the value to alter the room xy by, either 1: move one room, or 0: stay in the same room
def lock_resolve(room, direction):
  if room.lock_status(direction) == 'unlocked':
    return 1
  else:
    output('This exit is locked')
    return 0
#A function to control moving the player by altering the room xy location by one in the right direction assuming the exit is unlocked
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
    output('There is no exit to the {}'.format(direction))
  else:
    output('There is no exit that way')
  return (x,y)
#A basic function for getting items
def get(item):
  hero.inventory.append(item)
  curr_room.items.remove(item)
  print('===============\nYou got {}\n==============='.format(item.name))
while True:
    # print the description, exits, and ask for input
    print('You look around and see:\n')
    print(curr_room.description+'\n')
    if len(curr_room.items) > 0:
      print('In this room there is:')
      for item in curr_room.items:
        print(item.name)
    print('This room has the following exits:')
    for exit in curr_room.exits:
        print(exit)
    curr_input = input('What do you do? \n')
    #splits the input into words for sorting so we can deal with each word one by one in order
    word_split = curr_input.lower().split()
    
    if len(curr_input) == 0:
        output('you have to enter something buddy')
    elif word_split[0] in go_commands:
      curr_room = global_rooms[go_dir(direction=word_split[1], room=curr_room)]
    elif word_split[0] in dir_commands:
      curr_room = global_rooms[go_dir(direction=word_split[0],room=curr_room)]
    #If the player types get item it goes through each item in that room to check if it is what the player asked for, if it finds a match it executes the get function.  If no match is found it tells the player that the item isn't there
    elif word_split[0] in get_commands:
      item_got = False
      for item in curr_room.items:
        if item.name.lower() in item.get_names and item_got == False:
          get(item)
          item_got = True
      if item_got == False:
        output('{} is not in this room'.format(' '.join(word_split[1:])))
    #check first word for an inventory command then prints the contents of the player's inventory
    elif word_split[0] in inv_commands:
      if len(hero.inventory) == 0:
        output('You don\'t have anything in your inventory')
      else:
        print('===============\nYou have:')
        for item in hero.inventory:
          print(item.name)
        print('===============')
    #if the first word is a use command it sorts through items in the inventory and sees if the remaining words match the criteria for using it.  If no match is found it tells the player
    elif word_split[0]  in use_commands:
      item_use = False
      for item in hero.inventory:
        if (' '.join(word_split[1:]) in item.get_names) and (item_use == False):
          if type(item) == item_class.Key:
            item.unlock(curr_room)
            item_use = True
      if item_use == False:
        output('You don\'t have {}'.format(' '.join(word_split[1:])))
    #checks the first word for a look command, then determines what the player is trying to look at then prints the description of the object.  If no object is given by the player prints the room description.
    elif word_split[0] in look_commands:
      looked= False
      for item in curr_room.items:
        if ' '.join(word_split[1:]) in item.get_names:
          output('{}'.format(item.description))
          looked=True
      for item in hero.inventory:
        if ' '.join(word_split[1:]) in item.get_names:
          output('{}'.format(item.description))
          looked=True
      if len(word_split) == 1 or word_split[1] == 'room':
        output('{}'.format(curr_room.description))
        looked=True
      elif looked == False:
        output('You don\'t see any {}'.format(' '.join(word_split[1:])))
    #if the command isn't recognized
    else:
      output('I don\'t understand please try again')
