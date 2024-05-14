# Mason Cuchia 12/9/23
# This is a text based adventure game called The Woods of Shadows, coded using python
# The main character's name is Adrian and he is trying to find the magic book at the center
# of the forest to cure the diease that is spreading through out the land


import os, random, time, select, sys


# Items character is able to gain
items = {"Sword":False, "Shield":False, "Tooth":False, "Magic Book":False}


#lives for lock game
lives = 3


##########################################################
# These are variables for the monster fight              #
turn = "p" #p for player and m for monster turn          #
PattackReady = False # if the player is ready to attack  #
CattackReady = False # if the monster is ready to attack #
Pblock = False # if the player blocks                    #
Cblock = False # if the computer blocks                  #
Pattack = False # if the player attacks                  #
Cattack = False # if the monster attacks                 #
Plives = 2                                               #
Clives = 1                                               #
alive = True                                             #
firstTime = True                                         #
stunned = False                                          #
##########################################################



def win():
   """This function prints out a message when the player wins."""
   os.system("cls")
   title()
   print("You feel the ground start to shake as the book glows brighter and brighter.")
   print("You have cleansed the land from the raging diease and the people in town throw you a party.")
   print("Congratulations! You've saved the world.")
   time.sleep(3)
   if "Diamond" in items:
       print("Wow you found the hiden Diamond during your quest.")
       printDiamond()
   else:
       print("\n\n\n")
       printFireworks()
       print("\n\n\n")
  
   print("These are the items you found during your adventure.\n",items)




def bookAlter():
   os.system("cls")
   title()
   print("There is a clearing in the middle of a dark forest where a magical book sits on a alter.")
   print("You walk up to the book and grab it off its alter. The room starts shaking.")
   items["Magic Book"] = True
   time.sleep(3)
   print("BOOM!")
   time.sleep(1)
   print("BOOM!")
   time.sleep(1)
   print("BOOM!")
   time.sleep(1)
   print("The book opens and starts to glow.\nPress Enter to read the spell in the book.")
   while True:
       try:
           choice = input("> ")
           list = [""]
           if choice not in list:
               raise ValueError
           elif(choice.lower() in list[0]):#enter
               print("هل يمكنني صخرة ميلي. واااا")
               time.sleep(2)
               win()
               break
       except ValueError:
           print("Invalid input. Please press Enter.")


def fightBigMonster():
   Sattack = ""
   Pdodge = ""
   counter = 0
   lives = 3
   alive = True


   while alive:
       os.system("cls")
       title()
       printSkeleton()
       print(f"Your Lives: {lives}\n")


       attack = random.randint(1,2)
       if attack == 1:
           print("The skeleton attacks to your RIGHT.")
           Sattack = "r"
       else:
           print("The skeleton attacks to your LEFT.")
           Sattack = "l"


       print("You have 5 seconds to answer.")
       print("Do you want to dodge left or right? (l=left/r=right)")
       print("> ", end="")
       sys.stdout.flush()
       i, e, o = select.select( [sys.stdin], [], [], 5)
       if (i):
           letter = sys.stdin.readline().strip().lower()
           if letter == "l":
               print("You dodge left.")
               Pdodge = "l"
           elif letter == "r":
               print("You dodge right.")
               Pdodge = "r"
           else:
               print("That is not a valid input.")


       #checking for attack to the right
       if Sattack == "" or Pdodge == "":   
           print("\nYou did not make a choice and the skeleton hit you.")
           lives -= 1
           time.sleep(1.5)
       elif Sattack == "r" and Pdodge == "l":
           print("\n\nYou dodged the attack!")
           counter += 1
           time.sleep(1.5)
       elif Sattack == "r" and Pdodge == "r":
           print("\n\nThe skeleton's attack hit you.")
           lives -= 1
           time.sleep(1.5)
       #checking for attack to the left
       elif Sattack == "l" and Pdodge == "l":
           print("\n\nThe skeleton's attack hit you.")
           lives -= 1
           time.sleep(1.5)
       else:
           print("\n\nYou dodged the attack!")
           counter += 1
           time.sleep(1.5)


       if counter == 5:
           os.system("cls")
           title()
           printDeadSkeleton()
           print("\n\nGreat job! You defeated the skeleton!")
           print("\nPress Enter to continue.")
           while True:
               try:
                   choice = input("> ")
                   list = [""]
                   if choice.lower() not in list:
                       raise ValueError
                   elif choice.lower() == list[0]:#continue
                       deadSkeleton()
                       break
               except ValueError:
                   print("Invalid input. Please press Enter.")
           break
       if lives == 0:
           dead("player")
           alive = False


