def solution(s):
    arr=s.split()
    numbers = list(map(int, arr))
    min_value = min(numbers)
    max_value = max(numbers)
    return f"{min_value} {max_value}"