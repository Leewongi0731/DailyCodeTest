# 6198번: 옥상 정원 꾸미기
N = int(input())
datas = [ int(input()) for i in range(N) ]

stack = []
result = 0
for data in datas:
    while stack:
        if stack[-1] <= data:
            stack.pop()
        else:
            break
    
    # stack에는 해당 data보다 큰 값으로만 이루어져 있음 -> 이전 건물(stack 값)에서 해당 건물(data)의 옥상을 볼 수 있음
    result += len(stack)
    
    stack.append( data )
print( result )