import random
monsters = ["Goblin", "Ghost", "Dragon"]
weapons = ["Sword", "sword", "Bow", "bow", "Magic", "magic"]
targets = ["Head", "Body", "Random"]
random_damage = [0, 1, 2, 3, 4, 5]
gob_damage = [0, 1, 2, 3]
gst_damage = [0, 1, 2, 3, 4, 5]
drag_damage = [0, 1, 2, 3, 4, 5, 6, 7]
gob_health = 10
gst_health = 15
drag_health = 20
monster_health = 0
player_health = 10

#Randomly picks monster 
monster_pick = random.SystemRandom()
monster_name = monster_pick.choice(monsters)

#Randomly picks target
target_pick= random.SystemRandom()
player_target = target_pick.choice(targets)

#Randomly picks player random attack damage
random_pick = random.SystemRandom()
random_dam = random_pick.choice(random_damage)

#Randomly picks  monster damage
random_gob = random.SystemRandom()
random_gob_damage = random_gob.choice(gob_damage)
random_gst = random.SystemRandom()
radnom_gst_damage = random_gst.choice(gst_damage)
random_drag = random.SystemRandom()
radnom_drag_damage = random_drag.choice(drag_damage)


def monster_pick(monster_name ):
    
    if  monster_name == "Goblin":                
        monster_health = gob_health
        
    elif  monster_name == "Ghost" :               
        monster_health = gst_health
        
    elif  monster_name == "Dragon":                
        monster_health = drag_health
    
def sword_damage(monster_name, weapon_choice, targets):
    #Goblin and Head
    if targets == targets[0] and monster_name == monsters[0]:
        monster_health - 5
        print "Goblin is at " + str(monster_health)
    #Goblin and Body
    elif targets == targets[1] and monster_name == monsters[0]:
        monster_health - 3
        print "Goblin is at " + str(monster_health)
    #Goblin and Random
    elif targets == targets[2] and monster_name == monsters[0]:
        monster_health - random_dam
        print "Goblin is at " + str(monster_health)

        
    #Ghost and Head
    if targets == targets[0] and monster_name == monsters[1]:
        monster_health - 3
        print "Ghost is at " + str(monster_health)
    #Ghost and Body
    elif targets == targets[1] and monster_name == monsters[1]:
        monster_health - 5
        print "Ghost is at " + str(monster_health)
    #Ghost and Random
    elif targets == targets[2] and monster_name == monsters[1]:
        monster_health - random_dam
        print "Ghost is at " + str(monster_health)


    #Dragon and Head
    if targets == targets[0] and monster_name == monsters[2]:
        monster_health - 1
        print "Dragon is at " + str(monster_health)
    #Dragon and Body
    elif targets == targets[1] and monster_name == monsters[2]:
        monster_health - 1
        print "Dragon is at " + str(monster_health)
    #Dragon and Random
    elif targets == targets[2] and monster_name == monsters[2]:
        monster_health - random_dam
        print "Dragon is at " + str(monster_health)



        
def bow_damage(monster_name, weapon_choice, targets):
    #Goblin and Head
    if targets == targets[0] and monster_name == monsters[0]:
        monster_health - 3
        print "Goblin is at " + str(monster_health)
    #Goblin and Body
    elif targets == targets[1] and monster_name == monsters[0]:
        monster_health - 5
        print "Goblin is at " + str(monster_health)
    #Goblin and Random
    elif targets == targets[2] and monster_name == monsters[0]:
        monster_health - random_dam
        print "Goblin is at " + str(monster_health)

        
    #Ghost and Head
    if targets == targets[0] and monster_name == monsters[1]:
        monster_health - 1
        print "Ghost is at " + str(monster_health)
    #Ghost and Body
    elif targets == targets[1] and monster_name == monsters[1]:
        monster_health - 1
        print "Ghost is at " + str(monster_health)
    #Ghost and Random
    elif targets == targets[2] and monster_name == monsters[1]:
        monster_health - random_dam
        print "Ghost is at " + str(monster_health)


    #Dragon and Head
    if targets == targets[0] and monster_name == monsters[2]:
        monster_health - 3
        print "Dragon is at " + str(monster_health)
    #Dragon and Body
    elif targets == targets[1] and monster_name == monsters[2]:
        monster_health - 5
        print "Dragon is at " + str(monster_health)
    #Dragon and Random
    elif targets == targets[2] and monster_name == monsters[2]:
        monster_health - random_dam
        print "Dragon is at " + str(monster_health)    


        
