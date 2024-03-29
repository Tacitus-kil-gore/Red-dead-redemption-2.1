from threading import Timer

#t = Timer(timeout, print, ['Sorry, times up'])
#t.start()
#prompt = "You have %d seconds to choose the correct answer...\n" % timeout
#answer = input(prompt)
#t.cancel()
battle_string = "PRESS THE BUTTON " + str(5) + " ON YOUR KEYBOARD WITHIN %d SECONDS TO FIRE \n"
timeout = 6
t = Timer(timeout, print, ["Times Up, you got hit"])
t.start()
prompt = battle_string % timeout
answer = input(prompt)
t.cancel()
