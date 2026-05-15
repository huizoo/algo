def time_to_minute(time):
    h, m = map(int, time.split(':'))
    return 60*h + m

def solution(book_time):
    answer = 0
    room = [0]
    book_time.sort()
    for start, end in book_time:
        start = time_to_minute(start)
        end = time_to_minute(end)
        target_idx = -1
        latest_end = -1
        for idx, room_end in enumerate(room):            
            if room_end <= start and latest_end < room_end:
                target_idx = idx
        
        if target_idx == -1:
            room.append(end+10)
        else:
            room[target_idx] = end+10
    
    return len(room)