def deadSkeleton():
   os.system("cls")
   title()


   print("You notice there is something sticking out of his body.")
   print("\nPress Enter to pick it up.")
   while True:
       try:
           choice = input("> ")
           list = [""]
           if choice not in list:
               raise ValueError
           elif(choice.lower() in list[0]):#enter
               print("\nYou Gained A Giant Bone!\n")
               items["Giant Bone"] = True
               printBone()
               break
       except ValueError:
           print("Invalid input. Please press Enter.")
   print("Press Enter to continue.")
   while True:
       try:
           choice = input("> ")
           list = [""]
           if choice not in list:
               raise ValueError
           elif(choice.lower() in list[0]):
               bookAlter()
               break
       except ValueError:
           print("Invalid input. Please press Enter.")




def bigMonster():
   os.system("cls")
   title()
   print("A giant skeleton is waiting for you on the other side of the door.")
   print("His attacks are much stronger than the Goblin's.")
   printSkeleton()
   print("\nAre you ready to fight him? (y=yes/n=no)")
   while True:
           try:
               choice = input("> ")
               list = ["y", "n"]
               if choice not in list:
                   raise ValueError
               elif(choice.lower() in list[0]):#yes
                   fightBigMonster()
                   break
               elif(choice.lower() in list[1]):#no
                   doors()
                   break
           except ValueError:
               print("Invalid input. Please enter y or n.")


def fightMax():
   global turn, Plives, Clives, alive, CattackReady, PattackReady, Pblock, Cblock, Pattack, Cattack, stunned, firstTime
   if firstTime:
       # set all the global variables back to default
       turn = "p" #p for player and m for monster turn          #
       Pblock = False # if the player blocks                    #
       Cblock = False # if the computer blocks                  #
       Pattack = False # if the player attacks                  #
       Cattack = False # if the monster attacks                 #
       Plives = 3                                               #
       Clives = 3                                               #
       alive = True
       stunned = False


   firstTime = False
   os.system("cls")
   title()
   printMaxTheScorpion()
   print(f"Max's Lives: {Clives}\nYour Lives: {Plives}\n")
       #if the player is ready to attack
   while alive:
       if turn == "p" and alive:
           print("It is your turn.\n")


           if stunned == False:
               print("Would you like to dodge or try to stomp on max? (d=dodge/s=stomp)")
               while True:
                   try:
                       choice = input("> ")
                       list = ["d","s"]
                       if choice.lower() not in list:
                           raise ValueError
                       elif choice.lower() == list[0]:#dodge
                           block("max")
                           break
                       elif choice.lower() == list[1]:#stomp
                           attack("max")
                           break
                   except ValueError:
                       print("Invalid input. Please enter d or s.")
           else:
               print("You are currently stunned, unable to move.")
               time.sleep(1)
               print("Press Enter to continue.")
               while True:
                   try:
                       choice = input("> ")
                       list = [""]
                       if choice.lower() not in list:
                           raise ValueError
                       elif choice.lower() == list[0]:#continue
                           stun()
                           break
                   except ValueError:
                       print("Invalid input. Please press Enter.")
       elif turn == "m" and alive: # max's turn to move
           print("It is the monster's turn.")
           num = random.randint(1, 20)
           if num <= 9:#stall
               print("Max gets confused and does nothing.")
               suspense()
           elif num > 9:#attack
               print("The monster attacks!")
               Cattack = True
               suspense()
           # hit detection system
           if Cattack and Pattack:
               print("You both attack, and your foot bounces off his stinger!")
               Pattack = False
               Cattack = False
               stunned = True
           else:
               if Pattack:
                   Clives -= 1
                   if Clives == 0:
                       dead("max")
                       break
                   else:
                       print("You hit him!")
                       print(f"Max has {Clives} lives left.")
                   Pattack = False
                  
               if Pblock and Cattack:
                   print("You dodged his attack.")
                   Cattack = False
               elif Pblock == False and Cattack == True:
                   Plives -= 1
                   print("Max hit you with his tail attack.")
                   print(f"You have {Plives} lives left.")
                   Cattack = False
                   if Plives == 0:
                       time.sleep(2)
                       dead("player")
                       break
           # change turns and reset values
           turn = "p"
           Pblock = False
           Cblock = False


def maxDead():
   print("You notice there is something shinny in his body.")
   print("\nPress Enter to pick it up.")
   while True:
       try:
           choice = input("> ")
           list = [""]
           if choice not in list:
               raise ValueError
           elif(choice.lower() in list[0]):#enter
               print("\nYou Gained A Diamond!\n")
               items["Diamond"] = True
               break
       except ValueError:
           print("Invalid input. Please press Enter.")
   print("Press Enter to continue.")
   while True:
       try:
           choice = input("> ")
           list = [""]
           if choice not in list:
               raise ValueError
           elif(choice.lower() in list[0]):
               bookAlter()
               break
       except ValueError:
           print("Invalid input. Please press Enter.")


