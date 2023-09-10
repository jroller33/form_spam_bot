import pyautogui
import random
import time


def tab_sleep():
    pyautogui.press('tab')
    time.sleep(0.5)     

def space_sleep():
    pyautogui.press('space')
    time.sleep(0.5)

def write_sleep(string):
    pyautogui.write(string)
    time.sleep(0.5)

def down_sleep():
    pyautogui.press('down')
    time.sleep(0.5)

def enter_sleep():
    pyautogui.press('enter')
    time.sleep(0.5)
    
def generate_email(first_name, last_name):
    num = str(random.choice(range(1, 99)))
    return f"{first_name}{last_name}{num}@gmail.com"

def generate_random_date(input):
    random_month = str(random.choice(range(1, 13)))
    random_day = str(random.choice(range(1, 29)))

    # validate input passed to the function. This decides the range for the random year
    if input == "child":
        random_year = str(random.choice(range(2013, 2019)))
    elif input == "parent":
        random_year = str(random.choice(range(1970, 1990)))
    else:
        print(f"[!] ERROR in generate_random_date() input")

    # if the day or month is only one digit, add a 0 in front of it (all random days and months need to be 2 digits)
    if len(random_day) == 1:
        random_day = f"0{random_day}"
    if len(random_month) == 1:
        random_month = f"0{random_month}"

    return f"{random_month}{random_day}{random_year}"    # MMDDYYYY
