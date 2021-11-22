scores = [[96, 84, 80], [96, 86, 76], [76, 95, 83], [89, 96, 69],\
          [90, 76, 91], [82, 66, 88], [83, 86, 79], [85, 90, 83]]   #점수가 저장되어있는 List
for i in range(len(scores)):            #List의 크기만큼 반복해서 더하는 2중for문
    sum = 0
    for j in range(len(scores[i])):
        sum = sum + scores[i][j]
        
    avg = sum / len(scores[i])          #List의 크기로 나누어서 평균을 구한다
    
    print("{}번째 학생의 점수 합계 : {}, 평균 : {:.2f}".format(i+1, sum, avg))