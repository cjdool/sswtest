import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
bp = []
for i in range(N):
    bp.append(list(map(int, sys.stdin.readline().split())))

visited = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 1

while True:
    visited[r][c] = 1

    nxd = d
    flag = True
    for i in range(4):
        nxd = (nxd-1) % 4
        nxr = r + dx[nxd]
        nxc = c + dy[nxd]

        if 0 <= nxr < N and 0 <= nxc < M and bp[nxr][nxc] == 0 and visited[nxr][nxc] == 0:
            r, c, d = nxr, nxc, nxd
            cnt += 1
            flag = False
            break

    if flag:
        nxd = (nxd+2) % 4
        nxr = r + dx[nxd]
        nxc = c + dy[nxd]

        if 0 <= nxr < N and 0 <= nxc < M and bp[nxr][nxc] == 0:
            r, c = nxr, nxc
        else:
            break

print(cnt)
