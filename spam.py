import pyautogui as spam
import time

limit = input("Enter Your Limit: ")
msg = input("Enter Your Message: ")

i = 0

time.sleep(10)

for i in range(0, int(limit)):
    msg += '.\n'
    spam.typewrite(msg)                     # ----> Sends exact number of messages
    spam.press('Enter')
    
    # i+=1           ----> This sends messages as factorial


# while 1<int(limit)         ----> This sends infinite messages