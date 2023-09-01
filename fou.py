N=int(input())
n=0
while c<N:
    if N%c==0:
        n=1
   
    c+=1  
if n==0:
    print("Yes")
else:
    print("No")    