def fact(n):
    return n * fact(n-1) if (n != 1) else 1

def Co(n, r):
    return fact(n) // fact(n-r) * fact(r)

if (__name__ == '__main__'):
    import sys
    print(sys.argv)
    if len(sys.argv) == 2:
        print(fact(int(sys.argv[1])))
    elif len(sys.argv) == 3:
        print(Co(int(sys.argv[1]), int(sys.argv[2])))

#폴더 주소 C:\Users\user\AppData\Local\Programs\Python\Python311\Lib\idlelib
#sys.path를 통해 나오는 주소로 모듈은 여기로 옮기기