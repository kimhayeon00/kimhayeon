N = int(input())
lst = list(map(int, input().split()))
cnt = 0
tmp = 0
lst2 = set(lst)
for i in lst2:
    A = lst.count(i)+tmp
    if A >= i :
        cnt += A//i
        tmp = A%i
    
print(cnt);
