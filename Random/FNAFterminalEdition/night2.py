import fnafInTheTerminal as f
import time
g=f.game()

def main():
    print("NIGHT TWO, 12:00AM")
    time.sleep(0.9)
    while g.alive==0:
        g.controls()
        bonnie=g.bonnieMove(75,50)
        chica=g.bonnieMove(75,50)
        foxy=g.foxy()
        g.animatronicProgression(2, chica, bonnie, foxy)
        if g.alive==3:
            import night3 as n3
            n3.main()
main()