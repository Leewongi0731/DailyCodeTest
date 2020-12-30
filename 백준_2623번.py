## 2623번: 음악프로그램
N, M = list(map(int, input().split()))
graph = [ [0 for i in range(N)] for j in range(N)]
for _ in range(M):
    data = list(map(int, input().split()))[1:]
    for i, firstData in enumerate(data):
        for j, secondData in enumerate( data[i+1:] ):
            graph[ firstData-1 ][ secondData-1 ] = 1

isNextSinger = [0 for i in range(N)]
visited = [0 for i in range(N)]
result = []
try:
    while len(result) != N:
        nextSinger = None
        
        for i in range( N ):
            if visited[i] == 0 and graph[i] == isNextSinger:
                nextSinger = i
                break
        
        if nextSinger == None:
            raise
        else:
            for i in range(N):
                graph[i][nextSinger] = 0
            visited[nextSinger] = 1
            result.append( nextSinger )
    
    result.reverse()
    for r in result:
        print(r + 1)
except:
    print(0)