from items import *

room_cell_a = {
    "name": "Cell A",

    "description":
    """There are dripping noises echoing throughout the cell and lots 
of snoring coming from other cells. There's a small sink and toilet 
in the corner of the room and a little beam of moonlight coming from 
a small window.""",

    "exits": {"west": "Library", "east": "Cleaning Closet", "south": "Kitchen"},

    "items": []
}

room_cell_b = {
    "name": "Cell B",

    "description":
    """The cell is almost empty apart from a bunk bed, a sink and a toilet. 
Everything is bolted in place for safety purposes therefore nothing can 
be taken from the cell.""",

    "exits":  {"west": "Cleaning Closet", "east": "Library", "south": "Shower"},

    "items": []
}

room_closet = {
    "name": "Cleaning Closet",

    "description":
    """You step into the small cleaning closet and it's full of cleaning products 
and equipment. You also notice a janitor's overall hanging on the back of 
the door.

From here you can go east to Cell B or west to Cell A.""",

    "exits": {"east": "Cell B", "west": "Cell A"},

    "items": [item_janitor_disguise]
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """You are in a large plain room with lots of benches lined up ready 
to accept prisoners for their meals. There's a cutlery stand and you notice there's
one knife that hasn't been cleared away.""",

    "exits": {"south": "Courtyard", "east": "Shower", "north": "Cell A"},

    "items": [item_bknife, item_chef_disguise]
}

room_shower = {
    "name": "Shower",

    "description":
    """This room is infested with damp and the walls and ceiling appear to 
be peeling apart. The floor is slippery and you find it hard to walk 
around the room without falling over. Underneath one of the shower 
heads is a bar of soap.""",

    "exits": {"north": "Cell B", "west": "Kitchen", "south": "Courtyard"},

    "items": [item_soap, item_shank]
}

room_courtyard = {
   "name": "Courtyard",

   "description":
   """The courtyard is lit by the moon in the night sky and seems eerily quiet
and lifeless. There are large watchtowers overlooking the courtyard but none 
of them seem to be manned at the moment. In the centre is some gym equipment 
and the outside is surrounded by benches. One of the benches seems to have a 
figure sat on it.""",
    
   "exits": {"north": "Kitchen", "east": "Shower", "south": "Warden's Office"},

   "items": []
}
    
room_warden = {
    "name": "Warden's Office",

    "description":
    """The Warden's office is very smart with shelves spread around the room holding 
books and other important looking documents. In the centre on the room there's a 
large desk with draws overflowing with paperwork. On the south side of the room has 
a door with the words fire escape written above it.""",

    "exits": {"north": "Courtyard", "south": "Exit"},

    "items": []
}

room_exit = {
    "name": "Exit",

    "description":
    """You manage to sneak out of the fire escape which leads to the employee car park. 
You hop into the Warden's car and drive towards to the exit of the prison. Luckily 
the guards don't bother checking who's inside and they open up the gates. You drive 
away from the prison with a smirk on your face and with the feeling of freedom.""",

    "exits": {"north": "Warden's Office"},

    "items": []
}

room_library = {
    "name": "Mystery Room",

    "description":
    """You enter the mysterious room and realise that this is the prison library.
It looks barely ever used as all the books are covered in dust and some are still
in boxes around the room. There's lots of paper around the room and the desks are
covered in important looking documents.""",

    "exits": {"east": "Cell B", "west": "Cell A" },

    "items": [item_documents]
}


rooms = {
    "Cell A": room_cell_a,
    "Cell B": room_cell_b,
    "Cleaning Closet": room_closet,
    "Kitchen": room_kitchen,
    "Shower": room_shower,
    "Courtyard": room_courtyard,
    "Warden's Office": room_warden,
    "Library": room_library,
    "Exit": room_exit
}
