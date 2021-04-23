import sys

N = int(sys.stdin.readline())
Alist = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

total = N
for people in Alist:
    if people-B > 0:
        if (people - B) % C == 0:
            total += (people-B) // C
        else:
            total += (people-B) // C + 1

print(total)