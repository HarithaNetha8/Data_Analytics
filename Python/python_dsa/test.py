# arr=[2,3,7,4,9]
# tar=7
# seen={}
# for num in arr:
#     if tar-num in seen:
#         print("pair found", num, tar-num)
#     seen[num]=True


# seen = {}
# for num in arr:
#     complement = tar - num
#     if complement in seen:
#         print(complement, num)
#     seen[num] = True

# # Find Missing Number
# arr=[1,2,3,5,6,7,8]
# n=len(arr)
# total =n*(n+1)//2
# print(total- sum(arr))

# Check Anagram (Without Sorting)
# from itertools import count


# str1="listen"
# str2="silent"
# if len(str1) != len(str2):
#     print("Not anagrams")
# else:
#     freq={}
#     for ch in str1:
#         freq[ch]=freq.get(ch,0)+1
#     for ch in str2:
#         if ch not in freq or freq[ch]==0:
#             print("Not anagrams")
#             break
#         freq[ch]-=1
#     else:
#         print("Anagrams")

# # Find Duplicate Elements in Array
# arr=[1,2,3,4,2,5,6,3]
# frq={}
# for num in arr:
#     frq[num]=frq.get(num,0)+1
# duplicates=[num for num, count in frq.items() if count>1]
# print("Duplicate elements:", duplicates)


# # Find Maximum Element in Array
# arr=[2,4,9,6,2]
# max=0
# for num in arr:
#     if num>max:
#         max=num
# print("Maximum element:", max)


# # Reverse a string without slicing
# str="Hello, World!"
# reversed_str=""
# for i in range(len(str)-1, -1, -1):
#     reversed_str+=str[i]
# print("Reversed string:", reversed_str)


# # Find intersection of two arrays
# arr1=[1,2,3,4,5]
# arr2=[4,5,6,7,8]
# intersection=set(arr1) & set(arr2)
# print("Intersection:", intersection)


# # Find largest and smallest element
# arr=[3,5,1,9,2]
# largest=arr[0]
# smallest=arr[0]
# for num in arr:
#     if num>largest:
#         largest=num
#     elif num<smallest:
#         smallest=num
# print("Largest element:", largest)
# print("Smallest element:", smallest)


# # Count frequency of characters in string
# str="hello world"
# freq={}
# for ch in str:
#     freq[ch]=freq.get(ch,0)+1
# print("Frequency of characters:", freq)


# # Palindrome string
# str="A man a plan a canal Panama"
# cleaned_str=str.replace(" ","").lower()
# if cleaned_str==cleaned_str[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")
