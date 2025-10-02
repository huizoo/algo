def clean(stack, answer, plans):
    while stack:
        answer.append(plans[stack.pop()][0])
    return answer

def solution(arr):
    answer = []
    stack = []
    arr.sort(key = lambda x: x[1])
    for row in arr:
        row[1] = int(''.join(row[1][:2])) * 60 + int(''.join(row[1][3:]))
        row[2] = int(row[2])
    length = len(arr)
    now = 0
    nxt = 1
    time = arr[0][1]
    flag = 0
    while len(answer) < length:
        d, e, f = arr[nxt]
        if flag == 1:
            flag = 0
            if stack and time < e:
                now = stack.pop()
                a, b, c = arr[now]
            else:
                while now in stack or arr[now][0] in answer:
                    now = min(now+1, length-1)
                nxt = min(nxt+1, length-1)
                d, e, f = arr[nxt]
                a, b, c = arr[now]
        else:
            if stack and time < b:
                now = stack.pop()
                nxt -= 1
            a, b, c = arr[now]
        b = max(time, b)
        if now == nxt == (length - 1):
            answer.append(a)
            answer = clean(stack, answer, arr)
            break
        z = b + c - e
        if z <= 0:
            answer.append(a)
            time += c
            flag = 1
            continue
        else:
            time = b + c - z
            arr[now][2] = z
            stack.append(now)
            while now in stack or arr[now][0] in answer:
                now = min(now+1, length-1)
            nxt = min(nxt+1, length-1)
            continue

    return answer