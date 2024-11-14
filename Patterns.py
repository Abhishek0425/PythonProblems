# *=> PATTERNS PROBLEMS 

# STEPS:

# 1. Controlling the number of Rows
# 2.  Controlling the number of Columns
# 3. Controlling values

# Examples:
# 1.

# * * * *
# * * * *
# * * * *
# * * * *

row=eval(input("Enter the row:"))
col=eval(input("Enter the cols:"))
for i in range(row):
    for j in range(col):
        print("*", end=' ')
    print()

# 2.

# $ $ $ $
# $ $ $ $
# $ $ $ $
# $ $ $ $

row=eval(input("enter the row:"))
col=eval(input("enter the cols:"))
for i in range(row):
    for j in range(col):
        print("$", end=' ')
    print()

# 3

# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
val=1
for i in range(row):
    for j in range(col):
        print(val, end=' ')
    print()
    val+=1

# 4.

# 3 3 3 3
# 2 2 2 2
# 1 1 1 1
# 0 0 0 0

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
val=3
for i in range(row):
    for j in range(col):
        print(val, end=' ')
    print()
    val-=1

# 5.

# 4 4 4 4
# 3 3 3 3
# 2 2 2 2
# 1 1 1 1

row=eval(input("Enter the rows:"))
col=eval(input("Enter the columns:"))
val=row
if val>9:
    val=9
for i in range(row):
    for j in range(col):
        print(val, end=' ')
    print()
    val-=1
    if val<1:
        val=9

# 6.

# 4 3 2 1
# 4 3 2 1
# 4 3 2 1
# 4 3 2 1

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
for i in range(row):
    val=col
    for j in range(col):
        print(val, end=' ')
        val-=1
    print()

# 7.

# A A A A
# B B B B
# C C C C
# D D D D

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
val=ord('A')
for i in range(row):
    for j in range(col):
        print(chr(val), end=' ')
    print()
    val+=1
    if val>ord('Z'):
        val=ord('A')

# 8.

# a a a a
# b b b b
# c c c c
# d d d d

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
val=ord('a')
for i in range(row):
    for j in range(col):
        print(chr(val), end=' ')
    print()
    val+=1
    if val>ord('z'):
        val=ord('a')

# 9.

# A B C D
# A B C D
# A B C D
# A B C D

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
for i in range(row):
    val=ord('A')
    for j in range(col):
        print(chr(val), end=' ')
        val+=1
        if val > ord('Z'):
            val = ord('A')
    print()

# 10.

# a b c d
# a b c d
# a b c d
# a b c d

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
for i in range(row):
    val=ord('a')
    for j in range(col):
        print(chr(val), end=' ')
        val+=1
        if val > ord('z'):
            val = ord('a')
    print()

# 11. if row=3 and col=3

# C C C
# B B B
# A A A

row=eval(input("Enter the row:"))
col=eval(input("Enter the col:"))
val=ord('C')
for i in range(row):
    for j in range(col):
        print(chr(val), end=' ')
    print()
    val-=1

# 12. if row=3 and col=3

# C B A
# C B A
# C B A

row=eval(input("Enter the row:"))
col=eval(input("Enter the col:"))
for i in range(row):
    val=ord('C')
    for j in range(col):
        print(chr(val), end=' ')
        val-=1
    print()

# 13.

# *
# * *
# * * *
# * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i>=j:
            print('*', end=' ')
        else:
            print(end=' ')
    print()

# 14.

# 1
# 2 2
# 3 3 3
# 4 4 4 4

n=eval(input("enter the value:"))
val=1
for i in range(n):
    for j in range(n):
        if i>=j:
            print(val, end=' ')
        else:
            print(end=' ')
    print()
    val+=1

# 15.

# 1
# 1 2
# 1 2 3
# 1 2 3 4

n=eval(input("enter the value:"))
for i in range(n):
    val=1
    for j in range(n):
        if i>=j:
            print(val, end=' ')
            val+=1
        else:
            print(end=' ')
    print()

# 16.

# 4
# 3 3
# 2 2 2
# 1 1 1 1

