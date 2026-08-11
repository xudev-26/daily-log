import random #for randomization
from array import array #import the specific tools from array module so we dont have to write array.array

def stats(health, gold, strength):#the purpose of this function is to show the stats of the player | the three parameters acts as a receiver for three data
    #inside the player function
    print("=" * 25)
    print("PLAYER STATS")
    print("=" * 25)
    print(f"Health: {health[0]} | Gold: {gold[0]} | Strength: {strength[0]}")#displaying the stats

def get_enemy(): #the purpose of this function is for the stats of the enemy
    enemies = {#dictionary that has list values that represent the enemy stats | index 0 is the health, 1 is the damage, and 2 is the gold it has
        "priest": [30, 5, 15], 
        "bishop": [40, 8, 20],
        "saintes": [60, 12, 30],
        "pope": [100, 20, 30]
    }

    name = random.choice(list(enemies.keys()))#get the enemies dictionary keys, then transform that into a list, then randomize them
    stats = enemies[name] #get the value of the pick keys in dictionary
    return name, stats #jobs done, so the data gets passed back into the function until the player function call its | this gets returned as tuple becuase 
    #it is a multiple values

def fight(health, gold, strength):#now for this function, this functions job is to receive the data given by player function and store them into it's parameter
    enemy_name, enemy_stats = get_enemy() # calls the last function and unpact it into two new variable to store the data, it is always positional
    #so enemy_name represents the name and enemy_stats of course represent the stats variable in the last function

    enemy_health = enemy_stats[0] #access the value from the list by calling its index position | so this is the health
    enemy_strength = enemy_stats[1] #this is the strength
    enemy_gold = enemy_stats[2]#this is the gold 

    print(f"\nA {enemy_name} appeared!")
    print(f"Enemy health is {enemy_health}")    
    print(f"Enemy strength is {enemy_strength}")

    while enemy_health > 0 and health[0] > 0: #this loop will keep running as long as the enemy health is not 0 and our health
        print("\n1. Attack")
        print("2. Run") #instructions same as the first print
        choice = input("> ") #getting the user input

        if choice == "1": #if the user enter 1 in the choice this is what will follow
            damage = random.randint(strength[0] - 2, strength[0] + 5) #our dmage gets randomize between 8-15, and store it in damage variable for future use
            if damage < 1: #this is just a chekcer if the random module suddenly picked something below 1 then sets its damage back to 1
                damage = 1
            
            enemy_health -= damage #the damage you've dealt is then minus to the enemy health by the -= function
            print(f"You dealt {damage} damage!") #just a display

            if enemy_health <= 0: #now if enemy health is equal or less than 0 the loops end
                print(f"You defeated {enemy_name}!")
                gold[0] += enemy_gold #because we've defeated the enemy, we got the gold it possesed by adding the value to our gold array
                strength[0] += 2 #same thing as before, because we've defeated the enemy, we add the value to our strength array
                print(f"You gained {enemy_gold} gold!")
                print("Your strength increased by 2!")
                return # Modifies the shared arrays, then exits fight() and goes back to player()

            enemy_damage = random.randint(enemy_strength - 2, enemy_strength + 3) #randomize the enemy_damage using random module and store it into enemy_damage variable 
            if enemy_damage < 1: #now this is the same as the last one, just a checker if the random module suddenly pick outside the choice
                enemy_damage = 1

            health[0] -= enemy_damage
            print(f"The enemy {enemy_name} dealt {enemy_damage} damage!")#display
        
        elif choice == "2": #if the user picked 2, the loops end 
            print("You are a coward!")
            return #loops end
        else:
            print("Invalid choice!")#any other choice is invalid so if you enter 5, it will keep asking. the loop will never break

def buff(health, strength): #another function for buffs, the two parameter is use to store the data its going to receive from the player function
    buffs = {#this is a nested dictionary, containing the buffs and the keys for it
        "1": {
            "Name": "Strength Potion",
            "Effectiveness": 10,
            "Health": 0
        },
        "2": {
            "Name": "Health Potion",
            "Effectiveness": 0,
            "Health": 30
        },
        "3": {
            "Name": "Power Potion",
            "Effectiveness": 5,
            "Health": 20
        }
    }

    print("\n===== BUFFS =====")
    print("1. Strength Potion (+10 Strength)")
    print("2. Health Potion (+30 Health)")
    print("3. Power Potion (+5 Strength, +20 Health)")

    choice = input("Choose a buff: > ")

    if choice in buffs: #now this validates if the input in choice variable is in the dictionary, if so then 
        selected = buffs[choice]  #get the value of the user choice | if 1 then it access the value inside 1
        strength[0] += selected['Effectiveness']
        health[0] += selected['Health'] #add the value to our stats
        print(f"You used {selected['Name']}") 
    else:
        print("Invalid Buff") #if you pick other choice, it will print this

def player(): #This is where everything actually happens
    print("================================")
    print("    WELCOME TO CHURCH DUNGEON     ")#DISPLAY
    print("================================")

    health = array('i', [100])#An array representing our stats  | that is accessed by other function, so this is where those actually came from | not actually accessed but those function are called here to access this
    gold = array('i', [0])
    strength = array('i', [10])

    while health[0] > 0: #while our health is greater than 0 then the loop will keep going
        stats(health, gold, strength) #calls the stat function to display our stats | like i said this is where everything happens

        print("\n1. Explore")
        print("2. Use Buff")
        print("3. Rest")#Instructions
        print("4. Quit")

        choice = input("Select your choice: > ")

        if choice == '1':#If the input in user is 1 then call the fight function 
            fight(health, gold, strength)
        
        elif choice == '2':#If input is 2 then call the buff function
            buff(health, strength)
        
        elif choice == '3':#If inputis 3 then randomize between 10 up to 25, how high the heal the player is going to receive
            heal = random.randint(10, 25)
            health[0] += heal #add the result of heal variable into our health
            print(f"You've recovered {heal} HP!")

        elif choice == '4': #Quit
            print("Weak, why did you give up")
            break

        else:
            print("Invalid Choice")#Like others if u input any other choice besides the instructions

        if gold[0] >= 100:#If the player has reach 100 gold or above then game ends, loops end
            print("Congrats you've won!")  
            break  

    if health[0] <= 0: #if dead, the same loops end
        print("You died")

player() #calls this function which is resposible for everything
