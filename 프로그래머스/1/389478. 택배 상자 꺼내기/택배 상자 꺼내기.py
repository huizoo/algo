# n : 총 개수, w : 한 층에 가능한 개수, 
def solution(n, w, num):
    몫 = n // w
    나머지 = n % w
    if 나머지 == 0:
        층수 = 몫 - 1
    else:
        층수 = 몫
        
    num몫 = num // w
    num나머지 = num % w
    if num나머지 == 0:
        num층수 = num몫 - 1
    else:
        num층수 = num몫
    
    answer = 층수 - num층수
    print(몫, 나머지, num몫, num나머지)
    if 층수 % 2 == num층수 % 2 : 
        if 나머지 == 0 and num나머지 != 0:
            answer += 1
        elif 나머지 >= num나머지 :
            answer += 1
    else:
        if 나머지 == 0:
            나머지 += w
        if num나머지 == 0:
            num나머지 += w
        if 나머지 + num나머지 > w:
            answer += 1
            
    print(몫, 나머지, num몫, num나머지)
    return answer