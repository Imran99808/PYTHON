# from itertools import count


N=int(input("="))

a = list(map(int,input().strip().split()))[:N]
count=0
# print(a[count+1])
c=N-1
for i in range(c):
     x=a[i]
     y=a[i+1]
     if x>y or x==y:
         count=1
         break
if count==0:
      print("YES")
else:
    print("NO")      
     