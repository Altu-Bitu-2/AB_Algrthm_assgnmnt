import sys

num=int(sys.stdin.readline().strip())
total=0
tips=[]
for _ in range(n):
    tips.append(int(sys.stdin.readline().strip()))
tips.sort(reverse=True)

for i in range(1,num+1):
    if tips[i-1]-(i-1)>0:
        total+=(tips[i-1]-(i-1))
    else:
        break
print(total)