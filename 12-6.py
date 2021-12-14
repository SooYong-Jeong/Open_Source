def sum(start, end):        #매개변수 start 와 end를 가지는 함수 정의
    total = 0               #총합을 저장하는 변수를 0으로 초기화 해 준다
    for i in range(start, end):     #range함수로 start에서 end까지 하나씩 모두 더하는 반복문
        total += i
    print("{} ~ {}의 정수 합계 : {}".format(start, end, total)) 
    
sum(10, 100)                #10 ~ 100의 점수 합계함수를 호출
sum(100, 1000)              #100 ~ 1000의 점수 합계함수를 호출
sum(1000, 10000)            #100 ~ 10000의 점수 합계함수를 호출