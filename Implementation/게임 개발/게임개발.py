N, M = map(int, input().split())

x, y, d = map(int, input().split())
mtx = []
cnt = 1
tmp = 0
for i in range(N):
    mtx.append(list(map(int,input().split())))

mtx[x][y] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
i = 0
while(True):
    d = (d+i) % 4
    i += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if mtx[nx][ny] == 0 :
        cnt +=1
        mtx[nx][ny] = 1
        x = nx
        y = ny
    else:
        tmp += 1
    if tmp == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if mtx[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        tmp = 0
print(cnt)

    
        
        