def stun():
   global turn, stunned
   turn = "m"
   stunned = False
   fightMax()


def passMax():
   os.system("cls")
   title()
   print("You say, 'Hey Max, do you mind if I pass?'\n")
   time.sleep(1)
   print("Max is considering...")
   printMaxTheScorpion()
   num = random.randint(2, 4)
   time.sleep(num)
   target = random.randint(1, 100)
   pent = random.randint(1,5)
   if pent == 1:
       if target <= 20:
           print("Max says, 'Alright! You're good to go.'")
           time.sleep(1.5)
           bookAlter()
       else:
           print("Max says, 'Nah man, that's weak.' and knocks you back to the start with one swift swipe of his tail.")
           time.sleep(3)
           playGame()
   elif pent == 2:
       if target > 20 and target <= 40:
           print("Max says, 'Okay, I guess I'll let you go.'")
           time.sleep(1.5)
           bookAlter()
       else:
           print("Max says, 'Not today buddy.' and knocks you back to the tree.")
           time.sleep(3)
           south()
   elif pent == 3:
       if target > 40 and target <= 60:
           print("Max says, 'You look like a friendly person.'\n'Here take this special Diamond.'")
           print("\nYou Gained A Diamond!\n")
           items["Diamond"] = True
           time.sleep(3)
           bookAlter()
       else:
           print("Max gets angry and starts yelling at you.\n")
           print("BLAH BLAH BLAH\nThen he sends you back to the doors.")
           time.sleep(3)
           doors()
   elif pent == 4:
       if target > 60 and target <=80:
           print("\nMax shrugs his shoulders and lets you through.")
           time.sleep(1.5)
           bookAlter()
       else:
           print("Max becomes very aggressive and attacks you!\n")
           time.sleep(1.5)
           dead("player")
   elif pent == 5:
       if target > 80 and target <= 100:
           print("Max gives you a high five and lets you through.")
           time.sleep(1.5)
           bookAlter()
       else:
           print("MAX IS A TOTAL JERK AND SENDS YOU BACK TO THE START OF THE FOREST.")
           time.sleep(3)
           playGame()


def smallMonster():
   global firstTime
   os.system("cls")
   title()
   print("This is Max the Scorpion.\nHe looks friendly but be careful be might attack.")
   printMaxTheScorpion()
   print("\nWould you like to fight him or take the 1/20 chance to ask him nicely to walk past? (f=fight/w=walk past)")
   while True:
       try:
           choice = input("> ")
           list = ["f", "w"]
           if choice.lower() not in list:
               raise ValueError
           elif choice.lower() in list[0]: # fight
               firstTime = True
               fightMax()
               break
           elif choice.lower() in list[1]: # walk past
               passMax()
               break
       except ValueError:
           print("Invalid input. Please enter f or w.")
  
def doors():
   os.system("cls")
   title()
   print("\nYou come across three doors that have a key hole the size of the tooth you picked up.")
   print("\nWhich door would you like to open? (1/2/3)")
   while True:
       try:
           choice = input("> ")
           list = ["1", "2", "3"]
           if choice not in list:
               raise ValueError
           elif(choice.lower() in list[0]):#1
               items.pop("Tooth", None)
               print(items)
               print("You used your tooth from your inventory to open the door.")
               smallMonster()
               break
           elif(choice.lower() == list[1]):#2
               print("You used your tooth from your inventory to open the door.")
               items.pop("Tooth", None)
               print(items)
               bookAlter()
               break
           elif(choice.lower() == list[2]):#3
               print("You used your tooth from your inventory to open the door.")
               items.pop("Tooth", None)
               print(items)
               bigMonster()
               break
       except ValueError:
           print("Invalid Input. Please enter a number between 1-3.")


def tooth():
   global Plives
   os.system("cls")
   title()
   print("You picked up his tooth and put it in your pocket.\n")
   items["Tooth"] = True
   print("These are the items you found during your adventure so far.\n",items)
   print("\nAre you ready to continue on the path? (y=yes/n=no)")
   while True:
           try:
               choice = input("> ")
               list = ["y", "n"]
               if choice not in list:
                   raise ValueError
               elif(choice.lower() in list[0]):#yes
                   print("First you drink a health potion and put on the goblins armor.")
                   Plives = 3
                   time.sleep(2)
                   print(f"Lives: {Plives}")
                   time.sleep(3)
                   doors()
                   break
               elif(choice.lower() in list[1]):#no
                   south()
                   break
           except ValueError:
               print("Invalid input. Please enter y or n.")


