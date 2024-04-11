
#imports:
import random
import time
from threading import Timer

#master loop, this loop will never be broken and will redefine all variables once it loops, effectively fully restarting the game, this could also be called the restart loop.
while True:
    #starting variables and constants:


    logo = """
       =%%%%%%%%@@@:*#%%%%%%%%-=@@@@@%%%##:     +%@@@@@%%%%+ =%%@@@@@@%%   -@@@@@    %@@@@@@@@%#.   .-*%%#**#%@@@%##*--:    
       =@@@%###@@@@-@@@@@@@@@@:=@@@@@@@@@@@+    *@@@@@@%@@@@+*@@@@@@@@@@   #@@@@@=   @@@@@@@@@@@@: -#@@@@@@@@@@@@@@@@#      
       +@@@#+++@@@@-@@@#         #@%@# %@@@#      %@@@+ @@@@**@@@=        .@@@@@@%    .@@@@::@@@@: *@@@@@@@@@@@@@@@@@*      
       +@@@@@@@@@@@+@@@%         #@@@= %@@@*      #@@@+ @@@@%*@@@=        +@@@@@@@:    @@@@: @@@@: +@@@@@*.:-==#@@@@@#      
       +@@@*-@@@@:. @@@@@@@@%    *@@@= #@@@*      +@@@+ %@@@%*@@@#==+=    %@@@+@@@#    @@@@..@@@@- +@@@@@.      +@@@@@.     
       +@@@* %@@@=  @@@@@@@@#    *@@@+ *@@@*      =@@@# #@@@%#@@@@@@@%   .@@@@ +@@@.   @@@@.:@@@@- =@@@@@.      -@@@@@.     
       =@@@% +@@@%  @@@@.        *@@@= *@@@*      +@@@# *@@@##@@@+--::   =@@@%=+@@@+  .@@@@..@@@@- =@@@@@+      #@@@@@-     
       =@@@@  @@@@- @@@@         *@@@= =@@@*      #@@@* #@@@##@@@-       *@@@@@@@@@%  .@@@@  %@@@- =@@@@@+     .@@@@@@#     
       -@@@@  +@@@% %@@@######+-*@@@@#=%@@@#    -#@@@@%*@@@@##@@@#****** @@@%+++#@@@:**@%@@**@@@@- -#*:  :     -@@@@@@%     
       -@@@#   @@@@:#@@@@@@@@@#*@@@@@@%@@@%:    -@@@@@@@@@@%=#@@@@@@@@@@.@@@:    %@@+%@@@@@@@@@@=             +@@@@@@@+     
        ::-:   :--. .-::::.....---=-------      .==-------:  :=---------.=--     :+=:======++==:            +@@@@@@@=       
       =%%%@@@@%.@@@@@@@+@@@@@@@%.*@@@@%@%:%%*   =%@*#@@@@@@%=@@@@@@@@@*#%%%%%*%%%%%@%-@@@=  %@@=.       .+@@@@@@@+         
       +@@*=-%@@:@@#+===:+%@@*+@@*#@@*++++:@@@# =@@@*#@@##@@@=+++@@@*++-+%@@*++@@++%@@-@@@@= @@@*:     .+@@@@@@@=.          
       =@@@@@@@@-@@=      *@@-:@@##@@.    :@@@@%@@@@*#@@##@@@+   @@@:    *@@  *@@  +@@=@@@@@-@@@#:   .*@@@@@@@+             
       +@@+*@@= :@@#===   *@@:-@@##@@%%#+ :@@@@@@@@@=%@@%+++=:   @@@:    #@@  #@@. +@@+@@@@@@@@@%  :*@@@@@@@#.              
       +@@+:@@# -@@@###   #@@:=@@#*@@*++= -@@%*@@+@@-#@@*        @@@.    #@%  #@@: =@@*@@@+@@@@@# =@@@@@@@@@###**######*    
       =@@* %@@:-@@+      #@@:=@@#*@@     -@@# =:-@@=%@@*        @@@.    %@%  *@@: =@@*@@@:-@@@@* *@@@@@@@@@@@%@@@@@@@@+    
       -@@* -@@*-@@%####-%@@@%%@@**@@%####+@@*   =@@-%@@=        @@@    #@@@%++@@*@@@@=@@@: =@@@+ +@@@@@@@@@@@@@@@@@@@@:    
       :**-  +##:####**#-*******= -*******-++-   -**.###=        %%@    *****+:++=+++*:+**.  =**- .*#***====++++++====:     
       
                                                (ultra low graphics)
        
    """


    #stores the town names, descriptions, and whether or not the mission for that town has been completed
    towns = {"Valentine" : ["""
    
A rough, raucous, hard-working town that provides livestock at auction to Heartlands landowners,
and rest and refreshment to thirsty cowboys.It's nicknamed 'Mudtown' because the streets, 
buildings, and most of the residents are rarely clean.
    
        """, False], "Strawberry" : ["""
        
Until recently, this mountain town was little more than a base camp for lumberjacks and hunters,
but more settlers and visitors have arrived as the local logging industry continues to grow.
A small, isolated community of honest working folk.
    
        """, False], "Saint Denis." : ["""
        
A lively, 200-year-old melting-pot city where industry magnates,
socialites, traders, sailors, workers, beggars, and thieves all live side by side.
With good rail, road, and river connections for sugar, cotton, and other commodities trading,
and a new electric power plant, business is booming.
    
        """, False], "Rhoades" : ["""
        
A prim and proper Southern town on the surface,
but many residents can't forget the Civil War or the town's pre-war glory days,
where the horrific oppression of the slave trade made white landowners rich.
Racial tensions, corruption, and old family feuds run deep.
    
        """, False], "Annesburg" : ["""
        
A mining town established by German settlers who discovered the rich coal seams in the surrounding hills.
The surrounding countryside and waterways are sooty and polluted from the
mining operations which have been running for almost a century
    
        """, False]}

    tuberculosis_stage = 0
    Arthur_morgan_hp = 150 - (tuberculosis_stage * 10)
    towns_num = list(range(len(towns)))
    money = 0
    missions_completed = 0
    all_missions_completed = False
    #costant variables:
    YEAR = 1899
    STARTING_TOWN = list(towns.keys())[1]



    # text vairiables. These vairables will be used to describe the setting and the missions
    #missions_t stands for missions text and this hash will store the enemies for each mission.
    #this will basically store the equivalent of cutscenes
    missions_t = {"""
    
You find dutch waiting for you in the saloon. He sits you down and takes a drink from his whiskey. 
"arthur you've got to have faith in me we just need 5000 more dollars and we can escape to tahiti." says dutch
"yeah i know" you replied.  "I've found another job robbing leviticus cornwall, that rich fella we robbed a couple months back in Blackwater." dutch says.
"awww no dutch not this again, leviticus cornwall has already sent that pinkerton detective agency after us, we dont need more trouble" you say.
"arthr your losing faith, you need to hav-BANG" 
"DUTCH VANDERLINDE COME OUTSIDE RIGHT NOW WITH YOUR HANDS UP THIS IS THE PINKERTON DETECTIVE AGENCY" you hear from outside the saloon.
"oh shoot the pinkertons are here" dutch says. dutch runs out the back door and you jump through the window to your left out into an alley.
you find a pinkerton in the alley with his hand on his gunholster staring at you.
    
    """ : 0, """
    
You find Dutch waiting on a cliff overlooking the town, he points to a jail and says "Thats where Micah is, you need to rescue him"
You cough and then reply "Id rather let the bastard rot". "You're losing faith in me arthur, we need Micah to go to tahiti"
dutch explains. You begrudgingly reply "oh all right just for you" You sneak down to the jail and blow it open with dynamite. 
"Good to see you black lung how have you been" Micah says. You tell him to hurry up and both of you run out of the jail. Micah says he 
needs to go find his guns and he will meet you back at camp, as you watch Micah run off, a Lawman shouts: "Put Your hands UP, NOW"
    
    """ : 1, """
    
You find dutch waiting with most of the gang outiside the Lemoyne County Bank. Dutch tells you the plan. "We are going to rob this bank,
and finnally have enough money to go to tahiti, Hosea is going to distract the lawmen, and we are going to break into the vault"
You and the gang put your mask on and barge inside, taking all the money from the vault. Suddenly you hear a BOOM, as the door blows
 open and Mr. Milton, a pinkerton demands that you come outside, or the mass amount of pinkertons 
and lawmen outside will open fire" He then brings out a bruised and handcuffed Hosea, who had been captured. Milton says, "Final chance
Dutch Vander-linde". After no response he shoots hosea. Dutch Tells everyone to climb onto the roof, however the ladder breaks, leaving you
and lenny in an alleyway, eventually you find a way onto the rooftops of the city, but the rest of the gang is gone. You hear a gunshot and 
turn around, lenny is dead and there is a lawman facing you.
    
    """ : 1, """
    
You find dutch waiting just outside the Braithwaite Manor, owned by the Braithwaites, a rich plantation family. He tells you that little 8 year old
jack marston has been kidnapped by the braithwaites and you need to get him back. You and the gang walk through the open plantations, and 
Dutch yells "Get down her now! You inbred Trash!", You and the gang search the house and Dutch finds jack, dutch says that him and the rest of 
the gang will take jack home, and you need to set the dynamite in order to blow up the Braithwaite manor. You set the charges and explode them
the Manor collapses in flames. As you are leaving you find a Braithwaite gaurd, who is pointing his gun at you.
    
    """ : 2, """
    
You find dutch waiting for you outside of the mines, saying that he has a job for you. He wants you and John Marston to blow up Bacchus Bridge, in 
order to create a diversion for a plan of his. Once you and john set the dynamite, and barely dodge a train, John says that he will meet you back at camp, 
he has to go talk to little jack, his son. You blow the bridge up and as you are walking away, a lawman confronts you.
    
    """ : 1, """
    
You escape and find 100 dollars on the corpse of your adversary. As you return to camp you find standoff. John is calling Micah a rat, and that Micah is
why the bank robbery went south, and how the pinkertons knew that you and dutch were in valentine. John is saying that Micah told the Pinkertons. John and Micah
are both pointing guns at each other. You side with John and Dutch sides with Micah. Dutch says "Who Amongst You Is With Me, And Who Is Betraying Me?", while pointing
his guns at you and John. BANG, the pinkertons have found camp, You and John run away to your horses and the rest of the gang who is with dutch gets on theirs, 
they chase after you and eventually you make it to the top of a hill. John says that he needs to go to his family, and you reply that you will hold the gang off
You shoot pinkertons and lawmen, but Micah jumps out behind you. (this final battle is designed to be hard)
    
    """ : 3}


    #thesem are all of the items in the game, dmg stands for the damage they do, reload speed is
    #the time it takes to reload, aim time is how easy it is to aim, higher is easier, and price is how much it will cost the player to purchase.
    ITEMS = {
    "Cattleman Revolver" : {"dmg" : 20, "reload speed": 1, "aim time" : 3, "price" : 100},
    "Springfield Rifle" : {"dmg" : 100, "reload speed" : 5, "aim time" : 1.5, "price" : 300 },
    "Colt M1911 Pistol" : {"dmg" : 40, "reload speed" : 1, "aim time": 3, "price" : 150},
    "Lancster Repeater": {"dmg": 60, "reload speed": 3, "aim time": 2, "price": 200}
    }

    #dictionary for the enemies, hp is the amount of health points they have, dmg is the
    #amount of damage they do per hit and aim skill is the chance out of 10 of hitting you
    ENEMIES ={
    "the pinkerton" : {"hp" : 100, "dmg" : 0, "aim skill" : 5},
    "the lawman" : {"hp" : 100, "dmg" : 30, "aim skill" : 6},
    "the braithwaite" : {"hp" : 100, "dmg" : 20, "aim skill" : 7},
    "micah" : {"hp" : 200, "dmg": 19, "aim skill" : 8}}

    inventory = ["Cattleman Revolver"] #inventory will start off with cattleman revolver only






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
    9999: Restart the game
    type answer here: """))
                if inpt not in towns_num:
                    print(towns[6]) #generates error
           except:
               if inpt == 9999:
                  return 9999
               else:
                  print("value must be an integer between 0 and 4")
           else:
                break
       if inpt < 5:
           print("Welcome to", list(towns.keys())[inpt], towns[list(towns.keys())[inpt]][0] , "You walk into the center of the town.")
           while True:
               try:
                   if towns[list(towns.keys())[inpt]][1] == True: #Checking if the mission for this town has already been done, and if so giving a different prompt for coninuities sake
                       print("The mission for this Town already has been completed")
                       inpm = int(input("""
