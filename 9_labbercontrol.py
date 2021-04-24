import sys


def laddermove():
    for j in range(N):
        y = j
        for i in range(H):
            if ladder[i][y] == 1:
                y += 1
            elif y > 0 and ladder[i][y-1] == 1:
                y -= 1
        if y != j:
            return False
    return True


def dfs(laddercnt, startrow, addedladder):
    global ret
    if laddercnt == addedladder:
        if laddermove():
            ret = laddercnt
        return

    for i in range(startrow, H):
        for j in range(N-1):
            if ladder[i][j] == 1: # 추가하려는 곳에 있는 경우
                continue
            if j > 0 and ladder[i][j-1] == 1: # 추가하려는 곳 왼쪽에 있는 경우
                continue
            if j < N-1 and ladder[i][j+1] == 1: # 추가하려는 곳 오론쪽에 있는 경우
                continue
            ladder[i][j] = 1
            dfs(laddercnt+1, i, addedladder)
            ladder[i][j] = 0


N, M, H = map(int, sys.stdin.readline().split())

ladder = [[0]*N for _ in range(H)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a-1][b-1] = 1

ret = sys.maxsize
flag = True
for caser in range(4):
    dfs(0, 0, caser)
    if ret != sys.maxsize:
        print(ret)
        flag = False
        break

if flag:
    print(-1)
