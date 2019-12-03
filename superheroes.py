import random

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

    #-----------------------------------------------------method----block--
    def block(self):

        random_value1 = random.randint(0,self.max_block)
        return random_value1
        


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())