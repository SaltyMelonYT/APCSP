import time
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import yt_dlp


filename='RockThatBody.wav'
script_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(script_dir, filename)

if os.path.exists(file_path):
    print()
else:
    URL='https://www.youtube.com/watch?v=uVup5khRXOA'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'CreateTask',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav'
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code=ydl.download(URL)
pygame.mixer.init()

audio_file_path='RockThatBody.wav'
pygame.mixer.music.load(audio_file_path)
pygame.mixer.music.play(-1)

duration = random.randrange(0, 1)

def slowprint(text, duration):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(duration)
    print()
time.sleep(15.7)

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
print()
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
print()
time.sleep(0.09)

slowprint("I wanna da-", 0.07)
slowprint("I wanna dance in the lights!", 0.1)
time.sleep(0.2)
slowprint("I wanna roc-", 0.07)
slowprint("I wanna rock your body!", 0.13)
time.sleep(0.2)
slowprint("I wanna go-", 0.07)
slowprint("I wanna go for a ride!", 0.12)
time.sleep(0.2)
slowprint("Hop in the music and rock your body right", 0.09)

print()
slowprint("Rock that body",0.04)
slowprint("come on, come on,", 0.07)
slowprint("rock that body", 0.06)
slowprint("(Rock your body)", 0.05)
slowprint("Rock that body",0.06)
slowprint("come on, come on,", 0.07)
slowprint("rock that body", 0.13)

print()
slowprint("rock that body", 0.08)
slowprint("come on, come on,", 0.07)
slowprint("rock that body", 0.08)
slowprint("(Rock your body)", 0.05)
slowprint("Rock that body",0.06)
slowprint("come on, come on,", 0.07)
slowprint("rock tha-", 0.11)

print()
slowprint("Let me see your body rock,", 0.09)
slowprint("Shakin' it from the bottom to top", 0.08)