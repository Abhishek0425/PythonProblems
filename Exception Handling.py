# *=> DEFAULT EXCEPT BLOCK

a=10
b=0
try:
    print(a/b)
except:
    print("zerodivisionerror")

# *=> SPECIFIC EXCEPT BLOCK

a='python'
try:
    print(a.append())
except AttributeError:
    print("Exception Handeled")

# *=> MULTIPLE EXCEPT BLOCK

a={1:2,3:4}
try:
    print(a.append())
except IndexError:
    print("Exception Handeled")
except AttributeError:
    print("Exceptiom Handeled")
except KeyError:
    print("Exception Handeled")
    # or
except(IndexError, AttributeError, KeyError):
    print("Error Handeled")

# *=> GENERIC EXCEPT BLOCK

a=10
b=0
try:
    print(a/b)
except Exception as error_msg:
    print("error handeled")
    print(error_msg)

# *=> NESTED TRY BLOCK

a="hello"
try:
    print(a)
    try:
        print(b)
    except:
        print("no Error")
except:
    print("error")

# *=> FINALLY KEYWORD

a=[1,2,3]

try:
    b=a.append(12)
    print(b)
except AttributeError:
    print("error is handeled")
finally:
    print("done")

# *=> USER DEFINED ERROR

# 1.
class helloerror(Exception):
    pass

def even(num):
    if num%2==0:
        return num,"even"
    else:
        raise helloerror
print(even(5))

# 2.
class hiierror(Exception):
    ...

def vowel_value(vowels):
    if vowels in ['a','e','i','o','u']:
        print('vowels')

    else:
        raise hiierror

vowel_value('x')


# 3.
class doneerror(Exception):
    ...

def datatype(a):
    if isinstance(a,(str,list,tuple)):
        return "Yes it is sequence"
    else:
        raise doneerror
print(datatype({1:'hello'}))


