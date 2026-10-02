def solution(prices):
    answer = [0]*len(prices)
    current_price = prices[0]
    stack = [(prices[0], 0)]
    today = 0

    for day in range(1, len(prices)):
        price = prices[day]
        today = day
        while stack and stack[-1][0] > price:
            p, d = stack.pop()
            answer[d] = today - d
        stack.append((price, day))
    
    while stack:
        _, d = stack.pop()
        answer[d] = today - d
        
    return answer

