N = int(input())
lst = list(map(int, input().split()))
cnt = 0
tmp = 0
for i in range(N+1):
    A = lst.count(i+1)+tmp
    if A >= i+1 :
        cnt += A//(i+1)
        tmp = A%(i+1)
    
print(cnt);
