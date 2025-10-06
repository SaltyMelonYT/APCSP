import backend
import commands
import items
from locations import city, meadow
slowput=backend.Core.slowinput
slowprint=backend.Core.slowprint
p1=backend.Player(input("Player name? "))
p1.location="home"
slowprint("You sat at home, alone and unbothered. You look out the window and into the grassy meadow. Then back around your house.")

visited_grassy_meadow = False

while p1.alive():
    commands.cmds(slowput("What do you want to do?"), p1)

    if p1.location == "grassy_meadow" and not visited_grassy_meadow:
        slowprint("You travel into the grassy meadow. The birds were chirping, and a rabbit hopped through the long grass.")
        slowprint("You spot something out of your eye. Go investigate?")

        while True:
            choice = input("y/n: ")
            if choice.lower() == "y":
                while True:
                    slowprint("You go to investigate and find its a map! Pick it up?")
                    choice = input("y/n: ")
                    if choice.lower() == "y":
                        slowprint("You pick it up. It's a map! You find it to be useful and put it in your inventory")
                        items.items["map"] = 1
                        break
                    elif choice.lower() == "n":
                        slowprint("You leave the map on the ground with no intention of seeing what it says or where it leads.")
                        break
                    else:
                        print("ERROR!\nPlease use proper syntax described")
                break

            elif choice.lower() == "n":
                slowprint("You choose to ignore the thing in the corner of your eye and continue walking in the meadow")
                break

            else:
                print("ERROR!\nPlease use the proper syntax described")
        
        visited_grassy_meadow = True


        