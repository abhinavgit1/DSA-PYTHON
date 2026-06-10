arr = [1,2,3,8,9,10,55]
if arr[0]<arr[1]:
    flarge=arr[1]
    slarge=arr[0]
else:
    flarge=arr[0]
    slarge=arr[1]
for el in arr[2:]:
    if el>flarge:
        slarge=flarge
        flarge=el
    elif el>slarge:
        slarge=el
print("Second Largest = ",slarg)