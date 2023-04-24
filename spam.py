import pyautogui as spam
import time

limit = input("Enter Your Limit: ")
msg = input("Enter Your Message: ")

i = 0

time.sleep(10)

while 1<int(limit):
    spam.typewrite(msg)
    spam.press('Enter')
    
    i+=1