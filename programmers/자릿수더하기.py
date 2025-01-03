def solution(n):
    result = 0  # 숫자를 더할 변수 초기화
    for digit in str(n):  # 숫자를 문자열로 변환하여 각 자릿수 순회
        result += int(digit)  # 각 자릿수를 정수로 변환하여 더하기
    return result