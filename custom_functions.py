import pyautogui
import random
import time
from random_address import real_random_address_by_postal_code


def tab_sleep():
    pyautogui.press('tab')
    time.sleep(0.5)     

def space_sleep():
    pyautogui.press('space')
    time.sleep(0.5)

def write_sleep(string):
    pyautogui.write(string, random.uniform(0.1, 1))
    time.sleep(0.5)

def down_sleep():
    pyautogui.press('down')
    time.sleep(0.5)

def enter_sleep():
    pyautogui.press('enter')
    time.sleep(0.5)

# ---------------------------------------

# these functions sleep for a random period of time. This is so the bot will mimic the way humans pause for random periods of time while filling out the form. The goal is for the bot to be indistinguishable from a human user, so it needs to mimic human behavior

def tab_rand_sleep():
    pyautogui.press('tab')
    time.sleep(random.uniform(0.5, 2))

def space_rand_sleep():
    pyautogui.press('space')
    time.sleep(random.uniform(0.5, 2))

def write_rand_sleep(string):
    pyautogui.write(string, random.uniform(0.1, 0.6))
    time.sleep(random.uniform(0.5, 2))

def down_rand_sleep():
    pyautogui.press('down')
    time.sleep(random.uniform(0.5, 2))

def enter_rand_sleep():
    pyautogui.press('enter')
    time.sleep(random.uniform(0.5, 2))

def write_rs_tab_rs(string):    # write_rand_sleep() then tab_rand_sleep()
    write_rand_sleep(string)
    tab_rand_sleep()


# --------------------------------------
email_providers = ["@gmail.com", "@outlook.com", "@yahoo.com", "@protonmail.com", "@aol.com", "@icloud.com"]
def generate_email(first_name, last_name):
    num = str(random.choice(range(1, 99)))
    provider = random.choice(email_providers)
    return f"{first_name}{last_name}{num}{provider}".lower()


area_codes = ["202", "771", "276", "434", "804", "240", "301", "410", "443", "667"]
def generate_phone():
    num = str(random.choice(range(2345678, 8765432)))       # 202-9999999
    area_code = random.choice(area_codes)
    return f"{area_code}{num}"


relatives = ["grandparent", "godparent", "uncle", "aunt", "great uncle", "great aunt"]
def generate_relationship():
    return random.choice(relatives)


zip_codes = ["20001", "20002", "20009", "20010", "20012", "20017", "20018", "20020", "20032", "20036"]
def generate_address():
    zip_code = random.choice(zip_codes)
    address = real_random_address_by_postal_code(zip_code)
    return address


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
