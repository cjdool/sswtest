import sys

def move():
    result = 0
    stack = [(0, 0, 0, 0)]
    queue = [(0, 0)]

    while stack:
        x, y, curd, curt = stack.pop()

        nxtd = curd
        nxtt = curt+1
        if str(curt) in dir:
            if dir[str(curt)] == 'D':
                nxtd = (curd+1) % 4
            else:
                nxtd = (curd-1) % 4

        if nxtd == 0: # right
            nx = x
            ny = y + 1
        elif nxtd == 1: # bot
            nx = x + 1
            ny = y
        elif nxtd == 2: # left
            nx = x
            ny = y - 1
        else: # top
            nx = x - 1
            ny = y

        if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in queue:
            queue.append((nx, ny))
            if (nx, ny) not in app:
                queue.pop(0)
            else:
                app.remove((nx, ny))
            stack.append((nx, ny, nxtd, nxtt))
        else: # 벽만남
            result = nxtt
            break

    return result


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
app = []
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    app.append((i-1, j-1))
L = int(sys.stdin.readline())
dir = {}
for _ in range(L):
    X, C = sys.stdin.readline().split()
    dir[X] = C

print(move())
