def fibo(n):
    if (n==1 or n==2):
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
    
n = int(input("n = "))
print(f"{n}번째 수열 : {fibo(n)}")