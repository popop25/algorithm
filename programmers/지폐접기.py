def solution(wallet, bill):
    answer = 0
    for i in wallet:
        if bill[0]>bill[1]:
            bill[0]/2
            answer+=1
        else:
            bill[1]/2
            answer+=1
    return answer

solution(30,15)