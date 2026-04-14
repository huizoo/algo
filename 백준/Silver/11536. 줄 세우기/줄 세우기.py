import sys
input = sys.stdin.readline

def main():
    N = int(input())
    names = [input().rstrip() for _ in range(N)]
    names2 = sorted(names)
    if names == names2:
        print("INCREASING")
    elif names == list(reversed(names2)):
        print("DECREASING")
    else:
        print("NEITHER")

if __name__ == "__main__":
    main()