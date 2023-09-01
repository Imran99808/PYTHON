from multiprocessing.sharedctypes import Value


def funargs(arg):
    print(type(arg))
    print(arg[0])

def funargs2(n,*args,**kwargs):
   # print(n)
   # print(type(kwargs))
   # print(args.t)
    #print(kwargs)
    print("HEloww")
    for i in args:
        print(i)
    print("Kwargs:") 
    for Key,Value in kwargs.items():
        print(f"{Key} is a {Value}")   
    


har=["harrt","rana","rohan","abal"]
normal="what i this"
kwhar={"harry":"Burger","shkil":"ruyti","Rana":{ "B":"maggi","L":"roti","D":"chicken"}}
#funargs(har)
funargs2(normal,*har,**kwhar)
