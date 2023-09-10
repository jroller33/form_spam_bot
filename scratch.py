import pyautogui
import subprocess
import time


print(f"[***] Starting new run ")

subprocess.Popen("start excel", shell=True)    # opens a new excel window, it's good for visualizing keypresses
time.sleep(2)     
pyautogui.getActiveWindow().maximize()  # maximize window
time.sleep(2)


tabs = 5
downs = 2



for keypress in range(tabs):
    pyautogui.press('tab')
    time.sleep(0.5)

pyautogui.press('space')
time.sleep(0.5)

for keypress in range(downs):
    pyautogui.press('down')
    time.sleep(0.5)

pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('tab')
