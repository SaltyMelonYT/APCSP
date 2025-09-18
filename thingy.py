import time
import random
import pygame

pygame.mixer.init()


audio_file_path="/home/jonathan/Music/Rock That Body [oBm0DJx9g8A].wav"
pygame.mixer.music.load(audio_file_path)
pygame.mixer.music.play(-1)

duration = random.randrange(0, 1)

def slowprint(text, duration):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(duration)
    print()


slowprint("This amazing script is brought to you", 0.1)
slowprint("Yours truely", 0.1)
slowprint("Please sit back", 0.1)
slowprint("And enjoy", 0.1)
slowprint("The ride", 0.1)
slowprint("\n #################################", 0.67)

slowprint("I wanna rock right now", 0.05)
time.sleep(0.09)

slowprint("I wanna,", 0.06)
time.sleep(0.07)

slowprint("I wanna rock right now.", 0.05)
time.sleep(0.09)

slowprint("I wanna,", 0.05)
time.sleep(0.07)

slowprint("I wanna rock right now,", 0.07)
time.sleep(0.15)

slowprint("Now", 0.07)
time.sleep(0.14)

slowprint("Now", 0.07)
time.sleep(0.14)

slowprint("Rock right now", 0.06)
time.sleep(0.16)

slowprint("I wanna,", 0.06)
time.sleep(0.07)

slowprint("I wanna rock right now.", 0.05)
time.sleep(0.09)

slowprint("I wanna,", 0.05)
time.sleep(0.07)

slowprint("I wanna rock right now,", 0.07)
time.sleep(0.09)

slowprint("I wanna,", 0.05)
time.sleep(0.07)

slowprint("I wanna rock-", 0.07)
time.sleep(0.09)
slowprint("...", 1)
time.sleep(0.09)

slowprint("I wanna da-", 0.07)
slowprint("I wanna dance in the lights!", 0.1)
time.sleep(0.2)
slowprint("I wanna roc-", 0.07)
slowprint("I wanna rock your body!", 0.13)
time.sleep(0.2)
slowprint("I wanna go-", 0.07)
slowprint("I wanna go for a ride!", 0.12)