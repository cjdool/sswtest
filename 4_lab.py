import sys
from collections import deque
from copy import deepcopy

def bfs(cnt):
    tempbp = deepcopy(bp)
    queue = deque(virusidx)

    while queue:
        x, y = queue.popleft()

        nxs = [x, x, x-1, x+1]
        nys = [y-1, y+1, y, y]

        for nx, ny in zip(nxs, nys):
            if 0 <= nx < N and 0 <= ny < M and tempbp[nx][ny] == 0:
                tempbp[nx][ny] = 2
                queue.append((nx, ny))
                cnt -= 1

    return cnt


N, M = map(int, sys.stdin.readline().split())
bp = []
virusidx = []
zeroidx = []
zcnt = 0
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if temp[j] == 2:
            virusidx.append((i, j))
        elif temp[j] == 0:
            zeroidx.append((i, j))
    bp.append(temp)

zcnt = len(zeroidx)
maxval = 0

for i in range(zcnt):
    a, b = zeroidx[i]
    bp[a][b] = 1
    for j in range(i+1, zcnt):
        c, d = zeroidx[j]
        bp[c][d] = 1
        for k in range(j+1, zcnt):
            e, f = zeroidx[k]
            bp[e][f] = 1
            maxval = max(maxval, bfs(zcnt-3))
            bp[e][f] = 0
        bp[c][d] = 0
    bp[a][b] = 0

print(maxval)