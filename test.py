import time
def Introanimation():


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


sd()
