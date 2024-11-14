# CONDITIONAL STATEMENTS

# *=> IF 
    
# 1. WAP to check the number is odd[take user input]?

a = eval(input("Enter the Number: "))
if a % 2 == 1:
    print("Number is odd", a)

# 2. WAP to check the number is even[take user input]?

a = eval(input("Enter the Number: "))
if a % 2 == 0:
    print("Number is Even", a)

# 3. WAP to check if the student has scored 70% print "good luck"[take user input]?

a = eval(input("Enter the Score: "))
if a == 70:
    print("Good Luck", a)

# 4. WAP to check which number is greater using if condition a = 98, b = 67?

a = 98
b = 67
if a > b:
    print("a is greater")

# 5. WAP to check if the given string has even length of character , s = "hey guys you all are osam" ?

s = "hey guys you all are osm"
if len(s) % 2 == 0:
    print("String have Even length")

# 6. WAP to check if the given number is divisible by 5 (take user input)?

a = eval(input("Enter the number: "))
if a % 5 == 0:
    print("Number is Divisible by 5")

# 7. WAP to check if the given programming is present in the list, p=["java","python","c","c++","RUBy","golang"]?

p = ["java", "python", "c", "c++", "RUBy", "golang"]
a = eval(input("Enter the char: "))
if a in p:
    print("Present in the List")

# 8. WAP to check eligible to vote take user input as a age?

a = eval(input("Enter the Age: "))
if a >= 18:
    print("Eligible for Vote")

# 9. WAP to check if the given number is postive take user input?

num = eval(input("Enter the Number: "))
if num > 0:
    print("Number is Positive")

# 10.wap to check if the given string is palindrome (take user input)?

str = eval(input("Enter the Str: "))
if str == str[::-1]:
    print("Str is Palindrome")
# Palindrome means when we read from forward direction or backward direction we get the same word

# 11. WAP to check if the first letter in the given string is consonent, s="lahari is a good student"?

a = ['a', 'e', 'i', 'o', 'u']
s = "lahari is a good student"
if s[0] in a :
    print("Consonent in the Str")

# 12. WAP to check the given string is uppercase or not (take user input)?

a = eval(input("Enter the Str: "))
if a.isupper():
    print("Str is in Uppercase")

# 13. WAP to check the given value is string (take user input)?

a = eval(input("Enter the Value: "))
if type(a) == str:
    print("Given Value is str")

# 14. WAP to display "Python Coding" if the number is greater than 1 and lessthan 5 (take user input)?

a = eval(input("Enter the Number: "))
if a > 1 and a < 5:
    print("Python Coding")

# 15. WAP to check whether given number is negative and print "its negative guys"?

a = eval(input("Enter the Value: "))
if a < 0:
    print("its negative guys")

# 16. WAP to check whether given input is divisible by 2 and 6 if condition is True ,convert the given number to complex number.(take user input)?

a = eval(input("Enter the Value: "))
if a % 2 == 0 and a % 6 == 0:
    b = complex(a)
    print(b)

# 17. WAP to check whether the given number is even or not,if even store the value inside the list (take user input)?

a = eval(input("Enter the Value: "))
if a % 2 == 0:
    b = [a]
    print(b)

# 18. WAP to check whether a given value is divisible by 5 and 7,if the value is divisible then display the square of the values (take user input)?

a = eval(input("Enter the Value: "))
if a % 5 == 0 and a % 7 == 0:
    b = a*a
    print(b)

# 19. WAP to check whether a given value is present in between 45 and 200 and the number should be divisible by 4 and 5 ,if satisfied,display the ascii chracters (take user input)?

num = eval(input("Enter the Value: "))
if num >= 45 or num <= 200 and num % 4 == 0 and num % 5 == 0:
    print("ASCII Character")

# 20. WAP to checking if a string contains a substring
#
# string="hello world"
# sub_string="world"?

string = "hello world"
sub_string = "world"
if sub_string in string:
    print("Yes, Present")

# 21. Finding the maximum value  and minimum value in a list
# l=[1,5,3,9,12]?

l = [1, 5, 3, 9, 12]
max_value = max(l)
min_value = min(l)
print("Max Value", max_value)
print("Min Value", min_value)

# 22. Finding the index of the maximum value in a list
# l=[1,5,3,9,2]?

