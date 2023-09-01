# A, B = map(int, input().split())
# e=str(A)
# f=str(B)
# c=e[::-1]
# d=f[::-1]
# i=0
# condition=0
# while i<len(c):
   
#    l=c[i]
#    m=int(l)
#    o=d[i]
#    n=int(o)
#    k=m+n
  
# # print(k)
#    if k>=10:
#        condition=1
#        break

#    i+=1
# if condition==1:
#     print("Yes")   
# else:
#     print("No") 
# def converts(s):
#     str1=""
#     for i in s:
#         print(i)
#         str1+=i
#     return str1
# A=['u', 'n', '$', '()', 'p', 'h', '!', ' ', '$', 't', '!', 'c', 'a', 't', 'e', 'd'] 
# converts(A)
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:]

print(a)
print(len(a))