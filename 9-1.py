"""
a = input("첫 번째 숫자를 입력하세요. : ")
b = input("두 번째 숫자를 입력하세요. : ")

c = int(a) + int(b)

print(c)
print(type(a), type(b), type(c))
"""
"""
inch = float(input("인치(inch)를 입력하세요 : "))

cm = inch * 2.54

print(f"센티미터 = {cm}")
"""
"""
a = input("높이를 입력하세요(cm). : ")
b = input("밑변의 길이를 입력하세요(cm). : ")

c = float(a)*float(b)/2

print(f"삼각형의 넓이는  : {c}cm^2")
"""
"""

x = int(input("숫자를 입력 하세요. : "))

if x > 0:
    print("양수")
elif x == 0:
    print("0")
else: print("음수")
"""
"""
num = int(input("숫자를 입력하세요."))
if num % 2 == 0:
    print("짝수")
else: print("홀수")
"""
"""
a = int(input("필기 성적을 입력하세요. : "))
b = int(input("실기 성적을 입력하세요. : "))

if a >= 80 & b >=80:
    print("합격")
else: print("불합격")
"""
"""
id = input("아이디를 입력하세요. : ")
level = int(input("레벨을 입력하세요. : "))

if (id == "abcd") | (level == 1):
    print("관리자 입니다.")
else: print("비관리자 입니다.")
"""
"""
age = int(input("나이를 입력하세요. : "))
pay = 3000

if (age >= 65) | (age < 7):
    pay = 0

print(f"입장료 : {pay}")"""
"""
sum  = 0
for i in range(1, 11):
    sum += i
    print(f"i의 값 : {i}, 합계 : {sum}")
"""
"""
for i in range(10):
    print(i, end = " ")
print()

print("---------------------------")
for i in range(1, 11, 2):
    print(i, end = " ")
print()
"""
"""
sum = 0

for i in range(1, 101):
    if i % 3 == 0:
        print(i, end = " ")
        sum += i

print("\n", "-" * 50)
print("1 ~ 100에서 3의 배수의 합계 : {}".format(sum))
"""
"""
word = input("문장을 입력하세요")

for x in word:
    print(x)
"""
#화씨온도 = 섭씨온도 * 9/5 + 32
print("-"*30)
print("\t섭씨\t  화씨")
print("-"*30)
for c in range(-20, 31, 5):
    f = c*9.0/5.0 + 32.0
    print("  %8d\t%6.1f"%(c, f))
print("-"*30)
