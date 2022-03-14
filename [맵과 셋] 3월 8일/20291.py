import sys

input = sys.stdin.readline

num = int(input())
files = dict()
for _ in range(num):
    type = list(map(str, input().rstrip()))

    ex = ""
    for i in range(type.index('.')+1, len(type)):
        ex += type[i]
        
    if files.get(ex) == None:
        files[ex] = 1
    else :
        files[ex] += 1

answer = []
for k, v in files.items():
    answer.append([k, v])

answer.sort()

for x in answer:
    print(x[0], x[1])