def monsterDead():
   print("His yellow tooth is sitting on the ground.")
   print("\nPress Enter to pick it up.")
   while True:
       try:
           choice = input("> ")
           list = [""]
           if choice not in list:
               raise ValueError
           elif(choice.lower() in list[0]):#enter
               tooth()
               break
       except ValueError:
           print("Invalid input. Please press Enter.")


def block(fight):
   global turn, Pblock
   if fight == "monster":
       Pblock = True
       print("You block with your shield.")
       turn = "m"
       time.sleep(1)
       fightMonster1()
   elif fight == "max": # attempt to dodge max
       Pblock = True
       #make a random number between 1-2
       randNum = random.randint(1, 2)
       if randNum == 1:
           print("You dodge to your left.")
       else:
           print("You dodge to your right.")
       turn = "m"
       time.sleep(1)
       fightMax()


def prepare():
   global turn, PattackReady
   PattackReady = True
   print("You prepare to attack.")
   turn = "m"
   time.sleep(1)
   fightMonster1()


def attack(fight):
   global turn, alive, PattackReady, Pattack
   if fight == "monster":
       PattackReady = False
       Pattack = True
       print("You attack the monster!")
       turn = "m"
       time.sleep(1)
       if alive:
           fightMonster1()
   elif fight == "max":
       Pattack = True
       print("You attack the monster!")
       turn = "m"
       time.sleep(1)
       if alive:
           fightMax()


def fightMonster1():
   global turn, Plives, Clives, alive, CattackReady, PattackReady, Pblock, Cblock, Pattack, Cattack
   os.system("cls")
   title()
   print(f"Monster's Lives: {Clives}\nYour Lives: {Plives}\n")
       #if the player is ready to attack
   while alive:
       if turn == "p" and alive:
           print("It is your turn.\n")
           if PattackReady:
               print("Would you like to block or attack? (b=block/a=attack)")
               while True:
                   try:
                       choice = input("> ")
                       list = ["b","a"]
                       if choice.lower() not in list:
                           raise ValueError
                       elif choice.lower() == list[0]:#block
                           block("monster")
                           break
                       elif choice.lower() == list[1]:#attack
                           attack("monster")
                           break
                   except ValueError:
                       print("Invalid input. Please enter b or a.")
           elif PattackReady == False:
               print("Would you like to block or prepare to attack? (b=block/p=prepare)")
               while True:
                   try:
                       choice = input("> ")
                       list = ["b","p"]
                       if choice.lower() not in list:
                           raise ValueError
                       elif choice.lower() == list[0]:#block
                           block("monster")
                           break
                       elif choice.lower() == list[1]:#prepare
                           prepare()
                           break
                   except ValueError:
                       print("Invalid input. Please enter b or p.")
       elif turn == "m" and alive:
           print("It is the monster's turn.")
           if CattackReady:
               num = random.randint(1, 10)
               if num <= 4:#block
                   print("The monster blocks with his wooden sheild.")
                   Cblock = True
                   suspense()
               elif num > 4:#attack
                   print("The monster attacks!")
                   CattackReady = False
                   Cattack = True
                   suspense()
                   if Plives == 0:
                       dead("player")
                       break
           elif CattackReady == False:
               num = random.randint(1, 10)
               if num <= 3:#block
                   print("The monster blocks with his wooden sheild.")
                   Cblock = True
                   suspense()
               elif num > 3:#prepare
                   print("The monster prepares to attack.")
                   CattackReady = True
                   suspense()
           # hit detection system
           if Cattack and Pattack:
               print("You both attack and your swords bounce off each other with a loud 'Cling'!")
               Pattack = False
               Cattack = False
           else:
               if Cblock and Pattack:
                   print("The monster was prepared and blocked your attack.")
                   Pattack = False
               elif Cblock == False and Pattack == True:
                   Clives -= 1
                   if Clives == 0:
                       dead("monster")
                       break
                   else:
                       print("You hit him!")
                       print(f"The monster has {Clives} lives left.")
                   Pattack = False
                  
               if Pblock and Cattack:
                   print("You blocked his attack.")
                   Cattack = False
               elif Pblock == False and Cattack == True:
                   Plives -= 1
                   print("The monster hit you with his attack.")
                   print(f"You have {Plives} lives left.")
                   Cattack = False
           # change turns and reset values
           turn = "p"
           Pblock = False
           Cblock = False


