first=1
second=1
count=1
n=6
while count<=n:
    if count==1:
        fibo=count
        print(fibo)
    elif count==2:
        fibo=1
        print(fibo)

    else:
         fibo=first+second
         print(fibo)
         first=second
         
         print("f=",first)
         second=fibo
         print("second=",second)
         
    count+=1    