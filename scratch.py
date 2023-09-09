import pyautogui
import subprocess
import time


print(f"[***] Starting new run ")

input = 3

subprocess.Popen("start chrome /incognito https://portals.veracross.com/aidan/form/general_inquiry", shell=True)    # opens a new incognito Chrome window

time.sleep(5)

for keypress in range(1, input+1):
    pyautogui.press('tab')
    time.sleep(0.5)