n=eval(input("enter the value:"))
val=n
for i in range(n):
    for j in range(n):
        if i>=j:
            print(val, end=' ')
        else:
            print(end=' ')
    val-=1
    print()

# 17.

# 4
# 4 3
# 4 3 2
# 4 3 2 1

n=eval(input("enter the value:"))
for i in range(n):
    val=n
    for j in range(n):
        if i>=j:
            print(val, end=' ')
            val-=1
        else:
            print(end=' ')
    print()

# 18.

# A
# B B
# C C C
# D D D D

n=eval(input("enter the value:"))
val=ord("A")
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(val), end=' ')
        else:
            print(end=' ')
    val+=1
    print()
    if val>ord('Z'):
        val=ord('A')

# 19.

# A
# A B
# A B C
# A B C D

n=eval(input("enter the value:"))
for i in range(n):
    val=ord('A')
    for j in range(n):
        if i>=j:
            print(chr(val), end=' ')
            val+=1
        if val>ord('Z'):
            val = ord('A')
        else:
            print(end=' ')
    print()


# 20.

# D
# C C
# B B B
# A A A A

n=eval(input("enter the value:"))
val=ord('A')+n-1
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(val), end=' ')
        else:
            print(end=' ')
    val-=1
    print()

# 21.

# D
# D C
# D C B
# D C B A

n=eval(input("enter the value:"))
for i in range(n):
    val=ord('A')+n-1
    for j in range(n):
        if i>=j:
            print(chr(val), end=' ')
            val-=1
        else:
            print(end=' ')
    print()

# 22.

# 1 1 1 1
#   2 2 2
#     3 3
#       4

n=eval(input("enter the value:"))
val=1
for i in range(n):
    for j in range(n):
        if i<=j:
            print(val, end=' ')
        else:
            print(' ',end=' ')
    val+=1
    print()

# 23.

# 1 2 3 4
#   1 2 3
#     1 2
#       1

n = eval(input('Enter the value: '))
for i in range(n):
    val = 1
    for j in range(n):
        if i <= j:
            print(val, end=' ')
            val += 1
        else:
            print(' ', end=' ')
    print()

# 24.

# 4 3 2 1
#   4 3 2
#     4 3
#       4

n=eval(input("enter the value:"))
for i in range(n):
    val=n
    for j in range(n):
        if i<=j:
            print(val, end=' ')
            val-=1
        else:
            print(' ', end=' ')
    print()

# 25.

# 4 4 4 4
#   3 3 3
#     2 2
#       1

n=eval(input("enter the value:"))
val=n
for i in range(n):
    for j in range(n):
        if i<=j:
            print(val, end=' ')
        else:
            print(' ',end=' ')
    val-=1
    print()

# 26.

# A B C D
#   A B C
#     A B
#       A

n=eval(input("enter the value:"))
for i in range(n):
    val=ord('A')
    for j in range(n):
        if i<=j:
            print(chr(val), end=' ')
            val+=1
        else:
            print(' ',end=' ')
    print()

# 27.

# A A A A
#   B B B
#     C C
#       D

n=eval(input("enter the value:"))
val=ord('A')
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(val), end=' ')
        else:
            print(' ',end=' ')
    val += 1
    print()

# 28.

# D C B A
#   D C B
#     D C
#       D

n=eval(input("Enter the value:"))
for i in range(n):
    val=ord('A')+n-1
    for j in range(n):
        if i<=j:
            print(chr(val), end=' ')
            val-=1
        else:
            print(' ',end=' ')
    print()

# 29.

# D D D D
#   C C C
#     B B
#       A

n=eval(input("Enter the value:"))
val=ord('A')+n-1
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(val), end=' ')
        else:
            print(' ',end=' ')
    val -= 1
    print()

# 30.

# Z Z Z Z
#   Y Y Y
#     X X
#       W

n=eval(input("enter the value:"))
val=ord('Z')
for i in range(n):
    for j in range(n):
        if i<=j:
            print(chr(val), end=' ')
        else:
            print(' ',end=' ')
    val-=1
    print()

# 31.

# Z Y X W
#   Z Y X
#     Z Y
#       Z

