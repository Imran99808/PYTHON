from random import *
user_pass=input("ENTER A PASS \n")
password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','@']
guess=""

while(guess!=user_pass):
    guess=""
    for letter in range(len(user_pass)):
        guess_letter=password[randint(0,26)]
        guess=str(guess_letter)+str(guess)
        print(guess)
print("you currect pass is",guess)    