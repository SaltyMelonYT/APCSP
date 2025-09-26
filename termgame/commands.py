import items
from backend import Locations, Core, Player
from locations import home
slowprint=Core.slowprint
def cmds(args, player, enemy=None):
    if args == "/h":
        print("food - list consumables\nheal - consume a good to heal\nweapons - see available weapons\nattack - attack an enemy with a specified weapon\nplaces - See a list of available places to travel to\ntravel - Travel to a location\n")
    
    elif args == "food":
        print(f"Your food options are {items.foods}")

    elif args == "heal":
        food=input("What do you want to eat? ")
        print(player.heal(food))
    
    elif args == "weapons":
        print(f"Your available weapons are {items.weapons}")
    
    elif args == "attack":
        if enemy is None:
            print("No enemy to attack right now")
        else:
            weapon=input("Weapon to use: ")
            print(player.attack(enemy, weapon))
    
    elif args == "inv":
        if not items.items:
            print("Your inventory is empty!")
        else:
            print(items.items)

    elif args == "places":
        places = []


        if player.location == "home":
            places.append("Grassy Meadow")
        elif player.location == "grassy_meadow":
            places.append("Home")

        if "map" in items.items:
            places.append("City")

        filtered = [p for p in places if p.lower().replace(" ", "_") != player.location]

        for i, place in enumerate(filtered, start=1):
            print(f"{i}.) {place}")

    
    elif args.startswith("travel"):
        parts = args.split()
        destinations = []

        destinations.append(("Grassy Meadow", Locations.grassy_meadow))
        if "map" in items.items:
            destinations.append(("City", Locations.city))

        if len(parts) == 1:
            for i, (name, _) in enumerate(destinations, start=1):
                print(f"{i}.) {name}")

            travel = input("Where do you want to travel to? ")

        else:
            travel = parts[1]

        if travel.isdigit():
            travel_num = int(travel)
            if 1 <= travel_num <= len(destinations):
                _, location_func = destinations[travel_num - 1]
                location_func(player)
            else:
                print("Invalid destination!")
        else:
            print("Invalid input!")
            
    else:
        print("Unknown command, enter /h for help")        