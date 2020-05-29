def Fibonacci(n):
    memory=0
    fib=1
    while fib < n and memory<n:
        fib+=memory
        if fib<n:
            yield fib
        else:
            break
        memory+=fib
        if memory<n:
            yield memory
        else:
            break


print(list(Fibonacci(100)))