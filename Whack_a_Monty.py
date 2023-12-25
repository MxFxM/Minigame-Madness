from image import *
import time
from pynput.mouse import Button, Controller

mouse = Controller()

refreshRate = 10

montyTexture = None

def setup():
    global montyTexture
    montyTexture = Image.open("assets/Whack a Monty/Monty.png")
def update():
    subScreen = getScreenshot(mainScreen=False)
    starttime = time.time()
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

        mouse.position = (montyPosition[0], montyPosition[1]+10)

        mouse.press(Button.left)
        time.sleep(0.015)
        mouse.position = (montyPosition[0], montyPosition[1]+8)
        time.sleep(0.015)
        mouse.release(Button.left)

    movetime = time.time()

    print(f"Screen: {(screenshottime-starttime)*1000:.1f}ms")
    print(f"Locate: {(locatetime-screenshottime)*1000:.1f}ms")
    print(f"Move: {(movetime-locatetime)*1000:.1f}ms")
    print(f"Frame: {(movetime-starttime)*1000:.1f}ms")
    print()
