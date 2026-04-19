def solution(triangle):
    N = len(triangle)
    dp = [triangle[0][0]]
    for i in range(N-1):
        dp2 = [0]*(i+2)
        for j in range(i+1):
            dp2[j] = max(dp2[j], dp[j]+triangle[i+1][j])
            dp2[j+1] = max(dp2[j+1], dp[j]+triangle[i+1][j+1])
        dp = dp2
    
    return max(dp)