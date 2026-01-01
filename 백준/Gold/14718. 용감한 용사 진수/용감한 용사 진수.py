import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
powers = sorted([x for x, _, _ in arr])
dexes = sorted([x for _, x, _ in arr])

answer = 1e9

for i in range(K-1, len(powers)):
    for j in range(len(dexes)):
        arr2 = []
        for a, b, c in arr:
            if a <= powers[i] and b <= dexes[j]:
                arr2.append(c)
        if len(arr2) >= K:
            arr2.sort()
            answer = min(answer, powers[i]+dexes[j]+arr2[K-1])

print(answer)