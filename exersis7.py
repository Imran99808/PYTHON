from pygame import mixer
from datetime import datetime
from time import sleep, time

def gatedate():
     return datetime.now()

def sound1(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while 1:
      global user_input
      user_input=input("=")  
      if user_input=="drank":
          mixer.music.stop()
          log("Drank water at")
          break
def sound2(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while 1:
      global user_input 
      user_input=input("=")  
      if user_input=="eydone":
          mixer.music.stop()
          log("Eyes Relaxed at")
          break
def sound3(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while 1:
      global user_input  
      user_input=input("=")  
      if user_input=="exdone":
          mixer.music.stop()
          log("Physical Activity done at")
          break
def log(value):
    if user_input=="drank":
        with open("water.txt","a") as op:
           op.write(str([str(gatedate())])+":"+value+"\n") 
    elif user_input=="eydone":
        with open("eyes.txt","a") as op:
           op.write(str([str(gatedate())])+":"+value+"\n") 
    elif user_input=="exdone":
         with open("exersise.txt","a") as op:
           op.write(str([str(gatedate())])+":"+value+"\n")   



if __name__ == '__main__':

 pat1=("C:\\Users\\Fuso\\Music\\pani.wav")
 pat2=("C:\\Users\\Fuso\\Music\\i.wav")
 pat3=("")
 init_water=time()
 init_i=time()
 init_e=time()
 water=40*60
 eyes=30*60
 exersise=45*60





 while 1:
    
    if time()-init_water>=water:
        print("Water Drinking time. Enter 'drank' to stop the alarm.")
        sound1(pat1)
        init_water=time()
    if time()-init_i>=eyes:
        print("Eye exercise time. Enter 'eydone' to stop the alarm.")
        sound2(pat2)
        init_i=time() 
    if time()-init_e>=exersise:
        print("Physical Activity Time. Enter 'exdone' to stop the alarm.")
        sound3(pat3)
        init_e=time()      
    