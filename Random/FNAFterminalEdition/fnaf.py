import time
import random
import os

class animatronic():
    def __init__(self, name, location=0):
        self.name=name
        self.location=location

class game():
    def __init__(self):
        self.Freddy=animatronic("Freddy")
        self.Chica=animatronic("Chica", 9)
        self.Bonnie=animatronic("Bonnie")
        self.Foxy=animatronic("Foxy")
    l_animatronic=[]
    r_animatronic=[]
    r_doorState=0 # Open
    l_doorState=0 # Open
    r_lightState=0 # off
    l_lightState=0 # off

    def alive(self):
        status=1

    def chicaMove(self):
        chance=random.randrange(0,50)
        # print(chance)
        toMove=self.Chica
        if chance<25:
            advance=random.randrange(1,3)
            # print("Chica advance chance:", advance)
            if toMove.location==9 and self.l_doorState==0:
                print("Uh oh! Chica killed you. GAME OVER")
                self.alive=0

            if advance==1: # Forward progression
                if toMove.location==0: # If on stage, move to dining area
                    toMove.location=toMove.location+1

                elif toMove.location==9: # Makes sure the Animatronic does not leave the play area
                    toMove.location=toMove.location-1

                elif toMove.location % 2 == 1: # If in dining area, or any other odd room, advance 2
                    toMove.location=toMove.location+2
                    if toMove.location==9:
                        self.l_animatronic.append("chica")

            elif advance==2: # Backwards progression
                if toMove.location==1 or toMove.location==0:
                    pass

                else:
                    toMove.location=toMove.location-2
                    if "chica" in self.l_animatronic:
                        self.l_animatronic.remove("chica")
        else:
            pass

    def bonnieMove(self):
        chance=random.randrange(0,50)
        # print(chance)
        toMove=self.Bonnie
        if chance<25:
            advance=random.randrange(1,3)
            # print("Bonnie advance chance:", advance)

            if advance==1: # Forward progression
                if toMove.location==0: # If on stage, move to dining area
                    toMove.location=toMove.location+1

                elif toMove.location==8: # Makes sure the Animatronic does not leave the play area
                    toMove.location=toMove.location-1

                elif toMove.location % 2 == 0: # If in dining area, or any other odd room, advance 2
                    toMove.location=toMove.location+2
                    if toMove.location==8:
                        self.r_animatronic.append("bonnie")

            elif advance==2: # Backwards progression
                if toMove.location==1 or toMove.location==0:
                    pass

                else:
                    toMove.location=toMove.location-2
                    if "bonnie" in self.r_animatronic:
                        self.r_animatronic.remove("bonnie")
        else:
            pass

    def animatronicProgression(self):
        choose=random.randrange(1,4)
        if choose==1:
            self.chicaMove()
        elif choose==2:
            self.bonnieMove()
        # print(choose)
            
    def l_light(self, input): # Controlled with p
        lightState=game.l_lightState
        if input.lower()=='p':
            if lightState==0:
                lightState=1
                print("Light on!")
                if 'freddy' in game.l_animatronic or 'chica' in game.l_animatronic:
                    print("Animatronic in door!")
                else:
                    print("Clear!")
            elif lightState==1:
                print("Light off!")
                lightState=0

    def r_door(self, input): # controlled with l
        if input.lower()=="l":
            if game.r_doorState==0:
                game.r_doorState=1
                print("Closed the door")
            else:
                game.r_doorState=0
                print("Opened the door")
    

    def r_light(self, input): # Controlled with q
        lightState=game.r_lightState
        if input.lower()=='q':
            if lightState==0:
                lightState=1
                print("Light on!")
                if 'bonnie' in game.r_animatronic:
                    print("Animatronic!")
                else:
                    print("Clear!")
            elif lightState==1:
                print("Light off!")
                lightState=0

    def l_door(self, input): # Controlled with a
        if input.lower()=="a":
            if game.l_doorState==0:
                game.l_doorState=1
                print("Closed the door")
            else:
                game.l_doorState=0
                print("Opened the door")

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def main():
    startTime = time.time()
    nightLength = 360       # 360 real seconds = 6 FNAF hours → 1 minute per in-game hour
    g = game()

    while True:
        currentTime = time.time()
        elapsed = currentTime - startTime

        hour = int(elapsed // 60)       # every 60 sec is 1 hour
        displayHour = (hour + 12) % 12  # convert to 12-hour format
        if displayHour == 0:
            displayHour = 12

        g.animatronicProgression()

        print(displayHour, "AM")
        action = input("What action? (h for help) ").lower()
        clear()
        if g.alive==0:
            break
        else:
            if action == 'q':
                g.r_light('q')
            elif action == 'l':
                g.r_door('l')
            elif action == 'p':
                g.l_light('p')
            elif action == 'a':
                g.l_door('a')
            elif action == 'h':
                print("""Q - Left light
A - Left door
P - Right light
L - Right door""")
            elif action == 'debug':
                print("Chica postion:", g.Chica.location)
                print("Bonnie position:", g.Bonnie.location)

            if elapsed >= nightLength:
                print("6 AM! You win!")
                g.alive=0

main()
