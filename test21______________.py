def fibo(n):
    li = [1,1]
    fb = 1
    for i in range(3, n+1):
        fb = li[0] + li[1]
        li[i%2] = fb
    return fb

n = int(input("n = "))
print(f"{n}번째 수열 : {fibo(n)}")