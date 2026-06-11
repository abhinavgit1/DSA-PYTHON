def remdup(arr):
    write = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[write]=arr[i]
            write += 1     
    print(arr[:write])
arr = list(map(int,input("Enter the array with space").split()))
remdup(arr)
           