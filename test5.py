def 오배수(a, b):
    x = a * b
    if (x % 5 == 0):
        print(f"{a}*{b}={a*b}, 5배수")
    else:
        print(f"{a}*{b}={a*b}, 아님")

오배수(2, 10)
오배수(2, 3)