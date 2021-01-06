# 9466번: 텀 프로젝트
T = int(input())
for _ in range(T):
    N = int(input())
    datas = list(map(int, input().split()))
    check = [ 0 for i in range(N) ]
    checkNum = 2
    for i in range(N):
        if check[i] != 0:
            continue
        
        next_index = datas[ i ] - 1
        while check[next_index] == 0:
            check[next_index] = checkNum
            next_index = datas[ next_index ] - 1
        
        if check[next_index] == checkNum: # team
            while check[next_index] == checkNum:
                check[next_index] = 1
                next_index = datas[ next_index ] - 1
        
        checkNum += 1    
            
    print( N-check.count(1) ) # 전체에서 팀을 이룬것만 빼줌