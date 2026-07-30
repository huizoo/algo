from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for size in course:
        counter = Counter()

        for order in orders:
            for combination in combinations(sorted(order), size):
                menu = ''.join(combination)
                counter[menu] += 1

        if not counter:
            continue

        max_count = max(counter.values())

        if max_count < 2:
            continue

        for menu, count in counter.items():
            if count == max_count:
                answer.append(menu)

    return sorted(answer)