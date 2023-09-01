print("which year you want to covert")
type=input("1.Bangla \n 2.English\n")
a=input("type year=")
b=int(a[0:2])
c=int(a[2:4])

def math1(p1,p2):
    sum1=p1-6
    sum2=p2+7
    final=str(sum1)+str(sum2)
    print("BANGLA YEAR=",final)

def math2(p1,p2):
      sum1=p1+6
      sum2=p2-7
      final=str(sum1)+str(sum2)
      print("ENGLISH YEAR=",final) 
   

if type=="1":
    math2(b,c) 
elif type=="2":
    math1(b,c)    

