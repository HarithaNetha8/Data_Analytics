# lst=[1,2,3,4,5,6,7,8]
# # print(lst)
# # lst.append(9)
# print(lst)
# # lst.remove(5)
# # print(lst)
# # lst.pop()
# print(lst)
# # lst.reverse()
# # print(lst)
# lst1=['haritha',22,'hyderabad']
# print(lst1[0])
# # print(lst1[-1])
# print(lst[::-1])
# print(lst[1:])
# print(lst[:2])
# print(lst[4:6])
# lst.insert(2,50)
# print(lst)

# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))
# print(sorted(lst))

# arr=[10,20,30]
# for i in arr :
#     print(i)

# for i in range(len(arr)):
#     print(arr[i])
#     \

#     #list compreension

# sq=[x*x for x in range(5)]
# print(sq)


#reversin array
# lst=[2,4,7,3,9,1]
# left=0
# r=len(lst)-1
# while left<r:
#     lst[left],lst[r] =lst[r], lst[left]
#     left+=1
#     r-=1
# print(lst)

#second larest element
# lst=[2,4,7,3,9,1]
# first=0
# second=0

# for i in lst:
#     if i>first:
#         second=first
#         first=i

#     elif i>second and i!=first:
#         second=i
# print(second)

#frequencyelement
lst=[2,4,7,3,9,1,2,3,7,3]
frq={}
for i in lst:
    if i in frq:
        frq[i]+=1
    else:
        frq[i]=1
print(frq)

#remove duplicates
lst=[2,4,7,3,9,1,2,3,7,3]
result=[]

for i in lst:
    if i not in result:
        result.append(i)
print(result)
