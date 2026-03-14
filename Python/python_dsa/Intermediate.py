# 1) Prefix Sum Technique
arr=[3,2,4,1,5]
prefix_sum=[0]*len(arr)
prefix_sum[0]=arr[0]
for i in range(1,len(arr)):
    prefix_sum[i]=prefix_sum[i-1]+arr[i]
print(prefix_sum)

# 2) Sliding Window Technique
arr=[1,3,-1,-3,5,3,6,7]
k=3
window_sum=sum(arr[:k])
max_sum=window_sum
for i in range(k,len(arr)):
    window_sum+=arr[i]-arr[i-k]
    max_sum=max(max_sum,window_sum)
print(max_sum)

# 3) Maximum Subarray Sum (Kadane's Algorithm)
arr=[-2,1,-3,4,-1,2,1,-5,4]
max_current=max_global=arr[0]
for i in range(1,len(arr)):
    max_current=max(arr[i],max_current+arr[i])
    if max_current>max_global:
        max_global=max_current
print(max_global)

# 4) Two Pointer Technique
arr=[1,2,3,4,5]
target=5
left=0
right=len(arr)-1
while left<right:
    current_sum=arr[left]+arr[right]
    if current_sum==target:
        print(f"Pair found: {arr[left]}, {arr[right]}")
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1

# 5) Find Pair With Target Sum
arr=[1,2,3,4,5]
target=5
seen=set()
for num in arr:
    complement=target-num
    if complement in seen:
        print(f"Pair found: {num}, {complement}")
        break
    seen.add(num)

# 7) Find Majority Element
arr=[2,2,1,1,1,2,2]
count={}
for num in arr:
    count[num]=count.get(num,0)+1
majority_element=max(count,key=count.get)
print(majority_element)


# 8) Find Maximum Difference
arr=[7,1,5,3,6,4]
min_price=arr[0]
max_profit=0
for i in range(1,len(arr)):
    min_price=min(min_price,arr[i])
    max_profit=max(max_profit,arr[i]-min_price)
print(max_profit)


# 9) Maximum element in each subarray
arr=[1,3,-1,-3,5,3,6,7]
k=3
max_in_subarrays=[]
for i in range(len(arr)-k+1):
    max_in_subarrays.append(max(arr[i:i+k]))
print(max_in_subarrays)


# 10) Maximum element in each subarray
arr=[1,3,-1,-3,5,3,6,7]
k=3
max_in_subarrays=[]
for i in range(len(arr)-k+1):
    max_in_subarrays.append(max(arr[i:i+k]))
print(max_in_subarrays)

# 11) Maximum consecutive ones
arr=[1,1,0,1,1,1]
max_count=0
current_count=0
for num in arr:
    if num==1:
        current_count+=1
        max_count=max(max_count,current_count)
    else:
        current_count=0
print(max_count)


# 12) Binary Search
def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=[1,2,3,4,5]
target=3
print(binary_search(arr,target))
# 13) Find Peak Element
arr=[1,2,3,1]
for i in range(len(arr)):
    if (i==0 or arr[i]>=arr[i-1]) and (i==len(arr)-1 or arr[i]>=arr[i+1]):
        print(f"Peak element found: {arr[i]} at index {i}")
        break
    