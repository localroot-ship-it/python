class Comnplex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"1i",self.img,"j")
    def __add__(self,num2):
        newReal=self.real+ num2.real
        newImg=self.img +num2.img
        return complex(newReal,newImg)
num1=complex(1,3)
print(num1)

num2=complex(4,6)
print(num2)

num3=num1+num2
print(num3)