import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(map(int, input().split()))

cnt = 1

for i in range(0, (N+1)//2):
    # 중앙값 이하의 수들을 2로 계속 나눴을 때 1이 되기까지의 나눗셈 횟수
    cnt += arr[i].bit_length() - 1

print(cnt)