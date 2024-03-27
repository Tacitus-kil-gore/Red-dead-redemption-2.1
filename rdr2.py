#imports:
import random

#starting variables and constants:

towns = {"Valentine." : ["""
    A rough, raucous, hard-working town that provides livestock at auction to Heartlands landowners,
    and rest and refreshment to thirsty cowboys.
    It's nicknamed 'Mudtown' because the streets, buildings, and most of the residents are rarely clean.
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
print(Arthur_morgan_hp)
towns_num = list(range(len(towns)))
missions_completed = 0
#costant variables:
YEAR = 1899
STARTING_TOWN = list(towns.keys())[1]



# text vairiables. These vairables will be used to describe the setting and the missions
#missions_t stands for missions text
missions_t = ["""
You find dutch waiting for you in the saloon. He sits you down and takes a drink from his whiskey. 
"arthur you've got to have faith in me we just need 5000 more dollars and we can escape to tahiti." says dutch
"yeah i know" you replied.  "I've found another job robbing leviticus cornwall, that rich fella we robbed last week in Blackwater." dutch says
"awww no dutch not this again, leviticus cornwall has already sent that pinkerton detective agency after us, we dont need more trouble" you say.
"arthr your losing faith, you need to hav-BANG" 
"DUTCH VANDERLINDE COME OUTSIDE RIGHT NOW WITH YOUR HANDS UP THIS IS THE PINKERTON DETECTIVE AGENCY" you hear from outside the saloon.
"oh shoot the pinkertons are here" dutch says. dutch runs out the back door and you jump through the window to your left out into an alley.
you find a pinkerton in the alley with his hand on his gunholster staring at you.
""", "insert strawwberry mission", "insert saint denis mission", "insert rhoades mission", "insert annesburg mission"]

#entity variables These variables will store the stats of entities

cattleman_revolver = {"dmg" : 20, "reload_speed": 1, "aim difficulty" : 3}
springfield_rifle = {"dmg" : 100, "reload_speed" : 5 "aim difficulty" : 1}

inventory = [cattleman revolver, hunting knife]

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

   print("Welcome to", list(towns.keys())[inpt], towns[list(towns.keys())[inpt]][0] , "You walk into the center of the town.")
   while True:
       try:
           inpm = int(input("""
           The place where Dutch waiting for you is down the road the left, where do you go:
           1: go left and meet dutch (this will start the mission)
           2: explore the town
           type answer here: """))

           if input not in list(range(1, 3)):
               print(towns[6]) #generates error

       except:
            print("value must be an integer between 1 and 2")
       else:
            break

   return inpt, inpm

def missions(t, m):
    print()

#main routine 
while True:

    #here the equivalent of the starting "cutscene" will play

    town_selection = entertown()
    tc = town_selection[0] #stands for town choice
    mve = town_selection[1] #variable stores the users choice of starting the mission or exploring the town. Mission Vs Explore hence the name, mve
    if mve == 1:
        print("n")
    elif mve == 2:
        print("g")
    else:
        print("something went wrong, game is restarting")
        continue