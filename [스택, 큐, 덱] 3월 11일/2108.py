from collections import Counter
import sys


n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
    
nums.sort()
nums_cnt = Counter(nums).most_common()

print(round(sum(nums) / n))

print(nums[n // 2])

if len(nums_cnt) > 1:
    if nums_cnt[0][1] == nums_cnt[1][1]:
        print(nums_cnt[1][0])
    else:
        print(nums_cnt[0][0])
else:
    print(nums_cnt[0][0])
    
print(nums[-1] - nums[0])