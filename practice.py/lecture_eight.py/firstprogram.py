class Student:
 name="naveed"
 s1= Student()
   print(s1)
              
#traffic light chrcking throught conditional statements 
light=input("light color :")
if (light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look around ")
elif(light=="green"):
    print("go go ..")
else:
    print("light is broken")

# grade checking through conditional statements
marks=int(input("enter marks :"))
if(marks>=90):
    print("grade A")
elif(marks<=89 and marks>=80):
    print("grade B")
elif(marks<=79 and marks>=70):
    print("grade C")
else:
    print("fail")"""
#check triangle type
"""a=int(input("enter side a :"))
b=int(input("enter side b :"))
c=int(input("enter side c :"))
if(a==b and b==c and a==c):
    print("equilateral triangle")
elif(a==b and b!=c and a!=c):
    print("isosceles triangle")
else:
    print("scalene triangle")

# login credentials in conditional statement
correct_username="naveed"
correct_password="1234"
for i in range(3):
      username=input("enter username :")
      password=(input("enter password :")) 

      if username==correct_username and password==correct_password :
        print("login successful ✅")
        break 
      else:
        print("invalid password❌")
else:
 print("account locked 🔒")
