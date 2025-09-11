# 2.9
import random
attempts=0
play=input("Would you like to play? y/N ")
num=random.randint(1,20)
while play.lower() == 'y':
    guess=int(input("What is your guess? "))
    if guess > 20 or guess < 1:
        print("please enter a valid number of 1-20")
    elif guess != num:
        attempts=attempts+1
        print("Wrong! Try again.")
    else:
        print("Correct! You win!")
        print(f"You attempted {attempts+1} times!")
        play=input("Play again? y/N ")
        num=random.randint
        attempts=0