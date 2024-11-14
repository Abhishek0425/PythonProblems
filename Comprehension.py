# *=> COMPREHENSION

# *=> LIST COMPREHENSION

# 1.wap to check even numbers in a list and return a list containing only even numbers?
# l=[2,32,1,52,31,24,56,75]

l = [2, 32, 1, 52, 31, 24, 56, 75]
print([i for i in l if i%2==0])

# 2.wap to check elements inside the collection are even or odd,if it is even
# make it square of that numbers,if it is odd make it as cube of that numbers?
# l=[2,3,5,1,7,2,3]

l=[2, 3, 5, 1, 7, 2, 3]
print([i**2 if i%2==0 else i**3 for i in l])

# 3.wap to return a list containing 10 multiples of 2?

print([i for i in range(2,21,2) if i%2==0])

# 4.wap to return a list containing 10 multiples of given value(take user input)?

a=eval(input("Enter the Value: "))
print([a*i for i in range(1,11)])

# 5.wap to take two lists as input and add that elements and return a single lists?

a=[1,2,3,4,5,6,7]
b=[3,6,7,23,5,66,33]
print([a+b])

# 6.wap to create a list containing tuples having two elements that is index and value of list?
# l=["hey","hello","good","evening","python"]

l=["hey", "hello", "good", "evening", "python"]
print([i for i in enumerate(l)])

# 7.wap to check length of strings present in tuple,if length is even append as it is ,else reverse it and append?
# l=("hey","hello","good","evenings","python")

l = ("hey", "hello", "good", "evening", "python")
print([i if len(i)%2==0 else i[::-1] for i in l])


# *=> SET COMPREHENSION

# 1.wap to remove repeated values and return in set?
# l=[2,3,4,2,5,6,2,3]

l=[2,3,4,2,5,6,2,3]
print(set(l))

# 2.wap to take two lists and return a set by adding elements present same index?
# l1=[2,3,4,5,6,7,8,9]
# l2=[5,6,7,8,9,1,2,3]

l1=[2,3,4,5,6,7,8,9]
l2=[5,6,7,8,9,1,2,3]
print({i for i in zip(l1,l2)})

# *=> DICT COMPREHENSION

# 1.wap to create a dictionary keys by taking from list,values are square of that key?
# l=[2,3,4,1,6,2,7,8,4]

l=[2,3,4,1,6,2,7,8,4]
print({i:i**2 for i in l})

# 2.wap to create a dictionary of values and index pair?
# l=["google","apple","python","orange"]

l=["google", "apple", "python", "orange"]
print({i for i in enumerate(l)})

# 3.wap create a dictionary having first char of word and word pair if word having even length?
# l=["google","apple","python","orange"]

l=["google", "apple", "python", "orange"]
print({i[0]:i for i in l if len(i)%2==0})

# 4.wap to check length of words and create a dict having word and word pair if it is even add as it is else reverse and add?
# l=["google","apple","python","orange"]

l=["google", "apple", "python", "orange"]
print({i: i if len(i)%2==0 else i[::-1] for i in l})

# 5.wap to check elements is pallindrome key and value should be same else value is reverse of key?
# l=["banana","malayalam","madam","sir","mom","dad"]

l=["banana", "malayalam", "madam", "sir", "mom", "dad"]
print({i:i if i==i[::-1] else i[::-1] for i in l})
