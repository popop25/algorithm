def solution(s):
    zero_count=0 # 제거 0 개수
    convert_count=0 # 이진 변환 수

    while s != "1":
        # 0 세고 제거
        zero_count += s.count("0")
        s = s.replace('0', '')
        #이진 변환
        s=bin(len(s))[2:]
        convert_count+=1
    return [convert_count, zero_count]