import time

def countdown(a,b=0):
    count=a
    remove=1
    while count!=b:
        print(f"{count}!")
        count=count-remove
        time.sleep(1)
    print("Countdown finished!")

countdown(5)