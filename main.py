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
    welcome()
    quest()
    hero()
    story_line()

    # status()
    # a = attack(1)
   

def welcome():
    print()
    print("Thank you for coming Hercules. You are the greatest of the Greek Heroes!")
    print("You have been tasked by King Eurystheus to undergo a few impossible quests outside the kingdom. ")
    print("Here's what The King wishes of you, the mightest of heros:\n   -Slay the vicious Nemean Lion.\n   -Defeat the impossible nine-headed Lernaean Hydra.\n   -Capture Cerberus the guard dog of Hades.")
    print()

def status(health, attack_1, powers):
   
    # health = health
    # attack_1 = attack_1
    # powers = powers
    print()
    choice = int(input("Who's status would you like to check?  \n1. My Status \n2. Enemy Status \nChoose now: " ))
    cont = True
    while cont == True:
        if choice == 1:

            hero()
    
            cont = False
        elif choice == 2:
            enemy(e_health, e_attack, e_powers)
            cont = False
        else:
            print("Try again")
            cont = True

def attack(move):
    if move == 1:
        print("You used Hercules Grip!")
        damage = random_number(move)
        h_math(damage)
    
    # elif choice == 2:
    #     print("Kick tornado!")Titan Kick
    # elif choice == 3:
    #     print("Super Combo Attack!")Hercules Might
    # elif choice == 4:
    #     print("Thanks I feel better!")The Call of Asclepius to Heal
    elif move == 5:
         status(health, attack_1, powers)
    else:
        ("Invalid choice. Please choose a number 1-4. ")
        return True

def quest():
    cont = True
    while cont == True:
        print()
        print("Which task would you like to do?  \n 1. Slay the vicious Nemean Lion. \n 2. Defeat the impossible nine-headed Lernaean Hydra. \n 3. Capture Cerberus the guard dog of Hades.")
        print()
        choice  = int(input("Enter your choice now. "))
        if choice == 1:
            print()
            print("You choose, The Nemean Lion")
            global e_health, e_attack
            e_health, e_attack = 500, 100
            e_powers = {"Attack1" : "Bite  ", "Attack2" : "Lion's Might  " , "Attack3" : "Earthquake  ", "Special" : "Iron Jaw" }
            enemy(e_health, e_attack, e_powers)
            
            cont = False
        # elif choice == 2:
        #     print(" You choose, The Nine-Headed Lernaean Hydra. ")
        #     powers = {"Attack 1" : "Snake Bite", "Attack 2" : "Vemon" , "Attack 3" : "Tusnami", "Special" : "Leviathan" }
        #     health, attack, powers = 1500, 500, powers 
        #     print("Your enemies stats are: \n Health: {}\n Attack Strenght: {}".format(health, attack)) 
        #     print(" Attacks Move:\n  " + powers["Attack1"] + "\n  " + powers["Attack2"] + "\n  " + powers["Attack3"] + "\n  " + powers["Special"])
        #     enemy(health, attack, powers)
    
        #     cont = False
        # elif choice == 3:
        #     print("You choose, Cerberus the guard dog of Hades.")
        #     powers = {"Attack1" : "Flame Breath", "Attack2" : "Bone Crusher" , "Attack3" : "Cerberus Pounce", "Special" : "Hell Hound" }
        #     health, attack, powers = 3000, 1000, powers 
        #     print("Your enemies stats are: \n Health: {}\n Attack Strenght: {}".format(health, attack)) 
        #     print(" Attacks Move:\n  " + powers["Attack1"] + "\n  " + powers["Attack2"] + "\n  " + powers["Attack3"] + "\n  " + powers["Special"])
        #     enemy(health, attack, powers)

        #     cont = False
        else:
            print("Invalid choice. Try again. ")
            cont = True
            print()


def enemy(x, y, z):
    global e_health, e_attack, e_powers
    e_health, e_attack, e_powers = x, y, z
    print() 
    print("Your enemies stats are:\nHealth: {}\nAttack Strenght: {}".format(e_health, e_attack)) 
    print("1Attacks Move:\n  1. " + e_powers["Attack1"] + "\n  2. " + e_powers["Attack2"] + "\n  3. " + e_powers["Attack3"] + "\n  4. " + e_powers["Special"])
    print()

def mylists(choice):
    if choice == 1:
        hero()
    elif choice == 2:
        enemy()


def hero():
    global  health, attack_1, powers
    powers = {"Attack1" : "Hercules Grip", "Attack2" : "Titan Kick" , "Super Move" : "Hercules Might", "Special" : "The Call of Asclepius to Heal" }
    health, attack_1 = 5000, 250
    print()
    print("Your Hero stats are: \nHealth: {}\nAttack Strenght: {}".format(health, attack_1))
    print("Attacks Moves:\n  1. " + powers["Attack1"] + "\n  2. " + powers["Attack2"] + "\n  3. " + powers["Super Move"] + "\n  4. " + powers["Special"])      
    print()

def h_math(num):
    if num == 1:
        e_health = e_health - num
    elif num == 2: 
        e_health = e_health - num
    elif num == 3:
        e_health = e_health - num
    elif num == 4:
        e_health = e_health - num

def e_math(num):
    if num <= 499:
        e = health = e_health - num
    elif num >= 500 and num <= 899:
        e = health = e_health - num
    elif num >= 900 and num <= 1999:
        e = health = e_health - num
    elif num >= 2000 and num <= 3999:
        e = health = e_health - num


def random_move(move):
    global total_damage
    total_damage = []
    move = e_powers 

    enemy_move = random.choice(move)
    if  enemy_move == move["Attack1"]: 
        print("The enemy used", move["Attack1"])
        damage = random_number(1)
        total_damage = [e_math(damage)]

    elif  enemy_move == move["Attack2"]: 
        print("The enemy used", move["Attack2"])
        damage = random_number(2)
        total_damage = [e_math(damage)]

    elif  enemy_move == move["Attack3"]: 
        print("The enemy used", move["Attack3"])
        damage = random_number(3)
        total_damage = [e_math(damage)]

    elif  enemy_move == move["Special"]: 
        print("The enemy used", move["Special"])
        damage = random_number(4)
        total_damage = [e_math(damage)]
        
       

def random_number(num):
    if num == 1:
        damage = random.randint(250, 499)
        return h_math(damage)

    elif num == 2:
        damage = random.randint(500, 899)
        return h_math(damage)

    elif num == 3:
        damage = random.randint(900, 1999)
        return e_math(damage)
        

    elif num == 4:
        damage = random.randint(2000, 3999)
        return e_math(damage)


def story_line():
    print("Your quest begans.")
    cont = True
    while cont == True:
        print()
        print("Your moves are:\n  1. " + powers["Attack1"] + "\n  2. " + powers["Attack2"] + "\n  3. " + powers["Super Move"] + "\n  4. " + powers["Special"] + "\n  5. Status" )
        print()
        choice = int(input("What would you like to do? "))
        attack(choice)
    
    print("Your target strike bac causing Damage.")






run_game()


