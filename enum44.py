l1=["Bhindi","Aloo","chopsticks","chowmin"]
#i=1
#for item in l1:
    #if i%2!=0:
        #print(f"buy product {item}")
    #i+=1    
for index,item in enumerate(l1):
    if index%2==0:
        print(f"buy product {item}")
