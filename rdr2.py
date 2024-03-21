#imports:
import random

#starting variables and constants:
inventory = ["cattleman revolver", "hunting knife"]
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
    From the Grizzly mountains of Ambarino to the southern Plantations of Lemoyne
    """]}

towns_num = list(range(len(towns)))
missions_completed = 0
#costant variables:
YEAR = 1899
STARTING_TOWN = list(towns.keys())[1]

# text vairiables. These vairables will be used to describe the setting and the missions



#functions:
# this function plays every time the player leaves a town, this acts as the main menu
def entertown(f):
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
       except:
            print("value must be an integer between 1 and 2")
       else:
            break

   return inpt, inpm


#main routine
entertown(1)