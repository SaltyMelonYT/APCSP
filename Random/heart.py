import time

def bpm():
    length=30
    print("Hello! Welcome to BPM counter")
    time.sleep(1)
    print("To use this, place your index and middle finger to a spot on your neck")
    time.sleep(1)
    print("When you feel a small bump, thats your pulse!")
    time.sleep(1)
    print("When you feel your pulse and are ready to begin, press enter!")
    begin=input()

    while True:
        if begin=='':
            while length!=0:
                print(length)
                length=length-1
                time.sleep(1)
            break
        else:
            print("No worries! Just press enter when you're ready")
            
    print("Great! Now that you've counted your BPM for 30 seconds, enter it now!")
    totalBpm=int(input())*2
    print("Your total BPM was:", totalBpm)

bpm()