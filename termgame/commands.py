import items
from backend import Locations
def cmds(args, player, enemy=None):
    if args == "/h":
        print("food - consume an item\nweapons - see available weapons\nattack - attack an enemy with a specified weapon\nplaces - See a list of available places to travel to\ntravel - Travel to a location")
    
    elif args == "food":
        print(f"Your food options are {items.foods}")
    
    elif args == "weapons":
        print(f"Your available weapons are {items.weapons}")
    
    elif args == "attack":
        if enemy is None:
            print("No enemy to attack right now")
        else:
            weapon=input("Weapon to use: ")
            print(player.attack(enemy, weapon))
    
    elif args == "places":
        print("1.) grassy meadow")
    
    elif args == "travel":
        print("1.) Grassy Meadow\n2.) City")
        travel=input("Where do you want to travel to? ")
        if travel == "1":
            Locations.grassy_meadow(player)
        elif travel=="2":
            Locations.city(player)
    
    else:
        print("Unknown command, enter /h for help")        