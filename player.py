from items import *
from map import rooms
from random import randint

inventory = [item_shank, item_documents, item_chef_disguise]


# set start room and current room at start
f = randint(0,2)

if f ==1:
    current_room = rooms["Cell A"]
    start_room = current_room
else:
    current_room = rooms["Cell B"]
    start_room = current_room