#checking number even or odd
n=int(input("enter a number"))
if(n%2==0):
    print(n,"is even number ")

else:
    print(n,"is odd number")

# check number is zero negative or positive
n=int(input("enter a number :"))
if(n==0):
    print("number is zero")
elif(n<0):
    print("number is negative")
elif(n>=0):
    print("number is positive")

#check age eligiblity
age=int(input("enter your age"))
if(age>=18):
    print(age,'is ELIGBLE FOR VOTE',)
elif(age<18):
    print(age,"is not eligible for vote")
#print largest number
a=int(input("enter first number"))
b=int(input("enter second number"))
if(a>b):
    print(a,"is largest number")
elif(b>a):
    print(b,"is largest number")

# checking leaf year or not 
year=int(input("enter year :"))
if(year%4==0 and year%100!=0 or year%400==0):
    print(year,"is leaf year")
else:
    print(year,"is not a leaf year")
