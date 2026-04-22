class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math /3))+"%"
stu1=student(38,39,39)
print(stu1.percentage)