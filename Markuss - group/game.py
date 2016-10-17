#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from random import *
from Intro import *
from GameOver import *



random_number = randint(0,3)
guard_probs = 1
guard = False
warden = False  #boolean values for guard and warden
has_key = False #boolean value for the exit key


def Guard_in_the_room():            ##sets the boolean value for guard on 10% propability
    if guard_probs == random_number:
        Guard = True
    else:
       Guard = False
    return Guard

po = Guard_in_the_room() ##gets the value from Guard in the room func


def list_of_items(items):

    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    """
    pass
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
    itemss = list_of_items(room["items"])
    if itemss != "":
        print ("There is " + itemss + " here.\n")
    else:
        pass



def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:


    """
    pass

    pol = list_of_items(items)
    print ("You have " + pol + ".\n" )

def print_room(room):

    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)              #makes sure that guard is not generated along with the warden
    if room["name"] != "Courtyard":
     po = Guard_in_the_room()
     guard = True
     if po is True:
         print()
         print("YOU HAVE MET A GUARD")
         print()

    else:
         warden = True
         print("YOU SEE THE PRISON WARDEN HERE\n HE HASNT SEEN YOU YET")
         print()
         print("HE HOLDS THE  KEY TO ESCAPE FROM THIS WRETCHED PLACE")
         print()




def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for it in room_items:
        print ("TAKE " + (it["id"]).upper() + " to take " + it["name"] + ".")
    for pog in inv_items:
        print ("DROP " + (pog["id"]).upper() + " to drop " + pog["name"] + ".")
    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:
"""
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    if po is False:
     current = current_room["exits"][direction]
     current_room = rooms[current]
     return current_room
    else:
        print ("YOU CANNOT RUN FROM THE WARDEN")
def execute_steal():

    if random.randint(0,100)<20:
        has_key=True
        return has_key


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
        print("you cannot take that")



def goBack():

 print("you failed")

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
        print("you cannot drop that")

def execute_trick():
    item = item_disguise
    room_inventory = current_room["items"]
    if item in room_inventory:

       trick_probability = 6 #60% probablity of tricking guard with the disguise on.
    else:
       trick_probability = 2 #20% probability of tricking guard without the disguise.

    random_int = randint(1,trick_probability)

    if random_int != int(trick_probability):

       return goBack()
    else:
       print("You successfully tricked the guard. Continue to the next room")
       return guard == False
    
def execute_kill():
    guard = False


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "trick":
        if len(command) >1:
            execute_trick()
        else:
            print("trick who?")
    elif command[0] == "kill":
        if len(command)>1:
            execute_kill()
        else:
            print("Kill who?")
    elif command[0] == "steal":
        if len (command)>1:
            execute_steal()
        else:
           print ("Steal what?")
    else:
        print("This makes no sense.")


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
    with the name given by "direction". For example:

   """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    Introanimation()
    # Main game loop
    while True:

        # Display game status (room description, inventory etc.)
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
