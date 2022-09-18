# You are Hercules, the greatest of the Greek Heroes! You have been tasked by 
#       King Eurystheus to slay the vicious Nemean Lion, defeat the impossible 
#       nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.

# Features:

# As a developer, I want to make at least five commits on GitHub with descriptive messages.
# As a user, I want an engaging story to be told using print() statements.
# As a user, I want Hercules (and each enemy), to have health, attack power, 
#       and a List of attack names saved in a Dictionary.

##########################################################################################################################

# As a user, I want the ability to select Hercules’ attack using a menu prompt.
# As a user, I want the foe’s attack to be chosen at random.
# As a user, I want the results of each attack to be logged in the terminal.

##########################################################################################################################

# As a developer, I want to use an Attack() function that will terminate when 
#       Hercules or an enemy’s health reaches zero.
# As a developer, I want my RunGame() function to call my other functions in 
#       a logical order that will determine game flow.
# As a developer, I want all of my functions to have a Single Responsibility. 
#       Remember, each function should do just one thing!

##########################################################################################################################
import random



def run_game():
    story_line()
    attack()

def story_line():
    print("Thank you for coming Hercules. You are the greatest of the Greek Heroes!")
    print("You have been tasked by King Eurystheus to undergo a few impossible quests outside the kingdom. ")
    print("Here's what is asked of you might hero:\n 1. Slay the vicious Nemean Lion, 2. Defeat the impossible nine-headed Lernaean Hydra and 3. Capture Cerberus the guard dog of Hades.")

def status(health, attack, powers):
    health = health
    attack = attack
    powers = powers

def attack():
    choice = input(int("What would you like to do?\n 1. Hard Punch\n 2. Kick\n 3. Super Combo\n 4. Heal  "))
    if choice == 1:
        print("Hard Punch!")
    elif choice == 2:
        print("Kick tornado!")
    elif choice == 3:
        print("Super Combo Attack!")
    elif choice == 4:
        print("Thanks I feel better!")
    else:
        ("Invalid choice. Please choose a number 1-4. ")

def quest(choice):
    choice  = input("Which task would you like to do?\n 1. Slay the vicious Nemean Lion.\n 2. Defeat the impossible nine-headed Lernaean Hydra.\n 3. Capture Cerberus the guard dog of Hades.\n Enter a number.")
    if choice == 1:
        print("You choose, The Nemean Lion")
        status(500, 100, "Iron Jaw" )
    elif choice == 2:
    print(" You choose, The Nine-Headed Lernaean Hydra. ")
        status(1500, 500, "Hydra Bite" )
    elif choice == 3:
    print("You choose, Cerberus the guard dog of Hades.")
        status(3000, 1000, "Bark Of Darkness" )
    else:
        print("Invalid choice. Try again. ")
        print()

def enemy(monster):
    print("")

def hero():
    print()         

def random_move(move):
    enemy_move = random.choice(move)




run_game()


