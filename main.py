from pyautogui import press
from pyautogui import FAILSAFE
from time import sleep
from random import uniform

FAILSAFE = True

while True:
    press('capslock')
    sleep(uniform(0.001, 0.005))
