def 큰수(a, b, c):
    res = a
    if (res < b):
        res = b
    if (res < c):
        res = c
    print("큰수=", res)

큰수(4,5,6)
큰수(6,4,5)
큰수(1,7,2)