import time
def game_over(death_message):
	game_over_message =  \
	"""
	   _____          __  __ ______      ______      ________ _____  
	  / ____|   /\   |  \/  |  ____|    / __ \ \    / /  ____|  __ \ 
	 | |  __   /  \  | \  / | |__      | |  | \ \  / /| |__  | |__) |
	 | | |_ | / /\ \ | |\/| |  __|     | |  | |\ \/ / |  __| |  _  / 
	 | |__| |/ ____ \| |  | | |____    | |__| | \  /  | |____| | \ \ 
	  \_____/_/    \_\_|  |_|______|    \____/   \/   |______|_|  \_\                                                               
		"""

	go_split = game_over_message.split('\n')
	for x in go_split:
		print(x)
		time.sleep(0.4)

	for x in range (0, 1):
		time.sleep(0.2)
		print()                                       

	print(str(death_message))

#When you call the game_over function you must enter a string (in quotation marks) to be displayed after the game over text
