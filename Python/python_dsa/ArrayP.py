# #nested loops
# arr=[1,4,8,2,9,4,2]
# for i in arr:
#     for j in arr:
#         if i%2==0 and j%2==0:
#             print(i,j)

# #frequency countin
# -> dictonary
# -> nested loops

# #duplicateselements findin ->witout set

# ----------------PROBLEMS ON ARRAYS DAY 2 AND 3-------------------------------

# # 1) COUNT  FREQ OF EACH ELEMENT
# arr=[2,9,3,7,4,2,8,3]
# frq={}
# for num in arr:
#     if num in frq:
#         frq[num]+=1
#     else:
#         frq[num]=1
# print(frq)


# # 2)REMOVE DUPLICATES FROM ARRAY
# arr=[2,9,3,7,4,2,8,3,7]
# res=[]
# for num in arr:
#     if num not in res:
#         res.append(num)
# print(res)

# # 3) SECOND LARGEST ELEMENT IN AN ARRAY
# arr=[2,9,3,7,4,2,8,3,7]
# first=0
# second=0
# for num in arr:
#     if num>first:
#         second=first
#         first=num
#     elif num>second and num!=first:
#         second=num
# print(second)

# # 4) SECOND SMALLEST ELEMENT IN AN ARRAY
# arr=[2,9,3,7,4,2,8,3,7]
# first=float('inf')
# second=float('inf')
# for num in arr:
#     if num<first:
#         second=first
#         first=num
#     elif num<second and num!=first:
#         second=num
# print(second)

# # 5)CHECK IF ARRAY IS SORTED OR NOT
# arr=[2,6,8,9]
# for i in range(len(arr)-1):
#     if arr[i]>arr[i+1]:
#         print('not sorted')
#         break
# else:
#     print('sorted')

# # 6)MOVE ALL ZEROS TO END OF ARRAY
# arr=[0,6,0,9,3,0,2,4,8]
# res=[]
# for i in range(len(arr)-1):
#     if arr[i]!=0:
#         res.append(arr[i])
# for i in range(len(arr)-1):
#     if arr[i]==0:
#         res.append(arr[i])
# print(res)

# arr=[0,6,0,9,3,0,2,4,8]
# res=[]
# for i in range(len(arr)-1):
#     if arr[i]!=0:
#         res.append(arr[i])

# print(res,[0]*(len(arr)-len(res)))

# # 7)FIND DUPLICATE ELEMENTS IN AN ARRAY
# arr=[2,6,4,9,3,9,7,4,8]
# res=[]
# for i in range(len(arr)):
#     if arr[i] in res:
#         print(arr[i])
#     else:
#         res.append(arr[i])    

# # 8)FIND ELEMENT WITH HIGHEST FREQUENCY IN AN ARRAY
# arr=[2,3,4,5,6,2,3,4,2,3,2,2]
# frq={}
# for num in arr:
#     if num in frq:
#         frq[num]+=1
#     else:
#         frq[num]=1
# max_frq=0
# res=None
# for key in frq:
#     if frq[key]>max_frq:
#         max_frq=frq[key]
#         res=key
# print(res)

# # 9)FIND FIRST REPEATING ELEMENT IN AN ARRAY
# arr=[2,3,4,5,6,2,3,4,2,3,2,2]
# res=[]
# for num in arr:
#     if num in res:
#         print(num)
#         break
#     else:
#         res.append(num)
# else:
#     print('no repeating element')

# DAY 3-------ADVANCE PROBLEMS------------

# # 1) ROTATE ARRAY BY 1

# arr=[1,2,3,4,5]
# temp=arr[-1]
# for i in range(len(arr)-1,0,-1):
#     arr[i]=arr[i-1]
# arr[0]=temp
# print(arr)

# # 2) ROTATE ARRAY BY K
# arr=[1,2,3,4,5]
# k=2
# k=k%len(arr)
# arr=arr[-k:]+arr[:-k]
# print(arr)

# # 3) FIND MISSING NUMBER IN AN ARRAY
# arr=[1,2,3,5]
# n=len(arr)+1
# total=n*(n+1)//2
# print(total - sum(arr))

# # 4)FIRST NON REPEATING ELEMENT IN AN ARRAY
# arr=[1,2,3,4,2,1]
# frq={}
# for num in arr:
#     if num in frq:
#         frq[num]+=1
#     else:
#         frq[num]=1

# for num in arr:
#     if frq[num]==1:
#         print(num)
#         break
# else:
#     print('no non repeating element')

# # 5) LEFT ROTATE AN ARRAY BY K
# arr=[1,2,3,4,5]
# k=2
# k=k%len(arr)
# arr=arr[k:]+arr[:k]
# print(arr)

# # 6) FIND INTERSECTION OF TWO ARRAYS
# arr1=[2,4,5,7,8]
# arr2=[3,4,6,7,9]
# res=[]
# for num in arr1:
#     if num in arr2 and num not in res:
#         res.append(num)
# print(res)

# # 7)REMOVE DUPLICATES IN PLACE IN AN ARRAY
# arr=[2,4,5,7,8,4,5]
# res=[]
# for i in range(len(arr)):
#     if arr[i] not in res:
#         res.append(arr[i])
# print(res)


