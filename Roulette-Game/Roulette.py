# Mason Cuchia 1/20/24
#copy of buckshot roulette


import os, time, random, pygame


# sounds
pygame.mixer.init()
reload = pygame.mixer.Sound("Roulette-Game/Sounds/reload.mp3")
shoot = pygame.mixer.Sound("Roulette-Game/Sounds/shoot.mp3")
empty = pygame.mixer.Sound("Roulette-Game/Sounds/empty-shot.mp3")
victory = pygame.mixer.Sound("Roulette-Game/Sounds/victory.mp3")
#playing the background music
pygame.mixer.music.load("Roulette-Game/Sounds/bg-music.mp3")
pygame.mixer.music.play(-1)




#global variables
check = 1
level = 1
Plives = 2
Dlives = 2
turn = "u" # u=you / d=dealer
firstTime = True


#create the empty mag
mag = {}




def title():
   print("---------------------------------\n\tBuckshot Roulette\n---------------------------------\n")


def suspense():
   #play gun click sound
   reload.play()
   for i in range(1, 5):
       if i < 4:
           print(i * "● ", end="\r")
       else:
           print("● ")
       time.sleep(1)


def load3Bullets():
   global mag
   number_chambers = 3
   number_bullets = 1
   #loads the gun in a random order for 3 bullets (1 live : 2 blank)
   print("Loading the gun")
   suspense()
   for i in range(1, number_chambers+1):
       if i > 2 and number_bullets == 1:
               mag[i] = "bullet"
               pass
       elif number_bullets == 0:
           mag[i] = "blank"
       else:
           num = random.randint(1,10)
           if num <= 5:
               mag[i] = "bullet"
               number_bullets -= 1
           else:
               mag[i] = "blank"


def turnChange(cancel):
   """This function changes the turns between user and dealer."""
   global turn


   if cancel == "cancel":
       level1()
   else:
       if turn == "u":
           turn = "d"
       else:
           turn = "u"
       level1()


def again():
   global firstTime
   #stop the background music
   pygame.mixer.music.fadeout(1000)
   os.system("cls")
   title()
   print("Would you like to play again? (y=yes/n=no)")
   while True:
       try:
           choice = input("> ")
           list = ["y","n"]
           if choice not in list:
               raise ValueError
           elif(choice.lower() in list[0]):#yes
               #play the music again
               pygame.mixer.music.play(-1)
               main()
               break
           elif(choice.lower() in list[1]):#no
               exit(1)      
       except ValueError:
           print("Invalid input. Please enter y or n.")


def main():
   global level, Plives, Dlives, turn, firstTime, mag, check
   #reset all variables
   check = 1
   level = 1
   Plives = 2
   Dlives = 2
   turn = "u"
   firstTime = True
   mag.clear()


   os.system("cls")
   title()
   print("This is a copy of the game Buckshot Roulette.")
   print("You are sitting at a table across from The Dealer.\n")
   print("Press Return to start the game.")
   while True:
       try:
           choice = input("> ")
           list = [""]
           if choice.lower() not in list:
               raise ValueError
           elif choice.lower() in list[0]:#return
               level1()
               break
       except ValueError:
           print("Invalid input. Please press Return.")


def level1():
   global level, Plives, Dlives, turn, firstTime, mag, check
   pygame.mixer.music.set_volume(.2)


   os.system("cls")
   title()
   print(f" -----------------------------------")
   print(f"| Your Lives: {Plives} - Dealer's Lives: {Dlives} |")
   print(f" -----------------------------------")
   if firstTime:
       print("\nThere is a gun loaded with 2 blanks and 1 live round.\nThey will be loaded into the gun in a random order.")
       print("If you shoot the gun at yourself and it is a blank round you get to go again.")
       # time.sleep(3)
       load3Bullets()
       firstTime = False


   #check if anyone has died
   if Plives == 0:
       print("The dealer killed you!")
       again()
   elif Dlives == 0:
       print("You killed the Dealer!")
       #play the victory sound
       victory.play()
       # level2()
       exit(1)


   #if it is your turn
   if turn == "u":
       print("It is your turn.\n")
       if check <= len(mag):
           print("Do you want to shoot at The Dealer or yourself? (d=dealer/y=yourself)")
           print("Enter d or y.")
           #ask the question
           try:
               choice = input("> ")
               list = ["d","y"]
               if choice.lower() not in list:
                   raise ValueError
               elif choice.lower() in list[0]:#shoot at the dealer
                   if mag[check] == "bullet":
                       time.sleep(2)
                       shoot.play()
                       print("You hit him!")
                       Dlives -= 1
                       time.sleep(1)
                   else:
                       time.sleep(2)
                       empty.play()
                       print("Nothing happened.")
                       time.sleep(1)
                   check += 1
                   time.sleep(2)
                   turnChange("x")
               elif choice.lower() in list[1]:#shoot at yourself
                   if mag[check] == "bullet":
                       time.sleep(2)
                       shoot.play()
                       print("You shot yourself!")
                       Plives -= 1
                       time.sleep(1)
                       check += 1
                       time.sleep(2)
                       turnChange("x")
                   else:
                       time.sleep(2)
                       empty.play()
                       print("Nothing happened.")
                       print("You get to go again.")
                       time.sleep(1)
                       check += 1
                       time.sleep(2)
                       turnChange("cancel")
           except ValueError:
               print("Invalid input. Please enter d or y.")
       else:
           print("The gun is empty.")
           #reset check
           check = 1
           # delete everything from mag
           mag.clear()
           #reload gun
           load3Bullets()
           turnChange("cancel")


   #if it is the dealer's turn
       #check if anyone has died
       if Plives == 0:
           print("The dealer killed you!")
           again()
       elif Dlives == 0:
           print("You killed the Dealer!")
           # level2()
           exit(1)


   elif turn == "d":
       print("\nDealer's Turn\n")
       if check > len(mag):
               print("The gun is empty.")
               turnChange("x")
       time.sleep(2)
       num = random.randint(1,2)
       # 1 = shoot at player
       if num == 1:
           if mag[check] == "bullet":
               shoot.play()
               print("He shot you!")
               Plives -= 1
               time.sleep(1)
           else:
               empty.play()
               print("Nothing happened.")
               time.sleep(1)
           check += 1
           time.sleep(2)
           turnChange("x")
       # 2 = shoot at yourself
       else:
           if mag[check] == "bullet":
               shoot.play()
               print("The dealer shot himself!")
               Plives -= 1
               time.sleep(1)
               check += 1
               time.sleep(2)
               turnChange("x")
           else:
               empty.play()
               print("Nothing happened.")
               print("You get to go again.")
               time.sleep(1)
               check += 1
               time.sleep(2)
               turnChange("cancel")
      
# def level2():
#    os.system("cls")
#    print("Welcome to level 2.")










if __name__ == "__main__":
   main()



