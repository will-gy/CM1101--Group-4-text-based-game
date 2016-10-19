from threading import Thread
import time
from random import randint
timer_time = ["3" , "2", "1"]
game_win = False
def exit_timer():
	global game_win
	while game_win == False:
		for x in timer_time:
			print("You have " + str(x) + " minute(s) remaining!")
			time.sleep(60)
			if x == "1" and game_win == False:
				print("game over")
				return
	return

def caesar_encrypt():
	global game_win
	x ="kirill is the best"
	k = x.replace(" ", "")
	pos = 0
	text = list(k)
	length = len(text)
	pasw = randint(1,3)
	print()
	
	crypt = ""
	aph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	while pos < length:
		new_position = aph.index(text[pos]) + pasw
		if new_position >= 26:
			new_position = new_position - 26
		text[pos]=aph[new_position]
		crypt = crypt + text[pos]
		pos = pos +1
	print("The key is " + str(pasw))
	print("The encrypted text reads " + str(crypt))
	print(x)
	print(k)
	user_guess = str(input("Enter your guess \n")) 
	user_guess = user_guess.replace(" ", "")
	user_guess = user_guess.lower()
	while game_win == False:
		if user_guess == k or user_guess == x:
			game_win == True
		else:
			print("Incorect guess, try again")
			user_guess = str(input("Enter your guess \n")) 
	if game_win ==True:
		return ("you escaped")

t1 = Thread(target = exit_timer)
t2 = Thread(target = caesar_encrypt)
t1.start()
t2.start()  