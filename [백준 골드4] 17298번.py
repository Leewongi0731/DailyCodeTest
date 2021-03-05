# 17298번: 오큰수
# 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
N = int(input())
datas = list(map(int, input().split()))

stack = [] # 가장 작은 값이 항상 top에 오도록.
answer = [ 0 for i in range(N) ]
for i, data in enumerate( datas ):
    while stack:
        if stack[-1][0] >= data:
            break
        else:
            value, index = stack.pop()
            answer[index] = data
    
    stack.append( [data, i] )
    
while stack: # stack에 남아있는 수는, 해당 수 이후로 더 큰 수가 나오지 않았다는 것
    value, index = stack.pop() 
    answer[index] = -1
    
print( ' '.join(map(str, answer)) )