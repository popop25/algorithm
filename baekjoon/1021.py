from collections import deque  # 큐를 사용하기 위한 라이브러리

def solution(n, m, positions):
    queue = deque(range(1, n+1))  # 1부터 n까지의 숫자로 큐 초기화
    count = 0  # 2,3번 연산의 총 횟수
    
    for target in positions:  # 뽑아야 할 각 숫자에 대해
        while True:
            # 뽑으려는 수가 맨 앞에 있으면
            if queue[0] == target:
                queue.popleft()  # 뽑기
                break
                
            # 뽑으려는 수의 위치 찾기
            target_idx = queue.index(target)
            
            # 왼쪽으로 가는게 더 빠른지, 오른쪽으로 가는게 더 빠른지 판단
            if target_idx <= len(queue) // 2:  # 왼쪽이 더 가까우면
                queue.rotate(-1)  # 왼쪽으로 한 칸 이동
                count += 1
            else:  # 오른쪽이 더 가까우면
                queue.rotate(1)  # 오른쪽으로 한 칸 이동
                count += 1
                
    return count

n = 10  # 큐의 크기
m = 3   # 뽑을 숫자의 개수
positions = [1, 2, 3]  # 뽑아야 할 숫자들
print(solution(n, m, positions))