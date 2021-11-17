def fib(n):
    if n in [0,1]:
        return n
    return fib(n-1) + fib(n-2)

size = int(input("size: "))

print([fib(n) for n in range(size)])
