import pyautogui
import subprocess
import time
import random
from datetime import datetime

ts = datetime.now()
timestamp_str = f'{ts:%Y-%m-%d--%H-%M-%S}--[YMD-hms]'



first_name_list = ["Tom", "Jason", "Larry", "Reginald", "Helene", "Esther"]
last_name_list = ["Jenkins", "Warnix", "Goodgame", "Beauregard", "Jones", "Patel"]



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


run_count = 0

try:
    while run_count < 1:      # run_count starts at 0 and goes up to 99

        print(f"[***] Starting new run at run_count: {run_count}")

        # first_name = random.choice(first_name_list)
        # last_name = random.choice(last_name_list)
        # gender = random.choice(range(1, 4))
        # child_DOB = generate_random_date("child")
        # applying_for_year = random.choice(range(1,3))
        # applying_for_grade = random.choice(range(1,13))

        # print(f"{first_name},{last_name}. G={gender} D={child_DOB} AY={applying_for_year} AG={applying_for_grade}")

        
        child_first_name = "Gerald"
        parent_first_name = "Larry"
        last_name = "Goodgame"
        gender = 1
        child_DOB = "01231969"
        applying_for_year = 2
        applying_for_grade = 10
        relationship = 2



        time.sleep(1)       # start new incognito Chrome window
        subprocess.Popen("start chrome /incognito https://portals.veracross.com/aidan/form/general_inquiry", shell=True)    # opens a new incognito Chrome window

        time.sleep(5)       # let the site finish loading
        pyautogui.getActiveWindow().maximize()  # maximize Chrome window
        time.sleep(0.5)     

        # enter child's first and last name
        tab_sleep()
        write_sleep(child_first_name)
        tab_sleep()
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
            pyautogui.press('down')
            time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)

        # select the grade they're applying for
        tab_sleep()    
        space_sleep()
        for keypress in range(applying_for_grade):
            pyautogui.press('down')
            time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)

        for tab in range(4):
            tab_sleep()
        
        time.sleep(0.5)     # enter parent's first and last name
        pyautogui.write(parent_first_name)
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.write(last_name)
        time.sleep(0.5)
        pyautogui.press('tab')

        # select relationship
        
        time.sleep(0.5)      
        pyautogui.press('space')
        time.sleep(0.5)
        for keypress in range(relationship):
            pyautogui.press('down')
            time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('tab')


        # enter email

        # enter phone




        run_count += 1
except KeyboardInterrupt:
    print(f"[!] Script exited at run_count: {run_count}")


# time.sleep(1)
# pyautogui.write('')

# time.sleep(1)
# pyautogui.press('tab')

# time.sleep(1)
# pyautogui.press('enter')        # submit name to search 

# time.sleep(11)          # wait for search results


# # press shift-tab 12 times to select the name, then press enter
# pyautogui.keyDown('shift')
# for tab in range(12):   
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"name tab {tab}")

# time.sleep(1)
# pyautogui.keyUp('shift')
# time.sleep(1)
# print(f"enter")
# pyautogui.press('enter')

# # shift-tab to personnel costs and press enter
# pyautogui.keyDown('shift')
# for tab in range(13):   
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"personnel costs tab {tab}")

# time.sleep(1)
# pyautogui.keyUp('shift')
# time.sleep(1)
# print(f"enter")
# pyautogui.press('enter')


# # gross pay and press enter
# pyautogui.keyDown('shift')
# for tab in range(13):   
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"name tab {tab}")

# time.sleep(1)
# pyautogui.keyUp('shift')
# time.sleep(1)
# print(f"enter")
# pyautogui.press('enter')


# # press tab 11 times to select download excel, then press enter. This opens a Save As window
# for tab in range(11):
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"excel tab {tab}")

# time.sleep(1)
# pyautogui.press('enter')    # opens 'Save As' window

# # clear filename, then use timestamp for excel filename
# time.sleep(5)
# print("before backspace")
# pyautogui.press('backspace')

# time.sleep(1)
# print("before write")
# pyautogui.write(str_timestamp)
# print(f"filename {str_timestamp}")


# time.sleep(1)
# pyautogui.keyDown('shift')

# # select left side nav bar
# time.sleep(1)
# for tab in range(3):
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"SaveAs 1 - {tab}")

# pyautogui.keyUp('shift')
# time.sleep(1)

# # select 'SCRIPT_OUTPUT' on left side nav bar and press enter
# pyautogui.press('down')
# time.sleep(1)
# pyautogui.press('enter')


# # press tab to select save, then press enter
# time.sleep(1)
# for tab in range(6):
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"ClickSave - {tab}")

# time.sleep(1)
# pyautogui.press('enter')    # press enter to save excel file








# active_window = pyautogui.getActiveWindow()
# active_window.minimize()



# pyautogui.press('tab')
# time.sleep(1)
# pyautogui.keyUp('shift')
# time.sleep(1)
# pyautogui.press('down')


# pyautogui.click(591, 521)