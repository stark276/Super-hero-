import random


# ---------------------------------------------------------------class------Ability--

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.strength = attack_strength
    
    def attack(self):
        random_value = random.randint(0,self.strength)
        return random_value
# ---------------------------------------------------------------class------Armor--
class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    
    def block(self):

        random_value1 = random.randint(0,self.max_block)
        return random_value1

# ---------------------------------------------------------------class-------Hero---

class Hero:
    
    def __init__(self, name, starting_health=100):

        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health








if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    # armor = Armor("Debugging Shield", 10)
    # print(armor.name)
    # print(armor.block())

    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)