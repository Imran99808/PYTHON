l=open("python_io_basic.text","rt")
print(l.tell())
print(l.readline())
l.seek(7)
print(l.tell())

print(l.readline())
#print(l.readlines())
#con=l.read()
#for line in l:
   # print(line,end="")
#print(con)
#con=l.read(33333)
#print("1",con)
#con=l.read(3)
#print("2",con)
l.close()