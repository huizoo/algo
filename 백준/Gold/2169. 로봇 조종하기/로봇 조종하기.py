import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] = (i, j)까지의 최댓값
dp = [[-float('inf')] * M for _ in range(N)]

# 첫 번째 행 초기화 (왼쪽에서 오른쪽으로만)
dp[0][0] = arr[0][0]
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + arr[0][j]

# 두 번째 행부터 처리
for i in range(1, N):
    # 왼쪽에서 오는 경우
    left = [-float('inf')] * M
    left[0] = dp[i-1][0] + arr[i][0]
    for j in range(1, M):
        left[j] = max(dp[i-1][j], left[j-1]) + arr[i][j]

    # 오른쪽에서 오는 경우
    right = [-float('inf')] * M
    right[M-1] = dp[i-1][M-1] + arr[i][M-1]
    for j in range(M-2, -1, -1):
        right[j] = max(dp[i-1][j], right[j+1]) + arr[i][j]

    # 최댓값 선택
    for j in range(M):
        dp[i][j] = max(left[j], right[j])

print(dp[N-1][M-1])