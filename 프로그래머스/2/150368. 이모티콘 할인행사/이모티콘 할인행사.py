from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discount_rates = [10, 20, 30, 40]
    
    for discounts in product(discount_rates, repeat=len(emoticons)):
        subscribers = 0
        revenue = 0
        
        for user_discount, user_limit in users:
            total = 0
            
            for discount, price in zip(discounts, emoticons):
                if discount >= user_discount:
                    total += price * (100 - discount) // 100
                    
            if total >= user_limit:
                subscribers += 1
            else:
                revenue += total
        
        if subscribers > answer[0]:
            answer = [subscribers, revenue]
        elif subscribers == answer[0] and revenue > answer[1]:
            answer = [subscribers, revenue]
    
    return answer