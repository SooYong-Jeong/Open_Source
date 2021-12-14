#5 / 100 / 5
def sum_besu(n1, n2, num):
    sum = 0
    for i in range(n1, n2 + 1):
        if i % num == 0:
            sum += i
        
    return sum

start = int(input("시작 수를 입력하세요 : "))
end = int(input("끝 수를 입력하세요 : "))
besu = int(input("합계를 구할 배수를 입력하세요 : "))

result = sum_besu(start, end, besu)

print("{} ~ {}의 정수 중 {}의 배수의 합 : {}".format(start, end, besu, result))