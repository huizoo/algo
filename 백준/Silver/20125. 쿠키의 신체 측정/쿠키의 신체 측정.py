import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    head =  arm1 = arm2 = waist = leg1 = leg2 = hx = hy = 0
    for i in range(N):
        line = input().rstrip()
        if not head:
            for j in range(N):
                if line[j] == '*':
                    head = 1
                    hx, hy = i, j
                    break
        elif arm1 == 0 and arm2 == 0:
            for j in range(hy-1, -1, -1):
                if line[j] == '*':
                    arm1 += 1
                else:
                    break
            for j in range(hy+1, N):
                if line[j] == '*':
                    arm2 += 1
                else:
                    break
        elif line[hy] == '*':
            waist += 1
        else:
            if line[hy-1] == '*':
                leg1 += 1
            if line[hy+1] == '*':
                leg2 += 1

                
        
    print(hx+2, hy+1)
    print(arm1, arm2, waist, leg1, leg2)


if __name__ == "__main__":
    solve()