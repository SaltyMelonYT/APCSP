import backend as be
import items
def cmds(args):
    if args == "/h":
        print("Use food to consume an item, and weapons to see your available weapons")
    elif args == "food":
        print(f"Your food options are {items.foods}")
    elif args == "weapons":
        print(f"Your available weapons are {items.weapons}")