def Convertl(string):
    list1=[]
    list1[:0]=string
    return list1
# Driver code
def converts(s):
    str1=""
    for i in s:
        str1+=i
    return str1
A=input("")

d="."
b=Convertl(A)
v=b[0].upper()
for i in range(len(A)):
     if i==0:
         b[0]=v
         continue
     if A[i]=="s":
         b[i]="$"
     elif A[i]=="i":
         b[i]="!"
     elif A[i]=="o":
         b[i]="()"    
print(converts(b)+d)        