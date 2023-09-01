def m1(x):
    fall=0
    while x>0:
    
        r=x%10
        fall=fall+r
        x=x//10
    el=fall
    lis.append(el)
    return lis
# fall=0
n=int(input("="))
lis=[]
while n>0:
    m1(n)
    n=int(input())
for i in lis:
    print(i)   