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
    

