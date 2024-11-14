# *=> FUNCTIONS 

# 1. WAP to the given string is palindrone or not?(take user input)

def palindrone():
    str = eval(input("Enter the String: "))
    if str==str[::-1]:
        print("Yes, It is palidrone")
    else:
        print("No, It is not palidrone")
palindrone()
#                                      OR
def palindrone(string):
    if string==string[::-1]:
        return True, string
    else:
        return False, string
print(palindrone('python'))
print(palindrone('pop'))

# 2. WAP to check number is odd or even?(take user input)

def number():
    num=eval(input("Enter the number: "))
    if num%2==0:
        print("Yes, it is Even")
    else:
        print("Yes, It is odd")
number()
#                                            OR
def number(int):
    if int%2==0:
        return True,int
    else:
        return False,int
print(number(2))
print(number(3))

# 3. WAP to perform addition and substraction if "a" is greater than "b" return sum else return difference?

def number(a,b):
    if a>b:
        return a+b,a,b
    else:
        return a-b,a,b
print(number(3,4))
print(number(4,2))

# 4. WAP to return length of variable keywords argumnets?

def string(** kwargs):
    return len(kwargs)
print(string(a=1, b=3, c=4, d=4))

# 5.WAP to return length of the variable positional arguments?

def string(* args):
    print(len(args))
string(1,2,3,4,455,5)

# 6. WAP to search for character in a given string and return corresponding index?
#   string="coding part is done"

string= "Coding part is done"
def func(string, char):
    print(char, string.index(char))
func(string,'o')

# 7. WAP to squareing of the element in the given list?
# l=[1,2,3,4,5]

list=[1,2,3,4,5]
def square_elements(list):
    square=[x**2 for x in list]
    print(square)
square_elements(list)

# 8. WAP to fetch last digit number(take user input)?

num=eval(input("Enter the Number: "))
def last_digit(num):
    last= num%10
    print(last)
last_digit(num)

# 9. WAP to read 3 numbers from the user,first two numbers should be added and the result of addition should be substracted by third number?

a=eval(input("Enter the Number: "))
b=eval(input("Enter the Number: "))
c=eval(input("Enter the Number: "))
def number(a,b,c):
    sum=a+b
    sub=sum-c
    print(sub)
number(a,b,c)

# 10. WAP to find square,cube,squareroot and cuberoot of a number(take user input)?

num=eval(input("Enter the Number: "))
def number(num):
    square= num**2
    cube= num**3
    squareroot=num^2
    cuberoot=num^3
    print(square,cube,squareroot,cuberoot)
number(num)

# 11. WAP to check the given characters is alphabets or digit or special characters(take input user)?

val=eval(input("Enter the Value: "))
def number(val):
    if 'a'<=val<='z' or 'A'<=val<='Z':
        print("Input is Alphabets")
    elif '0'<=val<='9':
        print("Input is digit")
    else:
        print("Input is Special Character")
number(val)

# 12. WAP to check given iterable is a sequence,if it is a sequeance reverse it,if not add one extra element to the iterable?

val=eval(input("Enter the Value: "))
def iterable(val):
    if isinstance(val, (list, tuple, str)):
        val1=val[::-1]
        print(val1)
    else:
        val2=eval(input("Enter the Value: "))
        add=val+val2
        print(add)
iterable(val)

# 13. WAP a function to print the below output
# func("TRACXN",1)
#should print RCN

def func(a):
    return a[1::2]
print(func('TRACXN'))


# 14. WAP  a function to print the below output
# func("TRACXN",0)
#should print TAX

def func(a):
    b=a[0::2]
    print(b)
func("TRACXN")

# 15. WAP  function take variable number of positional arguments
#    as input. how to check if the arguments are more than 5?

val=eval(input("Enter the Value: "))
def pos_arg(*args):
    if len(args)>5:
        print("Arguments is more than 5")
    else:
        print("Arguments is not more than 5")
pos_arg(val)

# 16. WAP to reverse any iterable without using reverse function?

val=eval(input("Enter the Value: "))
def func(val):
    res=val[::-1]
    print(res)
func(val)

# 17. WAP to return a dictionary with characters and ascii value pair?

val=eval(input("Enter the Value: "))
dict={}
def dict_1(val):
    dict[val]=ord(val)
    print(dict)
