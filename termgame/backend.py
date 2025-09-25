import items
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def heal(self, fooditem):
        if fooditem in items.foods:
            heal_amount = items.foods[fooditem]
            self.health += heal_amount
            if self.health > 100:
                self.health = 100
            return f"{self.name} consumed {fooditem}, health is now {self.health}"
        return "That food item does not exist!"
    
    def damage_mult(self, weapon):
        stats=items.weapons[weapon]
        multiplier=stats["damage"] * (stats["durability"]/100)
        return multiplier

    def attack(self, enemy, weapon):
        if weapon in items.weapons:
            damage_amount = items.weapons[weapon]["damage"] * self.damage_mult(weapon)
            enemy.takeDamage(damage_amount)
            msg = f"{self.name} attacked {enemy.name} with {weapon} for {damage_amount} damage!"
            if not enemy.alive():
                msg += f" {enemy.name} has been defeated!"
            return msg
        return "That weapon does not exist!"

    def action(self, question):
        import commands
        commands.cmds(input(question))
        
class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 125

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
