A, B = map(int, input().split())
e=str(A)
f=str(B)
if len(e)==1 and len(f)==1:
    print("No")
else:
 c=e[::-1]
 d=f[::-1]
 i=0
 condition=0
 x=len(c)
 y=len(d)
 if x<=y:
  while i<len(c):
 
    l=c[i]
    m=int(l)
    o=d[i]
    n=int(o)
    k=m+n
  
# print(k)
   
    if k>=10:
       condition=1
       break
   
    i+=1
 else:
  while i<len(d):
    l=c[i]
    m=int(l)
    o=d[i]
    n=int(o)
    k=m+n
   
    if k>=10:
       condition=1
       break
   
    i+=1   
 if condition==1:
    print("Yes")   
 else:
    print("No")    