l = [1, 5, 3, 9, 2]
index_value = l.index(max(l))
print("Index Value", index_value)

# 23. Removing duplicates from a list
# l=[11,12,1,31,31,"hero","hero"]?

l = [11, 12, 1, 31, 31, "hero", "hero"]
remove_duplicate = set(l)
print("No Duplicate", remove_duplicate)

# 24. Counting occurrence of an item in a list
# l=[1,2,3,4,2,2,2,7,8,5]?

l = [1, 2, 3, 4, 2, 2, 2, 7, 8, 5]
count_value = len(l)
print("Count", count_value)
count_of_2 = l.count(2)
print("Occurrence of 2 is", count_of_2)

# 25. Checking if all elements in a list are unique
# l=[1,2,3,4,5]?

l = [1, 2, 3, 4, 5]
are_unique = len(l) == len(set(l))
if are_unique:
     print("Yes, This is Unique")

# 26. WAP to check whether a character is in the alphabet or not,if it is alphabet,store the value inside  a dict(key as a character and value as a ascii value)?

b = eval(input("Enter the Value: "))
s = {}
if "a" <= b <= "z" or "A" <= b <= "Z":
    s[b] = ord(b)
    print(s)

# 27. WAP to check whether a character is in uppercase or not,if uppercase,convert to lower case and store the value inside the dictionary (character as key and ascii as value) take user input?

x = eval(input("Enter the Value: "))
s = {}
if "A" <= x <= "Z":
    x = x.lower()
    s[x] = ord(x)
    print(s)
    
# *=> IF-ELSE 

# 1. WAP to check given number is even remain as it is and if odd plus 1?

x = eval(input("Enter the Value: "))
if x % 2 == 0:
    print("even")
else:
    print("a+1")



 # 2. WAP to check given number ie palidrone or not where a=121?

a=121
b=str(a)
if b == b[::-1]:
    print("its palidrone")
else:
    print("its not palidrone")

# 3. WAP to check given dict length is even if even print as it is and if it is odd make even and print the dict
# d = {1:2, 3:4, 4:5} ?

d = {1:2, 3:4, 4:5}
if len(d) % 2 == 0:
    print("it is Even")
else:
    d.update({5:66})
    print(d)

# 4. WAP to order food from input
# food = ["vada", "dosa", "po0ri", "maggi", "pizza"] ?

food = ["vada", "dosa", "po0ri", "maggi", "pizza"]
a = eval(input("Enter the Food Name: "))
if a in food:
    print("Yes, You can order")
else:
    print("No, sorry not avalible")

# 5. WAP to check in given str first char is in upper case print as it is else print it in upper case
# a = "python"?

a = "python"
if a[0] == "A" <= a <= "Z":
    print(a)
else:
    a = a.capitalize()
    print(a)

# 6. WAP to check if the given number is even, if it is even reduce it to its half else make exponent[Take User Input]?

x = eval(input("Enter the Value: "))
if x % 2 == 0:
    x = x/2
    print(x)
else:
    x = x ** x
    print(x)

# 7. WAP to check the given number is even or odd[take user input]?

x = eval(input("Enter the Value: "))
if x % 2 == 0:
    print("Yes, it is even")
else:
    print("it is odd")

# 8. WAP to check whether the male and female are eligible for wedding[take a user input]?

female_age = eval(input("Enter the Age: "))
male_age = eval(input("Enter the Age: "))
if female_age >= 18 and male_age >= 21:
    print("Yes, You are eligible for wedding")
else:
    print("No, you are not eligible for wedding")

# 9. WAP to return upper case if the char is lower, else return same char[take user input]?

x = eval(input("Enter the value: "))
if "a" <= x <= "z":
    x = x.upper()
    print(x)
else:
    print(x)

# 10. WAP to return lower case if the upper, else return same char[take input value]?

x = eval(input("Enter the Value: "))
if "A" <= x <= "Z":
    x = x.lower()
    print(x)
else:
    print(x)

# 11. WAP to find greater value among the two number
# n1=34
# n2=54

n1 = 34
n2 = 54
if n1 > n2:
    print("n1 is greater ")
else:
    print("n2 is greater")

# 12. WAP to check if the given number is even or not,if it is not even add+1 and make it even (take user input)?

