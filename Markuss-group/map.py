from items import *

room_cell_a = {
    "name": "Cell A",

    "description":
    """ There are dripping noises echoing throughout the cell and lots of snoring coming from other cells. 
    There’s a small sink and toilet in the corner of the room and a little beam of moonlight coming from a small window. 
    From your knowledge there’s an exit south that leads to the Kitchen and a Cleaning Closet to the east. 
    But you also notice a mysterious door to the west. """,

    "exits": {"west": "Mystery Room", "east": "Cleaning Closet", "south": "Kitchen"},

    "items": []
}

room_cell_b = {
    "name": "Cell B",

    "description":
    """ The cell is almost empty apart from a bunk bed, a sink and a toilet.
    Everything is bolted in place for safety purposes therefore nothing can be taken from the cell. 
    You know that to the west there’s a Cleaning Closet, to the south is the Showers. 
    But you are unsure of what is to the east. """,

    "exits":  {"west": "Cleaning Closet", "east": "Mystery Room", "south": "Shower"},

    "items": []
}

room_closet = {
    "name": "Cleaning Closet",

    "description":
    """You step into the small cleaning closet and it’s full of cleaning products and equipment. 
    You also notice a janitor’s overall hanging on the back of the door. 
    From here you can go east to Cell B or west to Cell A. """,

    "exits": {"east": "Cell B", "west": "Cell A"},

    "items": [item_disguise]
}



room_kitchen = {
    "name": "Kitchen",

    "description":
    """You are in a large plain room with lots of benches lined up ready to accept prisoners for their meals. 
    To the side there's a cutlery stand and you notice there's still one knife that hasn't been cleared away.
    There's a door leading north back to cell A, an exit east leads to the Showers 
    and finally south there's a large door leading to the Courtyard.""",

    "exits": {"south": "Courtyard", "east": "Shower", "north": "Cell A"},

    "items": [item_bknife]
}


room_shower = {
    "name": "Shower",

    "description":
    """This room is infested with damp and the walls and ceiling appear to be peeling apart. 
    The floor is slippery and you find it hard to walk around the room without falling over. 
    Underneath one of the shower heads is a bar of soap. 
    From here you can head north towards Cell B, west to the Kitchen or south out to the Courtyard. """,

    "exits": {"north": "Cell B", "west": "Kitchen", "south": "Courtyard"},

    "items": [item_soap]
}

room_courtyard = {
   "name": "Courtyard",

   "description":"",
   """
"""
   "exits": {"north": "Kitchen", "east": "Shower", "south": "Warden's Office"},
   "items": []
}

    
room_warden = {
    "name": "Warden's Office",

    "description":
    """ 
""",

    "exits": {"north": "Courtyard", "south": "Exit"},

    "items": []
}

room_exit = {
    "name": "Exit",

    "description":
    """
""",

    "exits": {"north": "Warden's Office"},

    "items": []
}

room_deadend = {
    "name": "Mystery Room",

    "description": "TBC",

    "exits": {"east": "Cell A", "north": "Cell B"},

    "items": []
}



rooms = {
    "Cell A": room_cell_a,
    "Cell B": room_cell_b,
    "Cleaning Closet": room_closet,
    "Kitchen": room_kitchen,
    "Shower": room_shower,
    "Courtyard": room_courtyard,
    "Warden's Office": room_warden,
    "Mystery Room": room_deadend,
    "Exit": room_exit
}