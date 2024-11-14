# *=> MAP FUNCTION

# 1. WAP to create a list of 1st characters from each name?
# names=["manu","lohit","jivago","wank","yaseen"]

names=["manu", "lohit", "jivago", "wank", "yaseen"]
x=lambda a:a[0]
print(list(map(x,names)))

# 2. WAP to return list of name and length pair?
# names1=["laptop","mouse","board","house","week"]

names1= ["laptop", "mouse", "board", "house", "week"]
x=lambda a:(a,len(a))
print(list(map(x,names1)))

# 3. WAP to print sum of indices from both list?
# l1=[2,3,4,5,6]
# l2=[3,4,5]

l1=[2,3,4,5,6]
l2=[3,4,5]
x=lambda a,b:a+b
print(list(map(x,l1,l2)))

# 4. WAP to make a pair of names and age?
# names=["a","b","c","d"]
# age=[20,35,21,56]

names=["a","b", "c", "d"]
age=[20,35,21,56]
x=lambda a,b:(a,b)
print(list(map(x,names,age)))

# 5. WAP to return if the key is individual returns its value else return its type?
# d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}

d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}
x=lambda a:(f'd is individual: {a}' if isinstance(a,(int, bool, float, complex)) else f'd is not individual {type(a)}')
print(list(map(x,d)))

# *=> FILTER FUNCTION

# 1.WAP to return a list having only even values?
# l=[4,3,5,6,7,8,10]

l=[4,3,5,6,7,8,10]
x=lambda a: (a%2==0)
print(list(filter(x,l)))

# 2.WAP to return a list having only flowers?
# l=["sun flowers","banana tree","lilly flowers","lotus flower","marigold flowers"]

l=["sun flowers","banana tree","lilly flowers","lotus flower","marigold flowers"]

def list():
    for i in l.split():
        a=i[1]
print(list(filter(x,l)))