def suspense():
   time.sleep(.5)
   print(".")
   time.sleep(.5)
   print(".")
   time.sleep(.5)
   print(".\n")
   time.sleep(.5)
  
def fight1():
   os.system("cls")
   title()
   if "Tooth" != False: # if you have not been here before
       print("You find yourself on a dark path and you see a figure standing in the shadows.")
       print("The figure steps into the light. It is a forest goblin with green, scaley skin and big, yellow teeth.\n")
       time.sleep(.1)
       if items["Shield"] and items["Sword"]: #if you have both the items needed
           print("This is a turn based game where you will need to prepare to attack, then land an attack on the monster.")
           print("The monster will not be able to attack you until he prepares to attack. Good Luck.")
           print("\nAre you ready to fight? (y=yes/n=no)")
           while True:
               try:
                   choice = input("> ")
                   list = ["y", "n"]
                   if choice not in list:
                       raise ValueError
                   elif(choice.lower() in list[0]):#yes
                       fightMonster1()
                       break
                   elif(choice.lower() in list[1]):#no
                       south()
                       break
               except ValueError:
                   print("Invalid input. Please enter y or n.")
       else: # if you dont have the items need
           print("You need to find both the sword and the shield before you can fight this monster.")
           print("Find a path you have not yet explored.\n\n(Press Enter to go back to the path)")
           time.sleep(.1)
           while True:
               try:
                   choice = input("> ")
                   list = [""]
                   if choice not in list:
                       raise ValueError
                   elif(choice.lower() in list[0]):
                       south()
                       break
               except ValueError:
                   print("Invalid input. Please press Enter.")
   else: # if you have been here before
       os.system("cls")
       title()
       print("You will fight the goblin's ghost.")
       print("\nAre you ready to fight? (y=yes/n=no)")
       while True:
           try:
               choice = input("> ")
               list = ["y", "n"]
               if choice not in list:
                   raise ValueError
               elif(choice.lower() in list[0]):#yes
                   fightMonster1()
                   break
               elif(choice.lower() in list[1]):#no
                   south()
                   break
           except ValueError:
               print("Invalid input. Please enter y or n.")




def dieMessage():
   print("▀▄    ▄ ████▄   ▄       ██▄   ▄█ ▄███▄   ██▄   \n  █  █  █   █    █      █  █  ██ █▀   ▀  █  █  \n   ▀█   █   █ █   █     █   █ ██ ██▄▄    █   █ \n   █    ▀████ █   █     █  █  ▐█ █▄   ▄▀ █  █  \n ▄▀           █▄ ▄█     ███▀   ▐ ▀███▀   ███▀  \n               ▀▀▀ ")


def printSkeleton():
   print("              .7\n            .'/\n           / /\n          / /\n         / /\n        / /\n       / /\n      / /\n     / /         \n    / /          \n  __|/\n,-\__\.\n|f-'Y\|\n\()7L/\n cgD                            __ _\n |\(                          .'  Y '>,\n  \ \                        /_   _   \.\n   \\\                       )(_) (_)(|}.\n    \\\                      {  4A   } /\n     \\\                      \.uLuJJ/\l\n      \\\                     |3    p)/\n       \\\___ __________      /nnm_n//\n       c7___-__,__-)\,__)('.  \_>-<_/D\n                  //V     \_'-._.__G G_c__.-__<'/ ( \.\n                         <'-._>__-,G_.___)\   \.7\.\n                        ('-.__.| \.'<.__.-' )  \. \.\n                        |'-.__'\  |'-.__.-'.\   \. \.\n                        ('-.__''. \.'-.__.-'.|   \_\.\n                        \.'-.__''|!|'-.__.-'.)    \ \.\n                         '-.__''\_|'-.__.-'./      \ l\n                          '.__'''>G>-.__.-'>       .--,_\n                              ''  G\n")


def printMaxTheScorpion():
   print(" ___    ___\n( _<    >_ )\n/ /     \ \ \n\ \_._._/ /\n `-(    )-'\n   _|__|_\n  /_|__|_\ \n  /_|__|_\ \n  /_\__/_\ \n   \ || /  _)\n     ||   ( )\n     \ \__//\n      `---'")


def printFireworks():
   print("                                   .''.       \n       .''.      .        *''*    :_\/_:     . \n      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.\n  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-\n :_\/_:'.:::.    ' *''*    * '.\.'/.' _\(/_'.':'.'\n : /\ : :::::     *_\/_*     -= o =-   /)\   '  *\n  '..'  ':::'     * /\ *     .'/.\.'.   '\n      *            *..*         :\n        *\n        *")


