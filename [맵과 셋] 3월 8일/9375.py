test_case = int(input())

for i in range(test_case):
    num = int(input())
    clothes = {}
    for j in range(num):
        name,type = input().split()
        if type in clothes:
            clothes[type]+=1
        else:
            clothes[type] = 1 
    if len(clothes)==1:
        temp = list(clothes.keys())
        print(clothes[temp[0]])
    else:
        result = 1
        for i in clothes:
            result*=clothes[i]+1
        print(result-1)

