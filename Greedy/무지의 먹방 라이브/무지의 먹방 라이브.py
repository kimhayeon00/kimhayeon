# 정확성 42.9점, 효율성 0점
def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    answer = 0
    cnt = 0
    tmp = 0
    lenF = len(food_times)

    while True:
        if cnt == k:
            break
        tmp = tmp%lenF
        if food_times[tmp] > 0:
            food_times[tmp] -= 1
            cnt += 1
            tmp += 1
            # print(food_times)
        else:
            tmp += 1      
    
    for i in range(lenF):
        tmp = tmp%lenF
        if food_times[tmp] != 0:
            return tmp+1
        
        tmp += 1
                
