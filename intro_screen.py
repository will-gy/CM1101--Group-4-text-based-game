import time

def intro_animation():
	intro_title =  \
		"""
	  _____  _____  _____  _____  ____  _   _     ____  _____  ______          _  __
	 |  __ \|  __ \|_   _|/ ____|/ __ \| \ | |   |  _ \|  __ \|  ____|   /\   | |/ /
	 | |__) | |__) | | | | (___ | |  | |  \| |   | |_) | |__) | |__     /  \  | ' / 
	 |  ___/|  _  /  | |  \___ \| |  | | . ` |   |  _ <|  _  /|  __|   / /\ \ |  <  
	 | |    | | \ \ _| |_ ____) | |__| | |\  |   | |_) | | \ \| |____ / ____ \| . \ 
	 |_|    |_|  \_\_____|_____/ \____/|_| \_|   |____/|_|  \_\______/_/    \_\_|\_\   

        	                              -The Game-   
		"""

	intro_split = intro_title.split('\n')
	for x in intro_split:
		print(x)
		time.sleep(0.4)

	for x in range (0, 2):
		time.sleep(0.2)
		print()                                       

	print("Enter any character to start")




def set_start_cell():
    # this function sets the start cell variable- run during intro sequence

    global current_room

    cell_num = randint(1,2)

    if cell_num ==1:
        start_cell = rooms["Cell A"]
        current_room = start_cell
    else:
        start_cell = rooms["Cell B"]
        current_room = start_cell


"""
counter variable to decide if it's the beginning of the game?
set to 0 then incremented in intro screen? reset to 0 at game over?
game over room with no exits / exit to start?

"""