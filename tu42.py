import time



initiaL=time.time()
print(initiaL)

k=0
while k<45:
    print("Hellow")
    k+=1
print(time.time()-initiaL)    

initial2=time.time()
for i in range(45):
    print("hellow") 
print(time.time()-initial2) 

