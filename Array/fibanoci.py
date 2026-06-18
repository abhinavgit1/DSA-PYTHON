def fib(n):
    if n==1:
        return 1
    elif n == 0:
        return 0
    return fib(n-1)+fib(n-2)


n=int(input("Enter the number"))
ans=fib(n)
print(ans)