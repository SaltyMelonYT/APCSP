import backend
import items
p1=backend.Player(input("Player name? "))

print(f"Your player stats are:\nHealth: {p1.health}")

goblin=backend.Enemy("Goblin")

print("You have encountered a Goblin! What do you want to do?")

while goblin.alive:
    p1.action("Use /h to see available options! ")