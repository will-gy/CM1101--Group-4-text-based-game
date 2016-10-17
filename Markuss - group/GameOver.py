import time

def gameover():


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