The gunsmith is down the road to the right. where do you go?
0: exit the town
2: go right and visit the gunsmith
Type answer here: """))
                   else:
                        inpm = int(input("""
The place where Dutch waiting for you is down the road the left,
and the gunsmith is down the road to the right. Where do you go:
0: Turn around and leave the town
1: go left and meet dutch (this will start the mission)
2: go right and visit the gunsmith
type answer here: """))


                   if inpm == 0:
                       break
                   elif inpm not in list(range(1, 3)):
                       print(towns[6]) #generates error in order to trigger except block

               except:
                    print("value must be an integer between 1 and 2")
               else:
                    break



       return inpt, inpm


    #This is a function, it can be called at any time by typing combat(). Inside of the brackets you place the argument, this a variable which is will be used in the function. the argument in this case is named e. e is explained in a later comment
    #this particular function will be where arthur fights enemies. It will return a True if the player kills the enemies, it will return false if the player loses the battle
    def combat(e): #e a string which holds the name of the enemy that will be used in this funtion. This name is the key for the ENEMIES hash. For example, e could be "the pinkerton". This lets the function acess the values assinged to "the pinkerton"
        hp = Arthur_morgan_hp #stands for health points
        ehp = ENEMIES[e]["hp"] #stands for enemy health points
        debug = False

        #this is a while loop, it will repeat the code inside of it until its parameters are broken, in this example
        #the loop will repeat until either the player's or the enemy's hp is reduced to 0
        while hp > 0 or ehp > 0:

            print("You have", hp, "health")
            print("Your enemy is", e, "and they have", ehp, "health")

            #This is a for loop, if will iterate through the variable inventory. This loop will iterate through inventory list and print every item and its stats
            print("Your Inventory:")
            for c, i in enumerate(inventory): #enumerate allows me to add a counter for each item in a for loop
                print(inventory[c], ": ", ITEMS[i], "Type", c, "to select this weapon")
            #asks the user to select a weapon for the upcoming battle
            while True:
                try:
                    player_input = input("What weapon do you want to use? ")
                    weapon = inventory[int(player_input)]
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

            if debug == True: #does the same thing as killing the enemy
                print("You defeated", e)
                return True

            print("battle starting in 3")
            time.sleep(1)
            print("battle starting in 2")
            time.sleep(1)
            print("battle starting in 1")
            time.sleep(1)
            print("GO")


            #battle sequence will start, a random number will be chosen and the user will have to press that number on their
            #keyboard fast enough in order to fire, simulating quickdraw.
            #this uses threading in order to place a time limit on the users input, if the user does not input something in time, then it will print "Times Up, you got hit, press enter to reload the gun and fire again"
            battle_num = random.randint(0, 9)
            battle_string = "PRESS THE BUTTON " + str(battle_num) + " ON YOUR KEYBOARD WITHIN %d SECONDS TO FIRE \n"
            timeout = ITEMS[weapon]["aim time"]
            t = Timer(timeout, print, ["""
            
