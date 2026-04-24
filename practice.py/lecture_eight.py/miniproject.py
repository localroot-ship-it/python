# this is number guessing game.
import random

target=random.randint(1,100)
while True:
    userChoice=input("guess the target or quit (q) :")
    if(userChoice=="q"):
        break
    userChoice=int(userChoice)
    if(userChoice==target):
        print("success : correct guess!!")
        break
    elif(userChoice<target):
        print("your number is too small.take bigger guess... ")
    else:
        print("your number is too bigger.Take small guess...")
print("______game over_____")

# random passworord generartor
import random
import string
pass_len=10
charValues=string.ascii_letters + string.digits + string.punctuation
password=""
for i in range(pass_len):
    password+=random.choice(charValues)
print("your random password is ",password)

#second other method for password generator
import random
import string
pass_len=10
charValues=string.ascii_letters + string.digits + string.punctuation
res="*".join([random.choice(charValues) for i in range(pass_len)])
print(res)








