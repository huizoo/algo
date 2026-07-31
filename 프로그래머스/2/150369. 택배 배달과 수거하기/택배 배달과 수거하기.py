def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0

    for i in range(n - 1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]

        delivery_count = (delivery + cap - 1) // cap
        pickup_count = (pickup + cap - 1) // cap

        count = max(0, delivery_count, pickup_count)

        answer += 2 * (i + 1) * count

        delivery -= count * cap
        pickup -= count * cap

    return answer