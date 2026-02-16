import sys
input = sys.stdin.readline
minsik = {
    'a': '11',
    'b': '12',
    'k': '13',
    'd': '14',
    'e': '15',
    'g': '16',
    'h': '17',
    'i': '18',
    'l': '19',
    'm': '20',
    'n': '21',
    'ng': '22',
    'o': '23',
    'p': '24',
    'r': '25',
    's': '26',
    't': '27',
    'u': '28',
    'w': '29',
    'y': '30',
    }
N = int(input())
arr = []
Max = 0
for _ in range(N):
    st = input().rstrip()
    l = len(st)
    i = 0
    num = []
    while i<l:
        if st[i] == 'n' and i+1<l and st[i+1] == 'g':
            num.append(minsik['ng'])
            i += 2
        else:
            num.append(minsik[st[i]])
            i += 1
    st2 = ''.join(map(str, num))
    Max = max(Max, len(st2))
    arr.append([st, st2])

for i in range(N):
    n = arr[i][1]
    l = len(n)
    k = int(n)
    if Max != l:
        k *= 10**(Max-l)
    arr[i][1] = k

arr.sort(key=lambda x: x[1])
for x, y in arr:
    print(x)
    