def solution(balls, share):
    # 방법 1: math 모듈 사용
    from math import comb
    return comb(balls, share)

def solution(balls, share):
    # 방법 2: 팩토리얼을 이용한 직접 계산
    def factorial(n):
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    return factorial(balls) // (factorial(share) * factorial(balls - share))

print(solution(5, 3))  # 10
# 5개 중에서 3개를 선택하는 경우의 수는 10가지