Times Up!
Press enter to reload the gun and fire again
            
            """])
            t.start()
            prompt = battle_string % timeout
            answer = input(prompt)
            t.cancel()

            # tests to see if the player entered a value, and if so was the value was correct?
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
                except:
                    print("Please enter an integer")
                else:
                    break

            #checks whether player has killed the enemy, if not then the player will reload
            if ehp <= 0:
                print("You defeated", e)
                return True
            else:
                # reloading mechanic, the reload speed of the weapon will affect the amount of chances that the
                # enemy has to hit the player.
                print("reloading...")
                if player_inputted == False:
                    hp -= ENEMIES[e]["dmg"]
                    time.sleep(ITEMS[weapon]["reload speed"])
                    print(e, "hit you for", ENEMIES[e]["dmg"], "damage while you were reloading")
                else:
                    damage_taken = 0
                    for i in range(0, ITEMS[weapon]["reload speed"]): #for loop that determines how much damage you will get hit for while
                                                                    #reloading, for every one second of reload time the for loop will iterate,
                                                                    #and the enemy will have a chance of hitting you based on their "aim skill"
                        time.sleep(1)
                        if random.randint(1, 10) <= ENEMIES[e]["aim skill"]:
                            damage_taken += ENEMIES[e]["dmg"]
                            print("You got hit!")
                        else:
                            print("The enemy missed!")
                    hp -= damage_taken
                    print("You took", damage_taken, "damage total while reloading")
            if hp <= 0:
                print("You died, the game will now restart") #checks if the player died
                return False
            else:
                continue







    #this function will start the missions
    def missions(t):
        global tuberculosis_stage
        global Arthur_morgan_hp
        global towns_num
        global money
        global missions_completed
        global towns
    #prints the mission "cutscene" variable
        print(list(missions_t.keys())[t])
    #starts a battle with enemy by calling combat function
        if combat(list(ENEMIES.keys())[list(missions_t.values())[t]]) == True: #if the player wins then the combat function returns true
            missions_completed += 1
            if missions_completed >= 5:
                return True #if you have completed all missions then it will immediatly push you to the final mission
            else:

                print("""
            
