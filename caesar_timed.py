from threading import Thread
import time
from random import randint
from end_screen import *
timer_time = ["3" , "2", "1"]
game_win = False


def caesar_encrypt():
	global game_win
	x ="hello world"
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
	print("You look at your stolen key and you see the number " + str(pasw) + " written on it.")
	print("\nThe encrypted text reads " + str(crypt) + "\n")

	user_guess = str(input("Enter your guess:\n"))
	user_guess = user_guess.replace(" ", "")
	user_guess = user_guess.lower()
	while game_win == False:
		if user_guess == k or user_guess == x:
			game_win == True
			victory()
			return


		else:
			print("Incorect guess, try again \n")
			user_guess = str(input("Enter your guess:\n"))
			print()
	quit()



#if game_win == True:
#	print("you escaped")
