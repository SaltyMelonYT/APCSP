import fnafInTheTerminal as f
import time
import night5 as n5
g=f.game()

def main():
    print("NIGHT FOUR, 12:00AM")
    time.sleep(0.9)
    while g.alive==0:
        g.controls()
        bonnie=g.bonnieMove(20,10)
        chica=g.bonnieMove(20,10)
        foxy=g.foxy()
        freddy=g.freddyMove(20, 10)
        g.animatronicProgression(2, chica, bonnie, foxy, freddy)
        if g.alive==3:
            print("Congradulations...")
            print("You.... won....")
main()