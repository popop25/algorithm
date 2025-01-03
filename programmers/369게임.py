def solution(order):
    count = 0  # 카운터 초기화
    # 숫자를 문자열로 변환
    str_order = str(order)
    
    # 각 자릿수 확인
    for digit in str_order:
        if int(digit) != 0 and int(digit) % 3 == 0:  # 0은 제외하고 3의 배수 확인
            count += 1
    
    return count