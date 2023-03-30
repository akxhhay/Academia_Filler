
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
perm = input("Open up ACADEMIA website \n open the feeback page (refresh if already opened up)... I need all fields to be blank \n now come back \n if done type 'y' to proceed (y/n) ")
if perm == "y":
    comment = input("What is the comment that is required to fill in?  ")
    remark = input("\nWhat is the remark that you would like to Fill in?  ")
    a = int(input('\nHow many theory courses?'))
    b = int(input('\nhow many practical courses?'))
    print("NOW OPEN UP ACADEMIA WEBSITE FAST, tap somewhere blank AND JUST STARE AT IT atleast for a minute, kay??\nsince this is basically a huge macro don't touch anything or else the keystrokes will be executed somewhere else")
    time.sleep(5)

    def autotab(u):
        for k in range(u):
            keyboard.tap(Key.tab)

    def fillerfn(z):
        keyboard.type(remark)
        time.sleep(z)
        keyboard.tap(Key.enter)
        keyboard.tap(Key.tab)
      

    def autofill(x,y,z):
        for i in range(x): 
            fillerfn(2)
            for j in range(y-1):
                fillerfn(z)
            keyboard.type(comment)
            autotab(2)   
            
    autotab(2)
    autofill(a,14,1.6)
    autotab(1)
    autofill(b,13,1.6)
    print("thank me later \n ~fadhil")
else:
     print("restart and just type 'y' plz ")
















