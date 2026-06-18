def fact(n :int):
    if n<=1:
        return 1
    return n*fact(n-1)

num=int(input("Enter the number"))
sum=fact(num)
print(sum)