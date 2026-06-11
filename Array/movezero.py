arr = [0,1,0,3,12]
write = 0
for i in range(len(arr)):
    if arr[i] != 0:
        if write != i:
            arr[write]=arr[i]
            arr[i]=0
            write+=1
        else:
            write+=1
print(arr)
        

