#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from intro import *
from game_over import *
from random import *
import time


guard = False   # guard present if True
warden = False  # warden present if True
has_key = False # key to warden's office in possession if True
bypass = False  # ???


def Guard_in_the_room():
# sets the boolean value for guard- 1 in 3 chance

    global guard
    random_number = randint(1,3)

    # if current room is cells or courtyard, guard is false
    if current_room == rooms["Cell A"] or current_room == rooms["Cell B"] or current_room == rooms["Courtyard"]:
      guard = False

    # if not in cells/courtyard, guard appears when random number is equal to 1
    else:
      if random_number == 1:
        guard = True
        


def list_of_items(items):

    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string)."""

    empt_str = ""
    place_ho = []
    for x in items:
        empt_str = (x["name"])
        place_ho.append(empt_str)
    liststr = ", ".join(place_ho)
    return liststr

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:
    """
    pass
    item_str = list_of_items(room["items"])
    if item_str != "":
        print ("There is " + item_str + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here."."""

    item_str = list_of_items(items)
    print ("You have " + item_str + ".\n" )


def print_room(room):
    global bypass

    # display room name
    print()
    print(room["name"].upper())
    print()

    if bypass is False:
      Guard_in_the_room()

    else:
      bypass = False

    if room["name"] == "Courtyard":
      global warden
      warden = True
      print("""The warden is standing in the far corner, but he hasn't seen you.
You know he has the key you need to escape...\n""")

    # if guard in room, print weapon / trick actions
    if guard == True:
        print("UH OH, YOU HAVE RUN INTO A GUARD!\n")
        print_tricks()
        print_weapons()
        print()

    # if guard not in room, display room description
    else:
        print(room["description"])
        print()
        print_room_items(room)



def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads."""

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line. """

    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items. """

    # print normal menu only if guard = false
    if guard is False:
      print("You can:")

      # iterate over available exits and print exit and where it leads
      for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))

      # iterate over items in room and print take commands
      for item in room_items:
        print("TAKE " + (item["id"]).upper() + " to take " + item["name"] + ".")

      # iterate over items in inventory and print drop commands
      for item in inv_items:
        print("DROP " + (item["id"]).upper() + " to drop " + item["name"] + ".")
    
      print("\nWhat do you want to do?\n")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been lised by the function normalise_input(). """

    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there." """

    global current_room
    global warden
    
    # if current_room is courtyard, then warden is true
    if current_room["name"] == "Courtyard":
      warden = True
      # run warden()
    
    # if player doesn't have key and current room is courtyard and direction is south to warden's office
    if has_key == False and current_room["name"] == "Courtyard" and direction == "south":
      print("\nYou cannot open warden's office without the key which you know is on the warden...\n")

    elif guard == True:
      print("\nYOU CANNOT RUN FROM THE GUARD\n")

    # if guard is false, then you can leave the room
    elif guard is False:
      current = current_room["exits"][direction]
      current_room = rooms[current]
      return current_room
    
    

def execute_steal():
    global warden
    if random.randint(0,100)<20:
      has_key=True
      return has_key
      warden=False
    else:
      go_back()


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    index = 0
    if_test = 0

    # loop through item dictionaries in current room
    for item in current_room["items"]:

      # if given item matches item["id"]
      if item_id == item["id"]:

        # add item to inventory
        inventory.append(item)

        # delete list item with index
        item_id_dictionary = current_room["items"]
        del item_id_dictionary[index]
        
        # print statement
        print("\nYou took " + item["name"] + ".")

        # increment if_test to show that if was run i.e. item in room
        if_test = 1

      # increment z to give list index for current 
      index = index + 1

    # if test == 0, item wasn't found so it loop didn't run- item not in room
    if if_test == 0:
      print("\nYou cannot take that.\n")



def execute_drop(item_id):
  """This function takes an item_id as an argument and moves this item from the
  player's inventory to list of items in the current room. However, if there is
  no such item in the inventory, this function prints "You cannot drop that."
  """
  b = 0
  
  # loop over items in inventory
  for item in inventory:
    
    # if item input matches item id (i.e. item in inventory)
    if item_id == item["id"]:
      
      # if item is soap-
      if item["id"] == "soap":
        game_over("You dropped the soap. NEVER DROP THE SOAP IN PRISON.")

      # otherwise remove item from inventory
      inventory.remove(item)

      # add item to current room items list
      current_room["items"].append(item)

      # print message
      print("\nYou dropped " + item["name"] + ".")
      # increment b if item found
      b = 1

  # if b is 0 then item not in inventory
  if b == 0:
    print("\nYou cannot drop that.\n")





def go_back():
  global current_room
  current_room = start_room
  print()
  print("He didn't believe you and you've been returned to your cell. Bad luck.\n")



def print_weapons():
  """
  """

  # loop through items in inventory returning all weapons, i.e. items with damage > 0
  for item in inventory:
    if item["damage"] != 0:
      # increment kill_count to indicate 1 or more weapon available
      print ("KILL with " + (item["id"]).upper() + " to kill guard with " + item["name"] + ".")

  # also gives option to kill with bare hards
  print("KILL with HANDS to attempt to kill the guard with your bare hands.")

#print_weapons()


def print_tricks():
  """
  """
  # loop through items in inventory returning all trick items, i.e. items with trick > 0
  for item in inventory:
    if item["trick"] != 0:
      print ("TRICK with " + (item["id"]).upper() + " to trick the guard with " + item["name"] + ".")

  # also gives option to attempt trick
  print("TRICK with CHARM to attempt to trick the guard with a flimsy lie about being a lost visitor.")

#print_tricks()


def execute_trick(trick_item):
    """this function takes a weapon as an input, check if it's in your inventory, looks up 
    damage value from item dictionary, and multiplies it by a random number 1-5, then updates
    guard to False if more than 20. """
    
    global guard
    global bypass

    # set chance as random integer between 1-5
    chance = randint(1,5)

    # if weapon used is bare hands, then set damage as 1 and test
    if trick_item == "charm":
      if chance + 1 >= 5:
        guard = False
        print("You have successfully tricked the guard!")
      else:
        guard = False
        go_back()

    else:
      try:
      # loop through items in inventory looking for weapon id that matches user input
        for item in inventory:
          
          # guard dies if weapon * item damage is greater than 20
          if item["id"] == trick_item:
            if item["trick"] * chance > 20:
              guard = False
              bypass = True
              print("You have successfully tricked the guard!")
            else:
              guard = False
              go_back()
      except:
          print("test")


def execute_kill(weapon):
    """this function takes a weapon as an input, check if it's in your inventory, looks up 
    damage value from item dictionary, and multiplies it by a random number 1-5, then updates
    guard to False if more than 20. """
    
    global guard
    global bypass

    # set chance as random integer between 1-5
    chance = randint(1,5)

    # if weapon used is bare hands, then set damage as 1 and test
    if weapon == "hands":
      if chance + 1 >= 5:
        print("\nYou successfuly killed the guard!\n")
        guard = False
        bypass = True
      else:
        game_over("The guard was stronger than you and you died. Bad luck.")
        guard = False

    else:
      #loop through items in inventory looking for weapon id that matches user input
      for item in inventory:
        if item["id"] == weapon:
              
          #guard dies if chance * item damage is greater than 20
          if item["damage"] * chance > 20:
            guard = False
            bypass = True
            print("\nYou successfuly killed the guard!\n")
  
          else:
            guard = False
            game_over("The guard was stronger than you and you died. Bad luck.")





def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":     
        valid = is_valid_exit(current_room["exits"],command[1])
        if len(command) > 1 and valid is True:
            execute_go(command[1])
        else:
            print("\nGo where?\n")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("\nTake what?\n")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("\nDrop what?\n")

    elif command[0] == "trick":
        if len(command) >1:
            execute_trick(command[1])
        else:
            print("\nTrick with what?\n")

    elif command[0] == "kill":
        if len(command)>1:
            execute_kill(command[1])
        else:
            print("\nKill with what?\n")

    elif command[0] == "steal":
        if len (command)>1:
            execute_steal()
        else:
           print ("\nSteal what?\n")
    else:
        print("\nThis makes no sense.\n")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction"."""

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():

  # intro_animation()
    
  # Main game loop
  while True:

    # Display game status (room description, inventory etc.)
    print("\n"*2 + "*" * 90 + "\n" * 2)
    print_room(current_room)
    print_inventory_items(inventory)

    # Show the menu with possible actions and ask the player
    command = menu(current_room["exits"], current_room["items"], inventory)

    # Execute the player's command
    execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation

if __name__ == "__main__":
  main()