You escape and make it back to camp,
finding 100 dollars on the corpse of""", list(ENEMIES.keys())[list(missions_t.values())[0]], """
as you leave the town. You find a note 
in your tent where dutch tells 
you where he is waiting for you in the next town.
        
                """)

                money += 150
                tuberculosis_stage += 1 #tuberculosis stage increases with each mission and therefore arthurs health will go down after each mission
                towns[list(towns.keys())[t]][1] = True #sets the mission to completed
                return True
        else:
            return False #if player loses battle then this triggers the game to restart





    #gunsmith function lets player purchase new weapons
    def gunsmith(t):
        global inventory
        global money
        while True:

            print("Welcome to the firearms smithery of", t, "You have", money, "dollars. Here is our catalouge:")

            #for loop iterates through all items in the game and prints their name, stats, and key that the player had to press to select them.
            for c, i in enumerate(ITEMS):
                print(i, ITEMS[i], "press", c, "select this item")

            #loop protects against errors and missclicks
            while True:
                try:
                    item_choice = int(input("What item do you want to purchase?, type '9999' to leave the store and return to the open road. "))
                    item_choice_name = list(ITEMS.keys())[item_choice]
                except:
                    if item_choice == 9999:
                        print("You turn around and walk out of the store and out of the town")
                        return
                    else:
                        print("please input an integer corresponding to an item in the catalouge")
                        continue
                double_check = input("are you sure you want to purchase this item, press 0 for no, any other input will count as yes ")
                if double_check == "0":
                    continue
                else:
                    break

            #checks if player has enough money to purchase item
            if money - ITEMS[item_choice_name]["price"] < 0:
                print("you do not have enough money to purchase this item")
            else:
                money -= ITEMS[item_choice_name]["price"]
                inventory.append(item_choice_name)
                print("You are now the proud owner of a", item_choice_name)
                print("Here is your inventory now:", inventory)
                print("here is how much money you have now:", money)
            leave_gunsmith = input("press 0 to leave the gunsmith, any other input will return you to the catalouge.")
            if leave_gunsmith == "0":
                break
            else:
                continue

    #a function for the final mission, if you have played rdr2 then this is the one named "Red Dead Redemption"
    def final_mission():

        #there is a loop here because this mission is designed to be hard, and if the player dies, it would be very annoying to have to restart the whole game
        while True:
            print(list(missions_t.keys())[5]) #prints the "cutscene" string

            player_victory = combat(list(ENEMIES.keys())[list(missions_t.values())[5]])

            if player_victory == True: #starts the fight with micah
                #prints the ending "cutscene"
                print("""
            
