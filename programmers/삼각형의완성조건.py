def solution(sides):
    sides.sort()          # sort()는 None을 반환하고 리스트를 직접 정렬합니다
    if sides[2] < sides[0] + sides[1]:    # 정렬된 원래 리스트를 사용
        return 1        
    else:
        return 2         