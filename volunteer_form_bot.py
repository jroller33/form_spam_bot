import pyautogui
import subprocess
import time
import random
from datetime import datetime

from custom_functions import tab_sleep, space_sleep, write_sleep, down_sleep, enter_sleep
from custom_functions import generate_email, generate_phone, generate_random_date
from names import first_name_list, last_name_list

from hidden import url

run_count = 0

try:
    while run_count < 1:      # run_count starts at 0 and goes up to 99

        print(f"[***] Starting new run at run_count: {run_count}")

        
        now = datetime.now()
        timestamp_str = f'{now:%m.%d.%Y_%H.%M.%S}'
        current_date = f'{now:%m.%d.%Y}'

        # initialize the variables. every time this loop runs they will have different values
        first_name = random.choice(first_name_list)
        last_name = random.choice(last_name_list)
        full_name = f"{first_name} {last_name}"

        event_choice = random.choice(range(7))
        neg_event_choice = (7 - event_choice)
        committee_choice = random.choice(range(5))
        neg_committee_choice = (5 - committee_choice)
        other_choice = random.choice(range(3))
        neg_other_choice = (3 - other_choice)
        food_choice = random.choice(range(3))
        neg_food_choice = (3 - food_choice)

        email = generate_email(first_name, last_name)
        phone = generate_phone()

        print(f"[*] {first_name},{last_name} {email} {phone}")


        time.sleep(1)       # start new incognito Chrome window
        subprocess.Popen(f"start chrome /incognito {url}", shell=True)    # opens a new incognito Chrome window
        time.sleep(5)       # let the site finish loading
        pyautogui.getActiveWindow().maximize()  # maximize Chrome window
        time.sleep(0.5)     

        for tab in range(3):
            tab_sleep()
        write_sleep(email)

        tab_sleep()
        write_sleep(full_name)

        tab_sleep()
        write_sleep(phone)

        tab_sleep()
        space_sleep()

        for tab in range(5):
            tab_sleep()

        for choice in range(event_choice):
            tab_sleep()
        space_sleep()

        for tab in range(neg_event_choice):
            tab_sleep()
        space_sleep()   # selects first selection of 'Committees' (PA Leadership)

        # Evening of the arts worked








        # time.sleep(10)      # wait for the form to submit
        # pyautogui.getActiveWindow().close()  # close the Chrome window

        print(f"[*] This run: {run_count} has finished.\n\n\n")
        run_count += 1

except KeyboardInterrupt:
    print(f"[!] Script exited at run_count: {run_count}")





#         # enter child's first and last name
#         tab_sleep()
#         write_sleep(child_first_name)
#         tab_sleep()
#         write_sleep(last_name)

#         # select child's gender
#         tab_sleep()
#         if gender == 1:     
#             pyautogui.press('space')
#         elif gender == 2:
#             pyautogui.press('right')
#         elif gender == 3:
#             pyautogui.press('right')
#             time.sleep(0.5)
#             pyautogui.press('right')
#         else:
#             print(f"[!] ERROR in gender if/else")
#         time.sleep(0.5)

#         # enter child's DOB
#         tab_sleep() 
#         write_sleep(child_DOB)

#         # select the year they're applying for     
#         tab_sleep()       
#         space_sleep()
#         for keypress in range(applying_for_year):
#             down_sleep()
#         enter_sleep()

#         # select the grade they're applying for
#         tab_sleep()    
#         space_sleep()
#         for keypress in range(applying_for_grade):
#             down_sleep()
#         enter_sleep()

#         for tab in range(4):
#             tab_sleep()
        

#         # enter parent's first and last name
#         write_sleep(parent_first_name)     
#         tab_sleep()
#         write_sleep(last_name)
#         tab_sleep()
#         tab_sleep()


#         # select relationship
#         space_sleep()
#         for keypress in range(relationship):
#             down_sleep()
#         enter_sleep()
#         tab_sleep()


#         # enter email
#         write_sleep(email)
#         tab_sleep()

#         # enter phone
#         write_sleep(phone)
#         tab_sleep()

#         # select 'don't add another contact'
#         space_sleep()
        
#         # select interests
#         for choice in range(4):
#             tab_sleep()
#             space_sleep()

#         # tab_sleep()        # select 'submit'
#         # enter_sleep()      # SUBMIT FORM


#         log = open(current_date, 'a')   # filename is current_date. write in 'append' mode
#         log.write(f"[{timestamp_str}]\t C:{child_first_name},{last_name}\t P:{parent_first_name}\t {email}-{phone}\t DOB:{child_DOB} Gender:{gender}\t Y/G:{applying_for_year}-{applying_for_grade} Rel:{relationship}\n\n")
#         log.close()
