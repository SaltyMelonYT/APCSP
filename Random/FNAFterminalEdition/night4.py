import fnafInTheTerminal as f
import time
g=f.game()

def main():
    print("NIGHT FOUR, 12:00AM")
    time.sleep(0.9)
    while g.alive==0:
        g.controls()
        bonnie=g.bonnieMove(25,12)
        chica=g.bonnieMove(25,13)
        foxy=g.foxy()
        freddy=g.freddyMove(50, 30)
        g.animatronicProgression(2, chica, bonnie, foxy, freddy)
        if g.alive==3:
            import night5 as n5
            n5.main()
main()