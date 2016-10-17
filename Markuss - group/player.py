from items import *
from map import rooms
from random import randint

inventory = [item_soap]




f = randint(0,2)
if f ==1:
    current_room = rooms["Cell A"]
else:
    current_room = rooms["Cell B"]