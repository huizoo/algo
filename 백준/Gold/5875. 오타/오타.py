import sys
input = sys.stdin.readline

def main():
    st = input().rstrip()
    
    total = ans = 0
    for x in st:
        if x == '(':
            total += 1
        else:
            total -= 1

    if total < 0:
        to = 0
        for x in st:
            if x == '(':
                to += 1
            else:
                to -= 1
                ans += 1
            if to == -1:
                break
    elif total > 0:
        to = 0
        for x in reversed(st):
            if x == ')':
                to += 1
            else:
                to -= 1
                ans += 1
            if to == -1:
                break
    print(ans)

if __name__ == "__main__":
    main()
