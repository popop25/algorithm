def solution(s):
    words = s.split(' ')  # 공백도 유지하기 위해 split(' ') 사용
    for i in range(len(words)):
        if words[i]:  # 단어가 비어 있지 않을 경우만 처리
            words[i] = words[i].capitalize()
    result = ' '.join(words)  # 공백 유지하며 다시 합치기
    return result
