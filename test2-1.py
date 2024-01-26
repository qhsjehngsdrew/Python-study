def 큰값(a, b):
    if a > b:
        res = a
    else :
        res = b
    return res

def 큰수(a, b, c):
    print(큰값(큰값(a,b), c))

큰수(4,5,6)
큰수(6,4,5)
큰수(1,7,2)