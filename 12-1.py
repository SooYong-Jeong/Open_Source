def average(*scores):
    sum = 0
    for i in range(len(scores)):
        sum += scores[i]
        
    avg = sum / len(scores)
    print("{} 과목의 평균 : {:.2f}".format(len(scores), avg))
    
average(80, 90, 100)
average(75, 80, 94, 78)
average(80, 73, 73, 86, 82)