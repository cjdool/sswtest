import sys
from collections import deque
import heapq


def find_min_dist(start, maps, current_size):
    queue = deque()
    queue.append(start)

    x, y, cnt = start
    maps[x][y] = 0
    min_dist = []
    visited = set()
    visited.add((x, y))
    while queue:
        x, y, cnt = queue.popleft()

        nxs = [x-1, x, x, x+1]
        nys = [y, y-1, y+1, y]

        for nx, ny in zip(nxs, nys):
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                if maps[nx][ny] == 0 or maps[nx][ny] == current_size:  # passable
                    queue.append((nx, ny, cnt+1))
                    continue
                elif maps[nx][ny] < current_size:  # eatable
                    heapq.heappush(min_dist, (cnt+1, nx, ny))

    if min_dist:
        return min_dist[0]
    else:
        return None


N = int(sys.stdin.readline())
bp = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if temp[j] == 9:
            start = (i, j, 0)
    bp.append(temp)

curtime = 0
cursize = 2
eatcnt = 0

while True:
    next_value = find_min_dist(start, bp, cursize)

    if next_value is None:
        break
    cnt, nx, ny = next_value
    curtime += cnt

    eatcnt += 1
    if eatcnt == cursize:
        cursize += 1
        eatcnt = 0

    start = (nx, ny, 0)


print(curtime)
