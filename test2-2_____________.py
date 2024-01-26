li = []
for i in range(5):
    li.append(int(input(f"li[{i}] = ")))

def 큰수(list):
    m = list[0]
    for i in range(0, 5):
        if (li[i] > m):
            m = li[i]
    print("list 중 가장 큰 수는", m)

큰수(li)