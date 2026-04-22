count=1
while count<=5:
    print('hello naveed',)
    count+=1
i=8
while i>=1:
   i-=1
   print(i)
#print numbers from 1 to hundred doing while loop
i=1
while i<=100:
    print(i)
    i+=1
#print numbers from 100 to 1 using while loop
i=100
while i>=1:
    print(i)
    i-=1
#print multiplcation of n number
n=int(input("enter number:"))
i=1
while i<=10:
    print(n*i)
    i+=1
# print  elements of following list 
nums=[1,4,9,16,25,36,49,64,81,100]
heros=["ironman","thor","supeman","batman"]
i=0
while i<len(heros):
    print(heros[i])

i+=1
#search number for x usin loop 
nums=(1,4,6,16,25,36,49,64,81,100)
x=36
i=0
while i<len(nums):
    if(nums[i]== x):
        print("found at idx",i)
i+=1
#break statement 
i=0
while i<=5:
     if(i==3):
      i+=1
      continue
print(i)
i+=1
        

    
    
    


