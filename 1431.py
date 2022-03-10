import sys

num = int(sys.stdin.readline())

serial_nums = [input() for _ in range(num)]

def sum_digit(x):
    result = [int(serial_num) for serial_num in x if serial_num.isdigit()]
    return sum(result)

serial_nums.sort(key=lambda x: (len(x),sum_digit(x),x))

for i in serial_nums:
    print(i)