target=int(input("Enter the number"))
ans=0
low=0
high=target
while(low<=high):
    mid=((low+high)//2)
    if mid*mid == target:
        print(mid)
        break
    elif mid*mid < target:
        ans=mid
        low=mid+1
    elif mid*mid > target:
        high = mid-1
else:
    print(ans)