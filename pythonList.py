from cgi import print_directory
from re import A
from tkinter import N


grochery=["java","c","c++","python"]
grochery[1]="emon"
print(grochery)
numbers=[0,3,4,556,6,3]
#numbers[1]=400
#numbers.sort()
#numbers.reverse()
#numbers.remove(556)
#numbers.pop()
#Mutable- can change
#Immutable-cannot change
#print(numbers[1:5])
#print(max(numbers))
#print(numbers)
#_____TAPOL_____
#tp=(1,)
#print(tp)

n=123
fall=0

while n>0:
    r=n%10
    print("R",r)
    fall=fall+r
    print("fall",fall)
    int(n=n/10)
    print("N",n)
print(fall)    