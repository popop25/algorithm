def solution(n):
    binary=bin(n)
    ones_count = binary.count('1')
    for i in range(n):
        n+=1
        result=bin(n)
        one_count = result.count('1')
        if ones_count ==one_count:
            return n