N = int(input())
lst = list(map(int, input().split()))
cnt = 0

for i in range(N+1):
    if lst.count(i+1) >= i+1 :
        cnt +=1
    
print(cnt);