def magic_damage(monster_name, weapon_choice, targets):
    #Goblin and Head
    if targets == targets[0] and monster_name == monsters[0]:
        monster_health - 1
        print "Goblin is at " + str(monster_health)
    #Goblin and Body
    elif targets == targets[1] and monster_name == monsters[0]:
        monster_health - 1
        print "Goblin is at " + str(monster_health)
    #Goblin and Random
    elif targets == targets[2] and monster_name == monsters[0]:
        monster_health - random_dam
        print "Goblin is at " + str(monster_health)

        
    #Ghost and Head
    if targets == targets[0] and monster_name == monsters[1]:
        monster_health - 5
        print "Ghost is at " + str(monster_health)
    #Ghost and Body
    elif targets == targets[1] and monster_name == monsters[1]:
        monster_health - 3
        print "Ghost is at " + str(monster_health)
    #Ghost and Random
    elif targets == targets[2] and monster_name == monsters[1]:
        monster_health - random_dam
        print "Ghost is at " + str(monster_health)


    #Dragon and Head
    if targets == targets[0] and monster_name == monsters[2]:
        monster_health - 5
        print "Dragon is at " + str(monster_health)
    #Dragon and Body
    elif targets == targets[1] and monster_name == monsters[2]:
        monster_health - 3
        print "Dragon is at " + str(monster_health)
    #Dragon and Random
    elif targets == targets[2] and monster_name == monsters[2]:
        monster_health - random_dam
        print "Dragon is at " + str(monster_health)    
        
        
def monster_damage(monster_name):      
    if monster_name == monsters[0]:
        player_health - random_gob_damage
        print "You have " + str(player_health) + " HP"
    if monster_name == monsters[1]:
        player_health - random_gst_damage
        print "You have " + str(player_health) + " HP"
    if monster_name == monsters[2]:
        player_health - random_drag_damage
        print "You have " + str(player_health) + " HP"        
        
def main():         
    print "A " + monster_name + " has appeared before you! It looks angry."

    choice = None
    while (choice is None ):
        print "Fight or Run?"
        choice = raw_input()
        if choice in ["Fight", "fight"]:
            while(monster_health > 0 and player_health > 0):
                weapon_choice = None
                while(weapon_choice is None):
                    print "Use Sword, Bow, or Magic?"
                    weapon_choice = raw_input()
                    if weapon_choice in ["Sword", "sword"] :
                        print "You picked a sword"
                        sword_damage(monster_name, weapon_choice, targets)
                        if monster_health > 0 and player_health > 0:
                            monster_damage(monster_name)
                        elif monster_health <= 0:
                            print "You win"
                        elif player_health <= 0:
                            print "You lose"
                    elif weapon_choice in ["Bow", "bow"] :
                        print "You picked a bow"
                        bow_damage(monster_name, weapon_choice, targets)
                        if monster_health > 0 and player_health > 0:
                            monster_damage(monster_name)
                        elif monster_health <= 0:
                            print "You win"
                        elif player_health <= 0:
                            print "You lose"
                    elif weapon_choice in ["Magic", "magic"] : 
                        print "You picked magic"
                        magic_damage(monster_name, weapon_choice, targets)
                        if monster_health > 0 and player_health > 0:
                            monster_damage(monster_name)
                        elif monster_health <= 0:
                            print "You win"
                        elif player_health <= 0:
                            print "You lose"
                    elif weapon_choice not in weapons:
                        print "That is not a choice"
                        weapon_choice = None            
        elif choice in ["Run", "run"]:
            exit()
        elif choice not in ["Fight", "fight", "Run", "run"]:
            print "I cannot comprehend your forign language"
            choice = None
        
monster_pick(monster_name )
main()
