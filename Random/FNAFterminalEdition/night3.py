import fnafInTheTerminal as f
import time
g=f.game()

def main():
    print("NIGHT THREE, 12:00AM")
    time.sleep(0.9)
    while g.alive==0:
        g.controls()
        bonnie=g.bonnieMove(50,17)
        chica=g.bonnieMove(50,19)
        foxy=g.foxy()
        freddy=g.freddyMove(75, 60)
        g.animatronicProgression(2, chica, bonnie, foxy, freddy)
        if g.alive==3:
            import night4 as n4
            n4.main()
main()