def printDiamond():
   print("                          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          \n                         @@@@                 @@@@@@@                  @@@@                         \n                        @@  @@               @@@    @@@               @@  @@                        \n                       @@    @@            @@@       @@@@            @@    @@                       \n                     @@@      @@@        @@@@          @@@@         @@      @@                      \n                    @@@         @@      @@@              @@@      @@@        @@                     \n                   @@            @@   @@@                  @@@   @@           @@@                   \n                  @@@            @@@@@@                      @@@@@@            @@@                  \n                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  \n                   @@               @@                        @@@             @@@                   \n                    @@@              @                       @@@             @@@                    \n                      @@              @                      @@             @@                      \n                       @@@            @@                    @@            @@                        \n                         @@@           @@                  @@@          @@@                         \n                           @@          @@                  @@          @@                           \n                            @@@         @@                @@         @@                             \n                              @@         @@              @@        @@@                              \n                                @@        @@            @@@       @@                                \n                                 @@       @@            @@      @@@                                 \n                                   @@      @@          @@      @@                                   \n                                    @@@    @@@        @@@    @@                                     \n                                      @@    @@@       @@   @@@                                      \n                                        @@   @@      @@   @@                                        \n                                         @@@  @@    @@@ @@@                                         \n                                           @@@@@@  @@@@@@                                           \n                                            @@@@@  @@@@                                             \n                                              @@@@@@@@                                              \n                                                @@@@                                                \n                                                 @@                                                 ")


def printBone():
   print("          :*****#*                                                                **********        \n      :#*****##******                                                          .*********#*****     \n    ******... ..::***#.                                                      .***#*:.     .:*****   \n  .****:          .:#**.                                                    *****.           .****  \n .#*#.              .***:                                                  #***:        ..     .*** \n ***.     ..         *****                                               ***#*.                 #** \n **: .                :*****:                                          :*****.                  *** \n **:                     .*#*******#*****:...             ..::*****#******.                    ***: \n :*#                    ..       .****#************************#***:        :                 ***.  \n  **#  .**                       .                                                          .#**    \n   :****#*                                                                                 ****     \n    .****                                                                                 *****     \n     ***.                                                                                 *#**#     \n    .**.                                                                                    ***#    \n   ***.                  *:.                                                .                :#**   \n  ***            .:       .     .:*****##***************##******:...     .   .                :**.  \n :**:                  :*******##******::::......::::::**********##***********::              ***.  \n ***                .******                                            :*****####*.          .***   \n ***.          .:  :****.                                                 *********  ::  *.:****    \n :****        .*******:                                                     #******************     \n  .#*****:..::**#****                                                        .*****####******       \n    :#*****##******                                                             :********:          \n       :*******#.                                                                                   \n")                                                                                              
     
def printDeadSkeleton():
   print("              .7\n            .'/\n           / /\n          / /\n         / /\n        / /\n       / /\n      / /\n     / /         \n    / /          \n  __|/\n,-\__\.\n|f-'Y\|\n\()7L/\n cgD                            __ _\n |\(                          .'  Y '>,\n  \ \                        /_   _   \.\n   \\\                       )(X) (X)(|}.\n    \\\                      {  4A   } /\n     \\\                      \.uLuJJ/\l\n      \\\                     |3    p)/\n       \\\___ __________      /nnm_n//\n       c7___-__,__-)\,__)('.  \_>-<_/D\n                  //V     \_'-._.__G G_c__.-__<'/ ( \.\n                         <'-._>__-,G_.___)\   \.7\.\n                        ('-.__.| \.'<.__.-' )  \. \.\n                        |'-.__'\  |'-.__.-'.\   \. \.\n                        ('-.__''. \.'-.__.-'.|   \_\.\n                        \.'-.__''|!|'-.__.-'.)    \ \.\n                         '-.__''\_|'-.__.-'./      \ l\n                          '.__'''>G>-.__.-'>       .--,_\n                              ''  G\n")




def dead(type):
   """This function will run if the player dies"""
   global alive
   alive = False
   if type == "tree":
       os.system("cls")
       title()
       print("The giant, mysterious face in the tree yells.\n")
       print("'WHO DARES DISTURB ME?'")
       print("'YOU WILL DIE!'")
       time.sleep(3)
       os.system("cls")
       title()
       for i in range(4):
           print("\n")
       dieMessage()
       for i in range(4):
           print("\n")
       print("Would you like to quit or try again? (q=quit/return key=try again)")
   elif type == "lock":
       os.system("cls")
       title()
       for i in range(4):
           print("\n")
       dieMessage()
       for i in range(4):
           print("\n")
       print("Would you like to quit or try again? (q=quit/return key=try again)")
   elif type == "player":
       os.system("cls")
       title()
       dieMessage()
       for i in range(4):
           print("\n")
       print("Would you like to quit or try again? (q=quit/return key=try again)")
   elif type == "monster":
       print("You killed the monster!")
       monsterDead()
       return
   elif type == "max":
       print("You squished Max!")
       maxDead()
       return
      
   while True:
       try:
           choice = input("> ")
           if choice not in ["q", ""]:
               raise ValueError
           if choice == 'q':
               exit(1)
           elif choice == '':
               main()
               break
       except ValueError:
           print("\nInvalid Input. Press return or q")


