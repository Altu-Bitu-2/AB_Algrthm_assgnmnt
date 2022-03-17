from sys import stdin

n, k = map(int, stdin.readline().split())
queue = [str(i) for i in range(1, n + 1)]
answer = []

cnt = 1
while len(queue) > 1 :
    if cnt < k:
        queue.append(queue.pop(0))
        cnt += 1
    else:
        answer.append(queue.pop(0))
        cnt = 1


answer.append(queue.pop(0))

print("<"+", ".join(answer)+">")