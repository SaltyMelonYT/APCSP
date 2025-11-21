import os
import FNAF_InTheTerminalV2
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
output = os.path.join(script_dir, "states.json")

if not os.path.exists(output):
    data = {"continueState": 1}
    with open(output, 'w') as f:
        json.dump(data, f, indent=4)

nums=["1","2",'3']
def main():
    g=FNAF_InTheTerminalV2.game()
    g.clear()
    g.load()
    print("Welcome to FNAF: In The Terminal")
    print("1.) New game (Night 1)")
    print(f"2.) Continue (Night {g.continueState})")
    print("3.) Exit")
    while True:
        game=input("What do you choose? ")
        if game not in nums:
            print("Invalid response type")
        else:
            game=int(game)
        if game == 1:
            g.clear()
            import night1
            night1.main()
        elif game == 2:
            if g.continueState==1:
                import night1
                night1.main()
            elif g.continueState==2:
                import night2
                night2.main()
            elif g.continueState==3:
                import night3
                night3.main()
            elif g.continueState==4:
                import night4
                night4.main()
            elif g.continueState==5:
                import night5
                night5.main()
        elif game == 3:
            exit()
        else:
            print("Not a valid response")

main()