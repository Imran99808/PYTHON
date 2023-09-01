import datetime
from time import localtime, sleep
sleep()
def m1():
    global sm
    sm=input()
    return sm
while 1:
    a=localtime()
    b=a.tm_min
    if b==30 or b==24:
          while 1:
            print("y")  
            
            if sm=="ok":
                  m1()
                  break
    elif b==45 or b==2 or b==15 or b==00:
        print("emon")