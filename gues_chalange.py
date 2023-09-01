a=1
print("------------------------------------you can guesses only 20 number----------------------------------------")
while(a<=20):
    a=a+1
    b=int(input("GUESS YOUR NUMBER="))
    if 17==b:
        print("GAME OVER")
        break
    elif a<b:
        print("OH!YOUR NUMBER IS GETTER THEN")
    elif a>b:
        print("OH!YOUR NUMBER IS LESS THEN")
