import random
import threading
import time
import os
import json

class animatronic():
    def __init__(self,name,location=0):
        self.name=name
        self.location=location

class game():
    def __init__(self):
        # MAIN GAME
        self.alive=0
        self.night=1
        self.continueState=1

        # Define Animatronics
        self.Chica=animatronic("Chica")
        self.Bonnie=animatronic("Bonnie")
        self.Foxy=animatronic("Foxy",10)
        self.Freddy=animatronic("Freddy")

        #OFFICE LOGIC
        self.r_doorState=0 # Open
        self.r_doorWay=[]
        self.r_lightState=0 # off
        self.l_doorState=0 # Open
        self.l_doorWay=[]
        self.l_lightState=0 # off
        
        # POWER FUNCTIONS
        self.powerDraw=1
        self.powerAmount=100
        self.displayPower=100

        # TIME FUNCTIONS
        self.startTime=0
        self.currentTime=0
        self.elapsed=0
        self.displayHour=12

        # FREDDY LOGIC
        self.freddyAdvance=0

        # CAMERA LOGIC
        self.cameraView=0 # The camera position
        self.cameraState=0 # Unviewed, 1 is viewing

        # FOXY LOGIC
        self.foxyProgress=0
        self.foxyState=0
        self.foxyMoveOn=0
        self.foxyDrain=1

    def load(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(script_dir, "states.json")

        try:
            with open(save_path, 'r') as f:
                data = json.load(f)
            self.continueState = data.get("continueState")
        except FileNotFoundError:
            self.continueState = 1

    def save(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output = os.path.join(script_dir, "states.json")

        data = {"continueState": self.continueState}

        with open(output, 'w') as f:
            json.dump(data, f, indent=4)

    nightConf = {
    1: {"chica": (100,50), "bonnie": (100,50), "foxy": (100, 90), "freddy": (0,0), "max": 3},
    2: {"chica": (75,50), "bonnie": (80,50), "foxy": (80,69), "freddy": (0,0), "max": 3},
    3: {"chica": (70,54), "bonnie": (60,30), "foxy": (75,40), "freddy": (55,28), "max": 4},
    4: {"chica": (65, 43), "bonnie":(50, 25), "foxy": (50, 40), "freddy": (50, 30), "max": 4},
    5: {"chica": (40, 10), "bonnie":(30, 15), "foxy": (35, 14), "freddy": (17, 7), "max": 4}
    }

    def r_door(self):
        if self.r_doorState==0:
            self.r_doorState=1
            print("Closed the door")
            self.powerDraw = self.powerDraw + 1
        else:
            self.r_doorState=0
            print("Opened the door")
            self.powerDraw = self.powerDraw - 1

    def l_light(self):
        if self.r_lightState==1: # Turn off opposite light
            self.r_lightState=0
            self.powerDraw-=1

        if self.l_lightState==0:
            self.l_lightState=1
            self.powerDraw+=1
            print("Right light on")
            if 'bonnie' in self.l_doorWay:
                print("ANIMATRONIC IN DOOR")
            else:
                print("Clear!")
        else:
            self.l_lightState=0
            self.powerDraw-=1
            print("Right light off")

    def l_door(self):
        if self.l_doorState==0:
            self.l_doorState=1
            print("Closed the door")
            self.powerDraw = self.powerDraw + 1
        else:
            self.l_doorState=0
            print("Opened the door")
            self.powerDraw = self.powerDraw - 1

    def r_light(self):
        if self.l_lightState==1: # Turn off opposite light
            self.l_lightState=0
            self.powerDraw-=1

        if self.r_lightState==0:
            self.r_lightState=1
            self.powerDraw+=1
            print("Left light on")
            if 'chica' in self.r_doorWay or 'freddy' in self.r_doorWay:
                print("ANIMATRONIC IN DOOR")
            else:
                print("Clear!")
        else:
            self.r_lightState=0
            self.powerDraw-=1
            print("Left light off")
        
    def power(self): # Threaded process
        while self.alive==0:
            if self.powerDraw==1:
                self.powerAmount-=0.1
            elif self.powerDraw==2:
                self.powerAmount-=0.2
            elif self.powerDraw==3:
                self.powerAmount-=0.3
            elif self.powerDraw==5:
                self.powerAmount-=0.4
            self.displayPower=round(self.powerAmount)
            time.sleep(1)

    def powerDisplay(self):
        if self.powerDraw==1:
            print("[]")
        if self.powerDraw==2:
            print("[][]")
        if self.powerDraw==3:
            print("[][][]")
        if self.powerDraw==4:
            print("[][][][]")

    def time(self): # Threaded process
        while self.alive==0:
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
                self.continueState+=1
                self.save()
                break
    
    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def bonnieMove(self,activity,risk):
        chances=random.randint(0,activity)
        if chances>risk:
            advance=random.randint(1,2)
            #Full forward progression
            if advance==1:
                if self.Bonnie.location==8 and self.l_doorState==0: # Death logic
                    print("UH OH! Bonnie killed you. GAME OVER")
                    self.alive=1
                elif self.Bonnie.location==0 or self.Bonnie.location==1: # IF he's on the stage, move to dining room.
                    self.Bonnie.location+=1
                else: # IF he's anywhere else, move forward
                    if self.Bonnie.location==8: # Prevents him from leaving the pizzeria area
                        self.Bonnie.location-=2
                    else:
                        self.Bonnie.location+=2 # Forward progression
                        if self.Bonnie.location==8:
                            self.l_doorWay.append('bonnie')

            # Full backwards progression
            else:
                if self.Bonnie.location==1 or self.Bonnie.location==0: # He will not go back to the stage, or leave the game area
                    pass
                elif self.Bonnie.location==2:
                    self.Bonnie.location-=1
                else:
                    self.Bonnie.location-=2
                    if 'bonnie' in self.l_doorWay:
                        self.l_doorWay.remove('bonnie')
        else:
            pass

    def chicaMove(self,activity,risk):
        chances=random.randint(0,activity)
        if chances>risk:
            advance=random.randint(1,2)
            # Full forward progression
            if advance==1:
                if self.Chica.location==9 and self.r_doorState==0: # Death logic
                    print("UH OH! Chica killed you. GAME OVER")
                    self.alive=1
                elif self.Chica.location==0: # IF she's on the stage move her to the dining area
                    self.Chica.location+=1
                else: # IF anywhere else move her forward
                    if self.Chica.location==9:
                        self.Chica.location-=2 # Prevents her from leaving the pizzeria through forward progression
                    else:
                        self.Chica.location+=2
                        if self.Chica.location==9:
                            self.r_doorWay.append('chica')

            # Full backwards progression
            else:
                if self.Chica.location==0 or self.Chica.location==1:
                    pass
                else:
                    self.Chica.location-=2
                    if 'chica' in self.r_doorWay:
                        self.r_doorWay.remove('chica')

    def freddyMove(self,activity,risk):
        chances=random.randint(0,activity)
        if activity==0 and risk==0:
            pass
        else:
            if chances>risk and self.freddyAdvance==3:
                if self.Freddy.location==0 or self.Freddy.location==1:
                    self.Freddy.location+=1
                else:
                    if self.Freddy.location==9 and self.l_doorState==0:
                        print("UH OH! Freddy killed you. GAME OVER")
                    else:
                        self.Freddy.location+=2
                        if self.Freddy.location==9:
                            self.r_doorWay.append()
            else:
                self.freddyAdvance+=1

            if self.cameraState==1:
                self.freddyAdvance=0

    def foxyAttack(self): # This is supposed to be a threaded process. The player has 3 seconds to close the door
        time.sleep(3)
        if self.r_doorState==0:
            print("UH OH! Foxy killed you. GAME OVER")
            self.alive=1
        else:
            for i in range(3):
                print("**BANG**")
                time.sleep(0.4)
                self.powerAmount=self.powerAmount-self.foxyDrain
            self.Foxy.location=10
            self.foxyMoveOn=0
            self.foxyState=0
            self.foxyProgress=0
                
    def foxy(self, difficulty,risk):
        if self.foxyProgress==difficulty:
            self.foxyState+=1

        if self.foxyState==4:
            self.Foxy.location=6

        if self.Foxy.location==6 and self.foxyMoveOn==risk:
            print("Foxy is coming....")
            threading.Thread(target=self.foxyAttack).start()

    def animatronicProgession(self, night=1): # Threaded process
        settings = self.nightConf[night]
        max=settings.get("max",4)

        while self.alive == 0:
            # Randomly pick which animatronic moves
            choice = random.randint(1, max)
            
            if choice == 1:
                self.chicaMove(*settings["chica"])
            elif choice == 2:
                self.bonnieMove(*settings["bonnie"])
            elif choice == 3:
                self.foxy(*settings["foxy"])
            elif choice == 4:
                self.freddyMove(*settings["freddy"])
            time.sleep(random.randint(1,3))

    def cameraSystem(self):
        self.cameraState=1
        self.powerDraw+=1
        if self.l_lightState==1:
            self.l_lightState=0
            self.powerDraw-=1
        if self.r_lightState==1:
            self.r_lightState=0
            self.powerDraw-=1
        roomNums=['0','1','2','3','4','5','6','7','8','9','10']
        while True:
            if self.cameraView == 0:
                room='Stage'
            if self.cameraView == 1:
                room='Dining Room'
            if self.cameraView == 2:
                room='Backstage'
            if self.cameraView == 3:
                room='Bathrooms'
            if self.cameraView == 4:
                room="Storage Closet"
            if self.cameraView == 5:
                room='Kitchen'
            if self.cameraView == 6:
                room='West Hall'
            if self.cameraView == 7:
                room='East Hall'
            if self.cameraView == 8:
                room='West Corner'
            if self.cameraView == 9:
                room='East Corner'
            if self.cameraView == 10:
                room='Pirates Cove'
            self.clear()
            if self.Chica.location==self.cameraView:
                print("Chica")
            if self.Bonnie.location==self.cameraView:
                print("Bonnie")
            if self.Freddy.location==self.cameraView:
                print("Freddy")
            if self.Foxy.location==self.cameraView:
                print(f"Foxy({self.foxyState})")
            print(f"{self.displayPower}%")
            print(f"{self.displayHour}:00 AM")
            self.powerDisplay()
            print(f"A <-- {room}({self.cameraView}) --> D")
            change=input().lower()
            if change=='a':
                if self.cameraView==0:
                    self.cameraView=10
                else:
                    self.cameraView-=1
            elif change=='d':
                if self.cameraView==10:
                    self.cameraView=0
                else:
                    self.cameraView+=1
            elif change in roomNums:
                self.cameraView=int(change)
            elif change==' ':
                self.cameraState=0
                self.powerDraw-=1
                self.clear()
                break

    def controls(self):
        print(f"{self.displayPower}%")
        print(self.displayHour,"AM")
        self.powerDisplay()
        move=input("What is your action? (type h for help) ").lower()
        self.clear()
        if move=='q':
            self.l_light()
        elif move=='a':
            self.l_door()
        elif move=='p':
            self.r_light()
        elif move=='l':
            self.r_door()
        elif move==' ':
            self.cameraSystem()
        elif move=='debug':
            print(self.foxyProgress)
            print(self.foxyState)
            print(self.foxyMoveOn)
        elif move=='':
            if self.l_lightState==1:
                self.l_lightState=0
                self.powerDraw-=1
            elif self.r_lightState==1:
                self.r_lightState=0
                self.powerDraw-=1

#g=game()
#def main():
#    threading.Thread(target=g.power, daemon=True).start()
#    threading.Thread(target=g.time, daemon=True).start()
#    threading.Thread(target=g.animatronicProgession, daemon=True).start()
#    g.clear()
#    while g.alive==0:
#        g.controls()
#main()
            