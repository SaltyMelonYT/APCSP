import random
attempts=0
play=input("Would you like to play? y/N ")
num=random.randint(1,20)
print(num)
while play.lower() == 'y':
    guess=int(input("What is your guess? "))
    if guess > 20 or guess < 1:
        print("please enter a valid number of 1-20")
    elif guess != num:
        attempts+=1
        print("Wrong! Try again.")
        print(attempts)
    else:
        print("Correct! You win!")
        print(f"You attempted {attempts} times!")
        play=input("Play again? y/N ")
        num=random.randint
        attempts=0