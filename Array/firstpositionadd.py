arr = [1,2,2,2,3,4]
target = 2
left=0
ans=-1
high=len(arr)-1
while(left<=high):
    mid=(left+high)//2
    if arr[mid]==target:
        ans=mid
        high=mid-1
    elif arr[mid] < target:
        left = mid+1
    elif arr[mid] > target:
        high = mid - 1
print(ans)