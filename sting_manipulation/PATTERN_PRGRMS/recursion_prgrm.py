def rec_fibo (n):
    if n<=1:
        return n
    else:
        return rec_fibo (n-1) + rec_fibo(n-2)
nterms=10
print("fib seq is :")
for i in range (nterms):
    print(rec_fibo(i))