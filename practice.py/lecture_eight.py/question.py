#question one 
class Circle :
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius
c1=Circle(21)
print(c1.area())
print(c1.perimeter())

# employee distrubution
class Employee:
    def __init__(self,role,dept,salary):
      
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetail(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","it","75000")

engee1=Engineer("elonmusk",40)
engee1.showDetail()
#order gt check
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2):
        return self.price>odr2.price
odr1=Order("chips=",20)
odr2=Order("tea=",15)
print(odr1>odr2)
    
