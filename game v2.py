from map import rooms
from player import *
from items import *
from gameparser import *
from random import randint


def print_weapons():
  """
  """
  kill_count = 0

  # loop through items in inventory returning all weapons, i.e. items with damage > 0
  for item in inventory:
    if item["damage"] != 0:
      # increment kill_count to indicate 1 or more weapon available
      kill_count = kill_count + 1
      print ("KILL with " + (item["id"]).upper() + " to kill guard with " + item["name"] + ".")

  # if no kill items in inventory, gives option to kill with bare hards
  if kill_count == 0:
    print("KILL with HANDS to attempt to kill the guard with your bare hands.")

#print_weapons()


def print_tricks():
  """
  """
  trick_count = 0

  # loop through items in inventory returning all trick items, i.e. items with trick > 0
  for item in inventory:
    if item["trick"] != 0:
      print ("TRICK with " + (item["id"]).upper() + " to trick the guard with " + item["name"] + ".")
      # increment trick count
      trick_count = trick_count + 1

  # if no trick items available, gives option to attempt trick
  if trick_count == 0:
    print("TRICK with CHARM to attempt to trick the guard with a flimsy lie about being a lost visitor.")

#print_tricks()




def deal_with_guard():
  print("Uh oh, you've run into a guard!\n")

  print_weapons()
  print_tricks()


#if guard = True:
#  deal_with_guard()



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
        print("You have killed a guard.")
      else:
        print("Game over")

    else:
      #loop through items in inventory looking for weapon id that matches user input
      for item in inventory:
          if item["id"] == weapon:
              
              #guard dies if chance * item damage is greater than 20
              if item["damage"] * chance > 20:
                  guard = False
                  print("You have killed a guard")
              else:
                  print("game over")

#execute_kill("shank")



