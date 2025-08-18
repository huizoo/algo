def parse_time(time):
    arr = time.split(':')
    return int(arr[0])*60 + int(arr[1])

def solution(video_len, pos, op_start, op_end, commands):
    video_time = parse_time(video_len)
    pos_time = parse_time(pos)
    op_start_time = parse_time(op_start)
    op_end_time = parse_time(op_end)
    
    for command in commands:
        if op_start_time <= pos_time < op_end_time:
            pos_time = op_end_time
        if command == 'prev':
            pos_time -= 10
            if op_start_time <= pos_time < op_end_time:
                pos_time = op_end_time
            elif pos_time < 0:
                pos_time = 0
        else:
            pos_time += 10
            if op_start_time <= pos_time < op_end_time:
                pos_time = op_end_time
            elif pos_time > video_time:
                pos_time = video_time
    
    minute = pos_time // 60
    second = pos_time % 60
    if second < 10:
        second = '0' + str(second)
    if minute < 10:
        minute = '0' + str(minute)
    return f'{minute}:{second}'