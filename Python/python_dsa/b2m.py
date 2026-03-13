# 1️⃣ Arrays / Lists Practice
# Basic

# # Find largest element in list
# arr=[24,13,8,76,54,32,22]
# max=0
# for i in range(len(arr)):
#     if arr[i] > max:
#         max=arr[i]
# print(max)

# # Find smallest element
# arr=[24,13,8,76,54,32,22]
# min=arr[0]
# for i in range(len(arr)):
#     if arr[i] < min:
#         min=arr[i]
# print(min)

# # Find sum of elements
# arr=[24,13,8,76,54,32,22]
# sum=0
# for i in range(len(arr)):
#     sum+=arr[i]
# print(sum)

# # Reverse a list
# arr=[24,13,8,76,54,32,22]
# print(arr[::-1])

# # Check if array is sorted
# arr=[24,13,8,76,54,32,22]
# if arr.sort()==arr:
#     print("sorted")

# print(" not sorted")

# Example

# arr = [4, 2, 9, 1]
# Intermediate

# # Find second largest element
# arr = [4, 2, 9, 1]
# arr.sort()
# n=len(arr)
# print(arr[n-2])

# # Move all zeros to end
# arr=[0,1,0,3,2]
# res=[]
# for i in range(len(arr)):
#     if arr[i]!=0:
#         res.append(arr[i])
# print(res + len(res)*[0])


# # Remove duplicates from list
# arr=[1,2,2,3,1]
# res=[]
# for i in range(len(arr)):
#     if arr[i] not in res:
#         res.append(arr[i])

# print(res)


# # Find missing number
# arr=[1,2,3,5]
# n=len(arr)+1
# total =n*(n+1)//2
# print(total- sum(arr))


# # Find duplicates in array
# arr=[1,2,3,4,2,5,6,3]
# frq={}
# for num in arr:
#     frq[num]=frq.get(num,0)+1
# duplicates=[num for num, count in frq.items() if count>1]
# print("Duplicate elements:", duplicates)



# 2️⃣ Strings Practice
# Basic

# # Reverse a string
# str="Hello, World!"
# reversed_str=str[::-1]
# print(reversed_str)


# # Check palindrome
# str="madam"
# if str==str[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# # Count vowels and consonants
# vowel_count=0
# consonant_count=0
# vowels='aeiouAEIOU'
# s='hello everyone'
# for char in s:
#     if char in vowels:
#         vowel_count+=1
#     elif char.isalpha():
#         consonant_count+=1
# print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")


# # Remove spaces from string
# s='hello everyone'
# s=s.replace(" ","")
# print(s)


# # Count frequency of characters
# s='hello world'
# freq={}
# for ch in s:
#     freq[ch]=freq.get(ch,0)+1
# print("Frequency of characters:", freq)



# Intermediate
# =======================
# # Check anagram
# s1='listen'
# s2='silent'
# if sorted(s1)==sorted(s2):
#     print("Anagram")
# else:
#     print("not anagram")


# First non-repeating character
# s='hello everyone this is haritha macharla'
# frq={}
# for i in s:
#     frq[i]=frq.get(i,0)+1
# first_non_repeating=''
# for char in s:
#     if frq[char]==1:
#         first_non_repeating=char
#         break
# print(f"The first non-repeating character is '{first_non_repeating}'")


# # Remove duplicate characters
# s='hello everyone this is haritha macharla'
# unique_chars=''
# for char in s:
#     if char not in unique_chars:
#         unique_chars+=char
# print(unique_chars)

# "programming"
# → progamin

# # Find longest word in sentence
# s='hello everyone this is haritha macharla'
# words=s.split()
# longest_word=''
# for word in words:
#     if len(word)>len(longest_word):
#         longest_word=word
# print(f"The longest word is '{longest_word}'")


# # Reverse each word in sentence
# s='hello everyone this is haritha macharla'
# words=s.split()
# result=[]
# for word in words:
#     result.append(word[::-1])
# print(" ".join(result))


# Number Problems
# Basic

# Reverse a number

# 1234 → 4321

# Count digits

# Sum of digits

# Check palindrome number

# Find largest digit

# Intermediate

# Check prime number

# Find factorial

# Print Fibonacci series

# Check Armstrong number

# Check perfect number

# 4️⃣ Pattern Practice

# Practice printing patterns using loops.

# Example 1

# *
# **
# ***
# ****

# Example 2

# ****
# ***
# **
# *

# Example 3

#    *
#   ***
#  *****
# *******

# Example 4

# 1
# 12
# 123
# 1234

# Example 5

# A
# AB
# ABC
# ABCD


# 5️⃣ Mixed Logic Problems

# These are most important for coding rounds.

# Two Sum problem

# Example

# [2,7,11,15]
# target = 9

# Find intersection of two arrays

# [1,2,3]
# [2,3,4]
# → [2,3]

# Find element with highest frequency

# Find first repeating element

# Rotate array by k positions

# Example

# [1,2,3,4,5]
# k = 2
# → [4,5,1,2,3]
