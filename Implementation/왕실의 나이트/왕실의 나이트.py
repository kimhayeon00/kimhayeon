N = input()
arr = [int(N[1]),ord(N[0])-96]
cnt = 0
dr = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]

for i in range(8):
    lst1 = arr[0] + dr[i][0]
    lst2 = arr[1] + dr[i][1]
    if 0 < lst1 < 9 and 0 < lst2 < 9:
        cnt +=1

        
print(cnt)
