# def solution(a, b):
#     htm=60 * a
#     total = htm + b - 45
#     if total < 0:
#         total +=24 * 60
#     hour = total // 60
#     if hour >= 24:
#         hour -= 24
#     min = total % 60

#     return (hour, min)

# print(solution(10,10))

def solution(a, b):
    htm = 60 * a
    total = htm + b - 45
    if total < 0:
        total += 24 * 60
    hour = total // 60
    if hour >= 24:
        hour -= 24
    min = total % 60
    
    print(hour, min)  # 튜플 리턴 대신 print 사용

# 입력받기
h, m = map(int, input().split())
solution(h, m)