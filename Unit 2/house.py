import time
def slowprint(text, duration):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(duration)
    print()
    # This entire function prints it letter by letter

slowprint("      /\\", 0.05) # Roof
slowprint("     /  \\", 0.05) # Still roof
slowprint("    /    \\", 0.05) # Final bit of roof
slowprint("    |    |", 0.05) # Walls
slowprint("    |_#[]|", 0.05) # This is my window and door