n=eval(input("enter the value:"))
for i in range(n):
    val = ord('Z')
    for j in range(n):
        if i<=j:
            print(chr(val), end=' ')
            val -= 1
        else:
            print(' ',end=' ')
    print()

# 32.

# *
#   *
#     *
#       *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==j:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()

# 33.

# 1
#   2
#     3
#       4

n=eval(input("enter the value:"))
val=1
for i in range(n):
    for j in range(n):
        if i==j:
            print(val, end=' ')
        else:
            print(' ',end=' ')
    val+=1
    print()

# 34.

# 4
#   3
#     2
#       1

n=eval(input("enter the value:"))
val=n
for i in range(n):
    for j in range(n):
        if i==j:
            print(val, end=' ')
        else:
            print(' ',end=' ')
    val-=1
    print()

# 35.

# A
#   B
#     C
#       D

n=eval(input("enter the value:"))
val=ord('A')
for i in range(n):
    for j in range(n):
        if i==j:
            print(chr(val), end=' ')
        else:
            print(' ',end=' ')
    val+=1
    print()

# 36.

# D
#   C
#     B
#       A

n=eval(input("enter the value:"))
val=ord('A')+n-1
for i in range(n):
    for j in range(n):
        if i==j:
            print(chr(val), end=' ')
        else:
            print(' ',end=' ')
    val-=1
    print()

# 37.

# Z
#   Y
#     X
#       W

n=eval(input("enter the value:"))
val=ord('Z')
for i in range(n):
    for j in range(n):
        if i==j:
            print(chr(val),end=' ')
        else:
            print(' ',end=' ')
    val-=1
    print()

# 38.

#       *
#     *
#   *
# *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 39.

# 1 $ $ $
# # 2 $ $
# # # 3 $
# # # # 4

n=eval(input("enter the value:"))
val=1
for i in range(n):
    for j in range(n):
        if i==j:
            print(val,end=' ')
        elif i>j:
            print('#',end=' ')
        else:
            print('$',end=' ')
    print()
    val+=1
    if val>9:
        val=1

# 40.

# * * * * * * * * * *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# * * * * * * * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 41.

# * * * * * * * * * *
# * *               *
# *   *             *
# *     *           *
# *       *         *
# *         *       *
# *           *     *
# *             *   *
# *               * *
# * * * * * * * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 42.

# For even it not get proper center but for odd it get proper center

# * * * * * * * * * *
# * *             * *
# *   *         *   *
# *     *     *     *
# *       * *       *
# *       * *       *
# *     *     *     *
# *   *         *   *
# * *             * *
# * * * * * * * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 43.

# * * * * * * * * * *
# * *             * *
# *   *         *   *
# *     *     *     *
# *       * *       *
# * * * * * * * * * *
# *     *     *     *
# *   *         *   *
# * *             * *
# * * * * * * * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1 or i==n//2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 44.

# * * * * * * * * * *
# * *       *     * *
# *   *     *   *   *
# *     *   * *     *
# *       * *       *
# * * * * * * * * * *
# *     *   * *     *
# *   *     *   *   *
# * *       *     * *
# * * * * * * * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1 or i==n//2 or j==n//2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 45.

# * * * * *
#     *
#     *
#     *
#     *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 46.

# * * * * * * *
#       *
#       *
#       *
#       *
#       *
# * * * * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# 47.

# * * * * * * *
#           *
#         *
#       *
#     *
#   *
# * * * * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i+j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# 48.

# 1 3 5 7
# 1 3 5 7
# 1 3 5 7
# 1 3 5 7

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
for i in range(row):
    val=1
    for j in range(col):
        print(val,end=' ')
        val+=2
    print()

# 49.

# 2 4 6 8
# 2 4 6 8
# 2 4 6 8
# 2 4 6 8

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
for i in range(row):
    val=2
    for j in range(col):
        print(val,end=' ')
        val+=2
    print()

# 50.

# Z Z Z Z
# Y Y Y Y
# X X X X
# W W W W

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
val=ord('Z')
for i in range(row):
    for j in range(col):
        print(chr(val), end=' ')
    val-=1
    print()

# 51.

