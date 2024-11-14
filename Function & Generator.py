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



























