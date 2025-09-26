import backend
import commands
import items
from locations import city
slowprint=backend.Core.slowprint
p1=backend.Player(input("Player name? "))

while p1.alive():
    commands.cmds(input("What would you like to do?\nHINT! Use /h for help\n"),p1)
    if p1.location == "city":
        city.city_robber_encounter(p1)