import random
from re import A
list1=["s","w","g"]
# choice=random.choice(list1)


human_point=0
computer_point=0
def m1():  
   global human_point
   global computer_point
   
   if a==choice:
        print("hhhhhh")  
   elif a=="s":
       if choice=="w":
          human_point=human_point+1 
          print("YOU WIN")
          print(f"your guess {a} or computer guess {choice}\n")
          print(f"computer_point is {computer_point} and your point is {human_point} \n ")
         
      
      
       elif choice=="g":
          computer_point=computer_point+1
          print("YOU LOST")
          print(f"your guess {a} or computer guess {choice}\n")
          print(f"computer_point is {computer_point} and your point is {human_point} \n ")
          
          
   elif a=="w":
        if   choice=="s":
            computer_point=computer_point+1
            print("YOU LOST")
            print(f"your guess {a} or computer guess {choice}\n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")
            
     
        
             
        elif choice=="g":
            human_point=human_point+1
            print("YOU WIN")
            print(f"your guess {a} or computer guess {choice}\n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")

            
      
   elif a=="g":
        if choice=="w":
            computer_point=computer_point+1
            print("YOU LOST")
            print(f"your guess {a} or computer guess {choice}\n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")
            
 
        elif choice =="s":
            computer_point=computer_point+1
            print("YOU WIN") 
            print(f"your guess {a} or computer guess {choice}\n")
            print(f"computer_point is {computer_point} and your point is {human_point} \n ")

   else:
       print("YOUR INPUT IS WROMG")

def m2():
  global a,choice
  for x in range(1,11):
      choice=random.choice(list1)
      print("[", x ,"]"+"[S,W,G]Enter Your Iput=")  
      a=input()     
      m1()          
while 1:
     k=m2()

print("...........GAME OVER...........")

if human_point>computer_point:
    print(f"YOU WIN:YOUR SCORE({human_point})")
       

    

elif human_point<computer_point:
    print(f"COMPUTER WIN:COMPUTER SCORE({computer_point})")
       


else:
    print(f"MATCH DRAW:COMPUTER SCORE({computer_point}) OR YOUR SCORE({human_point}) ")
    print("YOU PLAY AGAIN Y/N")
    

