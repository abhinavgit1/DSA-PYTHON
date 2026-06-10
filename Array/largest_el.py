arr = [1,2,3,8,9,10,55]
temp=arr[0]
for el in arr:
    if el>temp:
        temp=el
print("largest : ",temp)