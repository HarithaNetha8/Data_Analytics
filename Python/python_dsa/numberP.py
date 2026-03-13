# # 1) REVERSE A NUMBER
# N=12345
# r=0
# while N>0:
#     d=N%10
#     r=r*10+d
#     N=N//10
# print("The reverse of the number is:",r)


# # 2) CHECK THE NUMB IS PALINDROME OR not
# N=121
# r=0
# value=N
# while N>0:
#     d=N%10
#     r=r*10+d
#     N=N//10
# if value==r:
#     print('te numb is palindrome')
# else :
#     print('te numb is not palindrome')


# # 3) COUNT DIGITS IN A NUMBER
# n=12134
# cnt=0
# while n>0:
#     cnt+=1
#     n=n//10
# print(cnt)


# # 4) CHECK hIF A NUMBER IS ARMSTRONG NUMBER OR NOT
# N=153
# value=N
# sum=0
# while N>0:
#     r=N%10
#     sum+=r ** 3
#     N=N//10

# if sum==value:
#     print('ARMSTRONG')
# else :
#     print(' not ARMSTRONG')


# 5) CHECK IF A NUMBER IS PRIME OR NOT
# n=6
# for i in range(2,int(n**0.5)+1):
#     if n % i ==0:
#         print('not a prime')
#     else :
#         print('prime')


# # 6) FIND THE FACTORS OF A NUMBER
# n=10
# for i in range(1,n+1):
#     if n% i==0:
#         print(i,end=' ')


# # 7) FIND THE GCD OF TWO NUMBERS
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
# print(gcd(48,18))


# # 8) FIND THE LCM OF TWO NUMBERS
# def lcm(a, b):
#     return (a * b) // gcd(a, b)
# print(lcm(48,18))

# # 9) CHECK IF A NUMBER IS PERFECT NUMBER OR NOT
# n=28
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print('perfect number')
# else:
#      print('not perfect number')


# # 10) CHECK IF A NUMBER IS A POWER OF 2 OR NOT
# n=14
# if n == 2**int(n**0.5):
#     print('power of 2')
# else:
#     print('not power of 2')



# # 11) SUM OF DIGITS IN A NUMBER
# n=12345
# sum=0
# while n>0:
#     sum+=n%10
#     n=n//10
# print(sum)


# 12) FACTORIAL OF A NUMBER
# n=5
# fact=1
# for i in range(1,n):
#     fact+=fact*i

# print(fact)


# 13) FIBONACCI SERIES UP TO N TERMS
# n=10
# a=0
# b=1
# print(a,b,end=' ')
# for i in range(2,n):
#     c=a+b
#     print(c,end=' ')
#     a=b
#     b=c


# # 14) LARGEST DIGIT IN A NUMBER
# n=1987
# la=0
# while n >0:
#     d=n%10
#     if d>la:
#         la=d
#     n=n//10
# print(la)


# # 15) REMOVE LAST DIGIT FROM A NUMBER
# n=1456
# n=n//10
# print(n)


# # 16) STRONG NUMBER OR NOT
# n=145
# value=n
# sum=0
# while n>0:
#     fact=1
#     d=n%10
#     for i in range(1,d+1):
#         fact*=i
#     sum+=fact
#     n=n//10
# if sum==value:
#     print('strong number')
# else:
#     print('not strong number')


# # 17) EVEN OR ODD NUMBER
# n=5
# if n%2==0:
#     print('even number')
# else :
    # print('odd number')


# # 18) SUM OF FIRST N NATURAL NUMBERS
# n=10
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)


# 19) ALL PRIME BETWEEN TWO NUMBERS
# n1=10
# n2=50
# for num in range(n1, n2 + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=' ')
    


# # 20) FIND THE SQUARE OF A NUMBER
# n=4
# print(n**2)


# # 21) NUMBER IS HARSHAD NUMBER OR NOT
# n=18
# value=n%10 
# s=0
# s+=value
# n=n//10
# if value%s==0:
#     print('harshad number')
# else:
#     print('not harshad number')
