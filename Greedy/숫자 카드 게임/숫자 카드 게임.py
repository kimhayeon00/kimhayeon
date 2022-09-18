N, M = map(int,input().split())
dic = {}
for i in range(N):
    lst = list(map(int, input().split()))
    dic[lst[0]] = min(lst)
dic = sorted(dic.items(), reverse=True)

print(dic[-1][0])
