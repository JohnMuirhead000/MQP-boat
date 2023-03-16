import time
import keyboard

timer = 0

while timer < 30:
    time.sleep(0.1)
    timer += 0.1
    keyboard.press('a')