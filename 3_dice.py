import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))
orders = list(map(int, sys.stdin.readline().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]  # top, east, west, north, south, bot

for order in orders:
    x = x + dx[order-1]
    y = y + dy[order-1]

    if 0 > x or x >= N or 0 > y or y >= M:
        x = x - dx[order-1]
        y = y - dy[order-1]
        continue

    if maps[x][y] == 0:
        maps[x][y] = dice[order]
    else:
        dice[order] = maps[x][y]
        maps[x][y] = 0

    if order == 1:
        # west -> top, east -> bot, top -> east, bot -> west
        dice = [dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]]
    elif order == 2:
        # west -> bot, east -> top, top -> west, bot -> east
        dice = [dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]]
    elif order == 3:
        # north -> bot, south -> top, top -> north, bot -> south
        dice = [dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]]
    else:
        # north -> top, south -> bot, top -> south, bot -> north
        dice = [dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]]

    print(dice[0])

