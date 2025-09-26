from backend import Enemy, Core, Player, Locations
import items
import commands
slowprint=Core.slowprint
slowput=Core.slowinput

def opening(player):
    if "grassy_meadow" not in player.visited:
        first_time(player)
        player.visited.add("grassy_meadow")
    elif "grassy_meadow_normal" not in player.visited:
        normal_entry(player)
        player.visited.add("grassy_meadow_normal")
    else:
        pass

def first_time(player):
    slowprint(f"{player.name} walks into the meadow that lies behind their house.")
    slowprint("Birds were chirping gleefully. Something in the distance caught your eyes")
    if slowput("Investigate? y/n ") == 'y':
        slowprint("You walk over, and find it's a map to a city not too far from your house")
        if slowput("Take map and put it in your inventory? y/n ") == 'y':
            items.items["map"] = 1
            slowprint("You put the map into your pocket and return inside.")
            player.location="home"


def normal_entry(player):
    slowprint(f"{player.name} walks into the meadow again. It's calm and peaceful here.")
