def 회문(문장):
    s = 0
    e = -1
    while (s < len(문장)):
        if (문장[s] != 문장[e]):
            return "No"
        s += 1
        e -= 1

    return "Yes"

s = ['우영우', '파이썬', '스위스', 'madam', 'nurses run']
for i in s:
    print(i, 회문(i))