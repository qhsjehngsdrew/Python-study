def facto(n):
    return 1 if(n==1) else n*facto(n-1)

n = int(input("n = "))
print(f"{n}! = {facto(n)}")