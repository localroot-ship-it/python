class Student:
   @staticmethod
   def hello():
       print("hello")
   def __init__(self,name,marks):
      self.name= name
      self.marks=marks
  
   def get_avg(self):
         
         sum=0
         for val in self.marks:
            sum+=1
            print("hi",self.name,"your avg score is :",sum/2)
s1=Student("tony stark",[90,80,90])
s1.get_avg()
s1=Student("iron man",[98,89,99])
s1.get_avg()
s1.hello()

class car:
    def __init__(self):
        self.acc=False
        self.brek=False
        self.clucth=False
    def start(self):
        self.acc=True
        self.clucth=True
        print("car started...")
car1=car()
car1.start()

class Account:
 def __init__(self,bal,acc):
   self.balance=bal
   self.account_no=acc
 def debit(self,amount):
      self.balance-=amount
      print("rs.",amount,"was debited")
      print("total balance=",self.get_balance())
 def credit(self,amount):
   self.balance+=amount
   print("rs.",amount,"was credited")
   print("total balance=",self.get_balance())

 def get_balance(self):
   return self.balance

acc1=Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
    
class student :
 def __init__(self,name):
   self.name=name

s1=student("naveed")
print(s1.name)

class Account:
   def __init__(self,acc,pass_acc):
      self.account=acc
      self.__pass_acc=pass_acc
      def reset_pass(self):
         print(self.__pass_acc)
acc1=Account(1234,"abcd")
print(acc1.account)


class car :
   color= "black"
   @staticmethod
   def start():
      print("car started..")
   def stop():
      print("car stopped..")
class toyotacar(car):
   def __init__(self,name):
      self.name=name
car1=toyotacar("fortuner")
car2=toyotacar("prius")
print(car2.name)


#traffic light checking through conditional statement
light=input("enter color :")
if (light=="red"):
   print("stop")
elif (light=="yellow"):
   print("look around")
elif(light=="green"):
   print("go go...")
else:
   print("light is broken")

#grade checking through conditional satements
marks=int(input("enter your marks :"))
if(marks>=90):
   print("grade A")
elif(marks<=89 and marks>=80):
   print("grade B")
elif(marks<=79 and marks>=70):
   print("grade c")
else:
   print("failed")

    