import os
import fnafInTheTerminal
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


nums=["1","2",'3']
def main():
    g=fnafInTheTerminal.game()
    fnafInTheTerminal.game.load
    clear()
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
            clear()
            import night1
            night1.main()
            break
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