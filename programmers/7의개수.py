def solution(array):
    # 배열의 모든 숫자를 문자열로 변환하고 연결
    str_num = ''.join(map(str, array))
    count = 0
    
    # 각 자리를 순회하면서 7의 개수를 세기
    for digit in str_num:
        if digit == '7':
            count += 1
            
    return count

# def solution(array):
#     return str(array).count('7')