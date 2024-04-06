#imports:
import random
import time
from threading import Timer
#starting variables and constants:

towns = {"Valentine." : ["""
A rough, raucous, hard-working town that provides livestock at auction to Heartlands landowners,
and rest and refreshment to thirsty cowboys.It's nicknamed 'Mudtown' because the streets, 
buildings, and most of the residents are rarely clean.
    """], "Strawberry." : ["""
Until recently, this mountain town was little more than a base camp for lumberjacks and hunters,
but more settlers and visitors have arrived as the local logging industry continues to grow.
A small, isolated community of honest working folk.
    """], "Saint Denis." : ["""
A lively, 200-year-old melting-pot city where industry magnates,
socialites, traders, sailors, workers, beggars, and thieves all live side by side.
With good rail, road, and river connections for sugar, cotton, and other commodities trading,
and a new electric power plant, business is booming.
    """], "Rhoades." : ["""
A prim and proper Southern town on the surface,
but many residents can't forget the Civil War or the town's pre-war glory days,
where the horrific oppression of the slave trade made white landowners rich.
Racial tensions, corruption, and old family feuds run deep.
    """], "Annesburg." : ["""
A mining town established by German settlers who discovered the rich coal seams in the surrounding hills.
The surrounding countryside and waterways are sooty and polluted from the
mining operations which have been running for almost a century
    """], "Open road." : ["""
Explore the open road of America. 
From the Grizzly mountains of Ambarino to the southern plantations of Lemoyne
    """]}

tuberculosis_stage = 0
Arthur_morgan_hp = 150 - (tuberculosis_stage * 10)
towns_num = list(range(len(towns)))
money = 0
missions_completed = 0
#costant variables:
YEAR = 1899
STARTING_TOWN = list(towns.keys())[1]



# text vairiables. These vairables will be used to describe the setting and the missions
#missions_t stands for missions text and this hash will store the enemies for each mission.
missions_t = {"""
You find dutch waiting for you in the saloon. He sits you down and takes a drink from his whiskey. 
"arthur you've got to have faith in me we just need 5000 more dollars and we can escape to tahiti." says dutch
"yeah i know" you replied.  "I've found another job robbing leviticus cornwall, that rich fella we robbed a couple months back in Blackwater." dutch says.
"awww no dutch not this again, leviticus cornwall has already sent that pinkerton detective agency after us, we dont need more trouble" you say.
"arthr your losing faith, you need to hav-BANG" 
"DUTCH VANDERLINDE COME OUTSIDE RIGHT NOW WITH YOUR HANDS UP THIS IS THE PINKERTON DETECTIVE AGENCY" you hear from outside the saloon.
"oh shoot the pinkertons are here" dutch says. dutch runs out the back door and you jump through the window to your left out into an alley.
you find a pinkerton in the alley with his hand on his gunholster staring at you.
""" : 0, "insert strawwberry mission" : 1, "insert saint denis mission" : 0, "insert rhoades mission" : 2, "insert annesburg mission" : 3}


#thesem are all of the items in the game, dmg stands for the damage they do, reload speed is
#the time it takes to reload and aim time is how easy it is to aim, higher is easier.
ITEMS = {
"cattleman_revolver" : {"dmg" : 20, "reload speed": 1, "aim time" : 3},
"springfield_rifle" : {"dmg" : 100, "reload speed" : 5, "aim time" : 1},
"m1911" : {"dmg" : 40, "reload speed" : 1, "aim time": 3}
}

#dictionary for the enemies, hp is the amount of health points they have, dmg is the
#amount of damage they do per hit and aim skill is the chance out of 10 of hitting you
ENEMIES ={
"the pinkerton" : {"hp" : 100, "dmg" : 20, "aim skill" : 4},
"the lawman" : {"hp" : 100, "dmg" : 30, "aim skill" : 6},
"the braithwaite" : {"hp" : 100, "dmg" : 20, "aim skill" : 7},
"micah" : {"hp" : 200, "dmg": 70, "aim skill" : 9}}

inventory = ["cattleman_revolver"]

#functions:
# this function plays every time the player leaves a town, or starts the game, this acts as the main menu
def entertown():
   while True:
       try:
            inpt = int(input("""
            You are now on the open road, where do you want to go next?
            0: Valentine
            1: Strawberry
            2: Saint Denis
            3: Rhoades
            4: Annesburg
            5: Explore the open road
            type answer here: """))
            if inpt not in towns_num:
                print(towns[6]) #generates error
       except:
            print("value must be an integer between 0 and 5")
       else:
            break
   if inpt < 5:
       print("Welcome to", list(towns.keys())[inpt], towns[list(towns.keys())[inpt]][0] , "You walk into the center of the town.")
       while True:
           try:
               inpm = int(input("""
               The place where Dutch waiting for you is down the road the left, where do you go:
               1: go left and meet dutch (this will start the mission)
               2: explore the town
               type answer here: """))

               if inpm not in list(range(1, 3)):
                   print("chung")
                   print(towns[6]) #generates error

           except:
                print("chug")
                print("value must be an integer between 1 and 2")
           else:
                break
   else:
       #insert content about exploring the world
       print("")

   return inpt, inpm



