import sys
input = sys.stdin.readline

num, length = map(int, input().split())
dict = {}
for i in range(num):
	word = input().strip()
    	
	if len(word) < length:
		continue
        
	if dict.get(word):
    		
		dict[word][0] += 1
	else:
    		
		dict[word] = [1, len(word), word]

answer = sorted(dict.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))

for a in answer:
	print(a[0])