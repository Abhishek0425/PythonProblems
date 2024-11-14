# *=> FOR LOOP 

# 1. WAP to print the number form 1 -20 segreate even and odd number into list?

Even = []
Odd = []
for i in range(1, 21, 1):
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)
print(Even)
print(Odd)

# 2. WAP to extract vowels and digits in a string
# s="hello123"?

s="hello123"
vowels = ("a", "e", "i", "o", "u")
for i in range(0, len(s) , 1):
    if s[i] in vowels or s[i].isdigit():
        print(s[i])

# 3. WAP to capitilize only the first letter of every word in the given list
# l=["vaidegi","rahul","shivam","kapil","patil"]?

l=["vaidegi","rahul","shivam","kapil","patil"]
for i in l:
    print(i.capitalize())

# 4. WAP to extract only individual datatypes form the list
#
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]?

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
for i in l:
    if isinstance(i, (int, float, bool, complex)):
        print(i)

# 5. WAP to extract only individual datatypes from the list and sum all the individual datatypes?
#
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
sum=0
for i in l:
    if isinstance(i, (int, float, bool, complex)):
        sum = sum+1
print("Sum is :", sum)

# 6. WAP to print the count of alphabets and numbers and space in the given string
#
# s="india got the independence in the year 1947"?

s="india got the independence in the year 1947"
count_alpha=0
count_num=0
count_space=0
for i in s:
    if i.isalpha():
          count_alpha+=1
    elif i.isdigit():
        count_num+=1
    else:
        count_space+=1
print("The Alphabates: ", count_alpha)
print("The Digits: ", count_num)
print("The Space: ", count_space)

# 7.WAP to check how many words are present in the given sentence
#
# s="hello world sentence"?

s="hello world sentence"
count_alpha=0
for i in s.split():
    if i.isalpha():
        count_alpha+=1
        print(i)
        print("Alphabates is: ", count_alpha)

# 8.WAP to create a dictionary and print the characters and its Ascii value pair
# s="hello world"
# output:--> {"h":asciivalue,"e":asciivalue........}

s="hello world"
dict={}
i=0
for i in s:
    char = ord(i)
    dict.update({i:char})
print(dict)

# 9.WAP to create a dictionary and traverse into it and if the length is even print as it else reverse it
#
# names=["apple","google","yahoo","microsoft","gmail","walmart"]
#
# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}

names=["apple","google","yahoo","microsoft","gmail","walmart"]
dict={}
for i in names:
   reverse = i[::-1]
   dict.update({i:reverse})
print(dict)

# 10.WAP to print series of factorial(take user input)?

num = eval(input("Enter the number: "))
fact=1
for i in range(1,num+1):
    fact= fact*i
print(fact)

# 11. WAP to create a dictionary with element and its count pair
#
# l=["yellow","red","black","pink","orannge","green","red","pink","yellow"]
# output:-->
# {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orannge': 1, 'green': 1}

l=["yellow","red","black","pink","orannge","green","red","pink","yellow"]
i=0
dict = {}
for i in l:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

# 12. WAP to find the length of the string without useing inbuilt function
# s="Never Give Up"?

x = "Never Give Up"
count=0
for i in x:
    if i in x:
        count+=1
print(count)

# 13.WAP to reverse a string without using inbuilt function
# x="you did it guys"

x="you did it guys"
count=0
for i in x:
    if i in x:
       count+=1
print(x[::-1])

# 14. WAP to print alternative character from a given string
# s="hello python"

s="hello python"
count=0
for i in s:
    if i in s:
        count+=1
print(s[0::2])

# 15. WAP to replace all the character with "-" if the characters occurs more than once in a string
# s="hellohai"
# o/p---->-e--o-ai

s="hellohai"
count=0
for i in s:
    if s.count(i)>1:
        s=s.replace(i,"-")
print(s)

# 16. WAP to get  output:--->1234 in below question
# t=("1","2","3","4")
#
t = ("1", "2", "3", "4")
for i in t:
    if i in t:
        print(i,end='')

