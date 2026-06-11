arr = [1, 2, 3, 4, 5]
j=len(arr)-1
for i in range(len(arr)//2):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    j-=1
print(arr)