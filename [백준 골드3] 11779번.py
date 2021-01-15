# 11779번: 최소비용 구하기 2
MAX_LENGTH = 1234567891
N = int(input())
M = int(input())
graph = { key : {} for key in range(1, N+1) }
for _ in range(M):
    a,b,c = list(map(int, input().split()))
    try: # 같은 경로 다른 가격 존재. -> 최저가격으로 set
        graph[a][b] = min( [ graph[a][b], c ] )
    except:
        graph[a][b] = c
s,e = list(map(int, input().split()))


dp = [ MAX_LENGTH for i in range(N+1) ] # 현재 밝혀진 시작지점에서의 최저 cost
path = []  # 최정 업데이트 된 값을 저장하여 경로 추정에 사용
visit = [ 0 for i in range(N+1) ]
visit[ s ] = 1
for key in graph[s].keys():
    dp[ key ] = graph[s][key]
    path.append( [s, key] )

while True:
    nextNode = dp.index( min(dp) )
    
    if nextNode == e: # end point에 도달했다면 break
        break
    
    for key in graph[ nextNode ].keys():
        if visit[ key ] == 1: # 이미 방문한 Node면 pass
            continue
            
        if dp[key] > dp[nextNode]+graph[nextNode][key]: # update
            dp[key] = dp[nextNode]+graph[nextNode][key]
            path.append( [nextNode, key] )
    
    dp[ nextNode ] = MAX_LENGTH
    visit[ nextNode ] = 1
    
result = [e]
tmp = e
for i in range( len(path)-1, -1, -1 ): # path list를 뒤에서 부터 순회하며 경로를 추정함
    if path[i][1] == tmp:
        result.append( path[i][0] )
        tmp = path[i][0]
        if tmp == s:
            break
            
totalCost = 0
for i in range( len(result)-1, 0, -1 ):
    totalCost += graph[ result[i] ][ result[i-1] ] 
    
print( totalCost )
print( len(result) )
for i in range( len(result)-1, -1, -1 ):
    print( result[i], end =' ' )