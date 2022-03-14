import sys

DAY = 24 * 60 * 60

h, m, s = map(int, sys.stdin.readline().split())
total = h * 60 * 60 + m * 60 + s
num_q = int(sys.stdin.readline())

for _ in range(num_q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 3:
        print(f'{total // 60 // 60} {(total // 60) % 60} {total % 60}')
    else:
        if query[0] == 1:
            total += query[1]
        elif query[0] == 2:
            total -= query[1]
        total %= DAY