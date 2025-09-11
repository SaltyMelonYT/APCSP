import time

def slowprint(text, duration, pause=False):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(duration)
        if pause == True and char == ',':
            time.sleep(duration+0.1)
    print()

lastName=input("What is your last name? ")
mom=input("What is your moms first name? ")
dad=input("What is your dads first name? ")
brother=input("What is your brothers name? ")

slowprint(f"{mom} {lastName}, {dad} {lastName}, {brother} {lastName}", 0.05, pause=True)