def solution(a, b):
    # 두 수를 문자열로 변환하여 각각의 순서로 붙이기
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    
    # 둘 중 큰 수 반환
    return max(ab, ba)

print(solution(9, 91))    # 991 출력
print(solution(89, 8))    # 898 출력