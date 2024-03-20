#imports:
import random

#starting variables and constants:
inventory = ["cattleman revolver", "hunting knife"]
towns = ["Valentine.", "Strawberry.", "Saint Denis.", "Rhoades.", "Annesburg.", "Open road."]
towns_num = list(range(len(towns)))
missions_completed = 0
#costant variables:
YEAR = 1899
STARTING_TOWN = towns[1]


#functions:
# this function plays every time the player leaves a town, this acts as the main menu.
def entertown(t):
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

   print("Welcome to", towns[inpt], "You walk into the center of the town.")
   inpm = input("""
   The place where dutch waiting for you is to the left, where do you go:
   1: go left and meet dutch (this will start the mission)
   2: explore the town
   type answer here: """)

   return inpt


#main routine
entertown(1)