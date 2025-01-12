def solution(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        # 중간에 음수가 되면 균형이 깨진 상태
        if count < 0:
            return False
    # 최종적으로 count가 0이면 균형이 맞음
    return count == 0
