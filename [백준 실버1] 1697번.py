# 1697번: 숨바꼭질
from collections import deque

N, K = list(map(int, input().split()))
if N == K: 
    print( 0 )
else:
    queue = deque()
    queue.append( [N, 0] )
    visited = [ False for i in range(200002) ]
    visited[ N ] = True
    result = 0
    while queue:
        subinPos, sec = queue.popleft()

        if subinPos-1 >= 0 and visited[subinPos-1]==False:
            visited[subinPos-1]=True
            queue.append( [subinPos-1, sec+1] )
            if subinPos-1 == K:
                result=sec+1
                break

        if subinPos+1 <= 100000 and visited[subinPos+1]==False:
            visited[subinPos+1]=True
            queue.append( [subinPos+1, sec+1] )
            if subinPos+1 == K:
                result=sec+1
                break

        if subinPos*2 <= 200000 and visited[subinPos*2]==False:
            visited[subinPos*2]=True
            queue.append( [subinPos*2, sec+1] )
            if subinPos*2 == K:
                result=sec+1
                break

    print( result )