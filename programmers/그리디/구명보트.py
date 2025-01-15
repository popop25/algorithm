def solution(people, limit):
    people.sort()  # 오름차순 정렬
    answer = 0
    left = 0           # 가장 가벼운 사람 인덱스
    right = len(people) - 1  # 가장 무거운 사람 인덱스
    
    while left <= right:
        if left == right:  # 한 명만 남은 경우
            answer += 1
            break
            
        # 가장 가벼운 사람 + 가장 무거운 사람 <= limit
        if people[left] + people[right] <= limit:
            left += 1   # 두 명 다 태움
            right -= 1
        else:
            right -= 1  # 무거운 사람만 태움
        answer += 1
        
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))