from hashlib import shake_128


s = set()
# print (type(s))
#s_from_list=set([1,2,3])
#print(s_from_list)
#print(type(s_from_list))

s.add(1)
s.add(2)

s1=s.union({1,2,3})
s.remove(2)
print(s,s1)