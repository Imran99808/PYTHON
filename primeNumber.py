i=int(input())
c=2
n=0
while c<i: 
    if i%c==0:
        n=1

   
    c+=1  
if n==0:
    print("Yes")
else:
    print("No")    