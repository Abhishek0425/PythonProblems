# *=> CLASS & OBJECT 

class employee:
    '''my employee details'''
    eid=430
    ename="karan"
    address='delhi'

# Calling through Class

print(employee.eid)
print(employee.ename)
print(employee.address)
print(employee.__doc__) #[docstring]
print(help(employee)) #[help]
print(employee.__dict__) #[dict]

# Calling Through Object

e=employee()
print(e.eid)
print(e.ename)
print(e.address)

# Example

# Modification Main Class and Object

# 1.

class demo:
    a=20
    b=30
d=demo()
d1=demo()
print(demo.a)
print(d.a)
print(d1.a)

# Modification in main class

demo.a=500
print(demo.a)
print(d.a)
print(d1.a)

# Modification in object

d.a=1000
print(demo.a)
print(d.a)
print(d1.a)

# Modification Again in main class

demo.a="OOPS"
print(demo.a)
print(d.a)
print(d1.a)

# Class test

class test:
    a=100

t=test
print(t)

t1=test()
print(t1)

print(id(test))
print(id(t1))


# *=> METHODE 

# 1. INSTANCE METHODE

class sample:
    def spam(self):
        print("hi")
        print(self)
s=sample()
print(s)
s.spam()

#calling by Class name
sample.spam(s)

#calling by Object name
s.spam()

# Instance method without Arguments

class employee:
    sal=100
    def salary(self):
        print(f"My total salary is {employee.sal}") #[we can call it by class name]
        print(f"My total salary is {self.sal}") #[we can call it by self calling]

e=employee()
e.salary()

# Instance methode using Arguments

class salary:
    def total(self,sal):
        print(f'my total salary is {1000+sal}')
e=salary()
e.total(5000)

# 1. WAP to give discount of 500 who shopped ruppess 3000 and they using credit card?

class Shoping:
    def details(self,name,produact,pay):
        total=0
        for key in produact:
            total=total+produact[key]

            if total>=3000 and pay=="creditcard":
                print(total-500)

            else:
                print(total)

s=Shoping()
s.details('akash',{"watch":4500},"creditcard")

# 2. WAP to accept list from user when the methode is called 1st index elements in the list if it is 'string' then reverse the string than replace in same position and return else
#  if it is a integer than ask for user is add a elements into a list and return the updates the list else reverse the list and return?

class check_datatype:
    def check(self,l):
        if isinstance(l[1],str):
            l[1]=l[1][::-1]
            return l

        elif isinstance(l[1],int):
            data=eval(input("enter the data"))
            l.append(data)
            return l

        else:
            return l[::-1]

c=check_datatype()
print(c.check([1,3+4j,3,4]))

# Using instance method better to call through self

class amazon:
    product='watch'
    price=3000
    c_name='karan'
    addr='delhi'
    def ord_list(self):
        print(f'my product is {amazon.product}, {amazon.price}, {amazon.c_name}, {amazon.addr}')
a=amazon()
a.c_name='sunny'
a.ord_list()

# 2. CLASS METHODE

# Ex 1

class demo:
    @classmethod
    def spam(cls):
        print('hii')
        print(cls)

d=demo()
print(d)
d.spam()
demo.spam()

# Ex 2

class demo:
    name='Abhi'
    @classmethod
    def student1(cls):
        print(f'The student name is {cls.name}')

    @classmethod
    def student2(cls):
        s=cls()
        s.name='Aman'
        print(f'The students name is {s.name}')
    @classmethod
    def student3(cls):
        s1=cls()
        s1.name="Arava"
        print(f'The student name is {s1.name}')
b=demo()
b.student1()
b.student2()
b.student3()

# 3. Create a class as bank and declare all the bank name, bank address, bank IFSC code, bank phone number as class variable and create a class methode and print all the bank
# general details for all the customer?

