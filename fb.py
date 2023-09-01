
def m1(l):
        el=len(l)
        lis.append(el)
        return lis
        
a=int(input())
lis=[]

for i in range(a):
    b= list(map(str,input("= ").strip().split()))[:]
    print(b)
    m1(b)
for i in lis:
    print(i)    