# Z Y X W
# Z Y X W
# Z Y X W
# Z Y X W

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
for i in range(row):
    val=ord('Z')
    for j in range(col):
        print(chr(val),end=' ')
        val-=1
    print()

# 52.

# 2 2 2 2
# 4 4 4 4
# 6 6 6 6
# 8 8 8 8

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
val=2
for i in range(row):
    for j in range(col):
        print(val,end=' ')
    val+=2
    print()

# 53.

# A C E G
# A C E G
# A C E G
# A C E G

row=eval(input("enter the row:"))
col=eval(input("enter the col:"))
for i in range(row):
    val=ord('A')
    for j in range(col):
        print(chr(val),end=' ')
        val+=2
    print()

# 54.

#       *
#     * *
#   * * *
# * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# 55.

# * * * *
# * * *
# * *
# *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()

# 56.

#       1
#     2
#   3
# 4

n=eval(input("enter the value:"))
val=1
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(val,end=' ')
        else:
            print(' ',end=' ')
    val+=1
    print()

# 57.

#       4
#     3
#   2
# 1

n=eval(input("enter the value:"))
val=4
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(val,end=' ')
        else:
            print(' ',end=' ')
    val-=1
    print()

# 58.

#       A
#     B
#   C
# D

n=eval(input("enter the value:"))
val=ord('A')
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(chr(val),end=' ')
        else:
            print(' ',end=' ')
    val+=1
    print()

# 59.

#       D
#     C
#   B
# A

n=eval(input("enter the value:"))
val=ord('A')+n-1
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(chr(val),end=' ')
        else:
            print(' ',end=' ')
    val-=1
    print()

# 60.

#       Z
#     Y
#   X
# W

n=eval(input("enter the value:"))
val=ord('Z')
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(chr(val),end=' ')
        else:
            print(' ',end=' ')
    val-=1
    print()

# 61.

# 1 2 3 4
# 1 2 3
# 1 2
# 1

n=eval(input("enter the value:"))
for i in range(n):
    val=1
    for j in range(n):
        if i+j<=n-1:
            print(val,end=' ')
        else:
            print(' ',end=' ')
        val+=1
    print()

# 62.

# 4 3 2 1
# 4 3 2
# 4 3
# 4

n=eval(input("enter the value:"))
for i in range(n):
    val=n
    for j in range(n):
        if i+j<=n-1:
            print(val, end=' ')
        else:
            print(' ',end=' ')
        val-=1
     
    print()

# 63.

# A B C D
# A B C
# A B
# A

n=eval(input("enter the value:"))
for i in range(n):
    val=ord('A')
    for j in range(n):
        if i+j<=n-1:
            print(chr(val),end=' ')
        else:
            print(' ',end=' ')
        val+=1
    print()

# 64.

# A A A A
# B B B
# C C
# D

n=eval(input("enter the value:"))
val=ord('A')
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print(chr(val),end=' ')
        else:
            print(' ',end=' ')
    val+=1
    print()

# 65.

#       D
#     C C
#   B B B
# A A A A

n=eval(input("enter the value:"))
val=ord('A')+n-1
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print(chr(val),end=' ')
        else:
            print(' ',end=' ')
    val-=1
    print()

# 66.

#          D
#       D  C
#    D  C  B
# D  C  B  A

n=eval(input("enter the value:"))


    
    
    # DOUBT, IF ANYONE SOLVE






# 67.

#       1
#     2 2
#   3 3 3
# 4 4 4 4

n=eval(input("enter the value:"))
val=1
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print(val,end=' ')
        else:
            print(' ',end=' ')
    val+=1
    print()

# 68.

# * * * * *
# 1 1 1 1 1
# * * * * *
# 2 2 2 2 2
# * * * * *

n=eval(input("enter the value:"))
val=1
for i in range(n):
    for j in range(n):
        if i%2==0:
            print('*',end=' ')
        else:
            print(val,end=' ')
    print()
    if i%2==1:
         val+=1

# 69.

# * 1 * 2 *
# * 1 * 2 *
# * 1 * 2 *
# * 1 * 2 *
# * 1 * 2 *

