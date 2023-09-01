
def vag(y):
 if y%4==0 and y%100!=0:
    print("yes")
 else:
    print("No")

if __name__ == '__main__':

  a=int(input("="))

  if a%400==0:
      print("yes")
  else:
      vag(a)    
