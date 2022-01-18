# N : 배열의 크기
# M : 숫자가 더해지는 횟수
# K : 한 숫자가 연속해서 더해질 수 있는 최대 횟수

N, M, K = map(int, input().split())
result = 0
num = list(map(int, input().split()))
num.sort(reverse=True)
for i in range(M):
    for j in range(K):
        if M == 0 : break
        result += num[0]
        M -= 1
    if M == 0 : break
    result += num[1]
    M -= 1
    
print(result)