# 17. WAP to Sum of numbers
# s = 'Sony12India567pvt21ltd'

s = 'Sony12India567pvt21ltd'
sum=0
for i in s:
    if i.isdigit():
        sum=sum+int(i)
print(sum)

# 18.WAP to print sum of internal and extrtenal list
# l = [[1,2,3], [4,5,6], [7,8,9]]
# output:-->
#    #internal = 6, 15, 24
#    #external --> 45

l = [[1,2,3], [4,5,6], [7,8,9]]
res=[]
for i in l:
    print(i)
    sum_internal=0
    for j in i:
        print(j)
        sum_internal+=j
    res.append(sum_internal)
print(res)

external=0
for a in l:
    print(a)
    for s in a:
        print(s)
        external+=s
print(external)

# 19. WAP to remove duplicates from the list without using set or empty list
# d=[1,2,3,4,5,6,7,1,2,3,4]?

d=[1,2,3,4,5,6,7,1,2,3,4]
lst=[]
for i in d:
    if i not in lst:
        lst.append(i)
print(lst)

# 20.Print all the missing numbers from 1-10 in the below list
#   l = [1, 2, 3, 4, 6, 7, 10]?

l = [1, 2, 3, 4, 6, 7, 10]
lst=[]
for i in range(1,11,1):
    if i not in lst:
        lst.append(i)
print(lst)

# 21.Reverse a list without using any built-in fucntions and slicing.
#   l = [1, 2, 3, 4]?

l = [1, 2, 3, 4]
for i in l:
    if i in l:
        s=l[::-1]
print(s)


# *=> [REVERSED, ENUMERATE, ZIP, ZIP_LONGEST]


# 22. WAP to create a dictionary word and reverse word pair
# s="tomorrow is weekend and non-veg special"
#
# o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}

s="tomorrow is weekend and non-veg special"
dict={}
for i in s.split():
    dict[i] = i[::-1]
print(dict)

# 23. WAP to create a dictionary index and word pair
# s="tomorrow is weekend and non-veg special"
#
# o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}

s="tomorrow is weekend and non-veg special"
i=0
dict={}
s1 = s.split()
# print(s1)
for i,s1 in enumerate(s1):
       dict[i]=s1
print(dict)

# 24. WAP to create a dictionary words and its length pair
# s="tomorrow is weekend and non-veg special"?
#
# o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}

s="tomorrow is weekend and non-veg special"
dict={}
for i in s.split():
    dict[i]=len(i)
print(dict)

# 25. WAP to create a dictionary characters and its corresponding upper case characters
# s="sunday"
#
# o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}

s="sunday"
i=0
dict={}
for i in s:
         dict[i]=i.upper()
print(dict)

# 26. WAP to create a dictionary Ascii and character pair
# l=[89,51,111,77,108,120]?
#
# o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}

l=[89,51,111,77,108,120]
dict={}
for i in l:
    dict[i]=chr(i)
print(dict)

# 27. WAP to  create a list of characters and its Ascii value pair
#
# s="sunday"?
#
# o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]

s="sunday"
lst=[]
for i in s:
    lst.append((i,ord(i)))
print(lst)

# 28. WAP to sum of same index element from
# l1=[1,2,3,4,5]
# l2=[2,3,4,5,6]
# l3=[11,12,13,14,15]?

l1=[1,2,3,4,5]
l2=[2,3,4,5,6]
l3=[11,12,13,14,15]
for i in zip(l1,l2,l3):
    print(sum(i))

# 29. WAP to pair values of both dictionary
#
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}?

d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}
dict={**d,**p}
print(dict)

# 30. WAP to group fruit name and country pair only if a fruit is even length
#
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}

d={"apple":45,"mango":67,"cherry":90,"berry":23}
p={"kashmir":"ind","america":"us","uk":"toronto","africa":"uganda"}
if len(d.keys()) % 2 ==0:
       dict={**d,**p}
       print(dict)
