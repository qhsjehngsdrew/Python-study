def 구구단(d):
    print(f"  {d} 단")
    for i in range(1, 10):
        print(f"{d} X {i} = {d*i}")

for i in range(2, 10):
    구구단(i)
    print("=" * 10)