n=eval(input("enter the value:"))
for i in range(n):
    val=1
    for j in range(n):
        if j%2==0:
            print('*',end=' ')
        else:
            print(val,end=' ')
            if j % 2 == 1:
                val += 1
    print()

# 70.

# * * * * *
# 1 2 3 4 5
# * * * * *
# 1 2 3 4 5
# * * * * *

n=eval(input("enter the value:"))
val=1
for i in range(n):
    for j in range(n):
        if i%2==0:
            print('*',end=' ')
        else:
            print(val,end=' ')
            if i%2==1:
                val+=1
                if val>n:
                    val=1
    print()

# 71.

# *
# 1 *
# 1 2 *
# 1 2 3 *

n=eval(input("enter the value:"))
for i in range(n):
    val=1
    for j in range(n):
        if i>j:
            print(val,end=' ')
        elif i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        val+=1
    print()

# 72.

# * $ $ $ $ $
# # * $ $ $ $
# # # * $ $ $
# # # # * $ $
# # # # # * $
# # # # # # *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i>j:
            print('#',end=' ')
        elif i==j:
            print('*',end=' ')
        else:
            print('$',end=' ')
    print()

# 73.

# * * * * * * * * * *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# *                 *
# * * * * * * * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# 74.

# * * * * * * * * * *
# * *             * *
# *   *         *   *
# *     *     *     *
# *       * *       *
# *       * *       *
# *     *     *     *
# *   *         *   *
# * *             * *
# * * * * * * * * * *

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

# 75.[doubt]

# * 1 2 3
# 1 * 1 2
# 1 2 * 3
# 1 2 3 *

n=eval(input("enter the value:"))
val1=1
for i in range(n):
    val2=1
    for j in range(n):
        if i>j:
            print(val2,end=' ')
            val2+=1
        elif i==j:
            print('*',end=' ')
        else:
            print(val1,end=' ')
            val1 += 1
    print()
    if val1 >= n:
        val1 = 1

# 76.

# 1
#   *
#     2
#       *

n=eval(input("enter the value:"))
val=1
for i in range(n):
    for j in range(n):
        if i==j and i%2==1:
            print('*',end=' ')
        elif i==j and i%2==0:
            print(val,end=' ')
        else:
            print(' ',end=' ')
    if i%2==0:
        val+=1
    print()

# 77.

#       A
#     *
#   B
# *

n=eval(input("enter the value:"))
val=ord('A')
for i in range(n):
    for j in range(n):
        if i+j==n-1 and i%2==0:
            print(chr(val),end=' ')
        elif i+j==n-1 and i%2==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    if i%2==0:
        val+=1
    print()

# 78. [doubt]

# A 4 3 2
# 4 B 3 2
# 4 3 C 2
# 4 3 2 D

n=eval(input("enter the value:"))
val1=ord('A')
for i in range(n):
    val2=n
    for j in range(n):
        if i==j:
            print(chr(val1),end=' ')
        elif i>j:
            print(val2,end=' ')
            val2 -= 1
        else:
            print(val2,end=' ')
            val2-=1
    val1 += 1
    print()

# 79.

# $ $ $ $
#   1 2 3
#     $ $
#       1

n=eval(input("enter the value:"))
val1=1
for i in range(n):
    val2 = 2
    for j in range(n):
        if i==j and i%2==0:
            print('$',end=' ')
        elif i==j and i%2==1:
            print(val1,end=' ')
        elif i<j and i%2==0:
            print('$',end=' ')
        elif i<j and i%2==1:
            print(val2,end=' ')
            val2+=1
        else:
            print(' ',end=' ')
    print()

# 80.

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

n=eval(input("enter the value:"))
str=1
spa=n-1
for i in range(n):
    for j in range(spa):
        print(' ',end=' ')
    for k in range(str):
        print('*',end=' ')
    print()
    str+=2
    spa-=1

#                                                  OR

n=eval(input("enter the value:"))
str=1
spa=n-1
for i in range(n):
    print("  "*spa+"* "*str)
    str+=2
    spa-=1

                                                #   OR

n=eval(input("enter the value:"))
for i in range(n):
    for j in range(n-1-i):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()

#                                                     OR

n=eval(input("enter the value:"))
for i in range(n):
    print("  "*(n-i-1)+"* "*(2*i+1))

