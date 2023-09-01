numbers=["3","34","64"]
numbers=list(map(int,numbers))
#for item in range(len(numbers)):
   # numbers[item]=int(numbers[item])
numbers[2]+=1  
#print(numbers[2]) 
#def rr(a):
#  return a*a
#num={2,3,4,5,6,7} 
#square=list(map(rr,num))
#print(square)
# ...............use lambda funktion....................
#num={2,3,4,5,6,7} 
#square=list(map(lambda x:x*x,num))
#print(square)
#........................................

#def square(a):
  #  return a*a
#def cube(a):
   # return a*a*a
#fun=[square,cube]
#for i in range (15):
        
      #  any=tuple(map(lambda x:x(i),fun)) 
        #print(any)       
#..........FILTER.............
#list1=[1,2,3,4,5,6,7]
#def gt_2(a):
  #  return a>2
#gt=list(map(gt_2,list1))
#gt=list(filter(gt_2,list1))
#print(gt) 
#...........REDUCE.......
from functools import reduce
from pprint import pprint  

list1=[1,2,3,4]
plus=reduce(lambda a,b:a+b,list1)
print(plus)
#def jog(a):
 #   num=0
  #  for i in list1:
   #        num+=i
    
    #return num

#plus=reduce(jog,list1)
#plus=jog(list1)
#print(plus)
#num=0
# for i in list1:
   # num+=i
   # print(num)

