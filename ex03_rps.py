# IMPORT THE MODULE
import random

name = input("To start, please enter your pseudo: ")

user_victory = 0
bot_victory = 0
nul = 0

# User parameters
while True : 
    print(name," : ", user_victory," Equality : ",nul, " Bot : ", bot_victory)

    userChoice = input("Let's choose about : (r)ock, (p)aper or (s)cissors: ")

    if userChoice == "q" : 
        print("You have quit the game !")
        break

    if userChoice != "r" and userChoice != "p" and userChoice != "s" :
        print("To quit the game, please enter 'q' or Ctrl+C")
        continue

    if userChoice == "r" : 
        print("Rock VS", end= ' ')

    elif userChoice == "p" :
        print("Paper VS", end= ' ')

    else : 
        print("Scissors VS", end= ' ')
    
# Bot parameters
    randomNumber = random.randint(1,3)
    
    if randomNumber == 1 : 
        botChoice = "r"
        print("Rock")

    elif randomNumber == 2 : 
        botChoice = "p"
        print("Paper")

    else : 
        botChoice = "s"
        print("Scissors")

# Users
if userChoice == botChoice : 
    print("It's an equality :/")
    nul = nul + 1

elif userChoice == "r" and botChoice == "s" : 
    print("Well done :)")
    user_victory = user_victory + 1

elif userChoice == "p" and botChoice == "r" : 
    print("Well done :)")
    user_victory = user_victory + 1

elif userChoice == "s" and botChoice == "p" : 
    print("Well done :)")
    user_victory = user_victory + 1

# Bot
elif userChoice == "s" and botChoice == "r" : 
    print("Aie, you loose :(")
    bot_victory = bot_victory + 1

elif userChoice == "r" and botChoice == "p" : 
    print("Aie, you loose :(")
    bot_victory = bot_victory + 1

elif userChoice == "p" and botChoice == "s" : 
    print("Aie, you loose :(")
    bot_victory = bot_victory + 1

