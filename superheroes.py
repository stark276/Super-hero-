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

# ---------------------------------------------------------------class-------Weapon---
class Weapon(Ability): 
    
    ###########def __init__(self, name, attack_strength):
                                
    def attack(self):
        return random.randint(self.strength // 2, self.strength)
        


# ---------------------------------------------------------------class-------Hero---

class Hero:
    
    def __init__(self, name, health=100):

        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = health
        self.current_health = health
        self.deaths = 0
        self.kills = 0
        
    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):                                   
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack() #ability.attack()  came from Ability through "ability" argument
        return total_damage     
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amt = 0):                           
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block


    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    
    def take_damage(self, damage): #this damage ==== total_damage += ability.attack()
        self.current_health -= damage - self.defend()
        return self.current_health

    def is_alive(self):
        if self.current_health >= 1:
            return True
        else:
            return False
    
    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():                      #making sure if they are alive
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:

                self_attack = self.attack()
                opp_attack = opponent.attack()

                self.take_damage(opp_attack)
                print(f"{opponent.name} 's  health : {opponent.current_health}")
                opponent.take_damage(self_attack)
                print(f"{self.name} 's  health : {self.current_health}")

                if self.is_alive == True:

                    print(opponent.name + " won!")
                    self.add_kill(1)
                    opponent.add_deaths(1)

                else:
                    print(self.name +  " Won!")
                    self.add_death(1)
                    opponent.add_kill(1)

            else:
                print("Draw")
        return False


    def add_kill(self, num_kills):
        self.kills += num_kills


    def add_death(self, num_deaths):
        self.deaths += num_deaths





# ---------------------------------------------------------------class-------team---


class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self,name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0


    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero)


    def add_hero(self, hero):
        self.heroes.append(hero)


    def stats(self):

        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))
    

    # def revive_heroes(self):
    #     for hero in self.heroes:
    #         hero.health = self.current_health

    # def attack_teams(self, other_team):
    #     ''' Battle each team against each other.'''
    #     while len(self.heroes) > 0 and len(other_team.heroes)> 0:
            



            
            
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight












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
    ability2 = Ability("Super Eyes", 90)
    ability3 = Ability("Wizard Wand", 800)
    ability4 = Ability("Wizard Beard", 100)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

  
# if __name__ == "__main__":
#     hero = Hero("Wonder Woman")
#     weapon = Weapon("Lasso of Truth", 90)
#     hero.add_weapon(weapon)
#     print(hero.attack())
  