dict_1(val)

# 18. WAP to reverse a iterable if you are passing string or list or tuple else print type of the data?

val=eval(input("Enter the Value: "))
def value(val):
    if isinstance(val, (str,list,tuple)):
        print(val[::-1])
    else:
        print(type(val))
value(val)

# 19. WAP to check the year is leap year or not?

def leapyear(year):
   if year % 100 == 0 and year % 400 == 0:
       print(year," is a leap year")
   elif year % 100 != 0 and year % 4 == 0:
       print(year,'is leap year')
   else:
       print(year,'is not a leap year')

year = eval(input("Enter the Year:"))
leapyear(year)

# *=> GENERATOR 

# 1. wagf to generate a+b,a-b,a*b,a/b by taking a and b from user?

a=eval(input("Enter the Value: "))
b=eval(input("Enter the Value: "))
def value(a,b):
    l1=a+b
    l2=a-b
    l3=a*b
    l4=a/b
    return l1,l2,l3,l4
print(value(a,b))

                                               # OR

a=eval(input("Enter the Value: "))
b=eval(input("Enter the Value: "))
def value(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b
print(list(value(a,b)))

# 2. wagf to generate only values which are divisible by 5
# l=[34,55,60,56,78,90,25,40]?

l=[34,55,60,56,78,90,25,40]
def value(l):
    for i in l:
        if i%5==0:
            print(i)
value(l)

                                                    # OR

l=[34,55,60,56,78,90,25,40]
def value(l):
    for i in l:
        if i%5==0:
            yield i
print(list(value(l)))

# 3. wagf to return a iterator which is having square root of values present in the list
# l=[25,36,49,81,9,16]?

l=[25,36,49,81,9,16]
from math import sqrt
def value(l):
    for i in l:
        # return(sqrt(i))
        print(sqrt(i))
print(value(l))

                                                        # OR

l=[25,36,49,81,9,16]
from math import sqrt
def value(l):
    for i in l:
        yield(sqrt(i))
print(list(value(l)))

# 4. wagf to return a iterator having tuples of word and its len pair and typecast into dictionary
# l=["instagram","facebook","whatsapp","meta","oracle"]

l=["instagram", "facebook","whatsapp","meta", "oracle"]
def value(l):
    lst=[]
    for i in l:
        lst.append((i, len(i)))
    return lst
print(value(l))
print(dict(value(l)))

                                       # OR

l=["instagram", "facebook","whatsapp","meta", "oracle"]
def value(l):
   for i in l:
       yield i, len(i)
print(list(value(l)))
print(dict(value(l)))

# 5. wagf to generate only numeric values in given list
# l=["flipcart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]?

l=["flipkart", "amazon", 78,[2,3,4],78,9.87,(5,3),45.36]
def value(l):
    for i in l:
        if isinstance(i,(int, float)):
            # return i
         print(i)
value(l)

                                                # OR

l=["flipkart", "amazon", 78,[2,3,4],78,9.87,(5,3),45.36]
def value(l):
    for i in l:
        if isinstance(i, (float, int)):
            yield i
print(list(value(l)))
print(list(value(l)))

# 6. wagf to generate a list if it is individual datatype reverse it else return as it is
# l=["flipcart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]?

l=["flipkart", "amazon", 78,[2,3,4],78,9.87,(5,3),45.36]
def value(l):
    for i in l:
        if isinstance(i,(float,int,complex,bool)):
            # i1=i[::-1]
            # return i1
            print(str(i)[::-1])
        else:
             print(i)
value(l)

                                                       # OR

l=["flipkart", "amazon", 78,[2,3,4],78,9.87,(5,3),45.36]
def value(l):
    for i in l:
        if isinstance(i, (float, int, complex, bool)):
            x=str(i)[::-1]
            yield x
        else:
            yield i
        print(i)
print(list(value(l)))


# 7. wagf to generate only the string with odd length in given list
# l=["alexa","siri","google","cortrena"]?

l=["alexa","siri","google","cortrena"]
def value(l):
    for i in l:
        if len(i)%2==1:
            print(i)
value(l)

                                                         # OR

l=["alexa","siri","google","cortrena"]
def value(l):
    for i in l:
        if len(i)%2==1:
            yield i
print(list(value(l)))

# 8. wagf to create a list of numbers if number are even square it else cube it
# l=[2,3,4,5,6,7]?

l=[2,3,4,5,6,7]
def value(l):
    for i in l:
        lst=[]
        if i%2==0:
            i=i**2
            print(i)
        else:
            i=i**3
            print(i)
value(l)

                                          # OR

l=[2,3,4,5,6,7]
def value(l):
    for i in l:

        if i%2==0:
            i=i**2
            yield i
        else:
            i=i**3
            yield i
print(list(value(l)))

# 9. wagf to return a list if words is of even length reverse it
# l=["hello","world","python","apple","google","walmart"]?

l=["hello","world","python","apple","google","walmart"]
def value(l):
    for i in l:
        if len(i)%2==0:
            print(i[::-1])
value(l)

                                                      # OR

l=["hello","world","python","apple","google","walmart"]
def value(l):
    for i in l:
        if len(i)%2==0:
            i=i[::-1]
            yield i
print(list(value(l)))

# 10. wagf to generate the first letter of the word as key and words starting with letter
# as value
# s="python is a programming language and programming is part of life"?

s="python is a programming language and programming is part of life"
def value(s):
    dict={}
    for i in s.split():
        f=i[0]
        if f in dict:
            dict[f].append(i)
        else:
            dict[f]=[i]
    print(dict)
print(value(s))

                                                      # OR

s="python is a programming language and programming is part of life"
def value(s):
    dict={}
    for i in s.split():
        f=i[0]
        if f in dict:
            dict[f].append(i)
        else:
            dict[f]=[i]
    yield dict
print(list(value(s)))



# 11. wap to fetch all the inteiger value from the list using generator?
# l=['hi', True, 2+2j, 99, 11,0.2]
# o/p=> [99,11]

l=['hi', True, 2+2j, 99, 11,0.2]
def sample():
    for i in l:
        if type(i)==int:
          yield i
print(list(sample()))

# *=> OTHERS 

# 1. WAP python function to find the GCD of 2 numbers or HCF of two numbers

# example:
# a = 4
# b = 10
# output = 2

# So basically HCF or GCD is the highest common divisor of the numbers in this case it is 2
# i.e. 4/2 and 10/2 ?

def findhcf(a,b):
    if a>b:
        smaller = b
    else:
        smaller = a
    for i in range(1,smaller+1):
        if a%i==0 and b%i==0:
            hcf = i
    return hcf
a = eval(input("a: "))
b = eval(input("b: "))
print("The HCF is:",findhcf(a,b))

# 2. WAP to find the lcm of two given numbers
# example
# a = 2
# b = 8
# output = 8 ?

def findlcm(a,b):
    if a>b:
        greater = a
    else:
        greater = b
    for i in range(greater,(a*b)+1):
        if i%a == 0 and i%b == 0:
            lcm = i
            return lcm

a = eval(input("a: "))
b = eval(input("b: "))
print("The LCM is:",findlcm(a,b))

# -> QUEUE - [First In First Out]
#
# OPERATIONS:
# ENQUEUE - insertion - Rear End
# DEQUEUE - deletion - Front End

# 3. WAP to implement the Queue operations on list?

def enqueue():
    n=eval(input("Enter the elemets to inserted into Queue:"))
    queue.append(n)
    print()

def dequeue():
    if len(queue)==0:
        print('QUERY IS EMPTY')
        print()
    else:
        print(queue[0],"is the elements deleted from the Queue")
        del queue[0]
        print()

def display():
    if len(queue)==0:
        print("QUERY IS EMPTY")
    else:
        print("ELEMENTS OF THE QUEUE ARE")
        for ele in queue:
            print(ele,end=' ')
        print("\nFront of the Queue is",queue[0])
        print("Rear of the Queue is",queue[-1])

queue = list()
while(1):
    print("Enter the option from below: \n1-Enqueue Operation\n2-Dequeue Operation\n3-Display\n4-Exit")
    option=eval(input())
    if option==1:
        print('ENQUEUE OPERTIONS')
        enqueue()
    elif option==2:
        print("DEQUEUE OPERTIONS")
        dequeue()
    elif option==3:
        print("DISPLAY")
        display()
    elif option==4:
        break
    else:
        print("Invalid Input")

# -> STACK-[Last In First Out]

# OPERATIONS:
# PUSH - insertion -> Done At Top
# POP - deletion -> Done At Top

# 4. WAP to implement the stack operations on lists ?

def push():
    n=eval(input("Enter the Element Inserted into the Stack:"))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
    print(n,'is the Element Inserted into the Stack')

def pop():
    if len(stack)==0:
        print('STACK IS EMPTY')
    else:
        print(stack[0],'is the Element Deleted from the Stack')
        del stack[0] #pop(0)

def display():
    if len(stack)==0:
        print('STACK IS EMPTY')
    else:
        print('Element of the Stack Are:')
        for ele in stack:
            print(ele)
        print("Top Element of the Stack is:", stack[0])

stack=list()
while(1):
    print("Enter the options from the Below: \n1-PUSH OPERATION\n2-POP OPERTAIONS\n3-DISPLAY OPERTAIOON\nEnter any Key to Exit")
    str=input()
    if str=='1':
        print('PUSH OPERATIONS')
        push()
    elif str=='2':
        print('POP OPERATIONS')
        pop()
    elif str=='3':
        print('DISPLAY OPERATIONS')
        display()
    else:
        print('EXIT FROM PROGRAM')
        break

# 5.WAP this program returns true if any one of the element in two lists is common ?

def check_num(list1,list2):
    final = False
    for i in list1:
        for j in list2:
            if i == j:
                final = True
                return final

print(check_num([1,2,3,4,5],[5,6,7,8,9]))

# 6. WAP python program to find sum of digits of a number in a list
# example:
# in = [12,23,43,66]
# ot = [3,5,7,12]  ?

def lis(st):
    l1 = st.split()
    l2 = []
    for i in l1:
        l2+=[int(i)]
    return l2

def sum_dig(l1):
    l2 = []
    for i in l1:
        sum=0
        for j in str(i):
            sum+=int(j)
        l2.append(sum)
    return l2

l1 = eval(input("Enter the Number:"))
print(sum_dig(l1))


# 7. WAP python function to find the factorial of a given number
# example:
# a = 4
# factorial = 24  ?

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

n = eval(input("Enter the Number:"))
print(fact(n))

# 8. WAP Python function to print the N fibonacci series
# example:
# n = 10
# 0 1 1 2 3 5 8 13 21 34 ?

def fibonacci(n):
    a = 0
    b = 1
    i = 0
    for i in range(n):
        print(a,end=' ')
        c = a+b
        a = b
        b = c

n = eval(input("Enter the Number:"))
fibonacci(n)

# 9. WAP Python program to interchange the first and the last element of the list ?

def lis(str):
    l1 = str.split()
    l2 = []
    for i in l1:
        l2+=[int(i)]
    return l2
def swap(l1):
   l1[0], l1[-1] = l1[-1],l1[0]
   return l1

l1 = eval(input("Enter the Value:"))
print(swap(l1))

# 10. WAP Python function to check whether the given number is perfect or not ?

# if the sum of the factors of the number is equal to the number then the number is perfect number

# Example : n = 6
# Finding Factors
# 6%1 = 0, 6%2 = 0, 6%3 = 0, 6%4 = 2, 6%5 = 1
# Factors of 6 = 1,2,3
# Sum of factors = 1+2+3 = 6(Given Number)
# So, 6 is the Perfect Number

def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            print(i,end = ' ')
            sum+=i
    if sum == n:
        print("\n",n,"is the Perfect Number")
    else:
        print("\n",n,"is not the Perfect Number")

n = eval(input("Enter the Number:"))
perfect(n)

# 11. WAP python function to remove the nth index from the given string and return a new string ?

def str_remove(str,n):
    last_str = str[:n-1] + str[n:]
    return last_str

str = input("Enter the Element to the String:")
n = eval(input("Enter the index of the Element that You want to Remove:"))
print(str_remove(str,n))

# 12. WAP to convert a given string into a list without using any inbuilt function ?
# example 1:
# st = python programmin language
# output = ['python','programmin','language']

# example 2:
# st = 1 2 3 4 5 6
# output = [1,2,3,4,5,6]

def tolist(n):
    l = []
    temp = " "
    for i in n:
        if i==" ":
            l.append(temp)
            temp=" "
        else:
            temp=temp+i
    l.append(temp)
    return l

n = eval(input("Enter the Value:"))
print(tolist(n))




























