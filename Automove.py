import pyautogui as pag
import random
import time

print("Enter the time required for break for screen awake in min : ")

# 22 is multiplying factor
breakTime = int(input()) * 22 

total_seconds = (breakTime*60.0)/22

for i in range(breakTime):

    x = random.randint(400,900)
    y = random.randint(300,800)

    pag.moveTo(x,y,0.5)

    time.sleep(2)

    total_seconds =total_seconds - 2.7
    print("Seconds left : {}".format(total_seconds))


