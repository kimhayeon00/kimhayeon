N = input()

mid = len(N)//2

a = 0
b = 0

for i in range(mid):
    a += int(N[i])
    b += int(N[i+mid])

if a == b:
    print("LUCKY")
else :
    print("READY")
