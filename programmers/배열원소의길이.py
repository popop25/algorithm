def solution(strlist):
    result = []  # 각 문자열의 길이를 저장할 리스트
    
    for s in strlist:  # strlist의 각 문자열에 대해
        result.append(len(s))  # 문자열의 길이를 result에 추가
        
    return result

# def solution(strlist):
#     return [len(s) for s in strlist]

strlist = ["We", "are", "the", "world!"]
result = solution(strlist)
print(result)  # [2, 3, 3, 6] 출력