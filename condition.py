# #traffic light code based on conditional statement
light=input("light color:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green" ):
     print("go")
else:
    (print("light is broken"))

# # grade mark distrubution based on conditional statement 
marks= int(input("marks:"))
if(marks>=90):
    print("grade A")
elif(marks>=80 and marks<90):
    print("grade B")
elif(marks>=70 and marks <80):
    print("grade c")
else:
    print("fail")

# here is single line if statement
food=input("food :")
eat= "yes" if food=="cake"  else "no"
print(eat)
#here is also single line if statement
food=input("food :")
print("sweet") if food=="cake" or food=="jelabi" else print("not sweet")
#claver is statement

age=int(input("age:"))
vote=("yes" , "no") [ age<18]





