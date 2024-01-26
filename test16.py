def facto(n):
    ft = 1
    for i in range(1, n+1):
        ft *= i
    return ft

n = int(input("n = "))
print(f"{n}! = {facto(n)}")