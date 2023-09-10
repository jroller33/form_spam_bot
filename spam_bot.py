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


ts = datetime.now()
timestamp_str = f'{ts:%Y-%m-%d--%H-%M-%S}--[YMD-hms]'

first_name_list = ["Tom", "Jason", "Larry", "Reginald", "Helene", "Esther"]
last_name_list = ["Jenkins", "Warnix", "Goodgame", "Beauregard", "Jones", "Patel"]



# def tab_sleep():
#     pyautogui.press('tab')
#     time.sleep(0.5)     

# def space_sleep():
#     pyautogui.press('space')
#     time.sleep(0.5)

# def write_sleep(string):
#     pyautogui.write(string)
#     time.sleep(0.5)

# def down_sleep():
#     pyautogui.press('down')
#     time.sleep(0.5)

# def enter_sleep():
#     pyautogui.press('enter')
#     time.sleep(0.5)
    
# def generate_random_date(input):
#     random_month = str(random.choice(range(1, 13)))
#     random_day = str(random.choice(range(1, 29)))
    
#     if input == "child":    # validate input passed to the function. This decides the range for the random year
#         random_year = str(random.choice(range(2013, 2019)))
#     elif input == "parent":
#         random_year = str(random.choice(range(1970, 1990)))
#     else:
#         print(f"[!] ERROR in generate_random_date() input")

#     if len(random_day) == 1:    # if the day or month is only one digit, add a 0 in front of it (MMDDYYYY)
#         random_day = f"0{random_day}"
#     if len(random_month) == 1:
#         random_month = f"0{random_month}"

#     return f"{random_month}{random_day}{random_year}"    # MMDDYYYY

# def generate_email(first_name, last_name):
#     num = str(random.choice(range(1, 99)))
#     return f"{first_name}{last_name}{num}@gmail.com".lower()

# def generate_phone():
#     num = str(random.choice(range(2345678, 8765432)))       # 202-9999999
#     area_code = "202"
#     return f"{area_code}{num}"


run_count = 0

try:
    while run_count < 1:      # run_count starts at 0 and goes up to 99

        print(f"[***] Starting new run at run_count: {run_count}")

        # initialize the variables. every time this loop runs they will have different values
        child_first_name = random.choice(first_name_list)
        parent_first_name = random.choice(first_name_list)
        last_name = random.choice(last_name_list)
        gender = random.choice(range(1, 4))
        child_DOB = generate_random_date("child")
        applying_for_year = random.choice(range(1,3))
        applying_for_grade = random.choice(range(1,13))
        relationship = random.choice(range(1, 3))
        print(f"{child_first_name},{last_name}. G={gender} D={child_DOB} AY={applying_for_year} AG={applying_for_grade}")


        time.sleep(1)       # start new incognito Chrome window
        subprocess.Popen("start chrome /incognito https://portals.veracross.com/aidan/form/general_inquiry", shell=True)    # opens a new incognito Chrome window
        time.sleep(5)       # let the site finish loading
        pyautogui.getActiveWindow().maximize()  # maximize Chrome window
        time.sleep(0.5)     


        # enter child's first and last name
        tab_sleep()
        write_sleep(child_first_name)
        tab_sleep()
        write_sleep(last_name)

        # select child's gender
        tab_sleep()
        if gender == 1:     
            pyautogui.press('space')
        elif gender == 2:
            pyautogui.press('right')
        elif gender == 3:
            pyautogui.press('right')
            time.sleep(0.5)
            pyautogui.press('right')
        else:
            print(f"[!] ERROR in gender if/else")
        time.sleep(0.5)

        # enter child's DOB
        tab_sleep() 
        write_sleep(child_DOB)

        # select the year they're applying for     
        tab_sleep()       
        space_sleep()
        for keypress in range(applying_for_year):
            down_sleep()
        enter_sleep()

        # select the grade they're applying for
        tab_sleep()    
        space_sleep()
        for keypress in range(applying_for_grade):
            down_sleep()
        enter_sleep()

        for tab in range(4):
            tab_sleep()
        

        # enter parent's first and last name
        write_sleep(parent_first_name)     
        tab_sleep()
        write_sleep(last_name)
        tab_sleep()
        tab_sleep()


        # select relationship
        space_sleep()
        for keypress in range(relationship):
            down_sleep()
        enter_sleep()
        tab_sleep()


        # enter email
        write_sleep(generate_email(parent_first_name, last_name))
        tab_sleep()

        # enter phone
        write_sleep(generate_phone())
        tab_sleep()

        # select 'don't add another contact'
        space_sleep()
        
        # select interests
        for choice in range(4):
            tab_sleep()
            space_sleep()

        # tab_sleep()        # select 'submit'
        # enter_sleep()      # SUBMIT FORM

        time.sleep(10)      # wait for the form to submit
        pyautogui.getActiveWindow().close()  # close the Chrome window
        run_count += 1

except KeyboardInterrupt:
    print(f"[!] Script exited at run_count: {run_count}")

