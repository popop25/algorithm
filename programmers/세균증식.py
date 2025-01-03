def solution(n, t):
    for i in range(t):
        n = n * 2    # 2배씩 증가
    return n

def solution(n, t):
    answer = 2**t * n
    return answer