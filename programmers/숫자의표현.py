def solution(n):
    count = 0
    k = 1
    while k * (k - 1) // 2 < n:  # k*(k-1)/2가 n보다 작을 때까지만 탐색
        # a가 양의 정수인지 확인
        if (n - k * (k - 1) // 2) % k == 0:
            count += 1
        k += 1
    return count

def expressions(num):
    answer = 0
    for i in range(1, num+1):
        summ = 0
        while (summ < num):
            summ += i
            i += 1
        if summ == num:
            answer += 1
    return answer

print(solution(15))  # 출력: 4
print(expressions(15))  # 출력: 4
