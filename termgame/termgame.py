import backend
import commands
import items
from locations import city, meadow
slowput=backend.Core.slowinput
slowprint=backend.Core.slowprint
p1=backend.Player(input("Player name? "))
p1.location="home"

while p1.alive():
