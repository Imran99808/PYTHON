import datetime


def gatedate():
     return datetime.datetime.now()


def take(x):
    if x==1:
        a=int(input("ENTER 1 FOR EXERSISE $ 2 FOR FOOD:"))
        if a==1:
            value=input("TYPE HERE \n")
            with open("Harry_exersise.txt","a") as op:
                op.write(str([str(gatedate())])+":"+value+"\n") 
        elif a==2:  
            value=input("TYPE HERE\n")
            with open("Harry_food.txt","a") as op:
                op.write(str([str(gatedate())])+":"+value+"\n")    
        else:
              print("TRRY AGAIN")
        print(".......................HEALTH MANAGEMENT SYSTEM....................")
        a=int(input("Press 1 for log the value $ 2 for retrive :"))
        m1(a)
      
    elif x==2:
        a=int(input("ENTER 1 FOR EXERSISE $ 2 FOR FOOD:"))
        if a==1:
            value=input("TYPE HERE \n")
            with open("Rohan_exersise.txt","a") as op:
                op.write(str([str(gatedate())])+":"+value+"\n") 
        elif a==2:  
            value=input("TYPE HERE\n")
            with open("Rohan_food.txt","a") as op:
                op.write(str([str(gatedate())])+":"+value+"\n")  

        else:
              print("TRRY AGAIN")
        print(".......................HEALTH MANAGEMENT SYSTEM....................")
        a=int(input("Press 1 for log the value $ 2 for retrive :"))
        m1(a)

    elif x==3:
        a=int(input("ENTER 1 FOR EXERSISE $ 2 FOR FOOD:"))
        if a==1:
            value=input("TYPE HERE \n")
            with open("Sajid_exersise.txt","a") as op:
                op.write(str([str(gatedate())])+":"+value+"\n") 
        elif a==2:  
            value=input("TYPE HERE\n")
            with open("Sajid_food.txt","a") as op:
                op.write(str([str(gatedate())])+":"+value+"\n")  
        else:
              print("TRRY AGAIN")
        print(".......................HEALTH MANAGEMENT SYSTEM....................")
        a=int(input("Press 1 for log the value $ 2 for retrive :"))
        m1(a)

    else:
        print("TRRY AGAIN")
        print(".......................HEALTH MANAGEMENT SYSTEM....................")
        a=int(input("Press 1 for log the value $ 2 for retrive :"))
        m1(a)
def retrieve(x):
    if k==1:
        a=int(input("ENTER 1 FOR EXERSISE $ 2 FOR FOOD:"))
        if a==1:
            with open("Harry_exersise.txt","r")as op:
                for d in op:
                    print(d)
        elif a==2:
            with open("Harry_food.txt"+"r")as op:
                for d in op:
                    print(d)
        else:
              print("<><><><><><><><><TRRY AGAIN")
        print(".......................HEALTH MANAGEMENT SYSTEM....................")
        a=int(input("Press 1 for log the value $ 2 for retrive :"))
        m1(a)


    elif k==2:
        a=int(input("ENTER 1 FOR EXERSISE $ 2 FOR FOOD:"))
        if a==1:
            with open("Rohan_exersise.txt","r")as op:
                for d in op:
                    print(d)
        elif a==2:
            with open("Rohan_food.txt"+"r")as op:
                for d in op:
                    print(d)
        else:
              print("TRRY AGAIN")
        print(".......................HEALTH MANAGEMENT SYSTEM....................")
        a=int(input("Press 1 for log the value $ 2 for retrive :"))
        m1(a)
    elif k==3:
        a=int(input("ENTER 1 FOR EXERSISE $ 2 FOR FOOD:"))
        if a==1:
            with open("Sajid_exersise.txt","r")as op:
                for d in op:
                    print(d)
        elif a==2:
            with open("Sajid_food.txt"+"r")as op:
                for d in op:
                    print(d)
        else:
               print("TRRY AGAIN")
        print(".......................HEALTH MANAGEMENT SYSTEM....................")
        a=int(input("Press 1 for log the value $ 2 for retrive :"))
        m1(a)         
 
    else: 
       print("TRRY AGAIN")
       print(".......................HEALTH MANAGEMENT SYSTEM....................")
       a=int(input("Press 1 for log the value $ 2 for retrive :"))
       m1(a)
        
         


print(".......................HEALTH MANAGEMENT SYSTEM....................")

    
def m1(a): 
    global k
    if a==1:
      k=int(input("PRESS 1 FOR HARRY 2 FOR ROHAN 3 FOR SAJID"))
      take(k)          
    elif a==2:
         k=int(input("PRESS 1 FOR HARRY 2 FOR ROHAN 3 FOR SAJID"))
         retrieve(k)


a=int(input("Press 1 for log the value $ 2 for retrive :"))
m1(a)

