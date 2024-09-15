                     # OOPS Part-1

# Creating a Class & Objects
"""class Student:
    name="Nithin"
s1=Student()
print(s1.name)"""

# Using Constructors
"""class Student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.mark=marks
s1=Student("Nithin",98)
print(s1.name,s1.mark)"""

# TO Create name of another student
"""s2=Student("Arjun",99)
print(s2.name,s2.mark)"""

# Class And Instance Attributes
"""class Student:"""
# Here car_company is a class attribute
"""car_company="Mercedes"""
"""def __init__(self,name):"""
# Here self.name is a instance attribute
"""self.name=name
s1=Student("G-Wagon")
print(s1.name)
print(s1.car_company)"""

# USE of Methods 
"""class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark"""
# Here hello,get_marks are methods in python 
"""def hello(self):
        print("Hello in Python",self.name)
    def get_marks(self):
        return self.mark
s1=Student("Nithin",98)
print(s1.name)
print(s1.get_marks())"""

# Create a class of student that takes marks of 3 subjects and a method to find average
"""class Student:"""
    # This is a parameterized constructor
"""def __init__(self,name,mark1,mark2,mark3):
         self.name=name
         self.mark1=mark1
         self.mark2=mark2
         self.mark3=mark3
    def average(self):
         avg = (self.mark1+self.mark2+self.mark3)/3
         return avg
s1=Student("Nithin",[98,96,98])
print(s1.average())"""

# Create a Bank Account details containing balance and account number and
# amount debited,credited and total balance remaining in the account
"""class Account:
    def __init__(self,balance,account):
        self.balance=balance
        self.account_no=account

    def debit(self,amount):
        self.balance -=amount
        print("Total amount debited is $",amount)
        print("Remaining amount is",self.total_balance())

    def credit(self,amount):
        self.balance +=amount
        print("Total amount Credited is $",amount)
        print("Total amount is",self.total_balance())

    def total_balance(self):
        return self.balance
acc1=Account(10000,1234)
acc1.debit(500)
acc1.credit(10000)
print("Total Bank Balance in the Account is",acc1.total_balance())"""

                         #OOPS Part-2
# Private & Public concept
# Private is conceptually indicated as double underscores' in a class in python
"""class Car:
    __name="Mercedes Benz"
    def __carname(self):
        print("Car name")
c1=Car()
print(c1.__carname())"""

# Inheritance
# Single level inheritance
"""class Car:
    @staticmethod
    def start():
        print("Car has started!")
    @staticmethod
    def stop():
        print("Car has stopped!")
class Mercedes(Car):
    def __init__(self,name):
        self.name=name
c1=Mercedes("Benz")
c2=Mercedes("GLS 550")
print(c1.stop())"""

# Multi-level inheritance
"""class Car:
    @staticmethod
    def start():
        print("Car has started!")
    @staticmethod
    def stop():
        print("Car has stopped!")
class Mercedes(Car):
    def __init__(self,name):
        self.name=name
class Gls_550(Mercedes):
    def __init__(self, type):
        self.type=type
g1=Gls_550("Diesel")
g2=Gls_550("Petrol")
g1.stop()"""

# Multiple Inheritance
"""class A:
    var1="Welcome to class A"
class B:
    var2="Welcome to class B" """
# Here class C is inheriting multiple parent classes A & B so it is multiple inheritance
"""class C(A,B):
    var3="Welcome to class C"
c1=C()
print(c1.var1)
print(c1.var2)
print(c1.var3)"""

# Super method() [Used to access parent class methods]
"""class Car:
    def __init__(self,type):
        self.type=type    
class Mercedes(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
c1=Mercedes("GLS_550","Electric")
print(c1.name)
print(c1.type)"""

# Class Method()[Used to modify the attributes of class]
"""class Car:
    name="Mercedes"
    @classmethod
    def changename(cls,name):
        cls.name=name       
c1=Car()
c1.changename("Benz")
print(Car.name)"""

# Property decorator in Python
"""class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
s1=Student(98,86,98)
print(s1.percentage)"""

# Polymorphism in  Python
# This is the common method to create a class to add complex numbers
"""class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownumber(self):
        print(self.real,"i +",self.img,"j")
    def add(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
o1=Complex(1,3)
o2=Complex(2,4)
o3=o1.add(o2)
o3.shownumber()"""

# We can use dunder functions to print complex numbers
"""class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownumber(self):
        print(self.real,"i +",self.img,"j")"""
    # For Addition
"""def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)"""
    # For Subtraction
"""def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)
o1=Complex(6,8)
o2=Complex(2,4)
o3=o1+o2
o3.shownumber()
o4=o1-o2
o4.shownumber()"""

"""class Employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def showDetails(self):
        print("Employees Role is:",self.role)
        print("Employees Department is:",self.dep)
        print("Employees Salary is:",self.salary)
e1=Employee("Software Engineer","IT",100000)
e1.showDetails()"""

# Create a class Engineer that inherits 3 attributes and show details
"""class Employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def showDetails(self):
        print("Employees Role is:",self.role)
        print("Employees Department is:",self.dep)
        print("Employees Salary is:",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Software Engineer","IT","10000")
e1=Engineer("Nithin",18)
e1.showDetails()"""

# Create a class using dunder function __gt__ to compare price of items
"""class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,order2):
        return (self.price>order2.price)
o1=Order("Chips",400)
o2=Order("Apples",100)
print(o1>o2)"""

        



        


        
        

        
        






        

    



        

        