def insideTree():
   print("You are inside a large oak tree and you see daylight coming through the leaves above you.")
   print("You see a strange face on the wall and he starts speaking to you.")
   print("'Hello traveler, I am the guardian of this forest and I have been watching you.'")
   print("'I will grant you this shield to aid you on your adventure. Good Luck.'")
   print("\nYou Gained A Shield!\n")
   items["Shield"] = True
   print("These are the items you found during your adventure so far.\n",items)
   print("\nAre you ready to leave the oak tree? (y=yes/n=no)")
   while True:
       try:
           choice = input("> ")
           list = ["y", "n"]
           if choice not in list:
               raise ValueError
           elif(choice.lower() in list[0]):#yes
               south()
               break
           elif(choice.lower() in list[1]):#no
               print("Well too bad, there's nothing else to do in here.")
               time.sleep(2)
               south()
               break
       except ValueError:
           print("Invalid input. Please enter y or n.")


def lockGame(level):
   global lives
   os.system("cls")
   title()
   #values
   target = random.randint(1, 9)
   guessesLeft = 0
   #difficulty selector
   if level == 1:
       guessesLeft = 5
   elif level == 2:
       guessesLeft = 3
       print("Congratulations! The first lock is picked!")
       print("You will now only have 3 guess to find the second number.\n")
   elif level == 3:
       print("Congratulations! The second lock is picked!\n")
       time.sleep(1)
       insideTree()
       return
   #game loop
   while True:
       try:
           print(f"Lives: {lives}")
           print(f"Guesses Left: {guessesLeft}")
           print("Enter a number between 1 and 9")
           guess = int(input("> "))
           if guess < 1 or guess > 9:
               raise ValueError
           guessesLeft -= 1
           #win
           if guess == target:
               level += 1
               lockGame(level)
               break
           elif guess < target:
               print("\nYour guess is too low. Try again.\n")
           else:
               print("\nYour guess is too high. Try again.\n")
       except ValueError:
           print("Invalid input. Please enter a number between 1-9.")
       #lost
       if(guessesLeft==0):
           print(f"\nYou ran out of guesses.\nThe number was {target}.")
           lives -= 1
           if lives == 0:
               print("You ran out of lives.")
               dead("lock")
               break
           print("Would you like to play again? (y=yes/n=no)")
           while True:
               try:
                   choice = input("> ")
                   list = ["y","n"]
                   if choice not in list:
                       raise ValueError
                   elif(choice.lower() in list[0]):#yes
                       pickLock()
                       break
                   elif(choice.lower() in list[1]):#no
                       south()
                       break
                  
               except ValueError:
                   print("Invalid input. Please enter y or n.")
           break


def pickLock():
   os.system("cls")
   title()
   print("You will have a certain number of guesses to find the mystery digit.\nThe digit will be between 1-9.")
   print("There will be 2 locks. Once you pick both locks correctly, then you will be allowed inside.")
   print("If you do not open the lock within 3 tries the tree monster will eat you.")


   print("\nAre you ready? (y=yes/n=no)")
   while True:
       try:
           choice = input("> ")
           list = ["y", "n"]
           if choice.lower() not in list:
               raise ValueError
           elif choice.lower() in list[0]:
               lockGame(1)
               break
           elif choice.lower() in list[1]:
               south()
               break
       except ValueError:
           print("Invalid input. Please enter y or n.")


def treeDoor():
   os.system("cls")
   title()
   print("You approach the tree and find the door is locked.\n")


   if items["Sword"] == True:
       print("Do you want to try and pick the lock or try to use your sword? (p=pick/s=sword/b=back)")
       while True:
           try:
               choice = input("> ")
               list = ["p", "s", "b"]
               if choice.lower() not in list:
                   raise ValueError
               elif choice.lower() in list[0]:#pick
                   pickLock()
                   break
               elif choice.lower() in list[1]:#sword
                   dead("tree")
                   break
               elif choice.lower() in list[2]:#back
                   south()
                   break
           except ValueError:
               print("Invalid input. Please enter p, s, or b.")
   else:
       print("Do you want to try and pick the lock or go back? (p=pick/b=back)")
       while True:
           try:
               choice = input("> ")
               list = ["p", "b"]
               if choice.lower() not in list:
                   raise ValueError
               elif choice.lower() in list[0]:#pick
                   pickLock()
                   break
               elif choice.lower() in list[1]:#back
                   south()
                   break
           except ValueError:
               print("Invalid input. Please enter p or b.")


