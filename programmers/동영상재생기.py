def solution(video_len, pos, op_start, op_end, commands):
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(":"))
        return minutes * 60 + seconds
    
    def seconds_to_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    # 시간을 초 단위로 변환
    video_seconds = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    opening_start = time_to_seconds(op_start)
    opening_end = time_to_seconds(op_end)

    for command in commands:
        # 1. 현재 위치가 오프닝 구간인지 먼저 확인
        if opening_start <= current_pos <= opening_end:
            current_pos = opening_end
            
        # 2. 그 다음 명령어 실행
        if command == "prev":
            if current_pos < 10:  # 10초 미만이면
                current_pos = 0   # 시작 위치로
            else:
                current_pos -= 10
        elif command == "next":
            if current_pos + 10 > video_seconds:  # 남은 시간이 10초 미만이면
                current_pos = video_seconds       # 끝 위치로
            else:
                current_pos += 10
                
        # 3. 이동 후 다시 오프닝 구간 체크
        if opening_start <= current_pos <= opening_end:
            current_pos = opening_end

    return seconds_to_time(current_pos)