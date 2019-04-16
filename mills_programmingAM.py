import random
def main():
# TODO : Create lists for the monsters, weapons, and targets.
    monsters = ["Goblin", "Ghost", "Dragon"]
    weapons = ["Sword", "Bow", "Magic"]
    targets = ["Head", "Body", "Random"]
# TODO : Create a function that gives you the health of a monster. It should take in a monster as a parameter and return the amount of health it starts with.
    def goblin_health(monsters ):
        if monsters == ("Goblin")
        gob_health = 10
        return gob_health
"""
def ghost_health(monsters[1] ):
    gst_health = 15
    return gst_health

def dragon_health(monsters[2] ):
    drag_health = 20
    return drag_health
"""# TODO : Create a function that calculates the amount of damage a player will do to a monster. Its parameters should be the monster, the weapon, and the target and it should return the amount of damage the player will do. You may create additional functions to break up the logic if you wish.
"""
# TODO : Create a function that calculates the amount of damage a monster will do to the player. It should take in a monster as a parameter and return the amount of health it starts with.

def main():
    # TODO : Randomly pick which monster the player will face this game. Set the result equal to the variable 'monster'.
    monster = None

    print "A " + str(monster) + " has appeared before you! It looks angry."

    choice = None
    while (choice is None):
        # TODO : Ask the player what they want to do. Their options are 'fight' and 'run'. Set the player's choice equal to the variable 'choice'.

        if choice not in ["fight", "run"]:
            print "I didn't understand that..."
            choice = None

    # TODO : Exit the program if the player chose to run away. Otherwise, wish them luck in their fight.

    # TODO : Set the monster's starting health by calling your function

    # TODO : Set the player's starting health to 10

    # Turn iterator
    while monster_health > 0 and player_health > 0:
        weapon = None
        while (weapon is None):
            # TODO : Ask the player what weapon they will use to attack the monster. Their options are 'sword', 'bow', and 'magic'. Set the player's choice equal to the variable 'weapon'.
            if weapon not in weapons:
                print "I didn't understand that..."
                weapon = None

        # TODO : Randomly pick where the player will attack the monster. Set the result equal to the variable 'target'.

        # TODO : Set the amount of damage the player will deal to the monster by calling your function

        # TODO : Deal damage to the monster.

        # TODO : If the monster is still alive, set the amount of damage the monster will deal to the player by calling your function

        # TODO : Deal damage to the player.

        # TODO : Inform the player of their health and the monster's health at the end of every turn

    # TODO : Display either a game over or victory message once either the player or the monster has run out of health
"""
main()
