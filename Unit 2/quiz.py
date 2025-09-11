import random
print("Your question is: \nWhat is 2+4?")
print(f"Is it \nA: {random.randrange(1,9)}, B: 6, or C: {random.randrange(1,9)}")
answer = input().lower()
if answer != "b" or answer != "6":
    print("Incorrect!")
else:
    print("Correct!")