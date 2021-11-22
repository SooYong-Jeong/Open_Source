n1 = int(input("Input the first number : "))
n2 = int(input("Input the second number : "))

n = int(input("합계를 구하고자 하는 배수를 입력하시오"))

sum = 0
i = n1

while i < n2 + 1:
    if i % n == 0:
        sum += i

    i += 1

print(f"{n1} ~ {n2} 까지의 정수 {n}의 배수의 합계 : {sum}")