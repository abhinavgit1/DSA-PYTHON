arr=[1,2,5,4,2,6,7]
peak=0
left=0
right=len(arr)-1
while left<right:
    mid=(left+right)//2
    if arr[mid]<arr[mid+1]:
        left = mid+1
    else:
        right = mid
print(left)
        

