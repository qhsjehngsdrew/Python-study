def hanoi(n, f, to, through):
    if (n==1):
        print(f"{f}->{to}")
    else:
        hanoi(n-1, f, through, to)
        hanoi(1, f, to, through)
        hanoi(n-1, through, to, f)

f = "A"
to = "C"
through = "B"
hanoi(3, f, to, through)