a = eval(input("Enter the Value: "))
if a % 2 == 0:
    print("Number is Even")
else:
    a = a+1
    print(a)

# 13. WAP to check whether the first character in the given string is starting with uppercase or Not if it is not Then capitalise it
# s="python"?

s = "python"
if s[0] == "A" <= s <= "Z":
    print("Yes, it is upper")
else:
    s = s.capitalize()
    print(s)

#  14. WAP to check if the given number is even ,if it is even reduce it to its Half else make exponent (take user input)?

a = eval(input("Enter the Value: "))
if a % 2 == 0:
    a = a/2
    print(a)
else:
    a = a ** a
    print(a)

#  15. WAP to check number should be divisible by 3 and 7 (take user input)?

x = eval(input("Enter the Value: "))
if x % 3 == 0 and x % 7 == 0:
    print("Yes, divisible ")
else:
    print("Not divisible")

#  16. WAP if the length of string is even then reverse else convert into upper case (take user input)?

a = eval(input("Enter the Value: "))
if len(a) % 2 == 0:
    a = a[::-1]
    print(a)
else:
    a = a.upper()
    print(a)

#  17. WAP to check a number is +ve/-ve number (take user input)?

a = eval(input("Enter the Value: "))
if a >= 0:
    print("Number is Positive")
else:
    print("Number is Negative")

#  18. WAP to check a data is individual or collection data type or not (take user input)?

a = eval(input("Enter the Value: "))
if type(a) in (int, float, complex, str):
    print("Datatype is Individual")
else:
    print("Datatype is Collection")

#  19. WAP to check whether the specified character is present in the given string
#
# s="Python"?

s = "Python"
a = eval(input("Enter the Value: "))
if a in s:
    print("Yes, Present")
else:
    print("Not, Present")

# 20. WAP to check the length of dictionary and length of dictionary is even or Not if even
# print as it is or else add a item and make it even
#
# D={"a":"apple","b":"ball","c":"cat"}?

D = {"a":"apple","b":"ball","c":"cat"}
if len(D) % 2 == 0:
    print("Yes, Even ", D)
else:
    D["d"] = "dog"
    print(D)

#  21. WAP to check the given number is greater than 5,if it is greater convert that number into negative number
# else print the same number?

a = eval(input("Enter the Value: "))
if a > 5:
    a = -a
    print(a)
else:
    print(a)

#  22. WAP to check the given number is smaller than 10 ,if it is smaller find the exponent of it
# else print the number as it is?

x = eval(input("Enter the Value: "))
if x < 10:
    x = x ** x
    print(x)
else:
    print(x)

# 23. WAP to check the given number is odd, if it is odd divide it by 2 and print reminder and quotient else print it is even (take user input)?

x = eval(input("Enter the Value: "))
if x % 2 == 1:
    x = x/2
    y = x%2
    z = x//2
    print("Reminder: ", y, "Quotient: ", z)
else:
    print("Number is Even")

#  24. WAP  to check the given character is alphabets or Not ,if it is alphabet create a replica of it for 2 time. (take user input)?

alp = eval(input("Enter the Alphabets: "))
if alp.isalpha():
    x = alp
    y = alp
    print("Yes, it is alphabet:", x)
    print("Yes, it is alphabet:", y)
else:
    print("No, it is not alphabets")

#  25. WAP to check whether the given number value is divisible by 6 or not,if it is divisible cube that number or
#    else perform left shift operation by 3 (take user input)?

num = eval(input("Enter the Number: "))
if num % 6 == 0:
    cube = num ** 3
    print("Cube of the Number is :", cube)
else:
    shift = num << 3
    print("Left Shift the Number is: ", shift)

#  26. WAP to check 1st value is pointing towards same memory address of value else print type of that value
#
# a=[1,2,3,4,5]?

a = [1, 2, 3, 4, 5]
b = a
if id(a[0]) == id(b[0]):
    print("ID of a :", id(a[0]))
    print("ID of b :", id(b[0]))
else:
    print("Type of that Value : ", type(a[0]))

#  27. WAP to check given number first digit is odd or even, a = 573?

a = 573
if int(str(a)[0]) % 2 == 0:
    print("Yes, It is Even")
else:
    print("Yes, It is odd")
