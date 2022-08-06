import pyautogui as pg
import time
time.sleep(10) #time duration starting time

for i in range(10): #how many times you will send the msg
    pg.write("hello")
    pg.press("Enter")






    #***************************with file******************

# import pyautogui,time
# time.sleep(5)
# f=open("filename.txt",'r')  #file must present with proper name and in this directory only
# for word in f:
#     pyautogui.typewrite(word)
#     pyautogui.press("Enter")
