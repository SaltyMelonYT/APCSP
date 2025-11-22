import FNAF_InTheTerminalV2 as f
import time
import threading
g=f.game()
def main():
    print("FIVE NIGHTS AT FREDDYS")
    time.sleep(0.6)
    print("TERMINAL EDITION")
    time.sleep(1)
    print("NIGHT ONE, 12:00AM")
    time.sleep(0.9)
    threading.Thread(target=g.power, daemon=True).start()
    threading.Thread(target=g.time, daemon=True).start()
    threading.Thread(target=g.animatronicProgession, daemon=True).start()
    g.clear()
    while g.alive==0:
        g.controls()
        g.clear()
    if g.alive==2:
        g.continueState=2
        g.save()
        import night2
        night2.main()
main()