def south():
   os.system("cls")
   title()
   print("You walk south and find a path that leads to a clearing.")
   print("In the clearing, you see a large tree with a small door.\n")
   if items["Shield"] == False:
       print("Do you want to open the door or walk past it? (o=open/p=pass/b=back)")
       while True:
           try:
               choice = input("> ")
               list = ["o", "p", "b"]
               if choice.lower() not in list:
                   raise ValueError
               elif choice.lower() in list[0]:#open
                   treeDoor()
                   break
               elif choice.lower() in list[1]:#pass
                   fight1()
                   break
               elif choice.lower() in list[2]:#back
                   playGame()
                   break
           except ValueError:
               print("Invalid input. Please enter o, p, or b.")
   else:
       print("Are you ready to walk past the tree? (y=yes/b=back)")
       while True:
           try:
               choice = input("> ")
               list = ["y", "b"]
               if choice.lower() not in list:
                   raise ValueError
               elif choice.lower() in list[0]:#yes
                   fight1()
                   break
               elif choice.lower() in list[1]:#back
                   playGame()
                   break
           except ValueError:
               print("Invalid input. Please enter o, p, or b.")


def north():
   os.system("cls")
   title()
   if items["Sword"]: # if you have a sword already
       print("You see nothing on this path.")
       time.sleep(2)
       playGame()
   else: # if you dont have a sword yet
       print("As you walk down the north path you see something shiny in the dirt just off the trail.")
       print("You walk over to it")
       print("\nPress Enter to pick it up.")
       while True:
           try:
               choice = input("> ")
               list = [""]
               if choice not in list:
                   raise ValueError
               elif(choice.lower() in list[0]):#enter
                   break
           except ValueError:
               print("Invalid input. Please press Enter.")


       os.system("cls")
       title()


       print("\nYou Gained A Sword!\n")
       items["Sword"] = True
       print("These are the items you found during your adventure so far.\n",items)
       print("You realize that the path comes to an end, so you turn around.")
       print("You once again see the paths north and south.\n")
       print("Press Enter to take the south path.")
       while True:
           try:
               choice = input("> ")
               list = [""]
               if choice.lower() not in list:
                   raise ValueError
               elif choice.lower() in list[0]:#Enter
                   south()
                   break
           except ValueError:
               print("Invalid input. Please press Enter.")


def playGame():
   os.system('clear')
   title()
   print("You are in a dense forest. The trees tower above you, casting long shadows.")
   print("You can see a path to the north and a path to the south.\n")
   print("Which path do you take? (n=north/s=south)")
   while True:
       try:
           choice = input("> ")
           list = ["n", "s"]
           if choice.lower() not in list:
               raise ValueError
           elif choice.lower() in list[0]:#north
               north()
               break
           elif choice.lower() in list[1]:#south
               south()
               break
       except ValueError:
           print("Invalid input. Please enter n, s, or l.")


def main():
   #reset the items
   items["Sword"] = False
   items["Shield"] = False
   items["Tooth"] = False
   items["Magic Book"] = False
   os.system("cls")
   title()
   print("Your name is Adrian, a brave adventurer.\nIn this story you will navigate through the mysterious Woods of Shadows where")
   print("you will encounter menacing monsters that you must fend off.")
   print("As you battle through the eerie forest, solving riddles and facing challenging foes,\nyour goal is to unravel the dark secret kept at the center the rotting forest.")
   print("You must find the magic book and save the kingdom.\n")
   print("Are you ready? (y=yes/n=no)")
   while True:
       try:
           choice = input("> ")
           list = ["y", "n"]
           if choice.lower() not in list:
               raise ValueError
           elif choice.lower() in list[0]:#yes
               print("You set off into the forest, ready to face whatever dangers lie ahead.\n")
               playGame()
               break
           elif choice.lower() in list[1]:#no
               print("You decide to leave the forest and return to your home.")
               exit(1)
          
       except ValueError:
           print("Invalid input. Please enter y or n.")


def title():
   print("---------------------\nThe Woods of Shadows\n---------------------\n")


if __name__ == "__main__":
   main()
   
  
  