#this function will be where arthur fights enemies.
def combat(e):
    hp = Arthur_morgan_hp #stands for health points
    ehp = ENEMIES[e]["hp"] #stands for enemy health points
    debug = False

    #this loop is the battle loop, this will repeat until either the player's or the enemy's hp is reduced to 0
    while hp > 0 or ehp > 0:

        print("You have ", hp, "health")
        print("Enemy:", e)
        #for loop which will iterate through inventory list and print every item and its stats
        print("Your Inventory:")
        for c, i in enumerate(inventory):
            print(inventory[c], ": ", ITEMS[i], "Type", c, "to select this weapon")
        #asks the user to select a weapon for the upcoming battle
        while True:
            try:
                player_input = input("What weapon do you want to use? ")
                weapon = int(list(player_input))
                print("You have selected: ", weapon)
            except:
                if player_input == "debug":
                    print("debug mode on")
                    debug = True
                    break
                else:
                    print("please type an integer that corresponds to a weapon in your inventory")
            else:
                break

        if debug == True:
            ehp = 0
            break

        print("battle starting in 3")
        time.sleep(1)
        print("battle starting in 2")
        time.sleep(1)
        print("battle starting in 1")
        time.sleep(1)
        print("GO")


        #battle sequence will start, a random number will be chosen and the user will have to press that number on their
        #keyboard fast enough in order to fire, simulating quickdraw.
        battle_num = random.randint(0, 9)
        battle_string = "PRESS THE BUTTON " + str(battle_num) + " ON YOUR KEYBOARD WITHIN %d SECONDS TO FIRE \n"
        timeout = ITEMS[weapon]["aim time"]
        t = Timer(timeout, print, ["Times Up, you got hit, press enter to reload the gun and fire again"])
        t.start()
        prompt = battle_string % timeout
        answer = input(prompt)
        t.cancel()

        # tests to see if the player entered a value, and if so the value was correct.
        while True:
            try:
                if answer == '':
                    player_inputted = False
                elif int(answer) == battle_num:
                    player_inputted = True
                    print("You hit the enemy for", ITEMS[weapon]["dmg"], "damage")
                    ehp -= ITEMS[weapon]["dmg"]
                    print(e, " now has ", ehp, " health left")
                else:
                    player_inputted = True
                    print("You missed the enemy")
                    print("They hit you for", ENEMIES[e]["dmg"], "damage")
                    hp -= ENEMIES[e]["dmg"]
                    print("You now have ", hp, "health left")
            except:
                print("Please enter an integer")
            else:
                break

        #checks whether player has won or lost the round
        if hp <= 0:
            print("You died, the game will now restart")
            break
        elif ehp <= 0:
            print("You defeated ", e)
            break
        else:
            # reloading mechanic, the reload speed of the weapon will affect the amount of chances that the
            # enemy has to hit the player.
            print("reloading...")
            time.sleep(ITEMS[weapon]["reload speed"])
            if player_inputted == False:
                hp -= ENEMIES[e]["dmg"]
                print(e, "hit you for", ENEMIES[e]["dmg"], "damage while you were reloading")
            else:
                damage_taken = 0
                for i in range(0, ITEMS[weapon]["reload speed"]):
                    if random.randint(1, 10) <= ENEMIES[e]["aim skill"]:
                        damage_taken += ENEMIES[e]["dmg"]
                hp -= damage_taken
                print("You took ", damage_taken, "damage while reloading")










#this function will start the missions
def missions(t):
    global tuberculosis_stage
    global Arthur_morgan_hp
    global towns_num
    global money
    global missions_completed


    print(list(missions_t.keys())[t])
    combat(list(ENEMIES.keys())[list(missions_t.values())[0]])
    print("""
    
You escape and make it back to camp,
finding 100 dollars on the corpse of""", list(ENEMIES.keys())[list(missions_t.values())[0]], """
as you leave the town. You find a note 
in your tent where dutch tells 
you where he is waiting for you in the next town.

    """)
    money += 100
    missions_completed += 1
    tuberculosis_stage += 1

#main routine 
while True:

    #here the equivalent of the starting "cutscene" will play

    town_selection = entertown()
    tc = town_selection[0] #stands for town choice
    mve = town_selection[1] #variable stores the users choice of starting the mission or exploring the town. Mission Vs Explore hence the name, mve
    if mve == 1:
        missions(tc)
    elif mve == 2:
        print("g")

