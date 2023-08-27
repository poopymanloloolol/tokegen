import ctypes







import datetime
import os;      import random
import colorama 
from colorama import Fore
from random     import randint
from time       import sleep
from pystyle    import *
from datetime   import datetime
import time
gen = 0
fail = 0
cap_solved = 0
cap_unsolved = 0
unlocked = 0
locked = 0

w = Fore.WHITE
r = Fore.RED
b = Fore.BLUE
g = Fore.LIGHTGREEN_EX
c = Fore.CYAN
m = Fore.LIGHTMAGENTA_EX
ll = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
fr = Fore.RESET
os.system("mode con:cols=137 lines=35")
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    
def set_window_title(title):
    try:
        console_handle = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except Exception as e:
        print(f'Error occurred while setting window title: {str(e)}')


clear()   
set_window_title(f' | Unlocked: {gen} | Locked: {locked} | Dumbboost')
print(Colorate.Vertical(Colors.blue_to_cyan, f"""
                        
made by kaung!!!!!!!!!!!!

""", 1))

sleep(randint(2, 4))

for i in range(randint(7, 10)):

    firsthour = datetime.now()

    hour_one = firsthour.hour
    minute_one = firsthour.minute
    second_one = firsthour.second

    curr_time_one = f'[{hour_one}:{minute_one}:{second_one}]'
    delays1 = [0.4, 0.3, 0.1, 0.9, 0.3]

    print(F"{curr_time_one} Session started")
    sleep(0.01)
    pass

    sleep(random.choice(delays1))

    print(F"{curr_time_one} (!) Captcha detected")
    sleep(0.01)
    pass


    sleep(0.2)


def generator():
    global gen
    global cap_solved 
    global cap_unsolved
    global unlocked
    global locked

    luck = randint(1, 27)

    delays = [0.2, 0.1, 0.12, 0.29]

    secondhour = datetime.now()

    hour_two = secondhour.hour
    minute_two = secondhour.minute
    second_two = secondhour.second

    curr_time_two = f'[{hour_two}:{minute_two}:{second_two}]'

    char = 'azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890'
    first = ''.join((random.choice(char) for i in range(26)))
    second = ''.join((random.choice(char) for i in range(6)))
    third = ''.join((random.choice(char) for i in range(28)))
    fourth = ''.join((random.choice(char) for i in range(8)))
    fifth = ''.join((random.choice(char) for i in range(16)))
    token = "MTExODY1NDcxxx" + first + '.' + second + '.' + third + '_' + fourth + '-' + fifth

    char1 = 'azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890azertyuiopqsdfghjklmwxcvbnAQZSEDRFTGYHUJIKOLPMWXCVBN1234567890'
    first2 = ''.join((random.choice(char1) for i in range(26)))
    second3 = ''.join((random.choice(char1) for i in range(6)))
    third4 = ''.join((random.choice(char1) for i in range(24)))
    fourth1 = ''.join((random.choice(char1) for i in range(14)))
    token1 = "MTExNTk1ND" + first2 + '.' + second3 + '.' + third4 + '***********'+ fourth1 


    if luck == 1 or luck == 2 or luck == 3 or luck == 16 or luck == 20:
        print(F"[ {lb}Humanize{fr}:] ({lb}!{fr}) {lb}Humanized{fr} (pfp, bio, hypesquad)")
        sleep(random.choice(delays))
        return generator()

    elif luck == 4 or luck == 5 or luck == 6 or luck == 7 or luck == 8 or luck == 9 or luck == 17 or luck == 21 or luck == 24:
        gen += 1  
        unlocked += 1
        print(f"[ {g}SUCCESS{fr}: ] ({g}+{fr}) {g}Unlocked{fr} |", token)
        print(f"[ {lr}Email{fr}:   ] ({lr}%{fr}) {lr}Email added{fr} | {lr}Token after verify{fr} |", token1)
        set_window_title(f'Dumbboost | Unlocked: {gen} | Locked: {locked} | Dumbbost')
        with open('Tokens Unlocked.txt', 'a') as file:
            file.write(f"{token}" + '\n')
        sleep(random.choice(delays))
        print(f"[ INFO:    ] ({m}${fr}) {m}Captcha Solved{fr}: {gen} | Captcha Unsolved: {locked}" )
        return generator()
    
    
    elif luck == 10 or luck == 11 or luck == 12 or luck == 18 or luck == 22 or luck == 25:
        print(F"[ {r}CAPTCHA{fr}: ] ({r}-{fr}) {r}Captcha detected{fr}, solving...")
        sleep(random.choice(delays))
        return generator()
    
    elif luck == 4 or luck == 5 or luck == 6 or luck == 7 or luck == 8 or luck == 9 or luck == 21 or luck == 24:
        print(f"[ {lr}Email{fr}:   ] ({lr}%{fr}) {lr}Email added{fr} |", token1)
        return generator()    
    
    elif luck == 23:
        print(f"[ {r}ERROR{fr}:   ] ({r}-{fr}) {r}Locked{fr} |", token)
        set_window_title(f'Nobody gen | Unlocked: {gen} | Locked: {locked} | trust')
        with open('Tokens Locked.txt', 'a') as file:
            file.write(f"{token}" + '\n')
        gen += 1
        locked += 1
        print(f"[ INFO:    ] ({m}${fr}) {m}Captcha Solved{fr}: {gen} | Captcha Unsolved: {locked}" )
        sleep(random.choice(delays))
        return generator()
    
    else:
        print(f"[ {r}ERROR{fr}:   ] ({r}-{fr}) Error when trying to solve the captcha")
        return generator()

generator() 