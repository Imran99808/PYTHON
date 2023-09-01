first=1
second=1
count=1
n=int(input())
while count<=n:
     if count==1:
        fibo=count
        
     elif count==2:
        fibo=1
        

     else:
         fibo=first+second
         first=second
         second=fibo
        
         
     count+=1 
print(fibo)  
