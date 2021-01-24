# 16953번: A → B
from collections import deque

A, B = list( map(int, input().split()) )

queue = deque()
queue.append( [A, 1] )
result = -1
while queue:
    a, count = queue.popleft()
    
    if a*2 < B:
        queue.append( [a*2, count+1] )
    elif a*2 == B:
        result = count+1
        break
        
    if a*10 + 1 < B:
        queue.append( [a*10+1, count+1] )
    elif a*10 + 1 == B:
        result = count+1
        break
        
print( result )