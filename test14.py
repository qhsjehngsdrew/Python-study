n = int(input("n = "))
ft = 1
for i in range(1, n + 1):
    ft *= i
    print(f"{i}! = {ft}")

print()
v = int(input("v = "))
ft = 1
for i in range(1, v + 1):
    ft *= i
print(f"{v}! = {ft}")