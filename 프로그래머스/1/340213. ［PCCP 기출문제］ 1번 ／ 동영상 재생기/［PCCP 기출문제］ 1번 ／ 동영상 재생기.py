def solution(video_len, pos, op_start, op_end, commands):
    def to_seconds(time_str):
        # "mm:ss"를 초 단위로 변환
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds

    def to_time(seconds):
        # 초를 "mm:ss" 형식으로 변환
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    # 시간 변환
    total = to_seconds(video_len)
    current = to_seconds(pos)
    start = to_seconds(op_start)
    end = to_seconds(op_end)

    # 초기 오프닝 체크
    if start <= current <= end:
        current = end

    # 명령 처리
    for cmd in commands:
        if cmd == "prev":
            current = max(0, current - 10)
        else:  # "next"
            current = min(total, current + 10)
        # 오프닝 구간 체크
        if start <= current <= end:
            current = end

    return to_time(current)