arr = [1,3,5,7,9,11,15]
target = 5
low=0
high=len(arr)-1
while(low<=high):
    mid=(low+high)//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid] < target:
        low=mid+1
    elif arr[mid] > target:
        high=mid-1
else:
    print("Position to be added",low)