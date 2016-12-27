def fibo(n):
    if n is 1:
        return 1
    if n is 0:
        return 1
    return fibo(n-2)+fibo(n-1)
