hour=int(input())
minut=int(input())
a=(hour*30)+(minut*0.5)
b=abs(minut*6)

mot=a-b

if mot <= 180 :
    print(mot)
else:
    print(360-mot)    