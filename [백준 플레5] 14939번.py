# 14939번: 불 끄기
def switchClick(i,j):
    for m in range(5):
        mi,mj = i + mx[m], j + my[m]
        if mi >= 0 and mj >= 0 and mi < 10 and mj < 10:
            graph[mi][mj] = switching[ graph[mi][mj] ]

def dfs( n, count ):
    global result
    if n == 100:
        for i in range(10):
            for j in range(10):
                if graph[i][j] == 'O':
                    return False

        result = min( result, count )
        return True
    
    
    i = n // 10
    j = n % 10
    if  i==0:
        # 불끄고 테스트
        switchClick(i, j)
    
        if dfs( n+1, count+1 ): return True
        else:
            # 실패라면 다시 불키기
            switchClick(i, j)
            return dfs( n+1, count )
    else:
        # 위에가 꺼져있다면 키면안됨. --> 키게된다면, 끌수 있는 방법이 이후에 존재하지 않음
        if i >= 1 and graph[i-1][j] == '#': 
            return dfs( n+1, count )
        
        # 불끄고 테스트
        switchClick(i, j)

        if dfs( n+1, count+1 ): return True
        else:
            # 위에가 켜져있는데, 해당지점에서 스위치가 불가능하다면, 결과는 불가능
            # 실패라면 다시 불키기
            switchClick(i, j)
            return False
################################################################
graph = [ list(input()) for i in range(10) ]

switching = { '#':'O', 'O':'#'}
mx = [ 0, -1, 0, 0, 1 ] # 자기위치 / 위 / 왼 / 오 / 아래
my = [ 0, 0, -1, 1, 0 ]
result = 123456789

dfs(0, 0)
            
print( result )