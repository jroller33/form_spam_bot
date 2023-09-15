import pyautogui
import subprocess
import time
import random
from datetime import datetime


from custom_functions import tab_sleep, tab_rand_sleep, space_rand_sleep, write_rand_sleep, down_rand_sleep, enter_rand_sleep, generate_email, generate_phone, generate_relationship, generate_address

from names import first_name_list, last_name_list
from hidden import test_special_url

run_count = 0
# max_loop = random.choice(range(50,100))
max_loop = 1
rand_run_id = random.choice(range(1,10000))

try:
    while run_count < max_loop:      # run_count starts at 0 and is incremented at the end of this loop
        start_now = datetime.now()
        start_timestamp_str = f'{start_now:%H.%M.%S_%m.%d.%Y}'
        current_date = f'{start_now:%m.%d.%Y}'
        print(f"[***] Starting new SPECIAL run at run_count:{run_count}, max_loop:{max_loop}, rand_run_id:{rand_run_id} [{start_timestamp_str}]")

        # initialize the variables. every time this loop runs they will have different values
        first_name = random.choice(first_name_list)
        last_name = random.choice(last_name_list)
        student_name = f"{random.choice(first_name_list)} {random.choice(last_name_list)}"

        email = generate_email(first_name, last_name)
        phone = generate_phone()
        relationship = generate_relationship()

        address = generate_address()
        address1 = address["address1"]
        city = address["city"]
        state = address["state"]
        postal_code = address["postalCode"]

        print(f"[*] {address1}, {city}, {state} {postal_code}")
    
        # history_choice = random.choice(range(1,3))

        print(f"[*] STU:{student_name} PAR:{first_name}, {last_name} - R:{relationship} E:{email} P:{phone}\n")


        time.sleep(5)       # start new incognito Chrome window
        subprocess.Popen(f"start chrome /incognito {test_special_url}", shell=True)    # opens a new incognito Chrome window
        time.sleep(5)       # let the site finish loading
        pyautogui.getActiveWindow().maximize()  # maximize Chrome window
        time.sleep(5)
        pyautogui.press('pageup')
        time.sleep(0.5)

        pyautogui.click(866,606)
        time.sleep(random.uniform(1,6))
        
        def write_rs_tab_rs(string):
            write_rand_sleep(string)
            tab_rand_sleep()
        
# def write_rand_sleep(string):
#     pyautogui.write(string, random.uniform(0.1, 0.6))
#     time.sleep(random.uniform(0.5, 2))

        write_rand_sleep(student_name)
        tab_rand_sleep()
        write_rand_sleep(first_name)
        tab_rand_sleep()
        write_rand_sleep(last_name)
        tab_rand_sleep()
        write_rand_sleep(email)
        tab_rand_sleep()
        write_rand_sleep(phone)
        tab_rand_sleep()
        write_rand_sleep(relationship)
        tab_rand_sleep()
        write_rand_sleep(address1)
        tab_rand_sleep()
        write_rand_sleep(city)
        tab_rand_sleep()
        write_rand_sleep(state)
        tab_rand_sleep()
        write_rand_sleep(postal_code)

        for tab in range(3):
            tab_rand_sleep()
        space_rand_sleep()
        tab_rand_sleep()
        # enter_rand_sleep()  # SUBMIT FORM

        time.sleep(5)      # wait for the form to submit
        pyautogui.getActiveWindow().close()  # close the Chrome window

        end_now = datetime.now()
        end_timestamp_str = f'{end_now:%H.%M.%S_%m.%d.%Y}'
        print(f"[*] This run: {run_count} has finished at [{end_timestamp_str}]\n\n")

        log = open(f"SPECIAL_BOT_{current_date}_{rand_run_id}.txt", 'a')
        log.write(f"run_count:{run_count}\t Start:[{start_timestamp_str}] - End:[{end_timestamp_str}]\t [{first_name}, {last_name}] STU:{student_name} - E:{email}\t P:{phone}\t REL:{relationship}\t [{address}] - max_loop:{max_loop} id:{rand_run_id}\n\n")
        log.close()


        # # initialize the variables. every time this loop runs they will have different values
        # first_name = random.choice(first_name_list)
        # last_name = random.choice(last_name_list)
        # student_name = f"{random.choice(first_name_list)} {random.choice(last_name_list)}"

        # email = generate_email(first_name, last_name)
        # phone = generate_phone()
        # relationship = generate_relationship()

        # address = generate_address()
        # address1 = address["address1"]
        # city = address["city"]
        # state = address["state"]
        # postal_code = address["postalCode"]

        run_count += 1

except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
    print(f"[!] Script exited at run_count: {run_count}")
