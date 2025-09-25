import items
import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.location="house"

    def heal(self, fooditem):
        if fooditem in items.foods:
            heal_amount = items.foods[fooditem]
            self.health += heal_amount
            if self.health > 100:
                self.health = 100
            return f"{self.name} consumed {fooditem}, health is now {self.health}"
        return "That food item does not exist!"
    
    def attack(self, enemy, weapon):
        if weapon in items.weapons:
            damage_amount = items.weapons[weapon]
            enemy.takeDamage(damage_amount)
            msg = f"{self.name} attacked {enemy.name} with {weapon} for {damage_amount} damage! {enemy.name} has {enemy.health} health"
            if not enemy.alive():
                msg += f" {enemy.name} has been defeated!"
            return msg
        return "That weapon does not exist!"
    def alive(self):
        return self.health > 0
    
class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 30

    def takeDamage(self, damageValue):
        self.health -= damageValue
        if self.health < 0:
            self.health = 0
        return f"{self.name} now has {self.health} health left."

    def attack(self, player):
        damage = random.randint(5, 15)
        player.health -= damage
        if player.health < 0:
            player.health = 0
        return f"{self.name} attacks {player.name} for {damage} damage! {player.name} now has {player.health} health."

    def alive(self):
        return self.health > 0

class NPC:
    def __init__(self, name):
        self.name = name

    def dialogue(self, text):
        Core.slowprint(text)

    def interact(self, opt1, opt2, opt3):
        print(f"1.) {opt1}")
        print(f"2.) {opt2}")
        print(f"3.) {opt3}")
        choice=input("Choose a number. ")
        return choice
    
class Core:
    def slowprint(text, duration=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(duration)
        print()

class Locations:

    @staticmethod
    def grassy_meadow(player):
        player.location="grassy_meadow"
        return "grassy_meadow"

    @staticmethod
    def city(player):
        player.location="city"
        return "city"