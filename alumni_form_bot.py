import pyautogui
import subprocess
import time
import random
from datetime import datetime

from custom_functions import tab_sleep, tab_rand_sleep, space_rand_sleep, write_rand_sleep, down_rand_sleep, enter_rand_sleep
from custom_functions import generate_email, generate_phone, generate_random_date

from names import first_name_list, last_name_list
from hidden import alumni_form_url

run_count = 0

try:
    while run_count < 1:      # run_count starts at 0 and goes up to 99

        print(f"[***] Starting new ALUMNI run at run_count: {run_count}")

        now = datetime.now()
        timestamp_str = f'{now:%m.%d.%Y_%H.%M.%S}'
        current_date = f'{now:%m.%d.%Y}'

        # initialize the variables. every time this loop runs they will have different values
        first_name = random.choice(first_name_list)
        last_name = random.choice(last_name_list)
        email = generate_email(first_name, last_name)
        phone = generate_phone()

        history_choice = random.choice(range(2))
        neg_history_choice = (1 - history_choice)

        print(f"[*] {first_name},{last_name} {email} {phone}")


        time.sleep(5)       # start new incognito Chrome window
        subprocess.Popen(f"start chrome /incognito {alumni_form_url}", shell=True)    # opens a new incognito Chrome window
        time.sleep(5)       # let the site finish loading
        pyautogui.getActiveWindow().maximize()  # maximize Chrome window
        time.sleep(0.5)     

        for tab in range(17):
            tab_sleep()

        for choice in range(history_choice):
            tab_rand_sleep()
        space_rand_sleep()

        tab_rand_sleep()
        tab_rand_sleep()

        write_rand_sleep(first_name)
        tab_rand_sleep()
        write_rand_sleep(last_name)

        for tab in range(4):
            tab_rand_sleep()

        write_rand_sleep(email)

        for tab in range(21):
            tab_rand_sleep()        

        enter_rand_sleep()          # SUBMIT
        time.sleep(random.uniform(2, 7))

        # write_rand_sleep(email)

        # tab_rand_sleep()
        # write_rand_sleep(full_name)

        # tab_rand_sleep()
        # write_rand_sleep(phone)

        # tab_rand_sleep()
        # space_rand_sleep()

        # for tab in range(5):
        #     tab_rand_sleep()

        # for choice in range(event_choice):
        #     tab_rand_sleep()
        # space_rand_sleep()

        # for tab in range(neg_event_choice):
        #     tab_rand_sleep()
        # space_rand_sleep()   # selects first selection of 'Committees' (PA Leadership)

        # Evening of the arts worked








        # time.sleep(10)      # wait for the form to submit
        # pyautogui.getActiveWindow().close()  # close the Chrome window

        print(f"[*] This run: {run_count} has finished.\n\n\n")
        run_count += 1

except KeyboardInterrupt:
    print(f"[!] Script exited at run_count: {run_count}")
