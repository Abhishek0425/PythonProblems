# *=> DECORATORS 

# 1.write a decorator function that prints "HELLO EVERYONE" message before executaed any function?

def outer(func):
     def inner():
          print("Hello Everyone")
          func()
     return inner

@outer
def func():
    print("hello")
func()

# 2.write a decorator function to print main function name before executing any decorator function?

def outer(func):
    def inner():
        print("Hello Everyone")
        print(func.__name__)
        func()
    return inner
@outer
def display():
    print("hello")
display()

# 3.write a decorator which inputs 5 seconds of dealy before executing any decorator function?

import time
def outer(func):
    def inner():
        time.sleep(5)
        print("Hello Everyone")
        func()
    return inner

@outer
def func():
    print("Hello")
func()

# 4.write a decorator function calculate the execution time of any function?

import time
def outer (func):
    def inner():
        start=time.time()
        end=time.time()
        a=end-start
        print(a)
        print("Hello Everyone")
        func()
    return inner

@outer
def display():
    print("Hello")
display()

# 5.wadf to check if the 1st arguments is lesser than 2nd argument if then swap them and perform division
# but the condition is you should not modify the orginal function?

def outer(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return(func(a,b))
    return inner
@outer
def division(a,b):
    print(a/b)
division(2,4)

# 6.wadf to add 2 numbers and display the message before "i am doing addition operation" after performing print the message "addition operation is done"

# o/p--->i am doing addition operation"
#        value
#      "addition operation is done

def outer(func):
    def inner(a,b):
        print("I am Doing Addition Operation")
        func(a,b)
        print("Addition Operation is done")
    return inner
@outer
def addition(a,b):
    print(a+b)
addition(4,6)

# 7.create a decorator to return only postive out from any substraction?

def outer(func):
    def inner(a,b):
        res=func(a,b)
        return abs(res)
    return inner
@outer
def sub(a,b):
    return(a-b)
print(sub(8,4))

# 8.create a decorator which counts the number of function calls?

count=0
def outer(func):
    def inner(a,b):
        global count
        res=func(a,b)
        count+=1
        return abs(res)
    return inner
@outer
def sub(a,b):
    return(a-b)
print(sub(8,4))
print(count)