class bank:
    bank_name1='Bank of India'
    bank_address1='Delhi'
    bank_IFSC1='SUP100FRST'
    bank_phoneno1=99921219992
    @classmethod
    def customer1(cls):
        print(f'The details of customer1 : {cls.bank_name1}, {cls.bank_address1},{cls.bank_IFSC1}, {cls.bank_phoneno1}')

    bank_name2= 'State Bank'
    bank_address2= 'Mumbai'
    bank_IFSC2 = 'SUP100FAWSD'
    bank_phoneno2 = 99922339992
    @classmethod
    def customer2(cls):
        print(f'The details of Customer2 : {cls.bank_name2}, {cls.bank_address2}, {cls.bank_IFSC2}, {cls.bank_phoneno2}')

    bank_name3 = 'Central Bank'
    bank_address3 = 'Goa'
    bank_IFSC3 = 'SERT100FAWSDE'
    bank_phoneno3 = 94255678781
    @classmethod
    def customer3(cls):
        print(f'The details of Customer3 : {cls.bank_name3}, {cls.bank_address3}, {cls.bank_IFSC3}, {cls.bank_phoneno3}')

    bank_name4 = 'American Bank'
    bank_address4 = 'Jaipur'
    bank_IFSC4 = 'SEANOH33KJIH'
    bank_phoneno4 = 8799293872

    @classmethod
    def customer4(cls):
        print(f'The details of Customer4 : {cls.bank_name4}, {cls.bank_address4}, {cls.bank_IFSC4}, {cls.bank_phoneno4}')
b=bank()
b.customer1()
b.customer2()
b.customer3()
b.customer4()

# 4. Write a python program that defines a class called book. The book class have the following attributes: Title, Author, year present in string format and it should also
# have class attributes books which is a list of all book object that has been created?

class book:
    book_title1="Home Alone"
    book_author1="William Adam"
    book_year1="2001"
    @classmethod
    def book1(cls):
        print(f'The Book1 Details is : {cls.book_title1}, {cls.book_author1}, {cls.book_year1}')

    book_title2 = "Try it"
    book_author2 = "Shawn Ford"
    book_year2 = "2011"

    @classmethod
    def book2(cls):
        print(f'The Book2 Details is : {cls.book_title2}, {cls.book_author2}, {cls.book_year2}')

    book_title3 = "Money Study"
    book_author3 = "Chetan Bagat"
    book_year3 = "2017"

    @classmethod
    def book3(cls):
        print(f'The Book3 Details is : {cls.book_title3}, {cls.book_author3}, {cls.book_year3}')

    book_title4 = "Alone it is"
    book_author4 = "Ford Allen"
    book_year4 = "2023"

    @classmethod
    def book4(cls):
        print(f'The Book4 Details is : {cls.book_title4}, {cls.book_author4}, {cls.book_year4}')

b=book()
b.book1()
b.book2()
b.book3()
b.book4()

# 3. STATIC METHODE

class test:
    @staticmethod
    def spam(a,b):
        return a+b
    @staticmethod
    def demo(a,b):
        return a*b
t=test()
print(t.spam(3,4))
print(t.demo(3,4))

t.a=100
t.b=300#[modification does not effects]


# *=> CONSTRUCTOR 

class shop:
    def __init__(self):
        print("stop class")
s=shop()
s.__init__()
shop.__init__(s)


# 1. PRE-DEFINED CONSTRUCTOR

class details:
    def shop1(self):
        print("shop1")
d=details()
d.shop1()

# 2. USER-DEFINED CONSTRUCTOR

# Types of User-defined Constructor

# 1. Without Arguments

class day1:
    def __init__(self):
        print('day1 class')
    def class2(self):
        print('dsay2 class')
d=day1()
d.class2()

day1.__init__(d)
day1.class2(d)

# 2. With Arguments

class employees:
    def __init__(self, name, age, work, addr):
        print(f'mmy name is {name},  my age is {age}, my work is {work}, my address is {addr}')
e=employees("Rahul",23, 'Operator', 'delhi')

# Instance varible[Doubt]

class shop:
    def __init__(self, name, prod_name, price):
        self.name=name
        self.prod_name=prod_name
        self.price=price
    def details(self):
        print(f'my name is {self.name}, i buy a {self.prod_name} and price is {self.price}')
s=shop
s.__init__('Rahul', 'Phone', '3000')
s.details()

# DEFAULT CONSTRUCTOR

class test:
    def __init__(self,a=0, b=0, c=0, d=0):
        print(a+b+c+d)
t=test(1,3)

# METHODE OVERLOADING

class sample:
    def add(self,a):
        print(a)

    def add(self, a, b):
        print(a,b)

    def add(self, a=0, b=0, c=0):
        print(a,b,c)

s=sample()
s.add(1,2,3)

# *=> INHERITANCE

# Types of Inheritance

# 1. SINGLE LEVEL INHERITANCE

class father:
    def home(self):
        print("This is father house")

class son(father):
    def enjoy(self):
        print("Enjoy the Father House")

s=son()
s.home()
s.enjoy()
print(dir(father))
print(dir(son))


# 2. MULTI-LEVEL INHERITANCE

class grandfather:
    def property(self):
        print("Transfer the property")

