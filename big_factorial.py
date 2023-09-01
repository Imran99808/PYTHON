
N=int(input())
i=0
a=1
while i<N:
  
    # print(i)
    if i==0:
       a*=N
    #    print(a)
    else:
       a*=N-i 
    #    print(a)   
    i+=1
copy=str(a)  
if len(copy)<=4:
   print(a)
else:
   o=int(copy[-4:])
   print(o)
  
     