import keyboard

def onKeyPressed(event):
    print(event)

keyboard.on_press(onKeyPressed('a'))