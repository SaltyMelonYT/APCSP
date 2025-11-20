import fnafInTheTerminal as f
import time
g=f.game()

def main():
    print("FIVE NIGHTS AT FREDDYS")
    time.sleep(0.6)
    print("TERMINAL EDITION")
    time.sleep(1)
    print("NIGHT ONE, 12:00AM")
    time.sleep(0.9)
    while g.alive==0:
        g.controls()
        bonnie=g.bonnieMove(100,50)
        chica=g.bonnieMove(100,75)
        foxy=g.foxy()
        g.animatronicProgression(2, chica, bonnie, foxy)
        if g.alive==2:
            import night2 as n2
            n2.main()
main()