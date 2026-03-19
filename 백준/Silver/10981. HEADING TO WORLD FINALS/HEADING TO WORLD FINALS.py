import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dic = dict()
for _ in range(N):
    university, team, problems, penalties = input().split()
    problems = int(problems)
    penalties = int(penalties)
    if university in dic:
        pro = dic[university][1]
        if pro < problems:
            dic[university] = [team, problems, penalties]
        elif pro == problems and dic[university][2] > penalties:
            dic[university] = [team, problems, penalties]
    else:
        dic[university] = [team, problems, penalties]

S = sorted(dic.values(), key=lambda x: (-x[1], x[2]))        
for i in range(K):
    print(S[i][0])