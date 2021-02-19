# 2021 카카오 공채: 합승 택시 요금
def solution(n, s, a, b, fares):
    maxVal = 999999999
    
    # 그래프 생성 및 초기화
    graph = [ [ maxVal for i in range(n+1) ] for i in range(n+1) ]
    for i in range(1, n+1): graph[i][i] = 0
    for c,d,f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    # Floyd-Warshall을 통해 각 지점에서 다른 지점의 최단거리를 계산
    # 양방향 그래프이기 떄문에 j는 i+1부터 셋팅
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                graph[i][j] = graph[j][i] = min( graph[i][j], graph[i][k] + graph[k][j] )
    
    # 둘이 같이 이동하다 분기하는 지점을 찾아 최단거리를 구함
    # cost : 시작->분기지점 + 분기지점->A + 분기지점->B
    answer = maxVal
    for i in range( 1, n+1 ):  
        answer = min( answer, graph[s][i] + graph[i][a] + graph[i][b] )
    return answer