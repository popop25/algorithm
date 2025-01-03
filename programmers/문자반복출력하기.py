def solution(my_string, n):
    #unique_str = ''.join(dict.fromkeys(my_string))  # 중복 제거
    result = ''
    for char in my_string:
        result += char * n
    return result