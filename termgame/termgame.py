import backend
import commands
slowprint=backend.Core.slowprint
p1=backend.Player(input("Player name? "))

while p1.alive():
    commands.cmds(input("What do you want to do? /h for help "), p1)

    if p1.location == "grassy_meadow":
        slowprint(f"{p1.name} encounters someone in the meadow. They approach them slowly.")
        jeremy=backend.NPC("Jeremy")
        jeremy.dialogue("Oh hello traveller! How are you?")
        choice=jeremy.interact("I'm doing fine, how about you?", "Where am I?", "Who are you?")
        if choice == "1":
            slowprint("I'm doing just fine")