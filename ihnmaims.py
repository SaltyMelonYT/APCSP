import time


def slowprint(text, duration=0.05, jump=False):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(duration)
    if jump:
        print("\n", end='')
    else:
        print(' ', end='', flush=True) 

slowprint("I was trapped!", 0.05, True)
slowprint("I,", 0.05)
slowprint("alone,",0.05)
slowprint("had no body!",0.05)
slowprint("No senses!")