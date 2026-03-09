# 1)REVERSE A STRING 

# s='GOOD MORNING'
# # print(s[::-1])
# result=''
# for i in s:
#     result=i+result
# print(result)


# 2)CHECK IF STRING IS PALINDROME OR NOT

# s='madam'
# if s==s[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# 3) COUNT VOWELS AND CONSONENTS

# s='GOOD MORNING'
# vowels='aeiouAEIOU'
# v=0
# c=0
# for char in s:
#     if char in vowels:
#         v+=1
#     else:
#         c+=1
# print('vowels:',v)
# print('consonents:',c)

# 4) COUNT CHARACTER FREQUENCE
# s='GOOD MORNING'
# frq={}
# for char in s:
#     frq[char]=frq.get(char,0)+1
# print(frq)

# 5) REMOVE SPACE FROM STRING 
s='GOOD MORNING everyone welcome to python programming'
# res=''
# for char in s:
#     if char!=' ':
#         res+=char
# print(res)

# 6) COUNT NUMBER OF WORDS IN SENTENCE 
# s='hello everyone this is haritha macharla'
# count=1
# for char in s:
#     if char == ' ':
#         count+=1
# print(count)

# 7) FIND FIRST NON REPEATING CHAR
# s='haritha macharla'
# frq={}
# for char in s:
#     frq[char]=frq.get(char,0)+1
# for char in s:
#     if frq[char]==1:
#         print(char)
#         break

# 8) REMOVE DUPLICATES CHARACTER FROM STRING 
# s='hello world'
# res=''
# for i in s:
#     if i not in res:
#         res+=i
# print(res)

# 9) FIND LONGEST WORD IN SENTENCE
# s='hello everyone this is haritha macharla'
# words=s.split() // split function is used to split the string into a list of words based on whitespace
# longest=words[0] // we initialize longest with the first word in the list, assuming it is the longest word initially
# for word in words: // we iterate through each word in the list of words
#     if len(word)>len(longest): // we compare the length of the current word with the length of the longest word found so far
#         longest=word // if the current word is longer than the longest word, we update longest to be the current word
# print(longest)

# 10) CHECK ANAGRAM IN PYTHON
# s='listen'
# t='silent'
# print(sorted(s)==sorted(t))

# 11) CHECK SUBSTRING IN STRING
# s='hello everyone this is haritha macharla'
# sub='haritha'
# if sub in s:
#     print('substring found')
# else:
#     print('substring not found')

# 12) REVERSE WORDS IN A SENTENCE
# s='hello everyone this is haritha macharla'
# print(' '.join(s.split()[::-1])) 

# # we split the string into a list of words using split(), reverse the list of words using [::-1], and then join the reversed list back into a string with spaces in between using ' '.join()


# 13) CHECK IF STRING IS ROTATION OF ANOTHER STRING
s='hello world'
# t='worldhello'
# if len(s)==len(t) and s in t+t:
#   we check if the length of both strings is the same and if s is a substring of t concatenated with itself (t+t). If both conditions are true, then s is a rotation of t.
#     print('s is rotation of t')
# else :
#     print('s is not rotation of t')

# 14) CHECK IF STRING IS PANGRAM OR NOT
# s='The quick brown fox jumps over the lazy dog'
# s=s.lower()
# set_s=set(s)
# alphabet=set('abcdefghijklmnopqrstuvwxyz') 
# if alphabet.issubset(set_s):
#     print('The string is a pangram.')
# else:
#     print('The string is not a pangram.')
