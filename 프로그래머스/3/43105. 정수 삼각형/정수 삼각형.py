def solution(triangle):
    answer = 0
    n = len(triangle)
    
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(i+1):
            dp[i][j] = max(
                dp[i-1][j-1] if j > 0 else 0,
                dp[i-1][j] if j < n-1 else 0
            ) + triangle[i][j]
    
    answer = max(dp[-1])
    return answer