from asyncio import _enter_task


a=[]
for i in range(5):
    x=int(input("ENTER NUMBER:"))
    a.append(x)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)