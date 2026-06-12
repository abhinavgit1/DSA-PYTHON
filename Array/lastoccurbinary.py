arr = [1,2,2,2,3,4]
target = 2
left=0
right=len(arr)-1
while(left<=right):
    mid=(left+right)//2
    if arr[mid] == target:
        ans=mid
        left=mid+1
    elif arr[mid] < target:
        left = mid+1
    elif arr[mid] > target:
        right=mid-1
    