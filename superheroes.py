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

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):                                    #<=====Abilities
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage     
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt = 0):                           #<=====Armors
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    def take_damage(self, damage): #this damage ==== total_damage += ability.attack()
        self.current_health -= damage - self.defend()
        return self.current_health

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
    
    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive(): #making sure if they are alive
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:

                self_attack = self.attack()
                opp_attack = opponent.attack()

                self.take_damage(opp_attack)
                opponent.take_damage(self_attack)

                if self.is_alive == False:
                    print(opponent.name + " won!")
                else:
                    print(self.name +  " Won!")
            else:
                print("Draw")
        return False












if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    # armor = Armor("Debugging Shield", 10)
    # print(armor.name)
    # print(armor.block())

    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)

    # ability = Ability("Great Debugging", 50)
    # ability1 = Ability("Debugging", 51)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(ability1)
    # print(hero.abilities)

    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())


    
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(1)
    # print(hero.is_alive())

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)