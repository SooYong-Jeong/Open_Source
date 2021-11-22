i = 0       #입력되는 성적의 순서를 표시하기위한 변수
sum = 0     #입력되는 성적의 합계를 저장하기 위한 변수
scores = [] #입력되는 성적을 저장하기 위한 List
while True: #scores list의 index i위치에 입력값을 저장하는 while문
    score = int(input("{}번째 성적을 입력하세요(종료시 -1 입력) : ".format(i + 1)))
    
    if score == -1:             #-1이 입력되면 성적입력을 중단하는 if예외처리
        break
    else:                       #list에 입력값을 저장하고 합계에 그 값을 더하고 순서를 하나 올리는 과정
        scores.append(score)    
        sum += scores[i]
        i += 1
if i == 0:
    print("입력된 성적이 없습니다.")        #성적 입력 없이 종료했을때
else:
    print("합계 : {}점 평균 : {:.2f}점".format(sum, sum/len(scores)))   #최종 출력