# 81.

#         1
#       2 2 2
#     3 3 3 3 3
#   4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5

n=eval(input("enter the value:"))
str=1
val=1
spa=n-1
for i in range(n):
    for j in range(spa):
        print(' ',end=' ')
    for k in range(str):
        print(val,end=' ')
    print()
    spa-=1
    str+=2
    val+=1
    if val>9:
        val=1


#                                                               OR

n=eval(input("enter the value:"))
val=1
for i in range(n):
    print('  '*(n-i-1)+(str(val)+' ')*(2*i+1))
    val+=1
    if val>9:
        val=1


# 82.

#         A
#       B B B
#     C C C C C
#   D D D D D D D
# E E E E E E E E E

n=eval(input("enter the value:"))
str=1
val=ord('A')
spa=n-1
for i in range(n):
    for j in range(spa):
        print(' ',end=' ')
    for k in range(str):
        print(chr(val),end=' ')
    print()
    spa-=1
    str+=2
    val+=1
    if val>ord('Z'):
        val=ord('A')

#                                                               OR

n=eval(input("enter the value:"))
val=ord('A')
for i in range(n):
    print('  '*(n-i-1)+(chr(val)+' ')*(2*i+1))
    val+=1
    if val>ord('Z'):
        val=ord('A')


# 83.

#         A
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I

n=eval(input("enter the value:"))
str=1
spa=n-1
for i in range(n):
    val = ord('A')
    for j in range(spa):
        print(' ',end=' ')
    for k in range(str):
        print(chr(val),end=' ')
        val += 1
        if val > ord('Z'):
            val = ord('A')
    print()
    spa-=1
    str+=2

# 84.

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

n=eval(input("enter the value:"))
str=2*n-1
spa=0
for i in range(n):
    for j in range(spa):
        print(' ',end=' ')
    for k in range(str):
        print('*',end=' ')
    print()
    str-=2
    spa+=1

# *=> A - Z PATTERNS

# 85. WAP  To print the pattern of alphabet A ?

# Enter the Value:5

#   * * *
# *       *
# * * * * *
# *       *
# *       *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if ((j==0 or j==n-1) and i!=0) or (i==0 and (j>0 and j<n-1)) or i==n//2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 86. WAP  To print the pattern of alphabet B ?

# Enter the Value:5

# * * * *
# *       *
# * * * *
# *       *
# * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if j==0 or (j==n-1 and (i!=n-1 and i!=0 and i!=n//2)) or ((i==0 or i==n//2 or i==n-1 )and j!=n-1) :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 87. WAP  To print the pattern of alphabet C ?

# Enter the Value:5

#   * * * *
# *
# *
# *
#   * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if (j==0 and (i!=0 and i!=n-1)) or ((i==0 or i==n-1) and j!=0):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 88. WAP  To print the pattern of alphabet D ?

# Enter the Value:5

# * * * *
# *       *
# *       *
# *       *
# * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if j==0 or (j==n-1 and (i!=0 and i!=n-1)) or ((i==0 or i==n-1) and j!=n-1):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 89. WAP  To print the pattern of alphabet E ?

# Enter the Value:5

# * * * * *
# *
# * * * * *
# *
# * * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or i==n-1 or j==0:
            print("*",end=" ")
        else:
            print(end=" ")
    print()

# 90. WAP  To print the pattern of alphabet F ?

# Enter the Value:5

# * * * * *
# *
# * * * * *
# *
# *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or j==0:
            print("*",end=" ")
        else:
            print(end=" ")
    print()

# 91. WAP  To print the pattern of alphabet G ?

# Enter the Value:5

