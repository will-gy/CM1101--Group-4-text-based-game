#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from intro import *
from game_over import *
from random import *
import time



guard = False   # boolean value for guard
warden = False  # boolean value for warden
has_key = False # boolean value for the exit key
bypass = False


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

    """This function takes a list of items and returns a comma-separated list of 
    item names (as a string). """

    empt_str = ""
    place_ho = []

    for x in items:
        empt_str = (x["name"])
        place_ho.append(empt_str)

    list_str = ", ".join(place_ho)
    return list_str


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names."""
    
    item_str = list_of_items(room["items"])
    if item_str != "":
        print("There is " + item_str + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". """
    
    item_str = list_of_items(items)
    print ("You have " + item_str + ".\n" )


def print_room(room):
    global bypass
    
    # display room name
    print()
    print(room["name"].upper())
    print()
    
    # bypass is set to true when ??
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
    this exit leads. """

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line."""

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

    if guard is False:
      print("You can:")
      # Iterate over available exits
      for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
      for item in room_items:
        print("TAKE " + (item["id"]).upper() + " to take " + item["name"] + ".")
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
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    global warden
    global guard

    # if you're in the courtyard, sets warden to true    
    if current_room["name"] == "Courtyard":
      warden = True
      # call warden function?

    # if no guard in the room- update current room
    if guard is False:
      new = current_room["exits"][direction]
      current_room = rooms[new]
      return current_room

    else:
      print ("\nYOU CANNOT RUN FROM THE GUARD\n")
      new_input = get_user_input()
      return new_input



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
    z=0
    b=0
    for x in current_room["items"]:
     if item_id == x["id"]:
      if x["id"] == "soap":
          print ("game over")
          gameover()
          exit()

      inventory.append(x)
      h = current_room["items"]
      del h[z]
      b= 1
     z = z +1
    if b == 0:
        print("\nYou cannot take that\n")
        get_user_input()



def go_back():
    """ This function returns you to your cell if you attempt to trick/steal and fail """

    global current_room
    current_room = start_room
    print("\nHe didn't believe you and you've been returned to your cell. Bad luck.\n")



def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    b =0
    for x in inventory:
        if item_id == x["id"]:
            inventory.remove(x)
            b = b +1
            current_room["items"].append(x)

    if b == 0:
        print("\nYou cannot drop that\n")
        get_user_input()



#if guard = True:
#  deal_with_guard()

def deal_with_guard():
  print("Uh oh, you've run into a guard!\n")

  print_weapons()
  print_tricks()


def print_weapons():
  """ This function prints a list of any weapons in your inventory and commands to call them """

  # loop through items in inventory returning all weapons, i.e. items with damage > 0
  for item in inventory:
    if item["damage"] != 0:
      print ("KILL with " + (item["id"]).upper() + " to kill guard with " + item["name"] + ".")

  # also gives option to kill with bare hards
  print("KILL with HANDS to attempt to kill the guard with your bare hands.")

#print_weapons()


def print_tricks():
  """ This function prints a list of any trick items in your inventory and commands to call them """

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
        print("You have tricked a guard.")
        guard = False
      else:
        go_back()

    else:
      #loop through items in inventory looking for weapon id that matches user input
        try:
            for item in inventory:
                if item["id"] == trick_item:
                  
                  #guard dies if chance * item damage is greater than 20
                  if item["trick"] * chance > 20:
                      guard = False
                      bypass = True
                      print("You have tricked a guard")
                  else:
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
        print("You have killed a guard.")
        guard = False 
      else:
        print("Game over")
        game_over("death message")

    else:
      #loop through items in inventory looking for weapon id that matches user input
      for item in inventory:
          if item["id"] == weapon:
              
              #guard dies if chance * item damage is greater than 20
              if item["damage"] * chance > 20:
                  print("You have killed the guard")
                  guard = False
                  bypass = True
              else:
                  print("game over")
                  game_over("death message")



def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":     
#        Guard_in_the_room()  #check's if guard in room
        valid = is_valid_exit(current_room["exits"],command[1])
        if len(command) > 1 and valid is True:
            execute_go(command[1])
        else:
            print("\nGo where?\n")
            new_input = get_user_input()
            print(new_input)
            print(new_input[1])
            execute_go(new_input[1])

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("\nTake what?\n")
            get_user_input()

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("\nDrop what?\n")
            get_user_input()

    elif command[0] == "trick":
        if len(command) >1:
            execute_trick(command[1])
        else:
            print("\nTrick with what?\n")
            get_user_input()

    elif command[0] == "kill":
        if len(command)>1:
            execute_kill(command[1])
        else:
            print("\nKill with what?\n")
            get_user_input()

    elif command[0] == "steal":
        if len (command)>1:
            execute_steal()
        else:
            print ("\nSteal what?\n")
            get_user_input()

    else:
        print("\nI don't understand, please try again.\n")
        get_user_input()


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    normalised_user_input = get_user_input()

    return normalised_user_input


def get_user_input():
    # Read player's input and return as normalised list of words

    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    print(normalised_user_input)

    return normalised_user_input



def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

   """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
#    intro_animation()
    
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
