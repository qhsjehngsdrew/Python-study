def fibo(n):
    li = []
    li.append(1)
    li.append(1)
    for i in range(2, n+1):
        li.append(li[i-2] + li[i-1])
    return li[n-1]

n = int(input("n = "))
print(f"{n}번째 수열 : {fibo(n)}")