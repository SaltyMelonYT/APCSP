import time
import random
import os
import json
import threading
class animatronic():
    def __init__(self, name, location=0):
        self.name=name
        self.location=location

class game():
    def __init__(self):
        self.Freddy=animatronic("Freddy")
        self.Chica=animatronic("Chica")
        self.Bonnie=animatronic("Bonnie")
        self.Foxy=animatronic("Foxy", 10)
        self.l_animatronic=[]
        self.r_animatronic=[]
        self.r_doorState=0 # Open
        self.l_doorState=0 # Open
        self.r_lightState=0 # off
        self.l_lightState=0 # off
        self.amount=100 # power level
        self.alive=0 # Alive, 1 is dead
        self.cameraState=0
        self.cameraSuspended=1
        self.continueState=4

        # POWER FUNCTIONS
        self.powerCount=0
        self.drainState=1 # Minimal power usage
        self.drainDisplay="[]"

        # TIME FUNCTIONS
        self.startTime=0 # Takes the start time
        self.currentTime=0 # Takes the current time
        self.elapsed = 0 # Sees how much time has elapsed
        self.displayHour=12

        # FOXY FUNCTIONS
        self.foxyState=0 # 0 is behind the curtain, 1 is peeking, 2 is open, 3 is outside, 4 is gone.
        self.FoxyPowerLoss=1
        self.FoxyCount=0
        self.FoxyMoveOn=0
        self.FoxyProceed = random.randint(3,5)

        self.FreddyCount=0

    def time(self):
        nightLength=360
        if self.startTime==0:
            self.startTime=time.time()
        else:
            pass
        self.currentTime=time.time()
        self.elapsed=self.currentTime-self.startTime
        hour = int(self.elapsed // 60)
        self.displayHour = (hour + 12) % 12
        if self.displayHour == 0:
            self.displayHour = 12

        if self.elapsed >= nightLength:
            self.clear()
            time.sleep(1.4)
            print("6 AM! You win!")
            self.alive=2
            self.continueState=self.continueState+1

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def chicaMove(self, max=50, theChance=25):
        chance=random.randint(0,max)
        toMove=self.Chica
        if chance<theChance:
            advance=random.randint(1,2)
            if toMove.location==9 and self.r_doorState==0: # Death Logic
                print("Uh oh! Chica killed you. GAME OVER")
                self.alive=1

            if advance==1: # Forward progression
                if toMove.location==0: # If on stage, move to dining area
                    toMove.location=toMove.location+1

                elif toMove.location==9: # Makes sure the Animatronic does not leave the play area
                    toMove.location=toMove.location-1

                elif toMove.location % 2 == 1: # If in dining area, or any other odd room, advance 2
                    toMove.location=toMove.location+2
                    if toMove.location==9:
                        self.r_animatronic.append("chica")

            elif advance==2: # Backwards progression
                if toMove.location==1 or toMove.location==0:
                    pass

                else: # This makes sure that if shes in the doorway she moves back
                    toMove.location=toMove.location-2
                    if "chica" in self.r_animatronic:
                        self.r_animatronic.remove("chica")
        else:
            pass

    def freddyMove(self, max=50, theChance=40):
        chance=random.randint(0,max)
        toMove=self.Freddy
        if chance<theChance:
            if self.FreddyCount==3:
                advance=random.randint(1,2)
                if toMove.location==9 and self.r_doorState==0: # Death Logic
                    print("Uh oh! Freddy killed you. GAME OVER")
                    self.alive=1

                if advance==1: # Forward progression
                    if toMove.location==0: # If on stage, move to dining area
                        toMove.location=toMove.location+1

                    elif toMove.location==9: # Makes sure the Animatronic does not leave the play area
                        toMove.location=toMove.location-1

                    elif toMove.location % 2 == 1: # If in dining area, or any other odd room, advance 2
                        toMove.location=toMove.location+2
                        if toMove.location==9:
                            self.r_animatronic.append("freddy")
                    else: pass

            elif self.cameraState==self.Freddy.location:
                self.FreddyCount=0

            else:
                self.FreddyCount=self.FreddyCount+1
        else:
            pass


    def bonnieMove(self, max=50, theChance=25):
        chance=random.randint(0,max)
        toMove=self.Bonnie
        if chance<theChance:
            advance=random.randint(1,2)
            if toMove.location==8 and self.l_doorState==0: # Bonnies kill logic
                print("Uh oh! Bonnie killed you. GAME OVER")
                self.alive=1

            if advance==1: # Forward progression
                if toMove.location==0: # If on stage, move to dining area
                    toMove.location=toMove.location+1

                elif toMove.location==8: # Makes sure the Animatronic does not leave the play area
                    toMove.location=toMove.location-1

                elif toMove.location % 2 == 0: # If in dining area, or any other odd room, advance 2
                    toMove.location=toMove.location+2
                    if toMove.location==8:
                        self.l_animatronic.append("bonnie")

            elif advance==2: # Backwards progression
                if toMove.location==1 or toMove.location==0:
                    pass

                else:
                    toMove.location=toMove.location-2
                    if "bonnie" in self.l_animatronic:
                        self.l_animatronic.remove("bonnie")
        else:
            pass

    def foxy(self):
        # Camera state checking determines his movements
        if self.cameraState!=10 and self.cameraSuspended==1:
            self.FoxyCount=self.FoxyCount+1
        elif self.cameraState==10:
            self.FoxyCount=0

        if self.FoxyCount>=self.FoxyProceed: # This is his actual proceeding, if the count is equal to the proceed value, he adds to his state
            self.foxyState=self.foxyState+1
            self.FoxyCount=0

        if self.foxyState==4: # If his state is equal to 4, he will move to the West Hallway.
            self.Foxy.location=6

        if self.cameraState==6 or self.FoxyMoveOn==2: # This gives the player a chance to check the camera for him, but if they don't he moves to the office.
            self.Foxy.location=8
            self.FoxyMoveOn=0
        elif self.foxyState==4:
            self.FoxyMoveOn=self.FoxyMoveOn+1

        if self.Foxy.location==8 and self.l_doorState==0: # Kill logic
            print("Uh oh! Foxy killed you. GAME OVER")
            self.alive=1

        elif self.Foxy.location==8 and self.l_doorState==1: # Drain power if the door is closed and he cannot get to the player
            for i in range(3):
                print("**BANG**")
                time.sleep(0.3)
            self.amount=self.amount-self.FoxyPowerLoss
            self.FoxyPowerLoss=self.FoxyPowerLoss+3
            self.foxyState=0
            self.Foxy.location=10

    def animatronicProgression(self, maxAnimatronics=2, chicaConf=None, bonnieConf=None, foxyConf=None, freddyConf=None):
        while self.alive==0:
            if maxAnimatronics<2:
                print("ERROR, game cannot work with less than 2 animatronics")
                exit()
            choose=random.randint(1,maxAnimatronics)
            if choose == 1 and chicaConf is not None:
                chicaConf()
            elif choose == 2 and bonnieConf is not None:
                bonnieConf()
            elif choose == 3 and foxyConf is not None:
                foxyConf()
            elif choose == 4 and freddyConf is not None:
                freddyConf()
            time.sleep(random.randint(1,3))
            
    def r_light(self):
        if self.r_lightState == 0:
            self.r_lightState = 1
            print("Light on!")
            if "chica" in self.r_animatronic or 'freddy' in self.r_animatronic:
                print("Animatronic in door!")
            else:
                print("Clear!")
        else:
            print("Light off!")
            self.r_lightState = 0

    def r_door(self):
        if self.r_doorState==0:
            self.r_doorState=1
            print("Closed the door")
            self.drainState = self.drainState + 1
        else:
            self.r_doorState=0
            print("Opened the door")
            self.drainState = self.drainState - 1 

    def l_light(self):
        if self.l_lightState == 0:
            self.l_lightState = 1
            print("Light on!")
            if "bonnie" in self.l_animatronic:
                print("Animatronic in door!")
            else:
                print("Clear!")
        else:
            print("Light off!")
            self.l_lightState = 0

    def l_door(self):
        if self.l_doorState==0:
            self.l_doorState=1
            print("Closed the door")
            self.drainState = self.drainState + 1
        else:
            self.l_doorState=0
            print("Opened the door")
            self.drainState = self.drainState - 1

    def power(self):
        while self.alive==0:
            # Multipliers
            if self.drainState == 1 and self.powerCount==3:
                chance=random.randint(0,10)
                if chance>=5:
                    self.amount=self.amount-random.randint(1,3)

            elif self.drainState == 2 and self.powerCount==3:
                chance=random.randint(0,10)
                if chance>=5:
                    self.amount=self.amount-random.randint(3,4)

            elif self.drainState == 3 and self.powerCount==3:
                chance=random.randint(0,10)
                if chance>=5:
                    self.amount=self.amount-random.randint(4,5)
            else:
                self.powerCount=self.powerCount+1

            if self.drainState==1:
                self.drainDisplay="[]"
            if self.drainState==2:
                self.drainDisplay="[][]"
            if self.drainState==3:
                self.drainDisplay="[][][]"
            time.sleep(random.randint(1,5))

    def cameraSystem(self):
        self.cameraSuspended=0
        self.cameraState
        roomNums=['0','1','2','3','4','5','6','7','8','9','10']
        while True:
            if self.cameraState == 0:
                room='Stage'
            if self.cameraState == 1:
                room='Dining Room'
            if self.cameraState == 2:
                room='Backstage'
            if self.cameraState == 3:
                room='Bathrooms'
            if self.cameraState == 4:
                room="Storage Closet"
            if self.cameraState == 5:
                room='Kitchen'
            if self.cameraState == 6:
                room='West Hall'
            if self.cameraState == 7:
                room='East Hall'
            if self.cameraState == 8:
                room='West Corner'
            if self.cameraState == 9:
                room='East Corner'
            if self.cameraState == 10:
                room='Pirates Cove'
            if self.Freddy.location == self.cameraState:
                print("Freddy")
            if self.Chica.location == self.cameraState:
                print("Chica")
            if self.Bonnie.location == self.cameraState:
                print("Bonnie")
            if self.Foxy.location == self.cameraState:
                print(f"Foxy ({self.foxyState})")
            print(f"{self.amount}%")
            print("Power Usage:", self.drainDisplay)
            print(self.displayHour,"AM")
            move=input(f"<--A {room}({self.cameraState}) D--> ")
            if move.lower() == 'a':
                if self.cameraState == 0:
                    self.cameraState=10
                else:
                    self.cameraState=self.cameraState-1
            elif move.lower() == 'd':
                if self.cameraState == 10:
                    self.cameraState=0
                else:
                    self.cameraState=self.cameraState+1
            elif move in roomNums:
                self.cameraState=int(move)
            elif move.lower() == ' ':
                self.clear()
                self.cameraSuspended=1
                break

            self.clear()

            moveChance=random.randint(0,50)
            if moveChance>40:
                print("CAMERA OFFLINE")
                self.animatronicProgression()
                time.sleep(random.randint(1,3))

    def controls(self):
                self.time()
                print(f"{self.amount}%")
                print("Power usage:", self.drainDisplay)
                print(self.displayHour, "AM")
                action = input("What action? (h for help) ").lower()
                self.clear()

                if action == 'q':
                    self.l_light()
                elif action == 'l':
                    self.r_door()
                elif action == 'p':
                    self.r_light()
                elif action == 'a':
                    self.l_door()
                elif action == ' ':
                    self.cameraSuspended=1
                    self.cameraSystem()
                elif action == 'h':
                    print("""Q - Left light
A - Left door
P - Right light
L - Right door""")
                elif action == 'debug':
                    print("Chica postion:", self.Chica.location)
                    print("Bonnie position:", self.Bonnie.location)
                    print("Freddy position:", self.Freddy.location)
                    print("Foxy progress:", self.foxyState)
                    print("Actions till next advancment:", self.FoxyCount)
                    print("Camera Suspended:", self.cameraSuspended)

    def save(self):
        data = {
            "continueState": self.continueState
        }
        output='states.json'
        with open(output, 'w') as f:
            json.dump(data, f, indent=4)

    def load(self):
        with open('states.json', 'r') as f:
            data = json.load(f)
        self.continueState=data['continueState']

g=game()
bonnie=g.bonnieMove()
chica=g.chicaMove()
threading.Thread(target=g.animatronicProgression, daemon=True).start()
def main():
    while g.alive==0:
        g.controls()

main()