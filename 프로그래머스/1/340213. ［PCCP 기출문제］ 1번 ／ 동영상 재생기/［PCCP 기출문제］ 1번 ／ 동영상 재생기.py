def solution(video_len, pos, op_start, op_end, commands):
    def get_second(time):
        return 60*int(time[0:2])+int(time[3:5])
    
    
    def is_op(time):
        if op_start <= time <= op_end:
            return True
        return False
    
    video_len = get_second(video_len)
    pos = get_second(pos)
    op_start = get_second(op_start)
    op_end = get_second(op_end)   
    
    if is_op(pos):
        pos = op_end
    
    for command in commands:
        if command == "next":
            pos = min(pos+10, video_len)
            if is_op(pos):
                pos = op_end                
        else:
            pos = max(pos-10, 0)
            if is_op(pos):
                pos = op_end
    minute = pos//60
    second = pos%60
    return ':'.join((f"0{minute}" if minute < 10 else f"{minute}", f"0{second}" if second < 10 else f"{second}"))