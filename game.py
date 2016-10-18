#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
from random import randint


random_number = randint(0,10)       #Generates random number form 1-10
#guard_probs = 1
guard = False

#temporary
current_room = rooms["Cell A"]

def guard_in_the_room():
# sets the boolean value for guard present in room based on 10% propability

    guard_prob = 1
    
    random_number = randint(0,10)
    if guard_prob == random_number:
        guard = True
    else:
        guard = False
    return guard

guard_present = guard_in_the_room() ##gets the value from Guard in the room func


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'
    """
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

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>
    """
    item_str = list_of_items(room["items"])
    if item_str != "":
        print ("There is " + item_str + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>
    """

    item_str = list_of_items(items)
    print ("You have " + item_str + ".\n" )


def print_room(room):

    # display room name
    print()
    print(room["name"].upper())
    print()

    # Display room description
    print(room["description"])
    print()
    print_room_items(room)

#print_room(current_room)    


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.


    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
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

    "TAKE <ITEM ID> to take <item name>."  etc... """

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        # Print the item and take command
        print ("TAKE " + (item["id"]).upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        # Print the item and drop command
        print ("DROP " + (item["id"]).upper() + " to drop " + item["name"] + ".")
    
    print("\nWhat do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room

    # if guard is not present, and room is valid, move rooms
    if guard_present is False:
        current = current_room["exits"][direction]
        current_room = rooms[current]
        return current_room

    # if guard is present you cannot leave room
    elif guard_present is True:
        print ("YOU CANNOT RUN FROM THE WARDEN")

    # if room choice not valid, print error
    else:
        print("You cannot go there.")

"""
    # check if guard is present (except if in cell or courtyard)
    if room != "courtyard" or "cell a" or "cell b":
        guard_present = guard_in_the_room()

    # if guard is present, run deal with guard function
        if guard_present is True:
            deal_with_guard()
        else:
"""


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    z= 0
    b= 0
    for x in current_room["items"]:
     if item_id == x["id"]:
      inventory.append(x)
      h = current_room["items"]
      del h[z]
      b= 1
     z = z +1
    if b == 0:
        print("you cannot take that")




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


#def execute_trick():
    #dfjfhdsjfs


    
def execute_kill(weapon):
    """this function takes a weapon as an input, check if it's in your inventory, looks up 
    damage value from item dictionary, and multiplies it by a random number 1-5, then updates
    guard to False if more than 20. """
    
    global guard

    # set chance as random integer between 1-5
    chance = randint(1,5)

    # if weapon used is bare hands, then set damage as 1 and test
    if weapon == "hands":
      if chance + 1 >= 5:
        print("You have killed a guard with your bare hands! Brutal!")
      else:
        print("Game over, you died")

    else:
      # loop through items in inventory looking for weapon id that matches user input
      for item in inventory:
          if item["id"] == weapon:
              
              # guard dies if chance * item damage is greater than 20
              if item["damage"] * chance > 20:
                  guard = False
                  print("You have killed the guard with " + item["name"] + ". Safe for now!")
              else:
                  print("Game over- you died")

#execute_kill("shank")





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
            print("Trick with what?")  # need to add some more trick items

    elif command[0] == "kill":
        if len(command)>1:
            execute_kill()
        else:
            print("Kill with what?")

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

#menu(current_room["exits"], current_room["items"], inventory)


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():

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
