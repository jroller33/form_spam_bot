import pyautogui
import subprocess
import time
import random
from datetime import datetime
from custom_functions import tab_sleep
from custom_functions import space_sleep
from custom_functions import write_sleep
from custom_functions import down_sleep
from custom_functions import enter_sleep
from custom_functions import generate_email
from custom_functions import generate_phone
from custom_functions import generate_random_date

from names import first_name_list
from names import last_name_list

run_count = 0

while run_count < 100:
    now = datetime.now()
    timestamp_str = f'{now:%m.%d.%Y_%H.%M.%S}'
    current_date = f'{now:%m.%d.%Y}'

    child_first_name = random.choice(first_name_list)
    parent_first_name = random.choice(first_name_list)
    last_name = random.choice(last_name_list)
    gender = random.choice(range(1, 4))
    child_DOB = generate_random_date("child")
    applying_for_year = random.choice(range(1,3))
    applying_for_grade = random.choice(range(1,13))
    relationship = random.choice(range(1, 3))
    email = generate_email(parent_first_name, last_name)
    phone = generate_phone()


    log = open(current_date, 'a')
    log.write(f"[{timestamp_str}]\t C:{child_first_name},{last_name}\t P:{parent_first_name}\t {email}-{phone}\t DOB:{child_DOB} Gender:{gender}\t Y/G:{applying_for_year}-{applying_for_grade} Rel:{relationship}\n\n")

    log.close()
    
    run_count += 1



# subprocess.Popen("start excel", shell=True)    # opens a new excel window, it's good for visualizing keypresses
# time.sleep(5)     
# pyautogui.getActiveWindow().maximize()  # maximize window
# time.sleep(2)

# pyautogui.getActiveWindow().close()  # maximize Chrome window

# tabs = 5
# downs = 2



# for keypress in range(tabs):
#     pyautogui.press('tab')
#     time.sleep(0.5)

# pyautogui.press('space')
# time.sleep(0.5)

# for keypress in range(downs):
#     pyautogui.press('down')
#     time.sleep(0.5)

# pyautogui.press('enter')
# time.sleep(0.5)
# pyautogui.press('tab')