class father(grandfather):
    def got(self):
        print("Father got the property")

class son(father):
    def enjoy(self):
        print("He enjoy the property")

s=son()
s.property()
s.got()
s.enjoy()

# 3. MULTIPLE INHERITANCE

class dad:
    def done(self):
        print("Done for family")

class mom:
    def donetoo(self):
        print("Also Done for family")

class son(dad,mom):
    def enjoy(self):
        print("Always Enjoy the Treatment")

s=son()
s.done()
s.donetoo()
s.enjoy()

# 4. HERICAL INHERITANCE

class dad:
    def done(self):
        print("Always done for their childs")

class daughter(dad):
    def enjoy(self):
        print("Always take princess treatment")

class son(dad):
    def responsible(self):
        print("Always take responsibilities")

# object for son
s=son()
s.done()
s.responsible()

# # object for daughter
d=daughter()
d.done()
d.enjoy()


# 5. HYBRID INHERITANCE[Doubt]

class grandfather:
    def property(self):
        print("Transfer the property")

class father(grandfather):
    def got(self):
        print("Father got the property")

class son1(father):
    def enjoy(self):
        print("He enjoy the property")

class dad(son1):
    def done(self):
        print("Always done for their childs")

class daughter(dad):
    def enjoy(self):
        print("Always take princess treatment")

class son2(dad):
    def responsible(self):
        print("Always take responsibilities")


# METHODE OVERRIDING

# 1. Method Chanining

class day1:
    def hello(self):
        print("How is  your Day1")

class day2(day1):
    def hello(self):
        print("Day1 and Day2 is connected to eachother")
        super().hello()

d2=day2()
d2.hello()

# 2. Constructor Chanining

class day1:
    def __init__(self):
        print("Demo Class")

class day2(day1):
    def __init__(self):
        print("Regular Class")
        super().__init__()

d2=day2()
d2.__init__()

# * => ABSTRACTION 

# Ex

from abc import (ABC,abstractmethod)
class bank(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdrawing(self,amount):
        pass

    @abstractmethod
    def checking_balaence(self):
        pass

class RBI(bank):
    def __init__(self,bal):
        self.bal=bal

    def deposit(self, amount):
        self.bal+=amount
        print(f'The deposited money is {self.bal}')

    def withdrawing(self,amount):
        print(f'The withdrawal money is {self.bal}')
        self.bal-=amount

    def checking_balaence(self):
        print(f'The balence of my account {self.bal}')

r=RBI(400000)
print(r.bal)
r.deposit(10000)
r.withdrawing(20000)
r.checking_balaence()

# Ex

from abc import ABC,abstractmethod

class bookmyshop(ABC):
    @abstractmethod
    def booking(self,price):
        pass

    @abstractmethod
    def cancelling(self,price):
        pass

    @abstractmethod
    def confirm(self):
        pass

class ticket(bookmyshop):
    def __init__(self,count):
        self.count=count

    def booking(self,price):
        self.count+=price
        print(f'The ticket i booked {self.count}')

    def cancelling(self,price):
        self.count-=price
        print(f'The ticket i cancelled {self.count}')

    def confirm(self):
        print(f'The ticket is Confirmed {self.count}')

b=ticket(5000)
print(b.count)
b.booking(300)
b.cancelling(100)
b.confirm()

# *=> ENCAPSALATION

# 1. Public

class Hello:
    def __init__(self, name, Class):
        self.name=name
        self.Class=Class

    def spam(self):
        print("Spam method")


h=Hello('Anup', '12th')
print(h.name)
print(h.Class)

# 2. Protected

class bank:
    _password=231455

    def atm(self):
        print(f'Password is')

b=bank()
print(b._password)
# Cant Modify
b._password=122345677
print(b._password)

# 3. Private

class helloworld:
    __name="Abhi"

    def spam(self):
        print("Hello spam")

h=helloworld()
# print(h.__name) cant access with this

print(helloworld.__dict__)
print(h._helloworld__name) #[By using object]
print(helloworld._helloworld__name) #[By usning class]

# *=> GETTER METHODE, SETTER METHODE & DELETER METHODE

class hello:
    def __init__(self, name):
        self.name=name

    def getter_method(self, name):
        print("getting the name")
        return self.name
    def setter_method(self, name):
        print("setting the name")
        self.name=name
    def deleter_method(self):
        print("deteing the value")
        del self.name
h=hello("Python")
print(h.getter_method("Pythonversion"))
h.setter_method("java")
print(h.setter_method("Pythonversion2"))
































