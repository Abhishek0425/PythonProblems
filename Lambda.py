# *=> LAMBDA 

# 1.WAP to find square and cube of given number?

s=100
y= lambda s:(s**2,s**3)
print(y(s))

# 2.WAP to check the given number is palindrome or not?

s='mom'
y = lambda s: f's is a palindrone'if s==s[::-1] else f's is not a palindrone'
print(y(s))

# 3.WAP to convert negative number to positive number?

a=-1
z = lambda a: (abs(a))
print(z(a))

# 4.WAP to return the key of a dictionary?
# a={"hello":"Sony","How":"are","you":"bye"}

a={"hello":"sony", "how":"are", "you":"bye"}
z = lambda a :[i for i in a]
print(z(a))

# 5.WAP to check if the number is even or odd?

a=100
z = lambda a : f'a is even' if a%2==0 else f'a is odd'
print(z(a))

# 6.WAP which returns first element of a sequence?

s="hello"
z = lambda s :s[0] if isinstance(s,(list, tuple, str)) else f's is not a sequence'
print(z(s))

# 7.WAP which returns length of any iterable?

s= "hello"
z = lambda s:len(s) if isinstance(s,(list, tuple, str, set, dict)) else f's is not a iterable'
print(z(s))

# 8.WAP which returns the list of squares of numbers in a list?
# l=[2,3,4,5,6]

l=[2,3,4,5,6]
z = lambda l:[i**2 for i in l]
print(z(l))

# 9.WAP to check list elements are palindrome or not?
# l=["nayana","kayak","mom","school","bag","dad"]

l=["nayana", "kayak", "mom", "school", "bag", "dad"]
z = lambda l:[f'l is a palindrone' if i==i[::-1] else f'l is not palidrone' for i in l]
print(z(l))

# 10.WAP to print the numbers present in a list with their corresponding indices pair?
#
# l=[100,200,300,400,500]

l=[100,200,300,400,500]
z = lambda l:[i for i in enumerate(l)]
print(z(l))

# 11.WAP to check a data is sequence if it is sequence then return length pair else type pair?

a="pyhton"
z = lambda a:f'sequence,{len(a)}' if isinstance(a,(list, tuple, str)) else (type(a), len(a))
print(z({1:2,4:5,6:7}))

# 12.WAP to check given number is divisible by 5 and 3?

a=eval(input("Enter the Value: "))
z = lambda a:f'Divisible' if a%5==0 and a%3==0 else f'not divisible'
print(z(a))

# 13.WAP to check even or odd,if it is even return square of that value else square root of that
# value?

from math import sqrt
a=eval(input("Enter the Value: "))
z = lambda a: f'even, {a**2}' if a%2==0 else f'odd,{sqrt(a)}'
print(z(a))

# 14.WAP to check len of given string ,if length is even return as it is else return reverse
# of that string?

a=eval(input("Enter the Value: "))
z = lambda a: f'even,{a}' if len(a)%2==0 else f'odd,{a[::-1]}'
print(z(a))

# 15.WAP to check length of given string and return value and length in tuple and dictionary?

a='python'
z = lambda a:(len(a),a)
x = lambda a:{len(a):a}
print(z(a))
print(x(a))
