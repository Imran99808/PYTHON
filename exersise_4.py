
def metho1(n):
      for i in range(0,n):
             for j in range(0,i+1):
                 print("*",end="")
                 
                 
        
             print("\r")
             
def method2(n):
    for i in range(n,0,-1):
             for j in range(0,i):
                    print("*",end="")
         
             print("\r")

while 1:
   a=int(input("enter you number="))
   choice=int(input("0 or 1="))
   new=bool(choice)
   if new==True:
       metho1(a)
   elif new==False:
        method2(a)      