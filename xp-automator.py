import keyboard
import mouse
from random import randint
from time import sleep

# import tkinter # to-do: look into this framework

##################################################
# Program to trick Fortnite into granting AFK XP #
##################################################

# Known problems:
# - In command prompt, if the program auto-clicks itself, the visual freezes but not the program (it tells the prompt to select)

switchTime = randint(60, 120) # 1-2 minutes

shouldStop = False
shouldPause = True

def checkPause(event):
    global shouldPause
    shouldPause = not shouldPause

def checkEnd(event):
    global shouldStop
    shouldStop = True

def getInputRange(values):
    length = len(values)
    index = None
    while index is None:
        for i in range(0, length):
            print(f"[{i + 1}] {values[i]}")
        try:
            tryInput = int(input("-> "))
            if(tryInput < 1 or tryInput > length):
                raise

            index = tryInput

        except:
            print(f"--Error--\nPlease type an number between [1-{length}]")
            
    return index


def secondsToClock(time):
    timeLeft = int(time)
    hours =  int(timeLeft / 3600)
    timeLeft %=  3600
    minutes = int(timeLeft / 60)
    timeLeft %= 60

    return f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(timeLeft).zfill(2)}"


# 1: LEGO
# 2: Jam Stage 
print("Select a mode")
mode = getInputRange(["Lego", "Jam Festival"])

print("\nSelect a time")
executions = None
index = getInputRange(["30 minutes", "1 hour", "3 hours (Time till max XP)", "Custom"])
if index == 1:
    executions = 30 * 60
elif index == 2:
    executions = 60 * 60
elif index == 3:
    executions = 3 * 60 * 60
elif index == 4:
    while executions is None:
        print("Enter a time (format: hr min sec, example: 1 30 0)")
        try:
            values = input("-> ").split()
            length = len(values)
            count = 0
            if length > 0:
                count += int(values[0]) * 3600
            if length > 1:
                count += int(values[1]) * 60
            if length > 2:
                count += int(values[2])

            if(count <= 0):
                raise

            executions = count

        except:
            print("--Error--\nInvalid input")


keyboard.on_release_key("p", checkPause)
keyboard.on_release_key("end", checkEnd)

print()
if mode == 1:
    print("Enter a LEGO creative world and place down a launch pad. Begin bouncing on the launchpad")
elif mode == 2:
    print("Enter Jam Festival and begin playing a song")

print("Press the 'p' key to activate the bot")

while shouldPause:
    pass

print("\nStarting\n")
while executions > 0:
    if shouldPause:
        continue
    
    if mode == 1:
        mouse.click()
    elif mode == 2:
        switchTime -= 1
        if switchTime == -1:
            keyboard.press("b")
        elif switchTime == -2:
            keyboard.press_and_release("space")
            keyboard.release("b")
            switchTime = randint(60, 120)

    message = f"Time remaining: {secondsToClock(executions)} (Press the 'p' key to pause or the 'end' key to terminate)"
    if mode == 2:
        message = f"Time until instrument switch: {secondsToClock(switchTime)} | " + message
    print(message, end="\r")

    executions -= 1
    sleep(1)

    if shouldStop:
        print("\n")
        break

keyboard.unhook_all()
