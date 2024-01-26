이름 = input("이름은?")
print("안녕하세요, " + 이름)

문자 = "가나다라"
print(문자, "길이 = ", len(문자))

print(문자, "0번째 = ", 문자[0])
print(문자, "0~1번째 = ", 문자[0:2])
print(문자, "끝 = ", 문자[-1])

나이 = 14
print(f"내 이름은 {이름}이고, 나이는 {나이}입니다.")
print("내 이름은 {이름}이고, 나이는 {나이}입니다.")

이름 = "Computer"
print(이름, "대문자로 : ", 이름.upper())
print(이름, "소문자로 : ", 이름.lower())

이름 = "컴퓨터"
print(이름)
새이름 = 이름.replace("터", "팅이 뭘까?")
print(새이름)
print(이름)

print("1부터 n까지 출력하기")
n = int(input("값 : "))
for i in range(1,n+1):
    print(i)
