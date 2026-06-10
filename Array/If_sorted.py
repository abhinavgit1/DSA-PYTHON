print("Enter the array")
issorted=True
arr = list(map(int,input("Enter the array divided by space : ").split()))
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        issorted=False
        break
print(issorted)


