import pyautogui
import subprocess
import time
import random
from datetime import datetime

from custom_functions import tab_sleep, tab_rand_sleep, space_rand_sleep, write_rand_sleep, down_rand_sleep, enter_rand_sleep, generate_email, generate_phone, generate_random_date

from names import first_name_list, last_name_list
from hidden import alumni_form_url

run_count = 0
# max_loop = random.choice(range(50,100))
max_loop = 334
rand_run_id = random.choice(range(1,10000))

try:
    while run_count < max_loop:      # run_count starts at 0 and is incremented at the end of this loop
        start_now = datetime.now()
        start_timestamp_str = f'{start_now:%H.%M.%S_%m.%d.%Y}'
        current_date = f'{start_now:%m.%d.%Y}'
        print(f"[***] Starting new ALUMNI run at run_count:{run_count}, max_loop:{max_loop}, rand_run_id:{rand_run_id} [{start_timestamp_str}]")

        # initialize the variables. every time this loop runs they will have different values
        first_name = random.choice(first_name_list)
        last_name = random.choice(last_name_list)
        email = generate_email(first_name, last_name)
        phone = generate_phone()
        history_choice = random.choice(range(1,3))

        print(f"[*] {first_name}, {last_name} - HC:{history_choice} E:{email} P:{phone}")


        time.sleep(5)       # start new incognito Chrome window
        subprocess.Popen(f"start chrome /incognito {alumni_form_url}", shell=True)    # opens a new incognito Chrome window
        time.sleep(5)       # let the site finish loading
        pyautogui.getActiveWindow().maximize()  # maximize Chrome window
        time.sleep(0.5)


        for tab in range(17):   # move cursor to first field
            tab_sleep()

        if history_choice == 1:
            tab_range = 19
            space_rand_sleep()
        elif history_choice == 2:
            tab_range = 18
            down_rand_sleep()
        else:
            print("!*!*!*!  ERROR IN HISTORY CHOICE  !*!*!*!*!")

        print(f"[*] Tab Range = {tab_range}")

        tab_rand_sleep()
        tab_rand_sleep()

        write_rand_sleep(first_name)
        tab_rand_sleep()
        write_rand_sleep(last_name)

        for tab in range(4):
            tab_rand_sleep()

        write_rand_sleep(email)

        tab_rand_sleep()
        tab_rand_sleep()
        write_rand_sleep(phone)

        for tab in range(tab_range):           # 18 for HC 2, 19 for HC 1
            tab_rand_sleep()

        enter_rand_sleep()          # SUBMIT THE FORM

        time.sleep(5)      # wait for the form to submit
        pyautogui.getActiveWindow().close()  # close the Chrome window


        end_now = datetime.now()
        end_timestamp_str = f'{end_now:%H.%M.%S_%m.%d.%Y}'
        print(f"[*] This run: {run_count} has finished at [{end_timestamp_str}]\n\n")

        log = open(f"ALUMNI_BOT_{current_date}_{rand_run_id}.txt", 'a')
        log.write(f"run_count:{run_count}\t Start:[{start_timestamp_str}] - End:[{end_timestamp_str}]\t {first_name}, {last_name} - E:{email}\t P:{phone}\t HC:{history_choice} TR:{tab_range}\t (if HC=1, TR=19. if HC=2, TR=18) - max_loop:{max_loop} id:{rand_run_id}\n\n")
        log.close()
        
        run_count += 1

except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
    print(f"[!] Script exited at run_count: {run_count}")
