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

from random_address import real_random_address

from random_address import real_random_address_by_postal_code


from names import first_name_list
from names import last_name_list


rand_run_id = random.choice(range(1,1000))

run_count = 0

zip_codes = ["20001", "20002", "20009", "20010", "20012", "20017", "20018", "20020", "20032", "20036"]

while run_count < 20:
    zip_code = random.choice(zip_codes)
    address = real_random_address_by_postal_code(zip_code)
    address1 = address["address1"]
    city = address["city"]
    state = address["state"]
    postal_code = address["postalCode"]

    print(f"{address1}, {city}, {state} {postal_code}")
    print("\n")

    run_count += 1
# for x in range(500):
#     history_choice = random.choice(range(1,3))
    
#     if history_choice == 1:
#         print("***** HC = 1 *****")

#     elif history_choice == 2:
#         print("***** HC = 2 *****")

#     else:
#         print("!*!*!*!  ERROR IN HISTORY CHOICE  !*!*!*!*!")

    # now = datetime.now()
    # timestamp_str = f'{now:%m.%d.%Y_%H.%M.%S}'
    # current_date = f'{now:%m.%d.%Y}'

    # first_name = random.choice(first_name_list)
    # last_name = random.choice(last_name_list)
    # email = generate_email(first_name, last_name)
    # phone = generate_phone()
    # history_choice = random.choice(range(1,3)) 
    
    # if history_choice == 1:
    #     tab_range = 19
    # elif history_choice == 2:
    #     tab_range = 18
    # else:
    #     print("!*!*!*!  ERROR IN HISTORY CHOICE  !*!*!*!*!")


    # log = open(f"ALUMNI_BOT_{current_date}_{rand_run_id}.txt", 'a')
    # log.write(f"[{timestamp_str}]\t {first_name}, {last_name} - E:{email}\t P:{phone}\t HC:{history_choice} TR:{tab_range}\t (if HC=1, TR=19. if HC=2, TR=18)\n\n")

    # log.close()
    



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
