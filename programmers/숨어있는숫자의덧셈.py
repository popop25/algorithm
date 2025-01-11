def solution(my_string):
    number = 0
    for i in range(len(my_string)):  # .len -> len()
        if my_string[i].isdigit():   # isinteger -> isdigit(), true -> True
            number += int(my_string[i])  # 문자열을 정수로 변환
    return number