Dutch arrives and looks over the scene, both you and micah barely alive, laying on the floor. Dutch doesnt say a word as he turns around and walks away. Micah slowly
gets up and hobbles away too. You can barely breathe, but muster the strength to crawl over to the clif face and watch the sun set, you are finnally at rest.


You Beat RDR2! The game will now restart
            
                """)
                break
            elif player_victory == False: #if the player loses the final battle they will restart the battle
                continue

    #main routine

    #here the equivalent of the starting "cutscene" will play
    print(logo)
    print("""
You are arthur morgan, the year is 1899, and you a member of the Vander-linde gang.
The gang is named after Dutch Vander-Linde, who founded the gang along with Hosea Mathews.
You and the rest of your gang are on the run from the Pinkerton Detective Agency, which 
was hired by Leviticus Cornwall to hunt you down after you robbed a train of his.
You leave the camp that the gang is staying at, you find a letter in your tent from Dutch
telling you where he is waiting for you. You have also recently caught tuberculosis, and are 
slowly dying, this is why your starting health will go down by 10 after every mission.
(This game is meant to roughly follow the story of RDR2. You can play the missions in any order
but ideally the missions are meant to be played in chronological order.)
How to play:
the numbers on your keyboard will be used as inputs.
eg:
 0 : Cookie
 1 : Milk
 in this situation you would press 0 to choose "cookie" and 1 to choose "milk"
 During combat you will have to "quickdraw". To do this the game will tell you 
 to input a number in a certian amount of time in order to fire. If you "miss" or 
 dont fire in time, then the enemy will hit you for a certian amount of damage. You
 will then have to reload your gun.(you will have to reload even if you hit the enemy)
 While reloading, the enemy will have a certian number of chances to hit you. This 
 number of chances is based on the "reload time of your gun"
    """)
    time.sleep(5)

    #start of the main main routine. this is the main loop for the gameplay of the game.
    while True:

        #defining arthur morgan hp here instead of with the reast of the variables becase it needs to be redefined after every mission
        Arthur_morgan_hp = 150 - (tuberculosis_stage * 10)

        # checks if every main mission has been completed
        if missions_completed >= 5:
            final_mission()
            break #breaks out of the main routine loop and restarts the master loop, restarting the game

        town_selection = entertown()
        if town_selection == 9999:
            print("Game Restarting")
            time.sleep(2)
            break
        tc = town_selection[0] #stands for town choice
        mvg = town_selection[1] #variable stores the users choice of starting the mission or visiting the gunsmith. Mission Vs Gunsmith hence the name, mvg
        if mvg == 0:
            print("You turn around and walk away from the town")
        elif mvg == 1:
            if missions(tc) == False: #if the player dies then the game is restarting
                print("Game Restarting")
                time.sleep(2)
                break
            else:
                continue
        elif mvg == 2:
            gunsmith(list(towns.keys())[tc])



time.sleep(2)#delays the game restart speed.




