import random
monsters = ["Goblin", "Ghost", "Dragon"]
weapons = ["Sword", "sword", "Bow", "bow", "Magic", "magic"]
targets = ["Head", "Body", "Random"]
random_damage = [0, 1, 2, 3, 4, 5]
gob_health = 10
gst_health = 15
drag_health = 20
health = 0
head = 0
body = 0
#Randomly picks monster 
monster_pick = random.SystemRandom()
monster_name = monster_pick.choice(monsters )
target_pick= random.SystemRandom()
player_target = target_pick.choice(targets )
"""random_pick = random.SystemRandom()
random_dam = random_pick.choice(random_damage)"""

def monster_pick(monster_name ):
    
    if  monster_name == "Goblin":                
        health = gob_health
        
    elif  monster_name == "Ghost" :               
        health = gst_health
        
    elif  monster_name == "Dragon":                
        health = drag_health
    
def weapon_damage(monster_name, weapon_choice, targets):
    if weapon_choice == weapons[:2] and monster_name == "Goblin":
        if target_pick == "Random":
        
        
        
        

    
        
        
        
def main():         
    print "A " + monster_name + " has appeared before you! It looks angry."

    choice = None
    weapon_choice = None
    while (choice is None ):
        print "Fight or Run?"
        choice = raw_input()
        if choice in ["Fight", "fight"]:
            while(weapon_choice is None ):
                print "Use Sword, Bow, or Magic?"
                weapon_choice = raw_input()
                if weapon_choice in ["Sword", "sword"] :
                    print "You picked a sword"
                    
                elif weapon_choice in ["Bow", "bow"] :
                    print "You picked a bow"
                elif weapon_choice in ["Magic", "magic"] : 
                    print "You picked magic"
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
