
# *=> GETCWD()

import os
print(os.getcwd())

# *=> CHDIR()

import os
os.chdir("/Users/adityasharma/Documents/Python Notes")

# *=> MKDIR() 

import os
os.mkdir("python and sql")

# *=> LISTDIR()

import os
print(os.listdir(r'/Users/adityasharma/Documents/Python Notes'))

# *=> RMDIR()

import os
os.rmdir("python and sql")

# *=> REMOVE() 

import os
os.remove("coding.txt")

# *=> CSV FILE HANDLING 

# *=> WRITER()

# EX:

import os
print(os.getcwd())
os.chdir("/Users/adityasharma/Documents/Python Notes")
print(os.getcwd())
import csv
with open("Happy.csv", "w") as fb:
    x=csv.writer(fb)
    x.writerow([["student_name", "Age", "Address"], ["Ravi", 45, "delhi"], ["vikas", 72, "pune"]])
os.popen("happy.csv")

# *=> DICT WRITER()

# EX:

import os
print(os.getcwd())
os.chdir("/Users/adityasharma/Documents/Tutorial")
print(os.getcwd())
import csv
with open ("funny.csv","w",newline='') as file:
    x=csv.DictWriter(file,fieldnames=["fruits_name", "price"])
    x.writeheader()
    x.writerow({"fruits_name":"Apple","price":400})
os.popen("funny.csv")

# *=> READING CSV FILE 

# *=> READER()

# EX:

with open("funny.csv","r") as file:
    x=csv.reader(file)
    print(list(x))

# *=> DICT READER()

# EX:

with open("funny.csv","r") as file:
    x=csv.DictReader(file)
    for i in x:
        print(i)

# *=> TELL() & SEEK()

x = open('pages.txt','r')
print(x.read())
print(x.tell())
print(x.seek(3))
print(x.tell())
print(x.readline())

# *=> PICKLING/SERIALIZATION & UNPICKLING/DESERIALIZATION

import pickle
a=['python','sql','web']
x=pickle.dumps(a)
print(a)
y=pickle.loads(a)
print(y)
with open('pages','rb')as file:
    # x=pickle.dumps(a,file)
    # print(x)
    y=pickle.load(file)
    print(y)


# When we have Same constructor in both Class then we have to pass the parents arguments in child class also

# *=> IS RELATION / INHERITANCE

# Ex

class flipkart:
    def __init__(self, cname, product, addr):
        self.cname=cname
        self.product=product
        self.addr=addr
    def details(self):
        print(f'Customer name is {self.cname}, product name is {self.product},  address is {self.addr}')

class ecommerce(flipkart):
    def __init__(self,cname, product, addr, location, total_product):
        super().__init__(cname,product,addr)
        self.location=location
        self.total_product=total_product

    def delivery_address(self):
        self.details()
        print(f"the location is {self.location}, total product is {self.total_product}")

e=ecommerce("Rahul", "tV", "delhi", "punjabi bagh", "100")
e.delivery_address()

# *=> HAS RELATION / COMPOSITION

# Ex

#  Using Method Format
class test1:
    def spam(self):
        print("spam class")

class test2:
    def spam2(self):
        t=test1()
        t.spam()
        print("spam class continous")

t1=test2()
t1.spam2()

# Using Constructor Format
class hello:
    def __init__(self):
        print("Hello Guys")

    def demo(self):
        print("What now")

class hello1:
    def __init__(self):
        print("Yep")

    def demo2(self):
        self.hello=hello()
        self.hello.demo
        print("Good Enough")
h=hello1()
h.demo2()


# *=> MRO[Method Resolution Order]

class son:
    def resp(self):
        print("Working")

class daughter:
    def sleep(self):
        print("Enjoy")

class parents(son, daughter):
    def suffers(self):
        print("working for childs")

p=parents()
print(parents.__mro__)
p.resp()
p.sleep()
p.suffers()


















