import sys
input = sys.stdin.readline
st = "No permutation"
answer = []
P = [0]*11
num = 1
for i in range(1, 11):
    num *= i
    P[i] = num

def abc(k):
    temp = 0
    for i in range(length):
        if used[i]: continue
        if k == temp:
            ans.append(A[i])
            used[i] = 1
            break
        temp += 1

while True:
    try:
        A, B = input().split()
        b = int(B)
        l = length = len(A)
        if P[l] < b:
            answer.append(f'{A} {B} = {st}')
            continue
        used = [0]*length
        ans = []
        while l > 1:
            l -= 1
            abc((b-1)//P[l])
            b = (b-1)%P[l]+1
        
        abc(0)
        answer.append(f'{A} {B} = {"".join(map(str, ans))}')
    except:
        break

print(*answer, sep='\n')