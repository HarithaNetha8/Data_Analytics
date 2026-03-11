# #pattern 1 : SQUARE PATTERN 
# N=5
# for i in range(N):
#     for j in range(N):
#         print("*", end=" ")
#     print()
# print()


# #Pattern 2 : RIGHT ANGLED TRIANGLE
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
# print()


# #Pattern 3 : REVERSE TRIANGLE
# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()
# print()


# #Pattern 4 : NUMBER TRIANGLE
# n=5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
# print()


# #Pattern 5 : SAME NUMBER TRIANGLE
# n=5
# for i in range(1, n+1):
#     for j in range(i):
#         print(i, end=" ")
#     print()
# print()


# #Pattern 6 : ALPHABET PATTERN
# n=5
# for i in range(1, n+1):
#     for j in range(i):
#         print(chr(66 + j - 1), end=" ")
#     print()
# print()



# #Pattern 7 : REVERSE ALPHABET PATTERN
# n=5
# for i in range(n):
#     for j in range(n-1-i):
#         print(chr(66 + j - 1), end=" ")
#     print()
# print()

# #practice problems

# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10
# n=4
# num=1
# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end=" ")
#         num+=1
#     print()
# print()

# # A 
# # B B
# # C C C
# # D D D D

# n=4
# for i in range(1, n+1):
#     for j in range(i):
#         print(chr(65 + i - 1), end=" ")
#     print()
# print()

# # 1
# # 2 1
# # 3 2 1
# # 4 3 2 1

# n=5
# for i in range(1, n+1):
#     for j in range(i, 0, -1): # i=1, j=1; i=2, j=2,1; i=3, j=3,2,1; i=4, j=4,3,2,1
#         print(j, end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(n-i-1):
#         print(j,end=' ')
#     print()

# PYRAMID PATTERN
n=5
for i in range(1, n+1):
        print(" "*(n-i) + "*" *(2*i-1))

# RIGHT PYRAMID PATTERN
n=5
for i in range(n, 0, -1):
        print(" "*(n-i) + "*" *(2*i-1))
print()
# # DIAMOND PATTERN
# n=5
# for i in range(1, n+1):
#         print(" "*(n-i) + "*" *(2*i-1))

# for i in range(n, 0, -1):
#         print(" "*(n-i) + "*" *(2*i-1))

# HOLLOW SQUARE PATTERN
n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# FLOYD'S TRIANGLE
n=5
num=1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()
print()


# NUMBER PYRAMID
n=5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end="")
    for j in range(i-1, 0, -1):
        print(j, end="")
    print()


# *
# * *
# * * *
# * * * *
# * * *
# * * 
# *
n=5
for i in range(1, n+1):
    print("* " * i)
for i in range(n-1, 0, -1):
    print("* " * i)


# 1
# 22
# 333
# 4444
n=5
for i in range(1, n+1):
    print(str(i) * i) #



# A
# A B A 
# A B C B A 
# A B C D C B A
n=5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64 + j), end="")
    for j in range(i-1, 0, -1):
        print(chr(64 + j), end="")
    print()



# *
# * *
# *   *
# *     *
# * * * * *
n=5
for i in range(1, n+1):
    for j in range(1, i+1):
        if j==1 or j==i or i==n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

