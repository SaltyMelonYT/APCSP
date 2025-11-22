import FNAF_InTheTerminalV2 as f
import time
import threading
g=f.game()
def main():
    print("NIGHT THRE, 12:00AM")
    time.sleep(0.9)
    threading.Thread(target=g.power, daemon=True).start()
    threading.Thread(target=g.time, daemon=True).start()
    threading.Thread(target=g.animatronicProgession, daemon=True).start()
    g.clear()
    while g.alive==0:
        g.controls()
    if g.alive==2:
        import night4
        night4.main()
main()