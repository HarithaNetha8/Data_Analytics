# CHECK IF A  STTRING CONTAIN ONLY NUMBERS
# s='1d34i678'
# if s.isdigit():
#     print("The string contains only numbers.")
# else:
#     print("The string does not contain only numbers.")

# #COUNT UPPERCASE AND LOWERCAS LETTERS
# s='GOOD MORNING everyone welcome to python programming'
# ucount=0
# lcount=0
# for i in s:
#     if i == i.upper():
#         ucount+=1
#     else:
#         lcount+=1

# print(ucount,lcount)

#FIND THE MOST FREQ CHARACTER IN A ASTRING
# s='hello everyone this is haritha macharla'
# frq={}
# for i in s:
#     frq[i]=frq.get(i,0)+1
#     max_frq=0
#     max_char=''
#     for char,count in frq.items(): # char is the key and count is the value
#         if count>max_frq:
#             max_frq=count
#             max_char=char
# print(f"The most frequent character is '{max_char}' with a frequency of {max_frq}")

#REVERSE EACH WORD IN A SENTENE
# s='data analytics'
# words=s.split()
# print(words)
# result=[]
# for word in words:
#     result.append(word[::-1])
#     print(result)
# print(' '.join(result))

#CAPTILIZE FIRST LETTER OF EVERY WORD
s='hello everyone'
words=s.split()
result=[]
for word in words:
    result.append(word.capitalize())
print(' '.join(result))
