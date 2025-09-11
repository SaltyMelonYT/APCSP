import random
import time

def slowprint(text, duration):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(duration)
    print()
    time.sleep(0.09)


begin=input("Ready to start? y/N ")

if begin.lower() == 'y':
    slowprint("Let the games begin!", 0.02)
    p1=input("What is Player 1's name? ")
    p2=input("What is Player 2's name? ")

while begin.lower() == 'y':
    begin='n'
    slowprint(f"{p1}, press enter to roll your dice.", 0.05)
    input()
    slowprint("Rolling...", 0.09)
    p1Num=random.randint(1,6)
    slowprint(f"{p2}, press enter to roll your dice.", 0.05)
    input()
    slowprint("Rolling...", 0.09)
    p2Num=random.randint(1,6)
    slowprint(f"{p1} rolled a {p1Num}, {p2} rolled a {p2Num}", 0.06)
    if p1Num > p2Num:
        slowprint(f"{p1} wins!", 0.04)
    elif p1Num == p2Num:
        tieBreak=input("Its a tie! Roll again? Y/n ")
        if tieBreak.lower() == 'n':
            slowprint("Okay! Enjoy the tie finish", 0.05)
        else:
            p1Re=random.randint(1,6)
            p2Re=random.randint(1,6)
            slowprint(f"{p1} rolled a {p1Re}, {p2} rolled a {p2Re}", 0.04)
            if p1Re > p2Re:
                slowprint(f"{p1} wins!", 0.04)
            else:
                slowprint(f"{p2} wins!", 0.04)
    else:
        slowprint(f"{p2} wins!", 0.04)
    begin=input("Continue to play? y/N ")