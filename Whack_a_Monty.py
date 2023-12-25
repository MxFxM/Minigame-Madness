from image import *
import time
from pynput.mouse import Button, Controller
from threading import Thread
from random import randint

mouse = Controller()

refreshRate = 10

montyTexture = None

screen = None
subScreen = None
screen_updated_flag = False

def setup():
    global montyTexture
    montyTexture = Image.open("assets/Whack a Monty/Monty.png")
    sc = Thread(target=captureScreen, daemon=True)
    sc.start()
def update():
    global screen
    global subScreen
    global screen_updated_flag
    starttime = time.time()
    if screen_updated_flag:
        subScreen = screen.copy()
        screen_updated_flag = False
    screenshottime = time.time()

    locatedMontyBounds = None
    try:
        locatedMontyBounds = pyautogui.locate(montyTexture, subScreen, confidence=0.85)
    except Exception as _:
        pass
    locatetime = time.time()

    # If a monty is located, then click on it.
    if locatedMontyBounds is not None:
        boundCenter = pyautogui.center(locatedMontyBounds)
        montyPosition = localToGlobalPosition(boundCenter, mainScreen=False)

        time.sleep(0.015)
        mouse.position = (montyPosition[0], montyPosition[1]+8)
        mouse.press(Button.left)
        time.sleep(0.015)
        mouse.position = (montyPosition[0]+randint(-2,2), montyPosition[1]+randint(-2,2))
        time.sleep(0.015)
        mouse.release(Button.left)

    movetime = time.time()

    print(f"Screen: {(screenshottime-starttime)*1000:.1f}ms")
    print(f"Locate: {(locatetime-screenshottime)*1000:.1f}ms")
    print(f"Move: {(movetime-locatetime)*1000:.1f}ms")
    print(f"Frame: {(movetime-starttime)*1000:.1f}ms")
    print()
def captureScreen():
    global screen
    global screen_updated_flag

    while True:
        screen = getScreenshot(mainScreen=False)
        screen_updated_flag = True