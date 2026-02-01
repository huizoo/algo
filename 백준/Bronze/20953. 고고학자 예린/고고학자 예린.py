import sys
input = sys.stdin.readline
T = int(input())
answer = []
def dolmen(a: int, b: int) -> int:
    return (a+b)*(a+b-1)*(a+b)
for _ in range(T):
    a, b = map(int, input().split())
    answer.append(dolmen(a, b)//2)

print(*answer, sep='\n')