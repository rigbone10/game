import random
monsters = ["Goblin", "Ghost", "Dragon"]
weapons = ["Sword", "Bow", "Magic"]
targets = ["Head", "Body", "Random"]

gob_health = 10
gst_health = 15
drag_health = 20
health = 0
#Randomly picks monster 
pick = random.SystemRandom()

monster_name = pick.choice(monsters )

def monster_pick(monster_name ):
    
    if  monster_name == "Goblin":                
        health = gob_health
        
    elif  monster_name == "Ghost" :               
        health = gst_health
        
    elif  monster_name == "Dragon":                
        health = drag_health
         
         
def main():         
    print "A " + monster_name + " has appeared before you! It looks angry."

    choice = None
    while (choice is None ):
        print "Fight or Run?"
        choice = raw_input()
        if choice in ["Fight", "fight"]:
            monster_pick(monster_name )
            
        elif choice in ["Run", "run"]:
            exit()
        if choice not in ["Fight", "fight", "Run", "run"]:
            print "I cannot comprehend your forign language"
            choice = None
        
monster_pick(monster_name )
main()
