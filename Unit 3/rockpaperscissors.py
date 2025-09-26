#def fight(p1,p2):
#    life1=3
#    life2=3
#    pick1=int(input("Player 1: Rock(1), paper(2), scissors(3) "))
#    pick2=int(input("Player 2: Rock(1), paper(2), scissors(3) "))
#    if pick1 == 1 and pick2 == 2:
#        print(f"{p2} beats {p1} with Paper")
#        life1=life1-1
#    elif pick2 == 1 and pick1 == 2:
#        print(f"{p1} beats {p2} with Paper")
#        life2=life2-1

#fight("Jonathan", "Walid")
import getpass
options=["Rock","Paper","Scissors"]

def fight(p1,p2):
    p1life=3
    p2life=3
    while True: 
        p1pick=int(getpass.getpass(f"{p1} Rock(1), paper(2), scissors(3) "))
        p2pick=int(getpass.getpass(f"{p2} Rock(1), paper(2), scissors(3) "))
        
        if p1pick==1 and p2pick==2:
            print(p2,"wins!")
            p1life=p1life-1
        elif p1pick==2 and p2pick==1:
            print(p1,"wins!")
            p2life=p2life-1

        if p1pick==2 and p2pick==3:
            print(p2,"wins!")
            p1life=p1life-1
        elif p1pick==3 and p2pick==2:
            print(p1,"wins!")
            p2life=p2life-1

        if p1pick==3 and p2pick==1:
            print(p2,"Wins!")
            p1life=p1life-1
        elif p1pick==1 and p2pick==3:
            print(p1,"wins!")
            p2life=p2life-1

        if p1pick==p2pick:
            print("T'was a tie!")

        print(f"{p1} lives: {p1life}\n{p2} lives: {p2life}")
        if p1life == 0 or p2life == 0:
            if p1life > p2life:
                print(f"{p1} is the champion!")
            else:
                print(f"{p2} is the champion!")
            break
fight("Walid","Jonathan")