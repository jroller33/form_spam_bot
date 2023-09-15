import pyautogui
import subprocess
import time
import random
from datetime import datetime


from custom_functions import tab_sleep, tab_rand_sleep, space_rand_sleep, write_rand_sleep, down_rand_sleep, enter_rand_sleep, write_rs_tab_rs, for_tab_sleep_range, generate_email, generate_phone, generate_relationship, generate_address

from names import first_name_list, last_name_list
from hidden import special_url

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
    
        print(f"[*] STU:{student_name} PAR:{first_name}, {last_name} - R:{relationship} E:{email} P:{phone}\n[{address1}, {city}, {state} {postal_code}]\n")


        time.sleep(1)       # start new incognito Chrome window
        subprocess.Popen(f"start chrome /incognito {special_url}", shell=True)    # opens a new incognito Chrome window
        time.sleep(10)       # let the site finish loading
        pyautogui.getActiveWindow().maximize()  # maximize Chrome window
        time.sleep(5)
        pyautogui.press('pageup')
        time.sleep(0.5)

        pyautogui.moveTo(866, 606, duration=0.5)
        pyautogui.click(866,606)
        time.sleep(random.uniform(1,4))
        
        write_rs_tab_rs(student_name)
        write_rs_tab_rs(first_name)
        write_rs_tab_rs(last_name)
        write_rs_tab_rs(email)
        write_rs_tab_rs(phone)
        write_rs_tab_rs(relationship)
        write_rs_tab_rs(address1)
        write_rs_tab_rs(city)
        write_rs_tab_rs(state)
        write_rs_tab_rs(postal_code)

        for_tab_sleep_range(2)

        space_rand_sleep()

        pyautogui.press('pagedown')
        pyautogui.press('pagedown')
        
        pyautogui.moveTo(645,391, duration=1)     # SUBMIT FORM
        pyautogui.click(645,391)        

        time.sleep(5)      # wait for the form to submit
        pyautogui.getActiveWindow().close()  # close the Chrome window

        end_now = datetime.now()
        end_timestamp_str = f'{end_now:%H.%M.%S_%m.%d.%Y}'
        print(f"[*] This run: {run_count} has finished at [{end_timestamp_str}]\n")

        log = open(f"SPECIAL_BOT_{current_date}_{rand_run_id}.txt", 'a')
        log.write(f"run_count:{run_count}\t Start:[{start_timestamp_str}] - End:[{end_timestamp_str}] [{first_name}, {last_name}] STU:{student_name} - E:{email} P:{phone} REL:{relationship} [{address1}, {city}, {state} {postal_code}] - max_loop:{max_loop} id:{rand_run_id}\n\n")
        log.close()

        run_count += 1

except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
    print(f"[!] Script exited at run_count: {run_count}")