# * * * * *
# *
# *     * * *
# *       *
# * * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n+1):
        if j==0 or ((i==0 or i==n-1 ) and j<n) or (j==n-1 and (i>=n//2 and i<=n-1)) or (i==n//2 and (j==n-2 or j==n)):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 92. WAP  To print the pattern of alphabet H ?

# Enter the Value:5

# *       *
# *       *
# * * * * *
# *       *
# *       *

n = eval(input("Enter the value:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 93. WAP  To print the pattern of alphabet I ?

# Enter the Value:5

# * * * * *
#     *
#     *
#     *
# * * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if j==n//2 or i==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 94. WAP  To print the pattern of alphabet J ?

# Enter the Value:5

# * * * * *
#     *
#     *
#     *
# * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or (i==n-1 and (j>=0 and j<=n//2)):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 95. WAP  To print the pattern of alphabet K ?

# Enter the Value:5

# *       *
# *     *
# *   *
# * *
# *   *
# *     *
# *       *

n = eval(input("Enter the Value:"))
row=0
col=n-1
for i in range(n+2):
    for j in range(n):
        if j==0 or (i==j+2 and j>1):
            print("*",end=' ')
        elif ((i==row and j==col) and j>0):
            print("*",end=' ')
            row+=1
            col-=1
        else:
            print(" ",end=' ')
    print()

# 96. WAP  To print the pattern of alphabet L ?

# Enter the value:5

# *
# *
# *
# *
# * * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 97. WAP  To print the pattern of alphabet M ?

# Enter the value:5

# *       *
# * *   * *
# *   *   *
# *       *
# *       *

n = eval(input("Enter the value:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=n//2):
            print("*",end=' ')
        elif (i+j==n-1 and j>n//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 98. WAP  To print the pattern of alphabet N ?

# Enter the Value:5

# *       *
# * *     *
# *   *   *
# *     * *
# *       *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 99. WAP  To print the pattern of alphabet O ?

# Enter the Value:5

#   * * *
# *       *
# *       *
# *       *
#   * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if ((j==0 or j==n-1) and (i!=0 and i!=n-1)) or ((i==0 or i==n-1) and (j!=0 and j!=n-1)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 100. WAP  To print the pattern of alphabet P ?

# Enter the Value:5

# * * * *
# *       *
# * * * *
# *
# *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if j==0 or ((i==0 or i==n//2) and j!=n-1) or (j==n-1 and (i>0 and i<n//2)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 101. WAP  To print the pattern of alphabet Q ?

# Enter the Value:5

#   * * *
# *       *
# *       *
# * *     *
#   * * *
#       *

n = eval(input("Enter the Value:"))
for i in range(n+1):
    for j in range(n):
        if ((j==0 or j==n-1) and (i>0 and i<n-1)) or ((i==0 or i==n-1) and (j>0 and j<n-1)) or (i==n-2 and (j>0 and j<n//2)) or (i==n and (j>n//2 and j<n-1)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 102. WAP  To print the pattern of alphabet R ?

# Enter the Value:5

# * * * *
# *       *
# * * * *
# *       *
# *       *
# *       *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if j==0 or (j==n-1 and (i!=0 and i!=n//2)) or ((i==0 or i==n//2) and j!=n-1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 103. WAP  To print the pattern of alphabet S ?

# Enter the Value:5

#   * * *
# *
#   * * *
#         *
#   * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if (j==0 and (i>0 and i<n//2)) or (j==n-1 and (i>n//2 and i<n-1)) or ((i==0 or i==n//2 or i==n-1) and (j>0 and j<n-1)):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 104. WAP  To print the pattern of alphabet T ?

# Enter the Value:5

# * * * * *
#     *
#     *
#     *
#     *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 105. WAP  To print the pattern of alphabet U ?

# Enter the Value:5

# *       *
# *       *
# *       *
# *       *
#   * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if ((j==0 or j==n-1) and i!=n-1) or (i==n-1 and (j>0 and j<n-1)):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 106. WAP  To print the pattern of alphabet V ?

# *          *
#   *      *
#     *  *
#       *

row=0
col=6
for i in range(4):
    for j in range(7):
        if i==j:
            print("*",end='')
        elif i==row and j==col:
            print("*",end=' ')
            row+=1
            col-=1
        else:
            print(" ",end=' ')
    print()

# 107. WAP  To print the pattern of alphabet W ?

# Enter the Value:5

# *       *
# *       *
# *   *   *
# * *   * *
# *       *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if (j==0 or j==n-1) or (j==i and i>=n//2):
            print("*",end=' ')
        elif (i+j==n-1 and i>=n//2):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 108. WAP  To print the pattern of alphabet X ?

# Enter the Value:5

# *       *
#   *   *
#     *
#   *   *
# *       *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 109. WAP  To print the pattern of alphabet Y ?

# Enter the Value:5

# *       *
#   *   *
#     *
#     *
#     *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if (i==j and i<n//2) or (i+j==n-1 and i<n//2) or (j==n//2 and i>=n//2):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 110. WAP  To print the pattern of alphabet Z ?

# Enter the Value:5

# * * * * *
#       *
#     *
#   *
# * * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i==0 or i+j==n-1 or i==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 111. WAP to Binary_alternate ?

# Enter the Value:5

# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1
# 0 1 0 1 0
# 1 0 1 0 1

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if (i%2==1 and j%2==1) or (i%2==0 and j%2==0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

# 112. WAP to Binary_even_odd_rows ?

# Enter the Value:5

# 0 0 0 0 0
# 1 1 1 1 1
# 0 0 0 0 0
# 1 1 1 1 1
# 0 0 0 0 0

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i%2==0:
            print("0",end=' ')
        else:
            print("1",end=' ')
    print()

# 113. WAP to Hollow_pattern or hollow_RAT[Right-Angled Triangle]  ?

# Enter the Value:5

#         *
#       * *
#     *   *
#   *     *
# * * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i==n-1 or j==n-1 or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 114. WAP to alpha_increasing ?

# Enter the Value: 5

# A
# B B
# C C C
# D D D D
# E E E E E

n = eval(input("Enter the Value: "))
val = ord("A")
for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(val),end=' ')
        else:
            print(' ',end=' ')
    print()
    val+=1

# 115. WAP to basic_pattern_1 ?

# Enter the Value:5

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()

# 116. WAP to basic_pattern_2 ?

# Enter the Value:5

# *
# * *
# * * *
# * * * *
# * * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 117. WAP to pyramid ?

# Enter the Value:5

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

n = eval(input("Enter the Value:"))
str = 1
spa = n-1
for i in range(n):
    for j in range(spa):
        print(" ",end=' ')
    for k in range(str):
        print("*",end=' ')
    print()
    str+=2
    spa-=1

# 118. WAP to inverted_R_A_T[Right-Angled Triangle]. ?

# Enter the Value:5

# * * * * *
# * * * *
# * * *
# * *
# *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 119. WAP to hr_pyramid ?

# Enter the Value:5

# *
#
# **
#
# ***
#
# ****
#
# *****

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end='')
    print('\n')

# 120. WAP to hollow_equil Triangle ?

# Enter the Value:5

#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

n = eval(input("Enter the Value:"))
str = 1
spa = n-1
for i in range(n):
    for j in range(spa):
        print(" ",end=' ')
    for k in range(str):
        if i == n-1 or k == 0 or k == str-1:
            print('*',end=' ')
        else:
            print(" ",end=' ')
    print()
    str+=2
    spa-=1

# 121.WAP to hollow_diamond ?

#       *
#     *   *
#   *       *
# *           *
#   *       *
#     *   *
#       *

for i in range(7):
    for j in range(7):
        if i+j==3 or i-j==3 or j-i==3 or i+j==9:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 122. WAP to half_sand_clock ?

# Enter the Value:5

# * * * * *
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *

n = eval(input("Enter the Value:"))
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

for i in range(1,n):
    for j in range(n):
        if i>=j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

# 123. WAP to pyramid pattern?

# Enter the Value:5

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = eval(input("Enter the Value:"))

# Top half (increasing pattern)

for i in range(1, n+1):
    for j in  range(i):
        print("*",end=' ')
    print()

# Bottom half (decreasing pattern)

for i in range(n-1, 0, -1):
    for j in range(i):
        print("*",end=' ')
    print()

# 124. WAP to pyramid pattern or cross_pyramid_increasing.?

# Enter the Number:5

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

n = eval(input("Enter the Number:"))

# Top half (increasing pattern)

for i in range(1, n+1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(i):
        print("*",end=' ')
    print()

# Bottom half (decreasing pattern)

for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ",end=' ')
    for k in range(i):
        print("*",end=' ')
    print()

