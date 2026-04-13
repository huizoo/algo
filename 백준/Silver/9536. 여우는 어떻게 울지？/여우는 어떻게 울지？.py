import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        sounds = input().split()
        animals = set()
        while True:
            animal = input().split()
            if animal[1] == 'goes':
                animals.add(animal[2])
            else:
                break
        fox = []
        for sound in sounds:
            if sound in animals:
                continue
            else:
                fox.append(sound)

        print(' '.join(map(str, fox)))

if __name__ == "__main__":
    main()