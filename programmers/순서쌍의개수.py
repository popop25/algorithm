def solution(n):
    count = 0
    for i in range(1, n + 1):  # 1부터 n까지 순회
        if n % i == 0:         # n을 i로 나눈 나머지가 0이면 약수
            count += 1
    return count