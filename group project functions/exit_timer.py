if has_key = True:
        print("THE WARDEN HAS SET OFF THE ALARM")
        time.sleep(1)
        print("YOU HAVE 3 MINUTES TO ESCAPE BEFORE YOU GET CAUGHT!")
        time.sleep(60)
        print("YOU HAVE TWO MINUTES LEFT TO ESCAPE")
        time.sleep(60)
        print("YOU HAVE ONE MINUTE LEFT TO ESCAPE")
        time.sleep(30)
        print("30 SECONDS, GET A MOVE ON")
        time.sleep(30)
gameover()
#This code 'should' work as a timer once the user has obtained the key, but I can't test it atm with the full game. I need to modify the game_over function as well.