else:
      print(d)
      print(p)

# 31. WAP to print only the even characters from each string in a list
# l=["programming","python","regular","class","raining","bangalor"]?
#
# o/p:-->
# p o r m i g
# p t o
# r g l r
# c a s
# r i i g
# b n a o

l=["programming","python","regular","class","raining","bangalor"]
i=0
for i in l:
    print(i[::2])

# 32. WAP to perform clear() in list without using inbuilt method
#
# lst = ['hai', 'hello', 'pyhton', 'world', 'jimgilala']?

lst = ['hai', 'hello', 'pyhton', 'world', 'jimgilala']
i=0
for i in lst:
    lst[:]=[]
print(lst)
print(type(lst))

# 33. WAP to extract & store the extensions of files in a list
# l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx',
#  'lambda.png', 'map.py', 'python.pdf', 'oops.py']?

l = ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx', 'lambda.png', 'map.py', 'python.pdf', 'oops.py']
lst=[]
for i in l:
    word=i.split(".")
    if word[0] not in lst:
        lst.append(word[1])
print(lst)

# 34. WAP to create a dictionary with words and its length pair and ends with vowel
#
# s="Today is Tuesday and attending python session"?

s="Today is Tuesday and attending python session"
s1=s.split()
# print(s1)
dict={}
for i in s1:
    if i[-1] in "aeiou":
     dict[i]=len(i)
print(dict)

# 35. WAP to create a dictionary with letter and its words starting with that letter pair
#
# s="hi hello good morning welcome to python session"?
#
# o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}

s = "hi hello good morning welcome to python session"
s1 =s.split()
# print(s1)
dict={}
for i in s1:
  f=i[0]
  if f in dict:
      dict[f].append(i)
  else:
     dict[f]=[i]
print(dict)

# 36. WAP to create a dictionary of characters and its indicies pair
# s="hello python"
#
# o/p->{"h":[0,9],"e":1............}

s = "hello python"
dict={}
for index,i in enumerate(s):
    if i in dict:
        dict[i].append(index)
    else:
        dict[i]=[index]
print(dict)

