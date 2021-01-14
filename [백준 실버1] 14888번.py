# 14888번: 연산자 끼워넣기
from itertools import permutations

N = int(input())
datas = list(map(int, input().split()))
pNum, sNum, mNum, dNum = list(map(int, input().split()))
operator = ['p'] * pNum + ['s'] * sNum + ['m'] * mNum + ['d'] * dNum

maxResult = -10000000000
minResult = 10000000000

for op in list(permutations(operator, N-1)):
    tmp = datas[0]
    for i in range(N-1):
        if op[i] == 'p':
            tmp+=datas[i+1]
        elif op[i] == 's':
            tmp-=datas[i+1]
        elif op[i] == 'm':
            tmp*=datas[i+1]
        elif op[i] == 'd':
            minusFlag = False
            if tmp < 0:
                minusFlag = True
                tmp = -tmp
            
            tmp //= datas[i+1]
            if minusFlag: tmp = -tmp
        
    maxResult = max( maxResult, tmp  )
    minResult = min( minResult, tmp  )      
print(maxResult)
print(minResult)