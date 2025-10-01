import backend
import commands
import items
from locations import city, meadow
slowput=backend.Core.slowinput
slowprint=backend.Core.slowprint
p1=backend.Player(input("Player name? "))
p1.location="home"
slowprint("You sat at home, alone and unbothered. You look out the window and into the grassy meadow. Then back around your house.")

while p1.alive():
    commands.cmds(slowput("What do you want to do?"), p1)