# 37. WAP to find the prime number ?
#
a=eval(input("enter the value:"))
for i in range(2,a//2+1):
    if a%i==0:
        print(a,"not a prime number")
    else:
       print(a,"prime number")

# 38. WAP to find the number is Armstrong or not?

num=153
a=str(num)
len=len(a)
res=0
for i in a:
    res=res+int(i)**len
if res==num:
    print("number is armstrong")
else:
    print("not a armstrong number")
print(res)


# *=> [BREAK, CONTINUE, PASS]


# 1.WAP to using this list get the below output
#
# l = ['sun flower', 'lilly flower', 'Marigold flower', 'lion animal','tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
#
# o/p:-->{'flower': ['sun', 'lilly', 'Marigold', 'lotus'], 'animal': ['lion', 'tiger', 'snake'], 'bird': ['eagle', 'pigeon']}

l = ['sun flower', 'lilly flower', 'Marigold flower', 'lion animal','tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
dict={}
for i in l:
    word= i.split()
    if word[1] not in dict:
        dict[word[1]]=[word[0]]
    else:
        dict[word[1]]+=[word[0]]
print(dict)

# 2.WAP to check the given number is armstrong or not (Armstrong : Sum of cube of the digits)
# num=370?

num=370
a=str(num)
b=len(a)
res=0
for i in a:
    res=res+int(i)**3

if res==num:
    print("armstrong")

else:
    print('its not a armstrong')

# 3.WAP to check whether string is ANAGRAM or not (anagrams : characters should be same it can different meaning)
# take user input?

char1=eval(input("Enter the Character: "))
char2=eval(input("Enter the Character: "))
if sorted(char1)==sorted(char2):
    print("Anagram")
else:
    print("Not Anagram")

# 4.WAP to get below o/p:
# s = 'Hi how are you'?

#exp o/p : 'iH woh era uoy'

s = 'Hi how are you'
a=""
for i in s.split():
    i=i[::-1]
    a+=i+''
print(a)

# 5.WAp to print longest word in a sentence
#
# s = 'life is full of surprises and miracles'

#exp o/p : surprises

s = 'life is full of surprises and miracles'
a=''
b=s.split()
max=0
for i in b:
    if len(b)>max:
        a=i
        max=len(i)
print(a)

# 6.Replaces whitespaces with new line char in the below string
# s = 'hello world welcome to python'?

s = 'hello world welcome to python'
b=s.replace(" ","\n")
print(b)

# 7 WAP to check  whether the elements inside the list is even or odd and i want the dictionary pair
#
# l=["apple","samsung","oracle","flipcart","facebook","instagram","amazon","ebay"]?
#
# o/p:-->{'odd': ['apple', 'samsung', 'instagram'], 'even': ['oracle', 'flipcart', 'facebook', 'amazon', 'ebay']}

l=["apple","samsung","oracle","flipcart","facebook","instagram","amazon","ebay"]
dict={}
for i in l:
    if len(i)% 2==0:
        if 'even' not in dict:
            dict['even']=[i]
        else:
            dict['even']+=[i]
    else:
        if 'odd' not in dict:
            dict['odd']=[i]
        else:
            dict['odd']+=[i]
print(dict)

# 8. WAP to traverse through a string and stop the execution at specified characters by useing break keyword
#
# s="hello guys tomorrow holiday"
# specified char="d"?

s="hello guys tomorrow holiday"
i=0
for i in s:
    if i in 'd':
        break
    print(i, end=' ')

# 9.WAP to print double digit numbers present in list by useing continue keyword
# l=[2,3,45,67,89,11,2,3,4,5,6,7,8,11]?

l=[2,3,45,67,89,11,2,3,4,5,6,7,8,11]
for i in l:
    if i <=9:
        continue
    print(i,end=' ')

# 10.WAP to print only postive numbers by useing continue keyword
#
# l=[1,5,-2,-45,55,88,-100,-63]?

l=[1,5,-2,-45,55,88,-100,-63]
for i in l:
    if i<=0:
        continue
    print(i, end=' ')

# 11.WAP to skip all the vowels in the given string
#
# s="good morning guys welcome to python session"?

s="good morning guys welcome to python session"
for i in s:
    if i in 'aeiou':
        continue
    print(i,end=' ')

# *=> WHILE LOOP 

# 1. WAP to print series of 20 natural number?

i = 1
while i <= 20:
    print(i, end=' ')
    i = i + 1

# 2. WAP to print series of Upper Case characters?

char = ord("A")
while char <= ord("Z"):
    print(chr(char), end=' ')
    char = char + 1

# 3. WAP to print series of Lower Case characters?

char = ord("a")
while char <= ord("z"):
    print(chr(char), end=' ')
    char = char + 1

# 4. WAP to print both uppercase and lowercase character?

char = ord("A")
char_1 = ord("a")
while char <= ord("Z") and char_1 <= ord("z"):
         print(chr(char_1), chr(char), end=' ')
         char_1 = char_1 + 1
         char = char + 1


# 5. WAP to print series of even numbers till 20 in reverse order?

num = 20
while num >= 1:
       print(num, end=' ')
       num = num - 2

# 6. WAP to count number of occurance of specified elements in the collections
#  s = 'Hello guys Good morning python is a programming language'?

s = 'Hello guys Good morning python is a programming language'
char = eval(input("Enter the Char: "))
i = 0
count = 0
while i < len(s):
    if char == s[i]:
        count=count+1
    i=i+1
print(f'The Specified elements is {char} and counts is {count}')

# 7. WAP to print even postional characters in the given string, s="hello world"?

s="hello world"
i = 0
while i < len(s):
    print(s[i], end=' ')
    i=i+2

# 8. WAP to print two different list and print even and odd numbers from 1-20?

even=[]
odd=[]
i=0
while i<=20:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    i=i+1
print(f"The Even Number is {even}")
print(f"The Even Number is {odd}")

 # 9.WAP to display the postion of the substring?

str = eval(input("Enter the Character: "))
substr = eval(input("Enter the String: "))
i = 0
while i<len(str):
    if substr in str[i]:
        print(i)
    i=i+1

# 10. WAP to print the number Table by using data given by user (take user input)?

num = eval(input("Enter the number: "))
i=0
while i<=10:
    print(f"{i}x{num}={i*num}")
    i=i+1

# 11. WAP to print the names only if the length of the names is even
# l=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"]?

l=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"]
i=0
while i<len(l):
    if len(l[i]) % 2 == 0:
        print(l[i])
    i=i+1

# 12. WAP to print the elements which in tuple,print only the if it is collection data types
# values=(10,2.5,[10,20],"hero",True,(3,4,5),{2,7},{90:"super"})?

values=(10,2.5,[10,20],"hero",True,(3,4,5),{2,7},{90:"super"})
i=0
while i < len(values):
    if isinstance(values[i], (list, set, dict, tuple)):
        print(values[i])
    i=i+1

# 13. WAP to print the name which is starting with vowel in the given list
# names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]?

names = ["agra", "bangalore", "mumbai", "pune", "indore", "isha", "eshwar", "surat"]
vowels = ["a", "i", "e", "o", "u"]
i = 0
while i<len(names):
    if names[i][0].lower() in vowels:
        print(names[i])
    i+=1

# 14. WAP to print sum of numbers in the list
# l=[2,4,6,7,8,9]?

l=[2,4,6,7,8,9]
i = 0
while i < len(l):
    print(sum(l))
    i+=1

# 15. WAP to extract only vowels and digits from the given string
# s="hellopython123"?

s="hellopython123"
c = ["a", "i", "e", "o", "u"]
i=0
while i<len(s):
    if s[i].isdigit() or s[i] in c:
        print(s[i])
    i+=1

# 16. WAP to iterate inside the list check if it is having nested list if yes merge it
#
# list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]?

#excepted output:-->list1=["hello",10,20.55,True,False,"hai","bye",False,"goodnight","enjoy the holiday"]

list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]
i=0
while i<len(list1):
    if isinstance(list1[i],(list)):
        nested_list = list1.pop(i)
        list1.extend(nested_list)
    else:
        i+=1
print("Merge List", list1)

# 17. WAP to print a number which are divisible by 5 from a list
#
# l=[63,20,67,55,85,31]?

l=[63,20,67,55,85,31]
i=0
while i<len(l):
    if l[i] % 5 == 0:
        print("Numbers: ", l[i])
    i+=1

# *=> OTHERS 

# 1. WAP to print the count of alphabets and numbers and space in the given string

# s="india got the independence in the year 1947"?

s="india got the independence in the year 1947"
count_alpha=0
count_space=0
count_digit=0
for i in s:
    if i.isalpha():
        count_alpha+=1
    elif i.isdigit():
        count_digit+=1
    else:
        count_space+=1
print("The alpha is ",count_alpha)
print("The digit is ",count_digit)
print("The space is ",count_space)

# 2. WAP to print the count of vowels and consonent in the given string

# s="india got the independence in the year 1947"?

s="india got the independence in the year 1947"
vowels="aeiouAEIOU"
count_vowels=0
count_consonent=0
for i in s:
    if i in vowels:
        count_vowels+=1
    else:
        count_consonent+=1
print("The vowels ",count_vowels)
print("The consonent ",count_consonent)

# 3. WAP to print series of factorial(take user input)?

n=eval(input("enter the value:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# 4. WAP to get below o/p:
# s = 'Hi how are you'?

# exp o/p : 'iH woh era uoy'

s = 'Hi how are you'
a=""
for i in s.split():
    i=i[::-1]
    a+=i+''
print(a)

# 5. WAP to check the given number is armstrong or not (Armstrong : Sum of cube of the digits)
# num=370?

num=370
a=str(num)
b=len(a)
res=0
for i in a:
    res=res+int(i)**3

if res==num:
    print("armstrong")

else:
    print('its not a armstrong')

# 6. WAP to find the prime number ?

a=eval(input("enter the value:"))
for i in range(2,a//2+1):
    if a%i==0:
        print(a,"not a prime number")
        break
else:
  print(a,"prime number")

# 7. WAP to create a dictionary with letter and its words starting with that letter pair

# s="hi hello good morning welcome to python session"?
# o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}

s = "hi hello good morning welcome to python session"
s1 =s.split()
# print(s1)
dict={}
for i in s1:
  f=i[0]
  if f in dict:
      dict[f].append(i)
  else:
     dict[f]=[i]
print(dict)

# 8. WAP to gave the n odd number?

# 1 3 5 7 9

n=eval(input("enter the value:"))
for i in range(1,2*n+1):
    if i%2!=0:
        print(i,end=' ')

                                              # OR

n=eval(input("enter the value:"))
for i in range(1,2*n+1,2):
    print(i,end=' ')

# 9. WAP to gave the n even number?

# 2 4 6 8 10

n=eval(input("enter the value:"))
for i in range(2,2*n+1,2):
    print(i, end=' ')

                                             # OR

n=eval(input("enter the value:"))
for i in range(2,2*n+1):
    if i%2==0:
        print(i,end=' ')

# 10. WAP to find the sum of 1 to n?

# Enter the value:5
# output -> 15

n=eval(input("Enter the value:"))
s=0
for i in range(1,n+1):
    s+=i
print(s)

# 11. WAP to find the sum of even number between 1 to n?

# Enter the value:10
# output -> 30

n=eval(input("Enter the value:"))
s=0
for i in range(1,n+1):
    if i%2==0:
        s+=i
print(s)

# 12. WAP to find the sum of odd number between 1 to n?

# Enter the value:10
# output -> 25

n=eval(input("Enter the value:"))
s=0
for i in range(1,n+1):
    if i%2!=0:
        s+=i
print(s)

# 13. WAP to find the factorial of n numbers?

# enter the value:5
# output -> 120

n=eval(input("enter the value:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# 14. WAP to find the number is prime or not?

# Enter the value:7
# output -> Number is a prime

n=eval(input("Enter the value:"))
for i in range(2,n//2+1):
    if n % i==0:
        print("Number is not a prime")
        break
else:
   print("Number is a prime")

# 15. WAP to find factor displaying of n number?

# Enter the value:6
# output->1
#         2
#         3
#         6

n=eval(input("Enter the value:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)

# 16. WAP to find factor displaying of n number and count the number of factor?

# enter the value: 6
# output -> Count of factors: 4

n=eval(input("enter the value: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count += 1
print("Count of factors:",count)

# 17. WAP to find the length of the number?

# Enter the value:-123
# output -> 3

n=abs(eval(input("Enter the value:")))
print(len(str(n)))

                                                    # OR

n=abs(eval(input("Enter the value:")))
c = 0
while n!=0: # also n>0
    c+=1
    n//=10 #removing last digit
print(c)

# 18. WAP to reverse the given number?

# Enter the value:123
# output -> 321

n=eval(input("Enter the value:"))
print(str(n)[::-1])

                                                    # OR

n=eval(input("Enter the value:"))
res=0
while n!=0: #also n>0
    reminder = n%10
    res = res*10+reminder
    n//=10 #removing last digit
print(res)

# 19. WAP to check if the number is palindrone or not?

# Enter the value:121
# output -> 121 is the palindrone

n=eval(input("Enter the value:"))
temp=n
res=0
while n!=0: #also n>0
    reminder=n%10
    res = res*10+reminder
    n//=10 #removing last digit
if temp == res:
    print(f"{temp} is the palindrone")
else:
    print(f"{temp} is not palindrone")

# 20. WAP to count the zero, odd and even from the given number?

# Enter the value:10004422
# output -> Zero is 3
#           Odd is 1
#           Even is 4

n=eval(input("Enter the value:"))
zero=0
odd=0
even=0
while n!=0:  # also n>0
    rem=n % 10
    if rem == 0:
        zero+=1
    elif rem % 2!=0:
        odd+=1
    else:
        even+=1
    n//=10 # removing the last digit
print("Zero is",zero)
print("Odd is",odd)
print("Even is",even)

                                                    # OR

n=eval(input("Enter the value:"))
zero=0
odd=0
even=0
for i in str(n):
    if int(i) == 0:
        zero+=1
    elif int(i) % 2==1:
        odd+=1
    else:
        even+=1
print("Zero is",zero)
print("Odd is",odd)
print("Even is",even)


# 21. WAP to calculate the sum of odd and even number?

# Enter the value:11112222
# output -> Odd sum is 4
#           Even sum is 8

n=eval(input("Enter the value:"))
odd_sum=0
even_sum=0
for i in str(n):
    if int(i) % 2==0:
        even_sum+=int(i)
    else:
        odd_sum+=int(i)
print("Odd sum is",odd_sum)
print("Even sum is",even_sum)

                                                         # OR

n=eval(input("Enter the value:"))
odd_sum=0
even_sum=0
while n!=0: #also n>0
    rem=n%10
    if rem % 2==0:
        even_sum+=rem
    else:
        odd_sum+=rem
    n//=10 #removing last digit
print("Odd sum is",odd_sum)
print("Even sum is",even_sum)

# 22. WAP to find the maximum and minimum digit from the given number?

# Enter the value:89783
# output -> Minimum is 3
#           Maximum is 9

n=eval(input("Enter the value:"))
max=0
min=9
while n!=0: #also n>0
    rem=n%10
    if rem > max:
        max=rem
    if rem < min:
        min=rem
    n//=10 #removing the last digit
print("Minimum is",min)
print("Maximum is",max)


                                                           # OR

n=eval(input("enter the value:"))
max=0
min=9
for i in str(n):
    if int(i) > max:
        max=int(i)
    if int(i) < min:
        min=int(i)
print("Minimum is",min)
print("Maximum is",max)


# 23. WAP to print the list by giving the intput value?

# Enter the value:5
# val: 1
# val: 2
# val: 3
# val: 4
# val: 5
# output-> [1, 2, 3, 4, 5]

l = []
n=eval(input("Enter the value:"))
for i in range(n):
    l.append(int(input("val: ")))
print(l)

# 24. WAP the fibonacci series by giving input?

# Enter the value:8
# output-> 0 1 1 2 3 5 8 13

n=eval(input("Enter the value:"))
a=0
b=1
i=0
for i in range(n):
    print(a,end=' ')
    c=a+b
    a=b
    b=c

                                                               # OR

n=eval(input("Enter the value:"))
a=0
b=1
i=0
while i!=n: #also i<n
    print(a, end=' ')
    c=a+b
    a=b
    b=c
    i+=1


# 25. WAP to find that given number is strong or not by giving input?

# Enter the value:145
# output-> 145 is a strong number

n=eval(input("Enter the value:"))
sum=0
temp=n
while n>0:
    rem=n%10
    #factorial
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sum+=fact
    n//=10 #removing last digit
if temp==sum:
    print(f"{temp} is a strong number")
else:
    print(f"{temp} is not a strong number")


# 26. WAP to print strong number between 1 to 1000?

# output-> 1 2 145

for n in range(1,1001):
    sum=0
    temp=n
    while n>0:
        rem=n%10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        sum+=fact
        n//=10
    if temp==sum:
        print(temp,end=' ')

# 27. WAP to find the maximum number from the given list
# l1=[10,20,30,50,40,200,500,700]?

# output-> The maximum number is: 700

l1=[10,20,30,50,40,200,500,700,'hello','good','hey','hep']
# print(max(l1))
max=0
for i in l1:
    if isinstance(i,(int,float)):
        if max < i:
            max = i
print("The maximum number is:",max)




















































































































































