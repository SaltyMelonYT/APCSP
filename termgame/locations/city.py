from backend import Enemy, Core, Player, Locations
import items
import commands
slowprint=Core.slowprint

def city_robber_encounter(player):
    if "city_robber" in player.visited:
        return
    
    player.visited.add("city_robber")
    robber = Enemy("Robber")
    
    slowprint(f"{player.name} is walking down an alley way, when out of nowhere a masked man steps out from behind a dumpster.")
    robber.dialogue("Stick your hands up and give me everything you got!")
    
    choice = input("Attack or flee? ").lower()
    if choice == "attack":
        robber.health=10
        slowprint("You choose to fight back!")
        while robber.alive():
            weapon=input("What weapon do you choose? /l to list available weapons ")
            if weapon=="/l":
                print(items.weapons)
            else:
                if weapon in items.weapons:
                    slowprint(Player.attack(player, robber, weapon))
                else:
                    print("Invalid choice! Try again")
            print(robber.attack(player))
    else:
        slowprint("You flee from the robber")