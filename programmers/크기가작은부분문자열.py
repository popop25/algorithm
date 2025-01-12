def solution(t, p):
    count = 0
    p_len = len(p)
    p_int = int(p)
    
    # 슬라이딩 윈도우 방식으로 부분 문자열 확인
    for i in range(len(t) - p_len + 1):
        part = t[i:i + p_len]  #p의 길이만큼 잘라서
        if int(part) <= p_int: # 정수로 변환하고 p와 비교하여
            count += 1 #작거나 같은 경우의 개수를 세줍니다
            
    return count