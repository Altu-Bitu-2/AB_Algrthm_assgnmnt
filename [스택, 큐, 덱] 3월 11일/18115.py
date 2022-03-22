n = int(input())
a = list(map(int, input().split()))
top, bottom = [], []

for i in range(1,n+1):
  temp = a[-i]
  if temp == 1:
    top.append(str(i))
  elif temp == 2:
    top.insert(-1, str(i))
  else:
    bottom.append(str(i))
top.reverse()
print(' '.join(top + bottom))