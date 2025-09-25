import random
import time
import math

def slowprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.2)
    print

def genNum(a,b,c,d):
    slowprint(f"{random.randint(a,b)+random.randint(c,d)}")
genNum(1, 10, 0, 40)

print(random.randint(-1, 0))