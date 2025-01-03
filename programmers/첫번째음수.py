def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

print(solution([1, 2, -3, 4, 5]))  
print(solution([1, 2, 3, 4, 5]))   # -1 출력