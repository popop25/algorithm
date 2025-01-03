def solution(board):
    n = len(board)  # 보드의 크기
    danger = set()  # 위험 지역을 저장할 set (중복 제거)
    
    # 8방향 이동을 위한 방향 벡터
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰가 있는 위치라면
                # 현재 위치를 위험 지역에 추가
                danger.add((i, j))
                
                # 8방향 주변 칸을 위험 지역에 추가
                for k in range(8):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    
                    # 보드 범위를 벗어나지 않는 경우에만 추가
                    if 0 <= ni < n and 0 <= nj < n:
                        danger.add((ni, nj))
    
    # 전체 칸의 개수에서 위험 지역의 개수를 뺀 값을 반환
    safe_area = n * n - len(danger)
    return safe_area

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
result = solution(board)
print(result)  # 16 출력 (5x5 보드에서 위험지역 9칸을 제외한 안전지역)