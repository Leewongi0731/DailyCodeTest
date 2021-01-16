# 13913번: 숨바꼭질 4
# list로 구현시, append 시간복잡도 떄문에 타임초과
from collections import deque

class Node:
    def __init__(self, p, d):
        self.p = p
        self.d = d
        
N, K = list(map(int, input().split()))
visit = [0 for i in range( 136001 )]
visit[N] = 1
queue = deque()
node = Node( "root",  N )
queue.append( node )
if N != K:
    while queue:
        node = queue.popleft()
        end = node.d
        # -1
        if end -1 >= 0 and visit[ end-1 ] == 0:
            visit[ end-1 ] = 1
            queue.append( Node( node, end-1 ) )
            if end-1 == K: break

        # +1
        if end + 1 <= 100000 and visit[ end+1 ] == 0:
            visit[ end+1 ] = 1
            queue.append( Node( node, end+1 ) )
            if end + 1 == K: break

        # x2
        if end * 2  <= 136000 and visit[ end*2 ] == 0:
            visit[ end*2 ] = 1
            queue.append( Node( node, end*2 ) )
            if end * 2 == K: break

node = queue.pop()
result = [ node.d ]
while node.p != "root":
    node = node.p
    result.append( node.d )
    
print( len(result) - 1 )
for i in range(len(result)-1,-1,-1): print( result[i], end = ' ' )