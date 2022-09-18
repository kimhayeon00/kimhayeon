arr = input()
cnt = 0
a = arr[-1]
for i in range(len(arr)):
    if a != arr[i]:
        cnt +=1
    a = arr[i]
print(cnt//2)
        
