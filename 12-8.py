def computMaxGong(x, y):
    if x > y:
        small = y
    else:
        small = x
        
    for i in range(1, small + 1):
        if((x % i == 0)&(y % i == 0)):
            result = i
    return result

num1 = int(input("첫 번째 수를 입력하세요 : "))
num2 = int(input("두 번째 수를 입력하세요 : "))

max_gong = computMaxGong(num1, num2)

print("{}과(와) {}의 최대공약수 : {}".format(num1, num2, max_gong))