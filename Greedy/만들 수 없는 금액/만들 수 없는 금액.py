N = int(input())
arr = list(map(int, input().split()))

a=1
for i in arr:
    if a < i:
        break
    a += i
    
print(a)
